from typing import List
import random
from coord import Coord
from action import Action

class Field:
    field_size = 10
    storage_size = 10
    fruits_size = 5

    def __init__(self, storage: List[Coord] = None) -> None:
        if storage is None:
            world = [Coord(x,y) for x in range(Field.field_size) for y in range(Field.field_size)]
            self._storage = random.sample(world, Field.storage_size)
        else:
            self._storage = storage
        self._fruits = None

    @staticmethod
    def in_field(coord: Coord):
        return 0 <= coord.x and coord.x < Field.field_size \
               and 0 <= coord.y and coord.y < Field.field_size

    def place_fruits(self) -> None:
        self._fruits = random.sample(self.storage, Field.fruits_size)

    @property
    def storage(self):
        return self._storage

    @property
    def fruits(self):
        if self._fruits is None: raise ValueError("Fruits are not set.")
        return self._fruits

    def can_get_fruits(self, coord: Coord) -> bool:
        return coord in self._fruits

    def get_reward(self, coord: Coord) -> int:
        if self.can_get_fruits(coord):
            self.fruits.remove(coord)
            return 1
        else:
            return 0
