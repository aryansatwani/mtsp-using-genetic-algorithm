import matplotlib.pyplot as plt
from globals import numTrucks
#def plotTSP(path, points):
def plotTSP(path):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    max_x = 0
    max_y = 0
    for index in range(numTrucks):
        truck_route = [(val.getX(),val.getY()) for val in path.route[index]]
        x = []
        y = []
        for x_val, y_val in truck_route:
            '''
            x.append(points[i][0])
            y.append(points[i][1])
            '''
            x.append(x_val)
            y.append(y_val)
        
        plt.plot(x, y, f'{colors[index]}o', label=f'Truck {index+1}')

        a_scale = float(max(x))/float(50)
        # Draw the primary path for the TSP problem
        plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale, 
                color =colors[index], length_includes_head=True)
        for i in range(0,len(x)-1):
            plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = a_scale,
                    color = colors[index], length_includes_head = True)
        new_max_x = max(x)
        if new_max_x > max_x:
            max_x = new_max_x
        new_max_y = max(y)
        if new_max_y > max_y:
            max_y = new_max_y

    #Set axis too slitghtly larger than the set of x and y
    plt.xlim(0, max_x*1.1)
    plt.ylim(0, max_y*1.1)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Run an example
    
    # Create a randomn list of coordinates, pack them into a list
    x_cor = [1, 8, 4, 9, 2, 1, 8]
    y_cor = [1, 2, 3, 4, 9, 5, 7]
    points = []
    for i in range(0, len(x_cor)):
        points.append((x_cor[i], y_cor[i]))

    # Create two path, teh second with two values swapped to simulate a 2-OPT
    # Local Search operation
    path4 = [0, 1, 2, 3, 4, 5, 6]
    path3 = [0, 2, 1, 3, 4, 5, 6]
    path2 = [0, 2, 1, 3, 6, 5, 4]
    path1 = [0, 2, 1, 3, 6, 4, 5]


    plotTSP(path1, points)
    