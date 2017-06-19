from typing import List
import random
from Coord import Coord

class Field:
    field_size = 10
    storage_size = 10
    fruits_size = 5

    def __init__(self, storage: List[Coord]) -> None:
        world = [Coord(x,y) for x in range(Field.field_size) for y in range(Field.field_size)]
        self.storage = random.sample(world, Field.storage_size)
        self.fruits = None

    def copy(self, storage: List[Coord]):

        self.storage = storage
        self.fruits = None

    @staticmethod
    def in_field(coord: Coord):
        return 0 <= coord.x and coord.x < Field.field_size \
               and 0 <= coord.y and coord.y < Field.field_size

    def place_fruits(self) -> None:
        self.fruits = random.sample(self.storage, Field.fruits_size)

