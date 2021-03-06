"""
pgoapi - Pokemon Go API
Copyright (c) 2016 tjado <https://github.com/tejado>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

Author: tjado <https://github.com/tejado>
"""

from __future__ import absolute_import

import re
import six
import logging
import requests
import time

from . import __title__, __version__, __copyright__
from pgoapi.rpc_api import RpcApi
from pgoapi.auth_ptc import AuthPtc
from pgoapi.auth_google import AuthGoogle
from pgoapi.utilities import parse_api_endpoint, get_lib_paths, get_time
from pgoapi.exceptions import AuthException, BannedAccount, NotLoggedInException, ServerBusyOrOfflineException, NoPlayerPositionSetException, EmptySubrequestChainException, AuthTokenExpiredException, ServerApiEndpointRedirectException, UnexpectedResponseException

from . import protos
from pogoprotos.networking.requests.request_type_pb2 import RequestType

logger = logging.getLogger(__name__)


class PGoApi:

    def __init__(self, provider=None, oauth2_refresh_token=None, username=None, password=None, position_lat=None, position_lng=None, position_alt=None, proxy_config=None, device_info=None):
        self.set_logger()
        self.log.info('%s v%s - %s', __title__, __version__, __copyright__)

        self._auth_provider = None
        if provider is not None and ((username is not None and password is not None) or (oauth2_refresh_token is not None)):
            self.set_authentication(provider, oauth2_refresh_token, username, password, proxy_config)

        self.set_api_endpoint("pgorelease.nianticlabs.com/plfe")

        self._position_lat = position_lat
        self._position_lng = position_lng
        self._position_alt = position_alt

        self._signature_lib = None
        self._hash_lib = None

        self._session = requests.session()
        self._session.headers.update({'User-Agent': 'Niantic App'})
        self._session.verify = True

        if proxy_config is not None:
            self._session.proxies = proxy_config

        self.device_info = device_info

    def set_logger(self, logger=None):
        self.log = logger or logging.getLogger(__name__)

    def set_authentication(self, provider=None, oauth2_refresh_token=None, username=None, password=None, proxy_config=None):
        if provider == 'ptc':
            self._auth_provider = AuthPtc()
        elif provider == 'google':
            self._auth_provider = AuthGoogle()
        elif provider is None:
            self._auth_provider = None
        else:
            raise AuthException("Invalid authentication provider - only ptc/google available.")

        self.log.debug('Auth provider: %s', provider)

        if proxy_config is not None:
            self._auth_provider.set_proxy(proxy_config)

        if oauth2_refresh_token is not None:
            self._auth_provider.set_refresh_token(oauth2_refresh_token)
        elif username is not None and password is not None:
            if not self._auth_provider.user_login(username, password):
                raise AuthException("User login failed!")
        else:
            raise AuthException("Invalid Credential Input - Please provide username/password or an oauth2 refresh token")

    def get_position(self):
        return (self._position_lat, self._position_lng, self._position_alt)

    def set_position(self, lat, lng, alt=None):
        self.log.debug('Set Position - Lat: %s Long: %s Alt: %s', lat, lng, alt)

        self._position_lat = lat
        self._position_lng = lng
        self._position_alt = alt

    def set_proxy(self, proxy_config):
        self._session.proxies = proxy_config

    def get_api_endpoint(self):
        return self._api_endpoint

    def set_api_endpoint(self, api_url):
        if api_url.startswith("https"):
            self._api_endpoint = api_url
        else:
            self._api_endpoint = parse_api_endpoint(api_url)

    def get_auth_provider(self):
        return self._auth_provider

    def create_request(self):
        request = PGoApiRequest(self, self._position_lat, self._position_lng,
                                self._position_alt, self.device_info)
        return request

    def activate_signature(self, signature_lib_path=None, hash_lib_path=None):
        if signature_lib_path: self.set_signature_lib(signature_lib_path)
        if hash_lib_path: self.set_hash_lib(hash_lib_path)

    def set_signature_lib(self, signature_lib_path):
        self._signature_lib = signature_lib_path

    def set_hash_lib(self, hash_lib_path):
        self._hash_lib = hash_lib_path

    def get_signature_lib(self):
        return self._signature_lib

    def get_hash_lib(self):
        return self._hash_lib

    def __getattr__(self, func):
        def function(**kwargs):
            request = self.create_request()
            getattr(request, func)(_call_direct=True, **kwargs )
            return request.call()

        if func.upper() in RequestType.keys():
            return function
        else:
            raise AttributeError

    def app_simulation_login(self):
        self.log.info('Starting RPC login sequence (iOS app simulation)')

        # Send empty initial request
        request = self.create_request()
        response = request.call()
        time.sleep(1.172)

        request = self.create_request()
        response = request.call()
        time.sleep(1.304)
        

        # Send GET_PLAYER only
        request = self.create_request()
        request.get_player(player_locale = {'country': 'US', 'language': 'en', 'timezone': 'America/Denver'})
        response = request.call()
        
        if response.get('responses', {}).get('GET_PLAYER', {}).get('banned', False):
            raise BannedAccount()

        time.sleep(1.356)

        request = self.create_request()
        request.download_remote_config_version(platform=1, app_version=4500)
        request.check_challenge()
        request.get_hatched_eggs()
        request.get_inventory()
        request.check_awarded_badges()
        request.download_settings()
        response = request.call()
        time.sleep(1.072)

        responses = response.get('responses', {})
        download_hash = responses.get('DOWNLOAD_SETTINGS', {}).get('hash')
        inventory = responses.get('GET_INVENTORY', {}).get('inventory_delta', {})
        timestamp = inventory.get('new_timestamp_ms')
        player_level = None
        for item in inventory.get('inventory_items', []):
            player_stats = item.get('inventory_item_data', {}).get('player_stats', {})
            if player_stats:
                player_level = player_stats.get('level')
                break

        request = self.create_request()
        request.get_asset_digest(platform=1, app_version=4500)
        request.check_challenge()
        request.get_hatched_eggs()
        request.get_inventory(last_timestamp_ms=timestamp)
        request.check_awarded_badges()
        request.download_settings(hash=download_hash)
        response = request.call()
        time.sleep(1.709)

        timestamp = response.get('responses', {}).get('GET_INVENTORY', {}).get('inventory_delta', {}).get('new_timestamp_ms')
        request = self.create_request()
        request.get_player_profile()
        request.check_challenge()
        request.get_hatched_eggs()
        request.get_inventory(last_timestamp_ms=timestamp)
        request.check_awarded_badges()
        request.download_settings(hash=download_hash)
        request.get_buddy_walked()
        response = request.call()
        time.sleep(1.326)

        timestamp = response.get('responses', {}).get('GET_INVENTORY', {}).get('inventory_delta', {}).get('new_timestamp_ms')
        request = self.create_request()
        request.level_up_rewards(level=player_level)
        request.check_challenge()
        request.get_hatched_eggs()
        request.get_inventory(last_timestamp_ms=timestamp)
        request.check_awarded_badges()
        request.download_settings(hash=download_hash)
        request.get_buddy_walked()
        response = request.call()

        self.log.info('Finished RPC login sequence (iOS app simulation)')

        return response

    """
    The login function is not needed anymore but still in the code for backward compatibility"
    """
    def login(self, provider, username, password, lat=None, lng=None, alt=None, app_simulation=True):

        if lat and lng:
            self._position_lat = lat
            self._position_lng = lng
        if alt:
            self._position_alt = alt

        try:
            self.set_authentication(provider, username=username, password=password, proxy_config=self._session.proxies)
        except AuthException as e:
            self.log.error('Login process failed: %s', e)
            return False

        if app_simulation:
            response = self.app_simulation_login()
        else:
            self.log.info('Starting minimal RPC login sequence')
            response = self.get_player()
            self.log.info('Finished minimal RPC login sequence')

        if not response:
            self.log.info('Login failed!')
            return False

        challenge_url = response.get('responses', {}).get('CHECK_CHALLENGE', {}).get('challenge_url', ' ')
        if challenge_url != ' ':
            self.log.error('CAPCHA required: ' + challenge_url)
            return challenge_url

        self.log.info('Login process completed')

        return True


