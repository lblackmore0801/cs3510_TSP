import sys
import math
import operator

# argument parsing
inputFile = sys.argv[1]
outputFile = sys.argv[2]
time = sys.argv[3]

coords = {}

def create_graph(coords):
    graph = {'vertices':[], 'edges': []}
    for node1, coords1 in coords.items():
        if node1 not in graph['vertices']:
            graph['vertices'].append(node1)
        for node2, coords2 in coords.items():
            if node1 != node2 and node1 < node2:
                graph['edges'].append((dist(coords1,coords2), node1, node2))
    return graph

def dist(node1, node2):
    d = [node1[0] - node2[0], node1[1] - node2[1]]
    return round(math.sqrt(d[0] ** 2 + d[1] ** 2))

parent = {}
rank = {}

def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if vertex != parent[vertex]:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] <= rank[root2]:
            parent[root1] = root2
        else:
	        parent[root2] = root1
    if rank[root1] == rank[root2]:
        rank[root2] += 1

def kruskal(graph):
    for vertex in graph['vertices']:
        make_set(vertex)
        minimum_spanning_tree = set()
        edges = graph['edges']
        edges.sort()
	#print edges
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):
            union(vertex, vertex2)
            minimum_spanning_tree.add(edge)
	    
    return sorted(minimum_spanning_tree)

with open(inputFile, 'r') as reader:
    for line in reader.readlines():
        lineDataArr = line.split()
        coords[int(lineDataArr[0].replace('.',''))] = (float(lineDataArr[1]), float(lineDataArr[2]))

print(coords)
graph = create_graph(coords)
print(graph)
mst = kruskal(graph)
print(mst)