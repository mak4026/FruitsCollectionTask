from coord import Coord
from baseAgent import BaseAgent
from field import Field
from typing import Callable
import sys
class Environment:
    def  __init__(self, engine: Callable[[Field], BaseAgent], field: Field, limit: int = 10000):
        self.field = field
        self.engine = engine(field)
        self.history = []
        self.LIMIT = limit

    def play(self):
        for t in range(self.LIMIT):
            if __debug__: sys.stderr.write("time: {}\n".format(t))
            cur_field = Field(self.field.storage)
            cur_field.place_fruits()
            record = self.engine.play_one_game(cur_field)
            self.history.append(record)

    def dump_record(self, name = None):
        filename = name or self.engine.__class__.__name__
        with open(filename+'.csv', 'w') as f:
            for i, r in enumerate(self.history):
                f.write("{},{}\n".format(i, r))
