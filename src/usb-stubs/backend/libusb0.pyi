from array import array
from ctypes import *
import usb.backend
from collections.abc import Iterable, Sequence

from typing import NewType

__all__ = ["get_backend"]

_usb_dev_handle = NewType("_usb_dev_handle", c_void_p)

class _usb_endpoint_descriptor(Structure):
    bLength: int
    bDescriptorType: int
    bEndpointAddress: int
    bmAttributes: int
    wMaxPacketSize: int
    bInterval: int
    bRefresh: int
    bSynchAddress: int
    extra_descriptors: Sequence[int] | None

class _usb_interface_descriptor(Structure):
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

class _usb_config_descriptor(Structure):
    bLength: int
    bDescriptorType: int
    wTotalLength: int
    bNumInterfaces: int
    bConfigurationValue: int
    iConfiguration: int
    bmAttributes: int
    bMaxPower: int
    extra_descriptors: Sequence[int] | None

# Opaque type
class _usb_device(Structure): ...

class _DeviceDescriptor:
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

    def __init__(self, dev: _usb_device) -> None: ...

class _LibUSB(usb.backend.IBackend):
    def enumerate_devices(self) -> Iterable[_usb_device]: ...
    def get_device_descriptor(self, dev: _usb_device) -> _DeviceDescriptor: ...
    def get_configuration_descriptor(
        self, dev: _usb_device, config: int
    ) -> _usb_config_descriptor: ...
    def get_interface_descriptor(
        self, dev: _usb_device, intf: int, alt: int, config: int
    ) -> _usb_interface_descriptor: ...
    def get_endpoint_descriptor(
        self, dev: _usb_device, ep: int, intf: int, alt: int, config: int
    ) -> _usb_endpoint_descriptor: ...
    def open_device(self, dev: _usb_device) -> _usb_dev_handle: ...
    def close_device(self, dev_handle: _usb_dev_handle) -> None: ...
    def set_configuration(
        self, dev_handle: _usb_dev_handle, config_value: int
    ) -> None: ...
    def get_configuration(self, dev_handle: _usb_dev_handle) -> int: ...
    def set_interface_altsetting(
        self, dev_handle: _usb_dev_handle, intf: int, altsetting: int
    ) -> None: ...
    def claim_interface(self, dev_handle: _usb_dev_handle, intf: int) -> None: ...
    def release_interface(self, dev_handle: _usb_dev_handle, intf: int) -> None: ...
    def bulk_write(
        self,
        dev_handle: _usb_dev_handle,
        ep: int,
        intf: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    def bulk_read(
        self,
        dev_handle: _usb_dev_handle,
        ep: int,
        intf: int,
        buff: array[int],
        timeout: int,
    ) -> int: ...
    def intr_write(
        self,
        dev_handle: _usb_dev_handle,
        ep: int,
        intf: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    def intr_read(
        self,
        dev_handle: _usb_dev_handle,
        ep: int,
        intf: int,
        buff: array[int],
        timeout: int,
    ) -> int: ...
    def iso_write(
        self,
        dev_handle: _usb_dev_handle,
        ep: int,
        intf: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    def iso_read(
        self,
        dev_handle: _usb_dev_handle,
        ep: int,
        intf: int,
        buff: array[int],
        timeout: int,
    ) -> int: ...
    def ctrl_transfer(
        self,
        dev_handle: _usb_dev_handle,
        bmRequestType: int,
        bRequest: int,
        wValue: int,
        wIndex: int,
        data: array[int],
        timeout: int,
    ) -> int: ...
    def clear_halt(self, dev_handle: _usb_dev_handle, ep: int) -> None: ...
    def reset_device(self, dev_handle: _usb_dev_handle) -> None: ...
    def is_kernel_driver_active(
        self, dev_handle: _usb_dev_handle, intf: int
    ) -> bool: ...
    def detach_kernel_driver(self, dev_handle: _usb_dev_handle, intf: int) -> None: ...

def get_backend(find_library=None) -> _LibUSB | None: ...
