from typing import List, Tuple
from environment import Environment
from qLearning import QLearning
from expected_sarsa import ExpectedSarsa
from hra import HybridRewardArchitecture

from field import Field
import json
import sys

from coord import Coord
from action import Action

def convert_keys(obj, convert=str):
    if isinstance(obj, list):
        return [convert_keys(i, convert) for i in obj]
    if not isinstance(obj, dict):
        return obj
    return {convert(k): convert_keys(v, convert) for k, v in obj.items()}

def view_history_graph(histories: List[Tuple[List[int], str]], num: int = 10) -> None:
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    for h in histories:
        # なめらかにする
        x = np.arange(len(h[0]))
        b = np.ones(num)/num
        y = np.convolve(np.array(h[0]), b, mode='same')
        plt.plot(x, y, label=h[1], antialiased=True)
    plt.title("FruitsCollectionTask")
    plt.xlabel("Episodes")
    plt.ylabel("Steps")
    plt.legend()

    plt.show()


f = Field()
f2 = Field(f.storage)
print(f.storage)
# e = Environment(QLearning, f)

e = Environment(HybridRewardArchitecture, f)
e.play()
e.dump_record()

e2 = Environment(ExpectedSarsa, f)
e2.play()
e2.dump_record()

# with open('q-qvalue.json','w') as f:
#     f.write(json.dumps(convert_keys(e.engine.qvalue), indent=4))

# view_history_graph([(e.history, e.engine.__class__.__name__)])
view_history_graph([(e.history, e.engine.__class__.__name__),
                    (e2.history, e2.engine.__class__.__name__)])

