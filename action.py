from enum import Enum
from coord import Coord

class Action(Enum):
    UP = Coord(0, 1)
    DOWN = Coord(0, -1)
    LEFT = Coord(-1, 0)
    RIGHT = Coord(1, 0)
