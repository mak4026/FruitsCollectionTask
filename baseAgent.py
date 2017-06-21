from typing import Tuple
from field import Field
from coord import Coord

class BaseAgent:
    def __init__(self):
        pass

    def play_one_game(self, field: Field) -> int:
        pass

    def play_one_step(self, field: Field) -> Coord:
        pass
