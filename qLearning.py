from field import Field
from action import Action
from coord import Coord
from baseAgent import BaseAgent
from random import randrange, random, choice

class QLearning(BaseAgent):
    EPSILON = 0.01
    ALPHA = 0.1
    GAMMA = 0.95
    TIME_LIMIT = 1000
    def __init__(self):
        self.t = 0
        self.qvalue = {}
        world = (Coord(x,y) for x in range(Field.field_size) for y in range(Field.field_size))
        for s in world:
            self.qvalue[s] = {}
            for a in Action:
                dst = s + a.value
                if Field.in_field(dst):
                    self.qvalue[s][a] = 1.0

    def play_one_game(self, field: Field) -> int:
        self.t = 0
        cur_s = Coord(randrange(Field.field_size), randrange(Field.field_size))
        while field.can_get_fruits(cur_s):
            cur_s = Coord(randrange(Field.field_size), randrange(Field.field_size))

        for t in range(QLearning.TIME_LIMIT):
            next_s = self.play_one_step(field, cur_s)
            if not field.fruits:
                # empty
                return t+1
            cur_s = next_s
            self.t += 1
        return QLearning.TIME_LIMIT

    def play_one_step(self, field: Field, cur: Coord) -> Coord:
        act = self.select_action(cur)
        dst = cur + act.value
        reward = float(field.get_reward(dst))
        max_q = max(self.qvalue[dst].values())
        self.qvalue[cur][act] = (self.qvalue[cur][act]
                    + QLearning.ALPHA
                    * (reward
                       + QLearning.GAMMA * max_q
                       - self.qvalue[cur][act]
                      )
                   )
        return dst

    def select_action(self, cur: Coord) -> Action:
        act = None
        # epsilon greedy
        if random() < self.EPSILON:
        # if random() < 1.0 / (self.t + 1):
            act = choice(list(self.qvalue[cur].keys()))
        else:
            act = max(self.qvalue[cur].items(), key=lambda x:x[1])[0]
            # print(act)
        return act
