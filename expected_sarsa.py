from field import Field
from action import Action
from coord import Coord
from qLearning import QLearning
from random import randrange, random, choice

class ExpectedSarsa(QLearning):
    def __init__(self, field: Field):
        super().__init__(field)

    def play_one_step(self, field: Field, cur: Coord) -> Coord:
        frt = frozenset(field.fruits)
        act = self.select_action(cur, frt)
        dst = cur + act.value
        reward = float(field.get_reward(dst))
        dst_frt = frozenset(field.fruits)
        # max_q = max(self.qvalue[dst][dst_frt].values())
        sarsa_value = self.expected_qvalue(dst, dst_frt)
        self.qvalue[cur][frt][act] = (self.qvalue[cur][frt][act]
                    + QLearning.ALPHA
                    * (reward
                       + QLearning.GAMMA * sarsa_value
                       - self.qvalue[cur][frt][act]
                      )
                   )
        return dst

    def expected_qvalue(self, cur: Coord, frt) -> float:
        max_act = max(self.qvalue[cur][frt].items(), key=lambda x:x[1])[0]
        n = len(self.qvalue[cur][frt])
        ans = 0.0
        for a in self.qvalue[cur][frt].keys():
            if a is not max_act:
                ans += (QLearning.EPSILON / n) * self.qvalue[cur][frt][a]
            else:
                ans += (QLearning.EPSILON / n + 1.0 - QLearning.EPSILON) * self.qvalue[cur][frt][a]
        return ans
