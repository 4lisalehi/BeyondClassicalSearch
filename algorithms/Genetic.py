import random


class Genetic:

    def __init__(self, problem, generation_count = 1000):
        self.problem = problem
        self.current_fitness_function = self.problem.fitness_function
        self.generation_count = generation_count
        # self.population_size = population_size

    def reproduce(self, x, y):
        x_state = x.state
        y_state = y.state
        length = len(x_state)
        index = random.randrange(length)
        return x_state[0:index] + y_state[index:length]

    def mutate(self, individual):
        return self.problem.mutate(individual)

    def initial_population(self, population_size):
        population = list()
        for i in range(population_size):
            node = self.problem.generateInitialNode()
            population.append(node)
        return population

    def select_parent(self, population, crossover_rate):
        i = 0
        while random.random() > crossover_rate:
            i += 1
        return population[i - 1]

    def select_couples(self, population, population_size):
        couples = list()
        crossover_rate = 0.25
        for _ in range(population_size):
            p1 = self.select_parent(population, crossover_rate)
            p2 = self.select_parent(population, crossover_rate)
            couples.append([p1, p2])
        return couples

    def get_population_fitness_details(self, problem, population):
        summation = problem.evaluate(population[0])
        best_node = worst_node = population[0]
        i = 1
        while i < len(population):
            summation += problem.evaluate(population[i])
            if problem.evaluate(population[i]) > problem.evaluate(best_node):
                best_node = population[i]
            elif problem.evaluate(population[i]) < problem.evaluate(worst_node):
                worst_node = population[i]
            i += 1
        return [worst_node, best_node, summation / len(population)]

    def weighted_choice(self, choices):
        total = sum(w for c, w in choices)
        choices_dict = dict(choices)
        r = random.uniform(0, total)
        upto = 0
        for k, v in choices_dict:
            if upto + v >= r:
                return k
            upto += v

    def select_new_population_roulette_wheel(self, nodes, population_size):
        choices = list()
        for node in nodes:
            choices.append((node, self.problem.evaluate(node)))
        selected_population = list()
        for i in range(population_size):
            selected_population.append(self.weighted_choice(choices))
        return selected_population

    def solve(self, problem, population_size=20, iterations=1000):

        population = self.initial_population(population_size)
        for i in range(iterations):
            offsprings = list()
            if problem.goalTest(population[0]):
                print('optimal solution found!')
                return population[0]
            couples = self.select_couples(population, population_size)
            for c in couples:
                offsprings.append(problem.doCrossover(c[0], c[1]))
            mutated_off_springs = list()
            for node in offsprings:
                problem.doMutation(node)
                mutated_off_springs.append(node)
            population = population + mutated_off_springs
            population = self.select_new_population_roulette_wheel(problem, population, population_size)
            details = self.get_population_fitness_details(problem, population)
            print('Details of generation #{}:'.format(i + 1))
            print('Worst node of the this generation:')
            problem.showNodeState(details[0])
            print('the best node:')
            problem.showNodeState(details[1])
            print('and average fitness of this generation is', details[2])
            print('_' * 100)
        print('this is the best found solution after ', iterations, ' iterations!')
        return population[0]
