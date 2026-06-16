from array import array
from typing import Any, Callable, Generic, Literal, TypeVar, overload
from typing_extensions import Never, override
from collections.abc import Iterator, Sequence
from ._typing import DataOrLength
from .backend import BackendProtocol
from . import _objfinalizer


__all__ = [
    "Device",
    "Configuration",
    "Interface",
    "Endpoint",
    "USBError",
    "USBTimeoutError",
    "NoBackendError",
    "find",
    "show_devices",
]

class _DescriptorInfo(str):
    @override
    def __repr__(self) -> str: ...

class USBError(IOError):
    backend_error_code: int | None
    def __init__(
        self, strerror: str, error_code: int | None = None, errno: int | None = None
    ) -> None: ...

class USBTimeoutError(USBError): ...
class NoBackendError(ValueError): ...

T_DEV = TypeVar("T_DEV", default=Any)
T_DEVH = TypeVar("T_DEVH", default=Any)

class Endpoint(Generic[T_DEV, T_DEVH]):
    device: Device[T_DEV, T_DEVH]
    index: int

    bLength: int
    bDescriptorType: int
    bEndpointAddress: int
    bmAttributes: int
    wMaxPacketSize: int
    bInterval: int
    bRefresh: int
    bSynchAddress: int
    extra_descriptors: Sequence[int] | None

    def __init__(
        self,
        device: Device[T_DEV, T_DEVH],
        endpoint: int,
        interface: int = 0,
        alternate_setting: int = 0,
        configuration: int = 0,
    ) -> None: ...
    def write(self, data: DataOrLength, timeout: int | None = None) -> int: ...
    @overload
    def read(self, size_or_buffer: int, timeout: int | None = None) -> array[int]: ...
    @overload
    def read(self, size_or_buffer: array[int], timeout: int | None = None) -> int: ...
    def clear_halt(self) -> None: ...

class Interface(Generic[T_DEV, T_DEVH]):
    device: Device[T_DEV, T_DEVH]
    alternate_index: int
    index: int
    configuration: Configuration[T_DEV, T_DEVH]

    bLength: int
    bDescriptorType: int
    bInterfaceNumber: int
    bAlternateSetting: int
    bNumEndpoints: int
    bInterfaceClass: int
    bInterfaceSubClass: int
    bInterfaceProtocol: int
    iInterface: int
    extra_descriptors: Sequence[int] | None

    def __init__(
        self,
        device: Device[T_DEV, T_DEVH],
        interface: int = 0,
        alternate_setting: int = 0,
        configuration: int = 0,
    ) -> None: ...
    def endpoints(self) -> tuple[Endpoint[T_DEV, T_DEVH], ...]: ...
    def set_altsetting(self) -> None: ...
    def __iter__(self) -> Iterator[Endpoint[T_DEV, T_DEVH]]: ...
    def __getitem__(self, index: int) -> Endpoint[T_DEV, T_DEVH]: ...

class Configuration(Generic[T_DEV, T_DEVH]):
    device: Device[T_DEV, T_DEVH]
    index: int

    bLength: int
    bDescriptorType: int
    wTotalLength: int
    bNumInterfaces: int
    bConfigurationValue: int
    iConfiguration: int
    bmAttributes: int
    bMaxPower: int
    extra_descriptors: Sequence[int] | None

    def __init__(self, device: Device[T_DEV, T_DEVH], configuration: int = 0) -> None: ...
    def interfaces(self) -> tuple[Interface[T_DEV, T_DEVH], ...]: ...
    def set(self) -> None: ...
    def __iter__(self) -> Iterator[Interface[T_DEV, T_DEVH]]: ...
    def __getitem__(self, index: tuple[int, int]) -> Interface[T_DEV, T_DEVH]: ...

