### cs3510_TSP
Traveling Salesman Problem Course Project  
Submitted: April 17, 2020  

### Group Members
* Lindsey Blackmore | lblackmore3@gatech.edu 
* Shivanee Persaud  | spersaud3@gatech.edu

### Files
* simulated_annealing.py: script that will perform simulated annealing on a given input of coordinates and will write the solution to the given output file within a given time period
* run_simulated_annealing.py: script to run manually and give the specified inputs, it will invoke simulated_annealing.py
* mat-test.txt: the test coordinates 
* mat-output.txt: the results of 10 runs of our program
* algorithm.pdf: an in-depth explanation of the simulated annealing algorithm and the pseudocode our project is based on  

### How To Run The Algorithm
Since this is a python program, it does not need to be compiled by the user. To run our simulated annealing algorithm, open a terminal and enter "python3 run_simulated_annealing.py <input-coordinates.txt> <output-tour.txt> <time>". The results will be written to output-tour.txt.
  
### Limitations
This algorithm has a random component so occasionally the path length that is output is not under 29,000. However, during our testing the range of outputs we encountered was roughly 27,600 to 30,300.
