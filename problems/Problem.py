from algorithms.State import State


class Problem:

    def __init__(self):
        self.init_state = State()

    def read_input(self):
        pass

    def initial_state(self):
        return self.init_state

    def random_initial_state(self):
        pass

    def actions(self, state):
        return []

    def result(self, state, action):
        return None

    def transition_model(self):
        pass

    def step_cost(self, state, action):
        return 0

    def path_cost(self, actions):
        return 0

    def goal_test(self, state):
        return False

    def evaluate(self, state):
        return 0

    def get_first_choice(self, state):
        pass
