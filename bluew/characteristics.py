"""
bluew.devices
~~~~~~~~~~~~

This module provides a ble characteristic object, that should be returned
by any EngineBluew when queried for available characteristics of a device.


:copyright: (c) 2017 by Ahmed Alsharif.
:license: MIT, see LICENSE for more details.
"""


from bluew.ppobj import PPObj


class BLECharacteristic(PPObj):
    """BLE Characteristic."""

    def __init__(self, **kwargs):
        attrs = {'Value', 'Flags', 'Notifying',
                 'Service', 'UUID', 'Path', 'NotifyAcquired'}
        super().__init__(attrs, **kwargs)