class Device(_objfinalizer.AutoFinalizedObject, Generic[T_DEV, T_DEVH]):
    bLength: int
    bDescriptorType: int
    bcdUSB: int
    bDeviceClass: int
    bDeviceSubClass: int
    bDeviceProtocol: int
    bMaxPacketSize0: int
    idVendor: int
    idProduct: int
    bcdDevice: int
    iManufacturer: int
    iProduct: int
    iSerialNumber: int
    bNumConfigurations: int
    address: int | None
    bus: int | None
    port_number: int | None
    port_numbers: Sequence[int] | None
    speed: int | None

    @override
    def __eq__(self, other: object, /) -> bool: ...
    @override
    def __hash__(self) -> int: ...
    def configurations(self) -> tuple[Configuration[T_DEV, T_DEVH], ...]: ...
    def __init__(self, dev: T_DEV, backend: BackendProtocol[T_DEV, T_DEVH]) -> None: ...
    @property
    def langids(self) -> tuple[int, ...]: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def product(self) -> str: ...
    @property
    def parent(self) -> Device[T_DEV, T_DEVH]: ...
    @property
    def manufacturer(self) -> str: ...
    @property
    def backend(self) -> BackendProtocol[T_DEV, T_DEVH]: ...
    def set_configuration(self, configuration: int | None = None) -> None: ...
    def get_active_configuration(self) -> Configuration[T_DEV, T_DEVH]: ...
    def set_interface_altsetting(
        self, interface: Interface[T_DEV, T_DEVH] | int | None = None, alternate_setting: int | None = None
    ) -> None: ...
    def clear_halt(self, ep: Endpoint[T_DEV, T_DEVH] | int) -> None: ...
    def reset(self) -> None: ...
    def write(self, endpoint: Endpoint[T_DEV, T_DEVH] | int, data: DataOrLength, timeout: int | None = None) -> int: ...
    @overload
    def read(self, endpoint: Endpoint[T_DEV, T_DEVH] | int, size_or_buffer: int, timeout: int | None = None) -> array[int]: ...
    @overload
    def read(self, endpoint: Endpoint[T_DEV, T_DEVH] | int, size_or_buffer: array[int], timeout: int | None = None) -> int: ...
    def ctrl_transfer(
        self,
        bmRequestType: int,
        bRequest: int,
        wValue: int = 0,
        wIndex: int = 0,
        data_or_wLength: DataOrLength = None,
        timeout: int | None = None,
    ) -> int | array[int]: ...
    def is_kernel_driver_active(self, interface: int) -> bool: ...
    def detach_kernel_driver(self, interface: int) -> None: ...
    def attach_kernel_driver(self, interface: int) -> None: ...
    def __iter__(self) -> Iterator[Configuration[T_DEV, T_DEVH]]: ...
    def __getitem__(self, index: int) -> Configuration[T_DEV, T_DEVH]: ...
    @property
    def default_timeout(self) -> int: ...
    @default_timeout.setter
    def default_timeout(self, tmo: int) -> None: ...

@overload
def find(
    find_all: Literal[False],
    backend: BackendProtocol[T_DEV, T_DEVH] | None = None,
    custom_match: Callable[[Device[T_DEV, T_DEVH]], bool]| None = None,
    **args: object,
) -> Device[T_DEV, T_DEVH] | None: ...
@overload
def find(
    find_all: Literal[True],
    backend: BackendProtocol[T_DEV, T_DEVH] | None = None,
    custom_match: Callable[[Device[T_DEV, T_DEVH]], bool]| None = None,
    **args: object,
) -> Iterator[Device[T_DEV, T_DEVH]]: ...
# find_all does not take a None. Assume it's always bool and all options have
# been exhausted by the above overloads.
@overload
def find(
    find_all: Never = ...,
    backend: BackendProtocol[T_DEV, T_DEVH] | None = None,
    custom_match: Callable[[Device[T_DEV, T_DEVH]], bool]| None = None,
    **args: object,
) -> Device[T_DEV, T_DEVH] | None: ...
def show_devices(
    verbose: bool = False,
    /,
    backend: BackendProtocol | None = None,
    **kwargs: object,
) -> _DescriptorInfo: ...
