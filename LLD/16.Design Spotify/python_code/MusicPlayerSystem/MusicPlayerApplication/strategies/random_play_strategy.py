import random
from typing import List, Optional
from ..models.song import Song
from ..models.playlist import Playlist
from .play_strategy import PlayStrategy

class RandomPlayStrategy(PlayStrategy):
    def __init__(self):
        self._current_playlist: Optional[Playlist] = None
        self._remaining_songs: List[Song] = []
        self._history: List[Song] = []

    def set_playlist(self, playlist: Playlist):
        self._current_playlist = playlist
        if not self._current_playlist or self._current_playlist.get_size() == 0:
            return

        self._remaining_songs = list(self._current_playlist.get_songs())
        self._history = []

    def has_next(self) -> bool:
        return bool(self._current_playlist and self._remaining_songs)

    def next(self) -> Song:
        if not self._current_playlist or self._current_playlist.get_size() == 0:
            raise RuntimeError("No playlist loaded or playlist is empty.")
        if not self._remaining_songs:
            raise RuntimeError("No songs left to play")

        idx = random.randint(0, len(self._remaining_songs) - 1)
        selected_song = self._remaining_songs.pop(idx)
        self._history.append(selected_song)
        return selected_song

    def has_previous(self) -> bool:
        return len(self._history) > 0

    def previous(self) -> Song:
        if not self._history:
            raise RuntimeError("No previous song available.")

        return self._history.pop()
