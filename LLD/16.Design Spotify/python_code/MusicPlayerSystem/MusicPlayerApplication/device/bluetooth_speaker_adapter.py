from ..models.song import Song
from .audio_output_device import IAudioOutputDevice
from ..external.bluetooth_speaker_api import BluetoothSpeakerAPI

class BluetoothSpeakerAdapter(IAudioOutputDevice):
    def __init__(self, api: BluetoothSpeakerAPI):
        self._bluetooth_api = api

    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self._bluetooth_api.play_sound_via_bluetooth(payload)
