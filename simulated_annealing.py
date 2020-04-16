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

        self.best_solution = None      # equivalent to the tour of nodes
        self.best_dist = float("Inf")  # equivalent to the shortest tour length
        self.distance_list = []

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
        curr_distance = self.path_dist(solution)
        solution.remove(solution[-1])
        if curr_distance < self.best_dist:  # If best found so far, update best distance
            self.best_dist = curr_distance
            self.best_solution = solution
        self.distance_list.append(curr_distance)
        return solution, curr_distance

    # distance of current path
    # CHANGED
    def path_dist(self, solution):
        curr_dist = 0
        for i in range(self.numof_nodes):
            curr_dist += self.dist(solution[i % self.numof_nodes], solution[(i + 1) % self.numof_nodes])
        return curr_dist

    # decide if candidate should be accepted or not based on probability
    # CHANGED
    def accept(self, candidate):
        candidate.append(candidate[0])
        candidate_dist = self.path_dist(candidate)
        candidate.remove(candidate[-1])
        if candidate_dist < self.curr_distance:
            self.curr_distance, self.curr_solution = candidate_dist, candidate
            if candidate_dist < self.best_dist:
                self.best_dist, self.best_solution = candidate_dist, candidate
        else:
            prob_acceptance = math.exp(-abs(candidate_dist - self.curr_distance) / self.temp)
            if random.random() < prob_acceptance:
                self.curr_distance, self.curr_solution = candidate_dist, candidate

    # run annealing algo
    # CHANGED
    def anneal(self):
        self.curr_solution, self.curr_distance = self.initial_solution()

        print("Start:")
        while self.temp >= self.stopping_temp and self.iteration < self.stopping_iter:
            candidate = list(self.curr_solution)
            l = random.randint(2, self.numof_nodes - 1)
            i = random.randint(0, self.numof_nodes - l)
            candidate[i : (i + l)] = reversed(candidate[i : (i + l)])
            self.accept(candidate)
            self.temp *= self.alpha
            self.iteration += 1

            self.distance_list.append(self.curr_distance)
        self.best_solution.append(self.best_solution[0])
        print("Best path obtained: ", self.best_solution)
        print("Best path length obtained: ", self.best_dist)
        improvement = 100 * (self.distance_list[0] - self.best_dist) / (self.distance_list[0])
        print(f"Improvement over greedy: {improvement : .2f}%")