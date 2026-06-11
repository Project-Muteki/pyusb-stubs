from array import array
from ctypes import *
from typing import Iterable, NewType
import usb.backend
import usb._objfinalizer as _objfinalizer
from _typeshed import Incomplete

from usb.backend._typing import (
    ConfigurationDescriptorProtocol,
    DeviceDescriptorProtocol,
    EndpointDescriptorProtocol,
    InterfaceDescriptorProtocol,
)

__all__ = [
    "get_backend",
    "LIBUSB_SUCCESS",
    "LIBUSB_ERROR_IO",
    "LIBUSB_ERROR_INVALID_PARAM",
    "LIBUSB_ERROR_ACCESS",
    "LIBUSB_ERROR_NO_DEVICE",
    "LIBUSB_ERROR_NOT_FOUND",
    "LIBUSB_ERROR_BUSY",
    "LIBUSB_ERROR_TIMEOUT",
    "LIBUSB_ERROR_OVERFLOW",
    "LIBUSB_ERROR_PIPE",
    "LIBUSB_ERROR_INTERRUPTED",
    "LIBUSB_ERROR_NO_MEM",
    "LIBUSB_ERROR_NOT_SUPPORTED",
    "LIBUSB_ERROR_OTHER",
    "LIBUSB_TRANSFER_COMPLETED",
    "LIBUSB_TRANSFER_ERROR",
    "LIBUSB_TRANSFER_TIMED_OUT",
    "LIBUSB_TRANSFER_CANCELLED",
    "LIBUSB_TRANSFER_STALL",
    "LIBUSB_TRANSFER_NO_DEVICE",
    "LIBUSB_TRANSFER_OVERFLOW",
]

LIBUSB_SUCCESS: int
LIBUSB_ERROR_IO: int
LIBUSB_ERROR_INVALID_PARAM: int
LIBUSB_ERROR_ACCESS: int
LIBUSB_ERROR_NO_DEVICE: int
LIBUSB_ERROR_NOT_FOUND: int
LIBUSB_ERROR_BUSY: int
LIBUSB_ERROR_TIMEOUT: int
LIBUSB_ERROR_OVERFLOW: int
LIBUSB_ERROR_PIPE: int
LIBUSB_ERROR_INTERRUPTED: int
LIBUSB_ERROR_NO_MEM: int
LIBUSB_ERROR_NOT_SUPPORTED: int
LIBUSB_ERROR_OTHER: int
LIBUSB_TRANSFER_COMPLETED: int
LIBUSB_TRANSFER_ERROR: int
LIBUSB_TRANSFER_TIMED_OUT: int
LIBUSB_TRANSFER_CANCELLED: int
LIBUSB_TRANSFER_STALL: int
LIBUSB_TRANSFER_NO_DEVICE: int
LIBUSB_TRANSFER_OVERFLOW: int

_libusb_device_handle = NewType("_libusb_device_handle", c_void_p)

class _libusb_endpoint_descriptor(Structure): ...
class _libusb_interface_descriptor(Structure): ...
class _libusb_interface(Structure): ...
class _libusb_config_descriptor(Structure): ...
class _libusb_device_descriptor(Structure): ...
class _libusb_iso_packet_descriptor(Structure): ...
class _libusb_transfer(Structure): ...

class _Device(_objfinalizer.AutoFinalizedObject):
    devid: Incomplete
    def __init__(self, devid) -> None: ...

class _DeviceHandle:
    handle: _libusb_device_handle
    devid: c_void_p
    def __init__(self, dev: _Device) -> None: ...

# TODO: it may be better to replace DeviceDescriptorProtocol, etc. by wrappers, like how the actual implementation works.
class _LibUSB(usb.backend.IBackend):
    def __init__(self, lib) -> None: ...
    def enumerate_devices(self) -> Iterable[_Device]: ...
    def get_parent(self, dev: _Device) -> _Device | None: ...
    def get_device_descriptor(self, dev: _Device) -> DeviceDescriptorProtocol: ...
    def get_configuration_descriptor(
        self, dev: _Device, config: int
    ) -> ConfigurationDescriptorProtocol: ...
    def get_interface_descriptor(
        self, dev: _Device, intf: int, alt: int, config: int
    ) -> InterfaceDescriptorProtocol: ...
    def get_endpoint_descriptor(
        self, dev: _Device, ep: int, intf: int, alt: int, config: int
    ) -> EndpointDescriptorProtocol: ...
    def open_device(self, dev: _Device) -> _DeviceHandle: ...
    def close_device(self, dev_handle: _DeviceHandle) -> None: ...
    def set_configuration(
        self, dev_handle: _DeviceHandle, config_value: int
    ) -> None: ...
    def get_configuration(self, dev_handle: _DeviceHandle) -> int: ...
    def set_interface_altsetting(
        self, dev_handle: _DeviceHandle, intf: int, altsetting: int
    ) -> None: ...
    def claim_interface(self, dev_handle: _DeviceHandle, intf: int) -> None: ...
    def release_interface(self, dev_handle: _DeviceHandle, intf: int) -> None: ...
    def bulk_write(
        self,
        dev_handle: _DeviceHandle,
        ep: int,
        intf: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    def bulk_read(
        self,
        dev_handle: _DeviceHandle,
        ep: int,
        intf: int,
        buff: array[int],
        timeout: int,
    ) -> int: ...
    def intr_write(
        self,
        dev_handle: _DeviceHandle,
        ep: int,
        intf: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    def intr_read(
        self,
        dev_handle: _DeviceHandle,
        ep: int,
        intf: int,
        buff: array[int],
        timeout: int,
    ) -> int: ...
    def iso_write(
        self,
        dev_handle: _DeviceHandle,
        ep: int,
        intf: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    def iso_read(
        self,
        dev_handle: _DeviceHandle,
        ep: int,
        intf: int,
        buff: array[int],
        timeout: int,
    ) -> int: ...
    def ctrl_transfer(
        self,
        dev_handle: _DeviceHandle,
        bmRequestType: int,
        bRequest: int,
        wValue: int,
        wIndex: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    def clear_halt(self, dev_handle: _DeviceHandle, ep: int) -> None: ...
    def reset_device(self, dev_handle: _DeviceHandle) -> None: ...
    def is_kernel_driver_active(self, dev_handle: _DeviceHandle, intf: int) -> bool: ...
    def detach_kernel_driver(self, dev_handle: _DeviceHandle, intf: int) -> None: ...
    def attach_kernel_driver(self, dev_handle: _DeviceHandle, intf: int) -> None: ...

def get_backend(find_library=None) -> _LibUSB | None: ...
