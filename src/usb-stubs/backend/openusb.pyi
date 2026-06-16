from array import array
from ctypes import *
from typing import NewType

from typing_extensions import override
import usb.backend
from collections.abc import Iterable, Sequence

__all__ = [
    "get_backend",
    "OPENUSB_SUCCESS",
    "OPENUSB_PLATFORM_FAILURE",
    "OPENUSB_NO_RESOURCES",
    "OPENUSB_NO_BANDWIDTH",
    "OPENUSB_NOT_SUPPORTED",
    "OPENUSB_HC_HARDWARE_ERROR",
    "OPENUSB_INVALID_PERM",
    "OPENUSB_BUSY",
    "OPENUSB_BADARG",
    "OPENUSB_NOACCESS",
    "OPENUSB_PARSE_ERROR",
    "OPENUSB_UNKNOWN_DEVICE",
    "OPENUSB_INVALID_HANDLE",
    "OPENUSB_SYS_FUNC_FAILURE",
    "OPENUSB_NULL_LIST",
    "OPENUSB_CB_CONTINUE",
    "OPENUSB_CB_TERMINATE",
    "OPENUSB_IO_STALL",
    "OPENUSB_IO_CRC_ERROR",
    "OPENUSB_IO_DEVICE_HUNG",
    "OPENUSB_IO_REQ_TOO_BIG",
    "OPENUSB_IO_BIT_STUFFING",
    "OPENUSB_IO_UNEXPECTED_PID",
    "OPENUSB_IO_DATA_OVERRUN",
    "OPENUSB_IO_DATA_UNDERRUN",
    "OPENUSB_IO_BUFFER_OVERRUN",
    "OPENUSB_IO_BUFFER_UNDERRUN",
    "OPENUSB_IO_PID_CHECK_FAILURE",
    "OPENUSB_IO_DATA_TOGGLE_MISMATCH",
    "OPENUSB_IO_TIMEOUT",
    "OPENUSB_IO_CANCELED",
]

OPENUSB_SUCCESS: int
OPENUSB_PLATFORM_FAILURE: int
OPENUSB_NO_RESOURCES: int
OPENUSB_NO_BANDWIDTH: int
OPENUSB_NOT_SUPPORTED: int
OPENUSB_HC_HARDWARE_ERROR: int
OPENUSB_INVALID_PERM: int
OPENUSB_BUSY: int
OPENUSB_BADARG: int
OPENUSB_NOACCESS: int
OPENUSB_PARSE_ERROR: int
OPENUSB_UNKNOWN_DEVICE: int
OPENUSB_INVALID_HANDLE: int
OPENUSB_SYS_FUNC_FAILURE: int
OPENUSB_NULL_LIST: int
OPENUSB_CB_CONTINUE: int
OPENUSB_CB_TERMINATE: int
OPENUSB_IO_STALL: int
OPENUSB_IO_CRC_ERROR: int
OPENUSB_IO_DEVICE_HUNG: int
OPENUSB_IO_REQ_TOO_BIG: int
OPENUSB_IO_BIT_STUFFING: int
OPENUSB_IO_UNEXPECTED_PID: int
OPENUSB_IO_DATA_OVERRUN: int
OPENUSB_IO_DATA_UNDERRUN: int
OPENUSB_IO_BUFFER_OVERRUN: int
OPENUSB_IO_BUFFER_UNDERRUN: int
OPENUSB_IO_PID_CHECK_FAILURE: int
OPENUSB_IO_DATA_TOGGLE_MISMATCH: int
OPENUSB_IO_TIMEOUT: int
OPENUSB_IO_CANCELED: int

_openusb_devid = NewType("_openusb_devid", c_uint64)
_openusb_dev_handle = NewType("_openusb_dev_handle", c_uint64)

class _usb_endpoint_desc(Structure):
    bLength: int
    bDescriptorType: int
    bEndpointAddress: int
    bmAttributes: int
    wMaxPacketSize: int
    bInterval: int
    bRefresh: int
    bSynchAddress: int
    extra_descriptors: Sequence[int] | None

class _usb_interface_desc(Structure):
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

class _usb_config_desc(Structure):
    bLength: int
    bDescriptorType: int
    wTotalLength: int
    bNumInterfaces: int
    bConfigurationValue: int
    iConfiguration: int
    bmAttributes: int
    bMaxPower: int
    extra_descriptors: Sequence[int] | None

class _usb_device_desc(Structure):
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

class _OpenUSB(usb.backend.IBackend):
    @override
    def enumerate_devices(self) -> Iterable[_openusb_devid]: ...
    @override
    def get_device_descriptor(self, dev: _openusb_devid) -> _usb_device_desc: ...
    @override
    def get_configuration_descriptor(
        self, dev: _openusb_devid, config: int
    ) -> _usb_config_desc: ...
    @override
    def get_interface_descriptor(
        self, dev: _openusb_devid, intf: int, alt: int, config: int
    ) -> _usb_interface_desc: ...
    @override
    def get_endpoint_descriptor(
        self, dev: _openusb_devid, ep: int, intf: int, alt: int, config: int
    ) -> _usb_endpoint_desc: ...
    @override
    def open_device(self, dev: _openusb_devid) -> _openusb_dev_handle: ...
    @override
    def close_device(self, dev_handle: _openusb_dev_handle) -> None: ...
    @override
    def set_configuration(
        self, dev_handle: _openusb_dev_handle, config_value: int
    ) -> None: ...
    @override
    def get_configuration(self, dev_handle: _openusb_dev_handle) -> int: ...
    @override
    def set_interface_altsetting(
        self, dev_handle: _openusb_dev_handle, intf: int, altsetting: int
    ) -> None: ...
    @override
    def claim_interface(self, dev_handle: _openusb_dev_handle, intf: int) -> None: ...
    @override
    def release_interface(self, dev_handle: _openusb_dev_handle, intf: int) -> None: ...
    @override
    def bulk_write(
        self,
        dev_handle: _openusb_dev_handle,
        ep: int,
        intf: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    @override
    def bulk_read(
        self,
        dev_handle: _openusb_dev_handle,
        ep: int,
        intf: int,
        buff: array[int],
        timeout: int,
    ) -> int: ...
    @override
    def intr_write(
        self,
        dev_handle: _openusb_dev_handle,
        ep: int,
        intf: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    @override
    def intr_read(
        self,
        dev_handle: _openusb_dev_handle,
        ep: int,
        intf: int,
        buff: array[int],
        timeout: int,
    ) -> int: ...
    @override
    def ctrl_transfer(
        self,
        dev_handle: _openusb_dev_handle,
        bmRequestType: int,
        bRequest: int,
        wValue: int,
        wIndex: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    @override
    def reset_device(self, dev_handle: _openusb_dev_handle) -> None: ...
    @override
    def clear_halt(self, dev_handle: _openusb_dev_handle, ep: int) -> None: ...

def get_backend(find_library=None) -> _OpenUSB | None: ...
