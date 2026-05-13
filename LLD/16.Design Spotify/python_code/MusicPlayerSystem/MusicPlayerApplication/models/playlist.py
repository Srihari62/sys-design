from typing import List
from .song import Song

class Playlist:
    def __init__(self, name: str):
        self._playlist_name = name
        self._song_list: List[Song] = []

    def get_playlist_name(self) -> str:
        return self._playlist_name

    def get_songs(self) -> List[Song]:
        return self._song_list

    def get_size(self) -> int:
        return len(self._song_list)

    def add_song_to_playlist(self, song: Song):
        if song is None:
            raise ValueError("Cannot add null song to playlist.")
        self._song_list.append(song)
