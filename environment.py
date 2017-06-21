from coord import Coord
from baseAgent import BaseAgent
from field import Field
class Environment:
    def  __init__(self, engine: BaseAgent, field: Field, limit: int = 10000):
        self.field = field
        self.engine = engine(field)
        self.history = []
        self.LIMIT = limit

    # def play(self):
    #     for t in range(self.LIMIT):
    #         cur_field = Field(self.field.storage)
    #         cur_field.place_fruits()
