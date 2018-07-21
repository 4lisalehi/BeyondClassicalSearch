from problems.Problem import Problem
import numpy as np


class Alphabet(Problem):

    def __init__(self):
        super().__init__()
        self.matrix = None
        self.n = 0
        self.m = 0
        self.k = 0
        self.words = list()

    def read_input(self):
        self.n, self.m = [int(x) for x in input().split()]
        self.matrix = np.array([['0'] * self.m] * self.n)
        self.k = int(input())

        self.words = input().split()

    def initial_state(self):
        return self.init_state

    def actions(self, state):
        pass

    def evaluate(self, state):
        val = 0
        for word in self.words:
            if self.check(state, word):
                val += 1
        return val

    def result(self, state, action):
        pass

    def dfs(self):
        pass
