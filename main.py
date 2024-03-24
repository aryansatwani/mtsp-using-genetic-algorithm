from galogic import *
import matplotlib.pyplot as plt
import progressbar
import visualizer
with open('E:\data1/att48_3.txt.txt', 'r') as f: 
    content = f.read().splitlines()[2:]
pbar = progressbar.ProgressBar()
for line in content:
    _, x, y = [float(val) for val in line.split()]
    RouteManager.addDustbin(Dustbin(x, y))
random.seed(seedValue)
yaxis = [] # Fittest value (distance)
xaxis = [] # Generation count
pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))
visualizer.plotTSP(globalRoute)
print("Evolving now:")
# Start evolving
for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)
print ('Global minimum distance: ' + str(globalRoute.getDistance()))
print ('Final Route: ' + globalRoute.toString())
visualizer.plotTSP(globalRoute)