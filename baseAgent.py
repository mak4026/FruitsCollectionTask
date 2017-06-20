from typing import Tuple
from field import Field
from coord import Coord

class BaseAgent:
    def __init__(self, field: Field):
        pass

    def play_games(self) -> None:
        pass

    def play_one_game(self) -> int:
        pass

    def play_one_step(self) -> Tuple[Coord, int]:
        pass