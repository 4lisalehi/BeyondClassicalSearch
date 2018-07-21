from .Node import Node
from .consts import INF, SUCCESS
import random


class HillClimbing:

    def __init__(self, problem):
        self.problem = problem
        self.visited_count = 0
        self.generated_count = 0
        self.expanded_count = 0
        self.path = list()
        self.goal = None

    def simple(self):
        current_node = Node(state=self.problem.initial_state())

        while True:
            self.path.append(current_node)
            self.expanded_count += 1
            max_eval = -INF
            max_node = None
            for action in self.problem.actions(current_node.state):
                self.visited_count += 1
                next_node = Node(state=self.problem.result(current_node.state, action))
                next_node_eval = self.problem.evaluate(next_node.state)
                if next_node_eval > max_eval:
                    max_eval = next_node_eval
                    max_node = next_node
            current_eval = self.problem.evaluate(current_node.state)
            if max_eval <= current_eval:
                self.goal = current_node
                return current_node
            current_node = max_node

    def random(self):
        current_node = Node(state=self.problem.initial_state())

        while True:
            self.path.append(current_node)
            self.expanded_count += 1
            current_eval = self.problem.evaluate(current_node.state)
            uphills = list()
            for action in self.problem.actions(current_node.state):
                self.visited_count += 1
                next_node = Node(state=self.problem.result(current_node, action))
                next_node_eval = self.problem.evaluate(next_node.state)

                if next_node_eval > current_eval:
                    uphills.append(next_node)

            if not uphills:
                self.goal = current_node
                return current_node

            index = random.randrange(len(uphills))
            current_node = uphills[index]

    def stochastic(self):
        current_node = Node(state=self.problem.initial_state())

        while True:
            self.path.append(current_node)
            self.expanded_count += 1
            current_eval = self.problem.evaluate(current_node.state)
            next_nodes = list()
            node_indices = list()
            index = 0
            for action in self.problem.actions(current_node.state):
                self.visited_count += 1
                next_node = Node(state=self.problem.result(current_node, action))
                next_eval = self.problem.evaluate(next_node.state)
                if next_eval >= current_eval:
                    next_nodes.append(next_node)
                    scaled_fitness = int(self.problem.evaluate(next_node.state)*100)
                    for i in range(scaled_fitness):
                        node_indices.append(index)
                    index += 1
            if not next_nodes:
                self.goal = current_node
                return current_node
            random.shuffle(node_indices)
            node_index = random.randrange(len(node_indices))
            current_node = next_nodes[node_index]

    def first_choice(self):
        self.expanded_count += 1
        number_of_tries = 20
        current_node = Node(state=self.problem.initial_state())
        for _ in range(number_of_tries):
            next_node = Node(state=self.problem.get_random_successor(current_node.state))
            self.generated_count += 1
            if self.problem.evaluate(next_node.state) > self.problem.evaluate(current_node.state):
                return next_node
        return None

    def random_restart(self):
        solution = None
        temp_max = -float('inf')
        number_of_iterations = 10
        for _ in range(number_of_iterations):
            temp_solution = self.simple()
            if self.problem.evaluate(temp_solution.state) > temp_max:
                solution = temp_solution
                temp_max = self.problem.evaluate(solution)
        return solution
