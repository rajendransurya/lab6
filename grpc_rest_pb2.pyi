from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class addMsg(_message.Message):
    __slots__ = ["a", "b"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...

class addReply(_message.Message):
    __slots__ = ["sum"]
    SUM_FIELD_NUMBER: _ClassVar[int]
    sum: int
    def __init__(self, sum: _Optional[int] = ...) -> None: ...

class dotProductMsg(_message.Message):
    __slots__ = ["a", "b"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: _containers.RepeatedScalarFieldContainer[float]
    b: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, a: _Optional[_Iterable[float]] = ..., b: _Optional[_Iterable[float]] = ...) -> None: ...

class dotProductReply(_message.Message):
    __slots__ = ["dotproduct"]
    DOTPRODUCT_FIELD_NUMBER: _ClassVar[int]
    dotproduct: float
    def __init__(self, dotproduct: _Optional[float] = ...) -> None: ...

class imageReply(_message.Message):
    __slots__ = ["height", "width"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class jsonImageMsg(_message.Message):
    __slots__ = ["img"]
    IMG_FIELD_NUMBER: _ClassVar[int]
    img: str
    def __init__(self, img: _Optional[str] = ...) -> None: ...

class rawImageMsg(_message.Message):
    __slots__ = ["img"]
    IMG_FIELD_NUMBER: _ClassVar[int]
    img: bytes
    def __init__(self, img: _Optional[bytes] = ...) -> None: ...
