from simulated_annealing import SimulatedAnnealing
import random
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]
time = sys.argv[3]

coords = []
with open(inputFile, 'r') as reader:
    for line in reader.readlines():
        lineDataArr = line.split()
        coord = [float(lineDataArr[1]), float(lineDataArr[2])]
        coords.append(coord)


if __name__ == "__main__":
    sa = SimulatedAnnealing(coords, outputFile, stopping_iter=10000)
    sa.anneal()