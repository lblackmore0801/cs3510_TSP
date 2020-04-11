import sys
import math

# argument parsing
inputFile = sys.argv[1]
outputFile = sys.argv[2]
time = sys.argv[3]

coords = {}
distances = {}

def dist(node1, node2):
    d = [node1[0] - node2[0], node1[1] - node2[1]]
    return round(math.sqrt(d[0] ** 2 + d[1] ** 2))

with open(inputFile, 'r') as reader:
    for line in reader.readlines():
        lineDataArr = line.split()
        coords[int(lineDataArr[0].replace('.',''))] = (float(lineDataArr[1]), float(lineDataArr[2]))

for node1, coords1 in coords.items():
    distances[node1] = {}
    for node2, coords2 in coords.items():
        distances[node1][node2] = dist(coords1, coords2) 

print(distances)