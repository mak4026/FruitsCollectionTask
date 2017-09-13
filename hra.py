from field import Field
from action import Action
from coord import Coord
from qLearning import QLearning
from random import randrange, random, choice
from itertools import product

class HybridRewardArchitecture(QLearning):
    def __init__(self, field: Field):
        self.t = 0
        self.qvalue = {}
        for st in field.storage:
            self.qvalue[st] = {}
            world = (Coord(x,y) for x in range(Field.field_size) for y in range(Field.field_size))
            for s in world:
                self.qvalue[st][s] = {}
                for a in Action:
                    dst = s + a.value
                    if Field.in_field(dst):
                        self.qvalue[st][s][a] = 1.0
                        if st == s:
                            self.qvalue[st][s][a] = 0.0

    def play_one_step(self, field: Field, cur: Coord) -> Coord:
        frt = frozenset(field.fruits)
        act = self.select_action(cur, frt)
        dst = cur + act.value
        reward = field.get_reward(dst)
        dst_frt = frozenset(field.fruits)

        # qvalue update
        for f in frt:
            if f in dst_frt:
                # dst_frtの中からはrewardは発生しない
                r = 0.0
            else:
                r = float(reward)

            max_q = max(self.qvalue[f][dst].values())
            self.qvalue[f][cur][act] = (self.qvalue[f][cur][act]
                    + QLearning.ALPHA
                    * (r
                       + QLearning.GAMMA * max_q
                       - self.qvalue[f][cur][act]
                      )
                   )
        return dst

    def select_action(self, cur: Coord, frt, eps=QLearning.EPSILON) -> Action:
        act = None
        # epsilon greedy
        if random() < eps:
            act = choice(list(Action))
            while not Field.in_field(cur + act.value):
                act = choice(list(Action))
        else:
            cur_qvalue = {a: 0.0 for a in Action if Field.in_field(cur + a.value)}
            for afrt, a in product(frt, cur_qvalue.keys()):
                cur_qvalue[a] += self.qvalue[afrt][cur][a]
            act = max(cur_qvalue.items(), key=lambda x:x[1])[0]
        return act
