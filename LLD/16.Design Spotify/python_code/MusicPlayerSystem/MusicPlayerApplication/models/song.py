class Song:
    def __init__(self, title: str, artist: str, file_path: str):
        self._title = title
        self._artist = artist
        self._file_path = file_path

    @property
    def title(self) -> str:
        return self._title

    @property
    def artist(self) -> str:
        return self._artist

    @property
    def file_path(self) -> str:
        return self._file_path

    # Keep original getter names for compatibility with translated code if needed
    def get_title(self) -> str:
        return self._title

    def get_artist(self) -> str:
        return self._artist

    def get_file_path(self) -> str:
        return self._file_path
