from typing import Optional
from ..models.song import Song
from ..device.audio_output_device import IAudioOutputDevice

class AudioEngine:
    def __init__(self):
        self._current_song: Optional[Song] = None
        self._song_is_paused = False

    def get_current_song_title(self) -> str:
        if self._current_song:
            return self._current_song.get_title()
        return ""

    def is_paused(self) -> bool:
        return self._song_is_paused

    def play(self, aod: IAudioOutputDevice, song: Song):
        if song is None:
            raise ValueError("Cannot play a null song.")
        
        # Resume if same song was paused
        if self._song_is_paused and song == self._current_song:
            self._song_is_paused = False
            print(f"Resuming song: {song.get_title()}")
            aod.play_audio(song)
            return

        self._current_song = song
        self._song_is_paused = False
        print(f"Playing song: {song.get_title()}")
        aod.play_audio(song)

    def pause(self):
        if self._current_song is None:
            raise RuntimeError("No song is currently playing to pause.")
        if self._song_is_paused:
            raise RuntimeError("Song is already paused.")
        
        self._song_is_paused = True
        print(f"Pausing song: {self._current_song.get_title()}")
