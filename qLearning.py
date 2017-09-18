from field import Field
from action import Action
from coord import Coord
from baseAgent import BaseAgent
from random import randrange, random, choice
from math import sqrt

def all_subset(list):
    return (frozenset(list[x] for x in range(len(list)) if ((i >> x) & 1 == 1)) for i in range(pow(2, len(list))) if bin(i).count("1") <= 5)
    # for i in range(1, pow(2, len(list))):
        # if bin(i).count("1") <= 5:
            # set(list[x] for x in len(list) if (i >> x) & 1 == 1)

class QLearning(BaseAgent):
    EPSILON = 0.1
    ALPHA = 0.1
    GAMMA = 0.95
    TIME_LIMIT = 300
    def __init__(self, field: Field):
        self.t = 0
        self.qvalue = {}
        world = (Coord(x,y) for x in range(Field.field_size) for y in range(Field.field_size))
        for s in world:
            self.qvalue[s] = {}
            for f in all_subset(field.storage):
                self.qvalue[s][f] = {}
                for a in Action:
                    dst = s + a.value
                    if Field.in_field(dst):
                        self.qvalue[s][f][a] = 0.5
                        if len(f) == 1 and s in f:
                            # terminal state
                            self.qvalue[s][f][a] = 0.0

    def play_one_game(self, field: Field) -> int:
        self.t += 1
        cur_s = Coord(randrange(Field.field_size), randrange(Field.field_size))
        while field.can_get_fruits(cur_s):
            cur_s = Coord(randrange(Field.field_size), randrange(Field.field_size))

        for t in range(QLearning.TIME_LIMIT):
            next_s = self.play_one_step(field, cur_s)
            if not field.fruits:
                # empty
                return t+1
            cur_s = next_s
        return QLearning.TIME_LIMIT

    def play_one_step(self, field: Field, cur: Coord) -> Coord:
        frt = frozenset(field.fruits)
        act = self.select_action(cur, frt)
        dst = cur + act.value
        reward = float(field.get_reward(dst))
        dst_frt = frozenset(field.fruits)
        max_q = max(self.qvalue[dst][dst_frt].values())
        self.qvalue[cur][frt][act] = (self.qvalue[cur][frt][act]
                    + QLearning.ALPHA
                    * (reward
                       + QLearning.GAMMA * max_q
                       - self.qvalue[cur][frt][act]
                      )
                   )
        return dst

    def select_action(self, cur: Coord, frt, eps=EPSILON) -> Action:
        act = None
        # epsilon greedy
        if random() < eps:
        # if random() < 1.0 / self.t:
            act = choice(list(self.qvalue[cur][frt].keys()))
        else:
            act = max(self.qvalue[cur][frt].items(), key=lambda x:x[1])[0]
            # print(act)
        return act

    def play_eval_game(self, field: Field) -> int:
        cur_s = Coord(randrange(Field.field_size), randrange(Field.field_size))
        while field.can_get_fruits(cur_s):
            cur_s = Coord(randrange(Field.field_size), randrange(Field.field_size))

        for t in range(QLearning.TIME_LIMIT):
            next_s = self.play_eval_one_step(field, cur_s, t)
            if not field.fruits:
                # empty
                return t + 1
            cur_s = next_s
        return QLearning.TIME_LIMIT

    def play_eval_one_step(self, field: Field, cur: Coord, t:int) -> Coord:
        frt = frozenset(field.fruits)
        act = self.select_action(cur, frt, 1/sqrt(t+1))
        dst = cur + act.value
        field.get_reward(dst)
        return dst
