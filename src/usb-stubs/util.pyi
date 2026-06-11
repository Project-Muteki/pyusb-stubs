from _typeshed import Incomplete
from array import array
from typing import Any, Callable, Iterable, Literal, TypeVar, overload

from .core import Device, Interface


DESC_TYPE_DEVICE: int
DESC_TYPE_CONFIG: int
DESC_TYPE_STRING: int
DESC_TYPE_INTERFACE: int
DESC_TYPE_ENDPOINT: int
ENDPOINT_IN: int
ENDPOINT_OUT: int
ENDPOINT_TYPE_CTRL: int
ENDPOINT_TYPE_ISO: int
ENDPOINT_TYPE_BULK: int
ENDPOINT_TYPE_INTR: int
CTRL_TYPE_STANDARD: Incomplete
CTRL_TYPE_CLASS: Incomplete
CTRL_TYPE_VENDOR: Incomplete
CTRL_TYPE_RESERVED: Incomplete
CTRL_RECIPIENT_DEVICE: int
CTRL_RECIPIENT_INTERFACE: int
CTRL_RECIPIENT_ENDPOINT: int
CTRL_RECIPIENT_OTHER: int
CTRL_OUT: int
CTRL_IN: int
SPEED_LOW: int
SPEED_FULL: int
SPEED_HIGH: int
SPEED_SUPER: int
SPEED_UNKNOWN: int

def endpoint_address(address: int) -> int: ...
def endpoint_direction(address: int) -> int: ...
def endpoint_type(bmAttributes: int) -> int: ...
def ctrl_direction(bmRequestType: int) -> int: ...
def build_request_type(direction: int, type: int, recipient: int) -> int: ...
def create_buffer(length: int) -> array[int]: ...

T = TypeVar('T')

@overload
def find_descriptor(desc: Iterable[T], find_all: Literal[True], custom_match: Callable[[T], bool] | None = None, **args: object) -> Iterable[T]: ...
@overload
def find_descriptor(desc: Iterable[T], find_all: Literal[False], custom_match: Callable[[T], bool] | None = None, **args: object) -> T: ...
@overload
def find_descriptor(desc: Iterable[T], custom_match: Callable[[T], bool] | None = None, **args: object) -> T: ...

def claim_interface(device, interface: Interface) -> None: ...
def release_interface(device, interface: Interface) -> None: ...
def dispose_resources(device: Device) -> None: ...
def get_langids(dev: Device) -> tuple[int]: ...
def get_string(dev: Device, index: int, langid: int | None = None) -> str | None: ...
