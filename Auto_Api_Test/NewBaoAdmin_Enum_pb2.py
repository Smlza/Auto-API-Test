# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NewBaoAdmin_Enum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='NewBaoAdmin_Enum.proto',
  package='proto',
  syntax='proto3',
  serialized_options=_b('Z\007.;proto'),
  serialized_pb=_b('\n\x16NewBaoAdmin_Enum.proto\x12\x05proto*\x84\x02\n\x0f\x41\x64minButtonEnum\x12\x0f\n\x0b\x43\x61ncelOrder\x10\x00\x12\x12\n\x0e\x43onfirmReceive\x10\x01\x12\x0e\n\nStartCheck\x10\x02\x12\r\n\tCheckPass\x10\x03\x12\r\n\tCheckFail\x10\x04\x12\x11\n\rAppraisalPass\x10\x05\x12\x11\n\rAppraisalFail\x10\x06\x12\x14\n\x10\x41ppraisalRefused\x10\x07\x12\x12\n\x0eSendBackSeller\x10\x08\x12\x0f\n\x0bSendToBuyer\x10\t\x12\n\n\x06Refund\x10\n\x12\t\n\x05Remit\x10\x0b\x12\n\n\x06\x44\x65tail\x10\x0c\x12\x0b\n\x07GoToAdd\x10\r\x12\r\n\tNoProcess\x10\x0e*k\n\x18\x41\x64minPublishFeedbackEnum\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x11\n\rToBeProcessed\x10\x01\x12\x14\n\x10\x41lreadyProcessed\x10\x02\x12\x19\n\x15NotProcessTemporarily\x10\x03\x42\tZ\x07.;protob\x06proto3')
)

_ADMINBUTTONENUM = _descriptor.EnumDescriptor(
  name='AdminButtonEnum',
  full_name='proto.AdminButtonEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CancelOrder', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ConfirmReceive', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StartCheck', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CheckPass', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CheckFail', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AppraisalPass', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AppraisalFail', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AppraisalRefused', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SendBackSeller', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SendToBuyer', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Refund', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Remit', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Detail', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GoToAdd', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NoProcess', index=14, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=34,
  serialized_end=294,
)
_sym_db.RegisterEnumDescriptor(_ADMINBUTTONENUM)

AdminButtonEnum = enum_type_wrapper.EnumTypeWrapper(_ADMINBUTTONENUM)
_ADMINPUBLISHFEEDBACKENUM = _descriptor.EnumDescriptor(
  name='AdminPublishFeedbackEnum',
  full_name='proto.AdminPublishFeedbackEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ToBeProcessed', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AlreadyProcessed', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NotProcessTemporarily', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=296,
  serialized_end=403,
)
_sym_db.RegisterEnumDescriptor(_ADMINPUBLISHFEEDBACKENUM)

AdminPublishFeedbackEnum = enum_type_wrapper.EnumTypeWrapper(_ADMINPUBLISHFEEDBACKENUM)
CancelOrder = 0
ConfirmReceive = 1
StartCheck = 2
CheckPass = 3
CheckFail = 4
AppraisalPass = 5
AppraisalFail = 6
AppraisalRefused = 7
SendBackSeller = 8
SendToBuyer = 9
Refund = 10
Remit = 11
Detail = 12
GoToAdd = 13
NoProcess = 14
Default = 0
ToBeProcessed = 1
AlreadyProcessed = 2
NotProcessTemporarily = 3


DESCRIPTOR.enum_types_by_name['AdminButtonEnum'] = _ADMINBUTTONENUM
DESCRIPTOR.enum_types_by_name['AdminPublishFeedbackEnum'] = _ADMINPUBLISHFEEDBACKENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
