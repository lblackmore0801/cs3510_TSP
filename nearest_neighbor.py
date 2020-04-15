import sys
import math

inputFile = sys.argv[1]
outputFile = sys.argv[2]
time = sys.argv[3]

coords = {}

with open(inputFile, 'r') as reader:
    for line in reader.readlines():
        lineDataArr = line.split()
        coords[int(lineDataArr[0].replace('.',''))] = (float(lineDataArr[1]), float(lineDataArr[2]))

def create_graph(coords):
    distances = []
    cities = []
    for node1, coords1 in coords.items():
        distances.append([])
        cities.append(node1)
        for node2, coords2 in coords.items():
            distances[node1 - 1].append(dist(coords1, coords2))
    return distances, cities

def dist(node1, node2):
    d = [node1[0] - node2[0], node1[1] - node2[1]]
    return round(math.sqrt(d[0] ** 2 + d[1] ** 2))

distances, cities = create_graph(coords)

def tsp(cities):
    start = cities[0]
    tour = [start]
    cities.remove(start)
    total_length = 0
    while cities:
        nn, length = nearest_neighbor(tour[-1], cities)
        total_length += length
        tour.append(nn)
        cities.remove(nn)
    total_length += distances[tour[-1] - 1][start - 1]
    tour.append(start)
    return tour, total_length

def nearest_neighbor(prev_city, cities):
    next_city = -1
    min_dist = float('inf')
    for city in cities:
        if distances[prev_city - 1][city - 1] < min_dist:
            min_dist = distances[prev_city - 1][city - 1]
            next_city = city
    return next_city, min_dist
    

tsp_tour, tour_length = tsp(cities)
print(tsp_tour)
print(tour_length)