class PGoApiRequest:

    def __init__(self, parent, position_lat, position_lng, position_alt,
                 device_info=None):
        self.log = logging.getLogger(__name__)

        self.__parent__ = parent

        """ Inherit necessary parameters from parent """
        self._api_endpoint = self.__parent__.get_api_endpoint()
        self._auth_provider = self.__parent__.get_auth_provider()

        self._position_lat = position_lat
        self._position_lng = position_lng
        self._position_alt = position_alt

        self._req_method_list = []
        self.device_info = device_info

    def call(self):
        if (self._position_lat is None) or (self._position_lng is None):
            raise NoPlayerPositionSetException()

        if self._auth_provider is None or not self._auth_provider.is_login():
            self.log.info('Not logged in')
            raise NotLoggedInException()

        request = RpcApi(self._auth_provider, self.device_info)
        request._session = self.__parent__._session

        signature_lib_path = self.__parent__.get_signature_lib()
        hash_lib_path = self.__parent__.get_hash_lib()
        if not signature_lib_path or not hash_lib_path:
            default_libraries = get_lib_paths()
            if not signature_lib_path:
                signature_lib_path = default_libraries[0]
            if not hash_lib_path:
                hash_lib_path = default_libraries[1]
        request.activate_signature(signature_lib_path, hash_lib_path)

        self.log.info('Execution of RPC')
        response = None

        execute = True
        while execute:
            execute = False

            try:
                response = request.request(self._api_endpoint, self._req_method_list, self.get_position())
            except AuthTokenExpiredException as e:
                """
                This exception only occures if the OAUTH service provider (google/ptc) didn't send any expiration date
                so that we are assuming, that the access_token is always valid until the API server states differently.
                """
                try:
                    self.log.info('Access Token rejected! Requesting new one...')
                    self._auth_provider.get_access_token(force_refresh=True)
                except:
                    error = 'Request for new Access Token failed! Logged out...'
                    self.log.error(error)
                    raise NotLoggedInException(error)

                """ reexecute the call"""
                execute = True
            except ServerApiEndpointRedirectException as e:
                self.log.info('API Endpoint redirect... re-execution of call')
                new_api_endpoint = e.get_redirected_endpoint()

                self._api_endpoint = parse_api_endpoint(new_api_endpoint)
                self.__parent__.set_api_endpoint(self._api_endpoint)

                """ reexecute the call"""
                execute = True
            except ServerBusyOrOfflineException as e:
                """ no execute = True here, as API retries on HTTP level should be done on a lower level, e.g. in rpc_api """
                self.log.info('Server seems to be busy or offline - try again!')
                self.log.debug('ServerBusyOrOfflineException details: %s', e)
            except UnexpectedResponseException as e:
                self.log.error('Unexpected server response!')
                raise

        # cleanup after call execution
        self.log.info('Cleanup of request!')
        self._req_method_list = []

        return response

    def list_curr_methods(self):
        for i in self._req_method_list:
            print("{} ({})".format(RequestType.Name(i), i))

    def get_position(self):
        return (self._position_lat, self._position_lng, self._position_alt)

    def set_position(self, lat, lng, alt=None):
        self.log.debug('Set Position - Lat: %s Long: %s Alt: %s', lat, lng, alt)

        self._position_lat = lat
        self._position_lng = lng
        self._position_alt = alt

    def __getattr__(self, func):
        def function(**kwargs):

            if '_call_direct' in kwargs:
                del kwargs['_call_direct']
                self.log.info('Creating a new direct request...')
            elif not self._req_method_list:
                self.log.info('Creating a new request...')

            name = func.upper()
            if kwargs:
                self._req_method_list.append({RequestType.Value(name): kwargs})
                self.log.info("Adding '%s' to RPC request including arguments", name)
                self.log.debug("Arguments of '%s': \n\r%s", name, kwargs)
            else:
                self._req_method_list.append(RequestType.Value(name))
                self.log.info("Adding '%s' to RPC request", name)

            return self

        if func.upper() in RequestType.keys():
            return function
        else:
            raise AttributeError
