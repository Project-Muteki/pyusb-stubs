"""
Public fields of various descriptors.
"""

from typing import Protocol
from collections.abc import Sequence

class DeviceDescriptorProtocol(Protocol):
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

class ConfigurationDescriptorProtocol(Protocol):
    bLength: int
    bDescriptorType: int
    wTotalLength: int
    bNumInterfaces: int
    bConfigurationValue: int
    iConfiguration: int
    bmAttributes: int
    bMaxPower: int
    extra_descriptors: Sequence[int] | None

class InterfaceDescriptorProtocol(Protocol):
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

class EndpointDescriptorProtocol(Protocol):
    bLength: int
    bDescriptorType: int
    bEndpointAddress: int
    bmAttributes: int
    wMaxPacketSize: int
    bInterval: int
    bRefresh: int
    bSynchAddress: int
    extra_descriptors: Sequence[int] | None
