# mtsp-using-genetic-algorithm

## Multiple Travelling Salesman Problem
- Here we are using a meta-heuristic approach which is much more space and time efficient than brute force approach.
- The time complexity for this algorithm is: O(m x N x G x c) where
  m = number of salesmen  <br>
  G = no. of generations(iterations)  <br>
  N = population size(Number of solutions)  <br>
  c = number of cities per salesman's territory  <br>

### Genetic Algorithm
Genetic Algorithm is based on natural selection and survival of the fittest.  <br>

Parents cross over to create an offspring, with a chance of mutation to be carried forward  <br>

### Test Cases
Test cases have been generated from TSPLib instead of random point generation.  <br>
Two datasets included:  <br>
[Berlin](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/berlin52_3.txt.txt)  <br>
[48 American State Capital Cities](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/att48_3.txt.txt)  <br>

### [Globals](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/globals.py)  <br>

Here it defines what a node is(it is a city).  <br>

**Parameters**
1. Population=100
2. Mutation = 0.02
3. Tournament Size = 15 (Best 15 solutions among population)
4. Elitism = true (if solution is good, do not cross/change it until next generation (until it continues to be part of tournament).
5. Garbage Trucks = 7
6. Route Lengths
   (i) Max has to between 160% to 60% of route length  <br>
   (ii) Min has to be between >0% to 60% of route length  <br>

### [Dustbin](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/dustbin.py)
This class gets x and y coordinates of the city (assuming each city has only one dustbin).

### [Population](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/population.py)
All constraints are kept here to initialise population.
- With every solution, it first makes a new route and generates an individual solution to generate a route sequence, then it is added to the new route.
- **Optimal Route**: Uses Get Fittest function which minimises length and maximises its reciprocal(continues for 10 iterations)
- **Get Fitness  Function**: Finds fitness of individual points.
- **Get Distance Function**: gets distance of two points-reciprocal of fitness
- **Get Route Function**: Given an index it gives a route

### [Route Manager](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/routemanager.py)
It keeps track of all dustbins in a city.

### [GALogic](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/galogic.py)
Its main aim is to evolve the population
- Elitism offset has 0(true of initial elitism value) or non-zero (false of initial elitism value)
- **Cross-over Function**: Parent 1 x Parent 2 ->child ((new node in solution, leading to mutation)
  1. Base Variable for cross-over operation only, and child with this base variable [0][0] is removed after crossing-over is complete.  <br>
- **Mutate**:
  1. Initialise index 1 and 2 as 0
  2. Select Mutation ranges
  3. Swapping Nodes
  4. Updating Route Length
- **Tournament**: Selects best 15 from population by calling getfitness() and returns distances covered in sub-routes.
*cross-over and mutation functions prevent the algorithm from stopping at local minima*

### [Main](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/main.py)
- Assigns x and y values using seed()-random number generator
- No. of Nodes=48
- No. of generations = 250

### [Visualizer](https://github.com/aryansatwani/mtsp-using-genetic-algorithm/blob/main/visualizer.py)
Plots solutions with varied colours indicating different trucks, making it interactive for the user.



