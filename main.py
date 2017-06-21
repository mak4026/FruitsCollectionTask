from environment import Environment
from qLearning import QLearning
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

f = Field()
e = Environment(QLearning, f)
e.play()
e.dump_record()
print(f.storage)
# print(e.engine.qvalue)

with open('q-qvalue.json','w') as f:
    f.write(json.dumps(convert_keys(e.engine.qvalue), indent=4))
