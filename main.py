from algorithms import HillClimbing, SimulatedAnnealing, Genetic
from problems import GraphColoring, Keyboard, Alphabet

alphabet_choices = ['alphabet', 'alpha']
keyboard_choices = ['keyboard']
gc_choices = ['graph coloring', 'graph', 'gc']

genetic_choices = ['genetic', 'gene', 'genetic']
simple_hc_choices = ['hill climbing', 'hill', 'hc']
stochastic_hc_choices = ['stochastic hill climbing', 'stochastic hc', 'stochastic']


def main():

    which_question = input('Enter the question you want to solve:\n')

    if which_question.lower() in alphabet_choices:
        alphabet = Alphabet()
        which_algorithm = input('Enter the algorithm you want to solve the problem with:\n')

        if which_algorithm.lower() in simple_hc_choices:

            pass
    elif which_question.lower() in keyboard_choices:
        keyboard = Keyboard()
        pass
    elif which_question.lower() in gc_choices:
        graphColoring = GraphColoring()
        pass


if __name__ == '__main__':
    main()
