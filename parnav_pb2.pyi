from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BTIQSampleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Sample8BitsInt: _ClassVar[BTIQSampleType]
    Sample16BitsInt: _ClassVar[BTIQSampleType]
Sample8BitsInt: BTIQSampleType
Sample16BitsInt: BTIQSampleType

class IqSample(_message.Message):
    __slots__ = ("i", "q")
    I_FIELD_NUMBER: _ClassVar[int]
    Q_FIELD_NUMBER: _ClassVar[int]
    i: int
    q: int
    def __init__(self, i: _Optional[int] = ..., q: _Optional[int] = ...) -> None: ...

class IqSample16(_message.Message):
    __slots__ = ("i", "q")
    I_FIELD_NUMBER: _ClassVar[int]
    Q_FIELD_NUMBER: _ClassVar[int]
    i: int
    q: int
    def __init__(self, i: _Optional[int] = ..., q: _Optional[int] = ...) -> None: ...

class BTIQSamplesReport(_message.Message):
    __slots__ = ("chan_idx", "rssi", "rssi_ant_id", "cte_type", "slot_durations", "packet_status", "per_evt_counter", "sample_count", "sample_type", "iqSample", "iqSample16")
    CHAN_IDX_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    RSSI_ANT_ID_FIELD_NUMBER: _ClassVar[int]
    CTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLOT_DURATIONS_FIELD_NUMBER: _ClassVar[int]
    PACKET_STATUS_FIELD_NUMBER: _ClassVar[int]
    PER_EVT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IQSAMPLE_FIELD_NUMBER: _ClassVar[int]
    IQSAMPLE16_FIELD_NUMBER: _ClassVar[int]
    chan_idx: int
    rssi: int
    rssi_ant_id: int
    cte_type: int
    slot_durations: int
    packet_status: int
    per_evt_counter: int
    sample_count: int
    sample_type: BTIQSampleType
    iqSample: IqSample
    iqSample16: IqSample16
    def __init__(self, chan_idx: _Optional[int] = ..., rssi: _Optional[int] = ..., rssi_ant_id: _Optional[int] = ..., cte_type: _Optional[int] = ..., slot_durations: _Optional[int] = ..., packet_status: _Optional[int] = ..., per_evt_counter: _Optional[int] = ..., sample_count: _Optional[int] = ..., sample_type: _Optional[_Union[BTIQSampleType, str]] = ..., iqSample: _Optional[_Union[IqSample, _Mapping]] = ..., iqSample16: _Optional[_Union[IqSample16, _Mapping]] = ...) -> None: ...
