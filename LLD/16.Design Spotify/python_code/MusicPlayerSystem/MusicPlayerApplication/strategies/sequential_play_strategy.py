from typing import Optional
from ..models.song import Song
from ..models.playlist import Playlist
from .play_strategy import PlayStrategy

class SequentialPlayStrategy(PlayStrategy):
    def __init__(self):
        self._current_playlist: Optional[Playlist] = None
        self._current_index = -1

    def set_playlist(self, playlist: Playlist):
        self._current_playlist = playlist
        self._current_index = -1

    def has_next(self) -> bool:
        if not self._current_playlist:
            return False
        return (self._current_index + 1) < self._current_playlist.get_size()

    def next(self) -> Song:
        if not self._current_playlist or self._current_playlist.get_size() == 0:
            raise RuntimeError("No playlist loaded or playlist is empty.")
        
        self._current_index += 1
        return self._current_playlist.get_songs()[self._current_index]

    def has_previous(self) -> bool:
        return self._current_index - 1 >= 0

    def previous(self) -> Song:
        if not self._current_playlist or self._current_playlist.get_size() == 0:
            raise RuntimeError("No playlist loaded or playlist is empty.")
        
        self._current_index -= 1
        return self._current_playlist.get_songs()[self._current_index]
