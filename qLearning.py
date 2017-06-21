from field import Field
from action import Action
from coord import Coord
from baseAgent import BaseAgent

class QLearning(BaseAgent):
    def __init__(self, field: Field):
        self.field = field
        self.EPSILON = 0.1
        self.ALPHA = 0.1
        self.GAMMA = 0.95
        self.t = 0
        self.qvalue = {}
        world = (Coord(x,y) for x in range(Field.field_size) for y in range(Field.field_size))
        for s in world:
            self.qvalue[s] = {}
            for a in Action:
                dst = s + a.value
                if Field.in_field(dst):
                    self.qvalue[s][a] = 0.0
