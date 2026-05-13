from ..models.song import Song
from .audio_output_device import IAudioOutputDevice
from ..external.headphones_api import HeadphonesAPI

class HeadphonesAdapter(IAudioOutputDevice):
    def __init__(self, api: HeadphonesAPI):
        self._headphones_api = api

    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self._headphones_api.play_sound_via_jack(payload)
