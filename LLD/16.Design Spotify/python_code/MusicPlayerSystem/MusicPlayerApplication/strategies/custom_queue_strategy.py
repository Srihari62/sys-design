from collections import deque
from typing import Optional, List, Deque
from ..models.song import Song
from ..models.playlist import Playlist
from .play_strategy import PlayStrategy

class CustomQueueStrategy(PlayStrategy):
    def __init__(self):
        self._current_playlist: Optional[Playlist] = None
        self._current_index = -1
        self._next_queue: Deque[Song] = deque()
        self._prev_stack: List[Song] = []

    def _next_sequential(self) -> Song:
        if self._current_playlist.get_size() == 0:
            raise RuntimeError("Playlist is empty.")
        self._current_index += 1
        return self._current_playlist.get_songs()[self._current_index]

    def _previous_sequential(self) -> Song:
        if self._current_playlist.get_size() == 0:
            raise RuntimeError("Playlist is empty.")
        self._current_index -= 1
        return self._current_playlist.get_songs()[self._current_index]

    def set_playlist(self, playlist: Playlist):
        self._current_playlist = playlist
        self._current_index = -1
        self._next_queue.clear()
        self._prev_stack.clear()

    def has_next(self) -> bool:
        if not self._current_playlist:
            return False
        return bool(self._next_queue) or ((self._current_index + 1) < self._current_playlist.get_size())

    def next(self) -> Song:
        if not self._current_playlist or self._current_playlist.get_size() == 0:
            raise RuntimeError("No playlist loaded or playlist is empty.")

        if self._next_queue:
            song = self._next_queue.popleft()
            self._prev_stack.append(song)

            # Update index to match queued song if it exists in the playlist
            song_list = self._current_playlist.get_songs()
            for i, s in enumerate(song_list):
                if s == song:
                    self._current_index = i
                    break
            return song

        return self._next_sequential()

    def has_previous(self) -> bool:
        return bool(self._prev_stack) or (self._current_index - 1 >= 0)

    def previous(self) -> Song:
        if not self._current_playlist or self._current_playlist.get_size() == 0:
            raise RuntimeError("No playlist loaded or playlist is empty.")

        if self._prev_stack:
            song = self._prev_stack.pop()

            # Update index to match stacked song
            song_list = self._current_playlist.get_songs()
            for i, s in enumerate(song_list):
                if s == song:
                    self._current_index = i
                    break
            return song

        return self._previous_sequential()

    def add_to_next(self, song: Song):
        if song is None:
            raise ValueError("Cannot enqueue null song.")
        self._next_queue.append(song)
