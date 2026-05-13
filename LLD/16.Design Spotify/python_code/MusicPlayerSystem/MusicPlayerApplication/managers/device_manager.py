from typing import Optional
from ..enums.device_type import DeviceType
from ..device.audio_output_device import IAudioOutputDevice
from ..factories.device_factory import DeviceFactory

class DeviceManager:
    _instance: Optional['DeviceManager'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DeviceManager, cls).__new__(cls)
            cls._instance._current_output_device = None
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'DeviceManager':
        return cls()

    def connect(self, device_type: DeviceType):
        # In Python, we don't need to manually delete the old device (GC handles it)
        self._current_output_device = DeviceFactory.create_device(device_type)

        if device_type == DeviceType.BLUETOOTH:
            print("Bluetooth device connected")
        elif device_type == DeviceType.WIRED:
            print("Wired device connected")
        elif device_type == DeviceType.HEADPHONES:
            print("Headphones connected")

    def get_output_device(self) -> IAudioOutputDevice:
        if not self._current_output_device:
            raise RuntimeError("No output device is connected.")
        return self._current_output_device

    def has_output_device(self) -> bool:
        return self._current_output_device is not None
