import math
import random


class SimulatedAnnealing:

    def __init__(self, problem):
        self.problem = problem
        self.generated_count = 0
        self.expanded_count = 0
        self.actions_count = 0

    def solve(self, schedule):
        current_node = self.problem.generate_initial_node()
        self.generated_count += 1
        t = 1
        while True:
            self.actions_count += 1
            T = schedule(t)
            if T <= math.pow(10, -5):  # it's almost zero.
                return current_node
            next_node = self.problem.get_random_successor(current_node)
            self.generated_count += 1
            delta_e = self.problem.evaluate(next_node.state) - self.problem.evaluate(current_node.state)
            if delta_e > 0:
                self.expanded_count += 1
                current_node = next_node
            elif random.random() < math.exp(delta_e / T):
                current_node = next_node
                self.expanded_count += 1
            t += 1
