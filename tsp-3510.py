import sys
import math
import operator

# argument parsing
inputFile = sys.argv[1]
outputFile = sys.argv[2]
time = sys.argv[3]

coords = {}

def create_graph(coords):
    distances = {}
    for node1, coords1 in coords.items():
        distances[node1] = {}
        for node2, coords2 in coords.items():
            distances[node1][node2] = dist(coords1, coords2)
    return distances

def dist(node1, node2):
    d = [node1[0] - node2[0], node1[1] - node2[1]]
    return round(math.sqrt(d[0] ** 2 + d[1] ** 2))

def mst_kruskal(graph):
    mst = []

    if len(graph) == 0:
        return []
    if len(graph) == 1:
        mst.append(graph[0])
        return mst

    edges = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            # avoid adding edges to self and two edges for each edge
            if vertex != neighbor and vertex < neighbor:
                edges.append((vertex,neighbor,graph[vertex][neighbor]))

    edges.sort(key = operator.itemgetter(2))
    print(edges)

with open(inputFile, 'r') as reader:
    for line in reader.readlines():
        lineDataArr = line.split()
        coords[int(lineDataArr[0].replace('.',''))] = (float(lineDataArr[1]), float(lineDataArr[2]))

graph = create_graph(coords)
mst_kruskal(graph)