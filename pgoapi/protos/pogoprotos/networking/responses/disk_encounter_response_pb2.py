# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/disk_encounter_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data.capture import capture_probability_pb2 as pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/disk_encounter_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n=pogoprotos/networking/responses/disk_encounter_response.proto\x12\x1fpogoprotos.networking.responses\x1a\"pogoprotos/data/pokemon_data.proto\x1a\x31pogoprotos/data/capture/capture_probability.proto\"\xea\x02\n\x15\x44iskEncounterResponse\x12M\n\x06result\x18\x01 \x01(\x0e\x32=.pogoprotos.networking.responses.DiskEncounterResponse.Result\x12\x32\n\x0cpokemon_data\x18\x02 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12H\n\x13\x63\x61pture_probability\x18\x03 \x01(\x0b\x32+.pogoprotos.data.capture.CaptureProbability\"\x83\x01\n\x06Result\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rNOT_AVAILABLE\x10\x02\x12\x10\n\x0cNOT_IN_RANGE\x10\x03\x12\x1e\n\x1a\x45NCOUNTER_ALREADY_FINISHED\x10\x04\x12\x1a\n\x16POKEMON_INVENTORY_FULL\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DISKENCOUNTERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.DiskEncounterResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_AVAILABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_IN_RANGE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_ALREADY_FINISHED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_INVENTORY_FULL', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=417,
  serialized_end=548,
)
_sym_db.RegisterEnumDescriptor(_DISKENCOUNTERRESPONSE_RESULT)


_DISKENCOUNTERRESPONSE = _descriptor.Descriptor(
  name='DiskEncounterResponse',
  full_name='pogoprotos.networking.responses.DiskEncounterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.DiskEncounterResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='pogoprotos.networking.responses.DiskEncounterResponse.pokemon_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capture_probability', full_name='pogoprotos.networking.responses.DiskEncounterResponse.capture_probability', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DISKENCOUNTERRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=548,
)

_DISKENCOUNTERRESPONSE.fields_by_name['result'].enum_type = _DISKENCOUNTERRESPONSE_RESULT
_DISKENCOUNTERRESPONSE.fields_by_name['pokemon_data'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_DISKENCOUNTERRESPONSE.fields_by_name['capture_probability'].message_type = pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2._CAPTUREPROBABILITY
_DISKENCOUNTERRESPONSE_RESULT.containing_type = _DISKENCOUNTERRESPONSE
DESCRIPTOR.message_types_by_name['DiskEncounterResponse'] = _DISKENCOUNTERRESPONSE

DiskEncounterResponse = _reflection.GeneratedProtocolMessageType('DiskEncounterResponse', (_message.Message,), dict(
  DESCRIPTOR = _DISKENCOUNTERRESPONSE,
  __module__ = 'pogoprotos.networking.responses.disk_encounter_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.DiskEncounterResponse)
  ))
_sym_db.RegisterMessage(DiskEncounterResponse)


# @@protoc_insertion_point(module_scope)
