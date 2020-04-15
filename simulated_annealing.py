import math
import random
import sys

class SimulatedAnnealing(object):
    def __init__(self, coords, temp=-1, alpha=-1, stopping_temp=-1, stopping_iter=-1):
        self.coords = coords
        self.numof_nodes = len(coords)
        self.temp = math.sqrt(self.numof_nodes) if temp == -1 else temp
        self.initial_temp = self.temp  # save inital T to reset if batch annealing is used
        self.alpha = 0.995 if alpha == -1 else alpha
        self.stopping_temp = 1e-8 if stopping_temp == -1 else stopping_temp
        self.stopping_iter = 100000 if stopping_iter == -1 else stopping_iter
        self.iteration = 1

        self.nodes = []
        for node in range(self.numof_nodes):
            self.nodes.append(node)

        self.best_solution = None
        self.best_fitness = float("Inf")  # equivalent to the shortest tour length
        self.fitness_list = []

    # calculate the euclidean distance between two points
    # CHANGED
    def dist(self, node1, node2):
        d = [self.coords[node1][0] - self.coords[node2][0], self.coords[node1][1] - self.coords[node2][1]]
        return round(math.sqrt(d[0] ** 2 + d[1] ** 2))    

    # nearest neighbor
    # CHANGED
    def initial_solution(self):
        start_node = random.choice(self.nodes)  # start from a random node
        solution = [start_node]

        unvisited = set(self.nodes)
        unvisited.remove(start_node)

        while unvisited:
            next_node = None
            min_dist = float('inf')
            for node in unvisited:
                if self.dist(start_node, node) < min_dist:
                    min_dist = self.dist(start_node, node)
                    next_node = node
            unvisited.remove(next_node)
            solution.append(next_node)
            start_node = next_node

        solution.append(solution[0])
        curr_fitness = self.fitness(solution)

        if curr_fitness < self.best_fitness:  # If best found so far, update best fitness
            self.best_fitness = curr_fitness
            self.best_solution = solution
        self.fitness_list.append(curr_fitness)
        return solution, curr_fitness

    def fitness(self, solution):
        """
        Total distance of the current solution path.
        """
        cur_fit = 0
        for i in range(self.numof_nodes):
            cur_fit += self.dist(solution[i % self.numof_nodes], solution[(i + 1) % self.numof_nodes])
        return cur_fit

    def p_accept(self, candidate_fitness):
        """
        Probability of accepting if the candidate is worse than current.
        Depends on the current temperature and difference between candidate and current.
        """
        return math.exp(-abs(candidate_fitness - self.cur_fitness) / self.temp)

    def accept(self, candidate):
        """
        Accept with probability 1 if candidate is better than current.
        Accept with probabilty p_accept(..) if candidate is worse.
        """
        candidate_fitness = self.fitness(candidate)
        if candidate_fitness < self.cur_fitness:
            self.cur_fitness, self.cur_solution = candidate_fitness, candidate
            if candidate_fitness < self.best_fitness:
                self.best_fitness, self.best_solution = candidate_fitness, candidate
        else:
            if random.random() < self.p_accept(candidate_fitness):
                self.cur_fitness, self.cur_solution = candidate_fitness, candidate

    def anneal(self):
        """
        Execute simulated annealing algorithm.
        """
        # Initialize with the greedy solution.
        self.cur_solution, self.cur_fitness = self.initial_solution()

        print("Starting annealing.")
        while self.temp >= self.stopping_temp and self.iteration < self.stopping_iter:
            candidate = list(self.cur_solution)
            l = random.randint(2, self.numof_nodes - 1)
            i = random.randint(0, self.numof_nodes - l)
            candidate[i : (i + l)] = reversed(candidate[i : (i + l)])
            self.accept(candidate)
            self.temp *= self.alpha
            self.iteration += 1

            self.fitness_list.append(self.cur_fitness)

        print("Best fitness obtained: ", self.best_fitness)
        improvement = 100 * (self.fitness_list[0] - self.best_fitness) / (self.fitness_list[0])
        print(f"Improvement over greedy heuristic: {improvement : .2f}%")

    def batch_anneal(self, times=10):
        """
        Execute simulated annealing algorithm `times` times, with random initial solutions.
        """
        for i in range(1, times + 1):
            print(f"Iteration {i}/{times} -------------------------------")
            self.temp = self.initial_temp
            self.iteration = 1
            self.cur_solution, self.cur_fitness = self.initial_solution()
            self.anneal()