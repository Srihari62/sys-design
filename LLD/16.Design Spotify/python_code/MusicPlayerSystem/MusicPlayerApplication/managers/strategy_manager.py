from typing import Optional
from ..enums.play_strategy_type import PlayStrategyType
from ..strategies.play_strategy import PlayStrategy
from ..strategies.sequential_play_strategy import SequentialPlayStrategy
from ..strategies.random_play_strategy import RandomPlayStrategy
from ..strategies.custom_queue_strategy import CustomQueueStrategy

class StrategyManager:
    _instance: Optional['StrategyManager'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StrategyManager, cls).__new__(cls)
            cls._instance._sequential_strategy = SequentialPlayStrategy()
            cls._instance._random_strategy = RandomPlayStrategy()
            cls._instance._custom_queue_strategy = CustomQueueStrategy()
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'StrategyManager':
        return cls()

    def get_strategy(self, strategy_type: PlayStrategyType) -> PlayStrategy:
        if strategy_type == PlayStrategyType.SEQUENTIAL:
            return self._sequential_strategy
        elif strategy_type == PlayStrategyType.RANDOM:
            return self._random_strategy
        else:
            return self._custom_queue_strategy
