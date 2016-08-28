# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/FortDeployPokemonResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data import PokemonData_pb2 as POGOProtos_dot_Data_dot_PokemonData__pb2
from POGOProtos.Data.Gym import GymState_pb2 as POGOProtos_dot_Data_dot_Gym_dot_GymState__pb2
from POGOProtos.Networking.Responses import FortDetailsResponse_pb2 as POGOProtos_dot_Networking_dot_Responses_dot_FortDetailsResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/FortDeployPokemonResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n?POGOProtos/Networking/Responses/FortDeployPokemonResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a!POGOProtos/Data/PokemonData.proto\x1a\"POGOProtos/Data/Gym/GymState.proto\x1a\x39POGOProtos/Networking/Responses/FortDetailsResponse.proto\"\xc4\x04\n\x19\x46ortDeployPokemonResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.POGOProtos.Networking.Responses.FortDeployPokemonResponse.Result\x12J\n\x0c\x66ort_details\x18\x02 \x01(\x0b\x32\x34.POGOProtos.Networking.Responses.FortDetailsResponse\x12\x32\n\x0cpokemon_data\x18\x03 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12\x30\n\tgym_state\x18\x04 \x01(\x0b\x32\x1d.POGOProtos.Data.Gym.GymState\"\xa1\x02\n\x06Result\x12\x11\n\rNO_RESULT_SET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12%\n!ERROR_ALREADY_HAS_POKEMON_ON_FORT\x10\x02\x12!\n\x1d\x45RROR_OPPOSING_TEAM_OWNS_FORT\x10\x03\x12\x16\n\x12\x45RROR_FORT_IS_FULL\x10\x04\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x05\x12\x1c\n\x18\x45RROR_PLAYER_HAS_NO_TEAM\x10\x06\x12\x1d\n\x19\x45RROR_POKEMON_NOT_FULL_HP\x10\x07\x12$\n ERROR_PLAYER_BELOW_MINIMUM_LEVEL\x10\x08\x12\x1a\n\x16\x45RROR_POKEMON_IS_BUDDY\x10\tb\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_PokemonData__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Gym_dot_GymState__pb2.DESCRIPTOR,POGOProtos_dot_Networking_dot_Responses_dot_FortDetailsResponse__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FORTDEPLOYPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.FortDeployPokemonResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_RESULT_SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_HAS_POKEMON_ON_FORT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_OPPOSING_TEAM_OWNS_FORT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FORT_IS_FULL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_HAS_NO_TEAM', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_FULL_HP', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_BELOW_MINIMUM_LEVEL', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_BUDDY', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=522,
  serialized_end=811,
)
_sym_db.RegisterEnumDescriptor(_FORTDEPLOYPOKEMONRESPONSE_RESULT)


_FORTDEPLOYPOKEMONRESPONSE = _descriptor.Descriptor(
  name='FortDeployPokemonResponse',
  full_name='POGOProtos.Networking.Responses.FortDeployPokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.FortDeployPokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_details', full_name='POGOProtos.Networking.Responses.FortDeployPokemonResponse.fort_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Networking.Responses.FortDeployPokemonResponse.pokemon_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_state', full_name='POGOProtos.Networking.Responses.FortDeployPokemonResponse.gym_state', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FORTDEPLOYPOKEMONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=811,
)

_FORTDEPLOYPOKEMONRESPONSE.fields_by_name['result'].enum_type = _FORTDEPLOYPOKEMONRESPONSE_RESULT
_FORTDEPLOYPOKEMONRESPONSE.fields_by_name['fort_details'].message_type = POGOProtos_dot_Networking_dot_Responses_dot_FortDetailsResponse__pb2._FORTDETAILSRESPONSE
_FORTDEPLOYPOKEMONRESPONSE.fields_by_name['pokemon_data'].message_type = POGOProtos_dot_Data_dot_PokemonData__pb2._POKEMONDATA
_FORTDEPLOYPOKEMONRESPONSE.fields_by_name['gym_state'].message_type = POGOProtos_dot_Data_dot_Gym_dot_GymState__pb2._GYMSTATE
_FORTDEPLOYPOKEMONRESPONSE_RESULT.containing_type = _FORTDEPLOYPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['FortDeployPokemonResponse'] = _FORTDEPLOYPOKEMONRESPONSE

FortDeployPokemonResponse = _reflection.GeneratedProtocolMessageType('FortDeployPokemonResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORTDEPLOYPOKEMONRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.FortDeployPokemonResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.FortDeployPokemonResponse)
  ))
_sym_db.RegisterMessage(FortDeployPokemonResponse)


# @@protoc_insertion_point(module_scope)