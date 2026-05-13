from typing import Optional
from .core.audio_engine import AudioEngine
from .models.playlist import Playlist
from .models.song import Song
from .strategies.play_strategy import PlayStrategy
from .enums.device_type import DeviceType
from .enums.play_strategy_type import PlayStrategyType
from .managers.device_manager import DeviceManager
from .managers.playlist_manager import PlaylistManager
from .managers.strategy_manager import StrategyManager

class MusicPlayerFacade:
    _instance: Optional['MusicPlayerFacade'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MusicPlayerFacade, cls).__new__(cls)
            cls._instance._audio_engine = AudioEngine()
            cls._instance._loaded_playlist: Optional[Playlist] = None
            cls._instance._play_strategy: Optional[PlayStrategy] = None
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'MusicPlayerFacade':
        return cls()

    def connect_device(self, device_type: DeviceType):
        DeviceManager.get_instance().connect(device_type)

    def set_play_strategy(self, strategy_type: PlayStrategyType):
        self._play_strategy = StrategyManager.get_instance().get_strategy(strategy_type)

    def load_playlist(self, name: str):
        self._loaded_playlist = PlaylistManager.get_instance().get_playlist(name)
        if not self._play_strategy:
            raise RuntimeError("Play strategy not set before loading.")
        self._play_strategy.set_playlist(self._loaded_playlist)

    def play_song(self, song: Song):
        if not DeviceManager.get_instance().has_output_device():
            raise RuntimeError("No audio device connected.")
        device = DeviceManager.get_instance().get_output_device()
        self._audio_engine.play(device, song)

    def pause_song(self, song: Song):
        if self._audio_engine.get_current_song_title() != song.get_title():
            raise RuntimeError(f'Cannot pause "{song.get_title()}"; not currently playing.')
        self._audio_engine.pause()

    def play_all_tracks(self):
        if not self._loaded_playlist:
            raise RuntimeError("No playlist loaded.")
        
        while self._play_strategy.has_next():
            next_song = self._play_strategy.next()
            device = DeviceManager.get_instance().get_output_device()
            self._audio_engine.play(device, next_song)
        
        print(f"Completed playlist: {self._loaded_playlist.get_playlist_name()}")

    def play_next_track(self):
        if not self._loaded_playlist:
            raise RuntimeError("No playlist loaded.")
        
        if self._play_strategy.has_next():
            next_song = self._play_strategy.next()
            device = DeviceManager.get_instance().get_output_device()
            self._audio_engine.play(device, next_song)
        else:
            print(f"Completed playlist: {self._loaded_playlist.get_playlist_name()}")

    def play_previous_track(self):
        if not self._loaded_playlist:
            raise RuntimeError("No playlist loaded.")
        
        if self._play_strategy.has_previous():
            prev_song = self._play_strategy.previous()
            device = DeviceManager.get_instance().get_output_device()
            self._audio_engine.play(device, prev_song)
        else:
            print(f"Completed playlist: {self._loaded_playlist.get_playlist_name()}")

    def enqueue_next(self, song: Song):
        if not self._play_strategy:
            raise RuntimeError("Play strategy not set.")
        self._play_strategy.add_to_next(song)
