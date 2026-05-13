from ..models.song import Song
from .audio_output_device import IAudioOutputDevice
from ..external.wired_speaker_api import WiredSpeakerAPI

class WiredSpeakerAdapter(IAudioOutputDevice):
    def __init__(self, api: WiredSpeakerAPI):
        self._wired_api = api

    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self._wired_api.play_sound_via_cable(payload)
