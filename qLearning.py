from baseAgent import BaseAgent

class QLearning(BaseAgent):
    def __init__(self):
        self.history = []
        self.EPSILON = 0.1
        self.ALPHA = 0.1
        self.GAMMA = 0.95
        self.t = 0
        self.qvalue = {}