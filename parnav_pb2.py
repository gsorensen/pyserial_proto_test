# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parnav.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cparnav.proto\x12\x06PARNAV\" \n\x08IqSample\x12\t\n\x01i\x18\x01 \x01(\x05\x12\t\n\x01q\x18\x02 \x01(\x05\"\"\n\nIqSample16\x12\t\n\x01i\x18\x01 \x01(\x05\x12\t\n\x01q\x18\x02 \x01(\x05\"\xc8\x02\n\x11\x42TIQSamplesReport\x12\x10\n\x08\x63han_idx\x18\x01 \x01(\r\x12\x0c\n\x04rssi\x18\x02 \x01(\x05\x12\x13\n\x0brssi_ant_id\x18\x03 \x01(\r\x12\x10\n\x08\x63te_type\x18\x04 \x01(\r\x12\x16\n\x0eslot_durations\x18\x05 \x01(\r\x12\x15\n\rpacket_status\x18\x06 \x01(\r\x12\x17\n\x0fper_evt_counter\x18\x07 \x01(\r\x12\x14\n\x0csample_count\x18\x08 \x01(\r\x12+\n\x0bsample_type\x18\t \x01(\x0e\x32\x16.PARNAV.BTIQSampleType\x12$\n\x08iqSample\x18\n \x01(\x0b\x32\x10.PARNAV.IqSampleH\x00\x12(\n\niqSample16\x18\x0b \x01(\x0b\x32\x12.PARNAV.IqSample16H\x00\x42\x11\n\x0fSampleBitsUnion*9\n\x0e\x42TIQSampleType\x12\x12\n\x0eSample8BitsInt\x10\x00\x12\x13\n\x0fSample16BitsInt\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'parnav_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BTIQSAMPLETYPE']._serialized_start=425
  _globals['_BTIQSAMPLETYPE']._serialized_end=482
  _globals['_IQSAMPLE']._serialized_start=24
  _globals['_IQSAMPLE']._serialized_end=56
  _globals['_IQSAMPLE16']._serialized_start=58
  _globals['_IQSAMPLE16']._serialized_end=92
  _globals['_BTIQSAMPLESREPORT']._serialized_start=95
  _globals['_BTIQSAMPLESREPORT']._serialized_end=423
# @@protoc_insertion_point(module_scope)
