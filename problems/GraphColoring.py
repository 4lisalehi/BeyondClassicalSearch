from .Problem import Problem
import numpy as np
from algorithms.State import State
from algorithms.Action import Action
from random import randrange


class GraphColoring(Problem):

    def __init__(self):
        super().__init__()
        self.n = 0
        self.k = 0
        self.graph_matrix = None
        self.colors = list()

    def read_input(self):
        self.n = int(input())
        self.k = int(input())
        self.graph_matrix = np.array([[False] * self.n] * self.n)
        for i in range(self.n):
            for j in range(self.n):
                self.graph_matrix[i, j] = int(input())
        colors = [0] * self.n
        for i in range(self.n):
            color = randrange(self.k) + 1
            colors[i] = color
        colors = [str(x) for x in colors]
        self.init_state.name = ''.join(colors)

    def initial_state(self):
        return self.init_state

    def goal_test(self, state):
        current_eval = self.evaluate(state)
        for action in self.actions(state):
            next_state = self.result(state, action)
            next_eval = self.evaluate(next_state)
            if next_eval < current_eval:
                return False
        return True

    def evaluate(self, state):
        val = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.graph_matrix[i, j] and state.name[i] == state.name[j]:
                    val += 1
        return val

    def actions(self, state):
        actions = list()
        for i in range(self.n):
            for k in range(1, self.k+1):
                if self.colors[i] != k:
                    actions.append(Action(name='{},{}'.format(i, k), cost=1))
        return actions

    def result(self, state, action):
        temp_name = "" + state.name
        i, c = action.name.split(',')
        i = int(i)
        c = int(c)
        charlist = list(temp_name)
        charlist[i] = c
        result_state = State(name=''.join(charlist))
        return result_state

    def get_first_choice(self, state):
        pass
