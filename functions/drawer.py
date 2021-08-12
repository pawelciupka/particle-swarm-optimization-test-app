from mpl_toolkits import mplot3d
import numpy as np
from math import *
import matplotlib.pyplot as plt
from matplotlib import cm

 
def draw(function, bound, title):
    x = np.linspace(-1*bound, bound, 100)
    y = np.linspace(-1*bound, bound, 100)
    
    X, Y = np.meshgrid(x, y)
    Z = function([X, Y])
    
    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    ax.plot_wireframe(X, Y, Z, color ='green')
    ax.set_title(title)
    
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.jet,
                       linewidth=0, antialiased=False)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
 


def f_ackley(position, a=20, b=0.2, c=2*pi):
    d = len(position)

    sum1 = 0
    sum2 = 0
    for pos in position:
        sum1 = sum1 + pos**2
        sum2 = sum2 + cos(c*pos)

    term1 = -a * exp(-b*sqrt(sum1/d))
    term2 = -exp(sum2/d)

    return term1 + term2 + a + exp(1)

def f_f2(position):
    d = len(position)
    sum = 0

    for ii in range (1, d+1):
        xi = position[ii-1]
        sum = sum + (xi-ii)**2

    return sum

def fitnessFunc(chromosome):
	"""F6 Griewank's function
	multimodal, symmetric, inseparable"""
	part1 = 0
	for i in range(len(chromosome)):
		part1 += chromosome[i]**2
		part2 = 1
	for i in range(len(chromosome)):
		part2 *= cos(float(chromosome[i]) / sqrt(i+1))
	return 1 + (float(part1)/4000.0) - float(part2)
    
def f_griewank(position):
    d = len(position)
    sum = 0
    prod = 1

    x1 = position[0]
    x2 = position[1]
    sum = (x2**2)/4000 + (x2**2)/4000
    xd1 = x1 / sqrt(1)
    prod = cos(xd1) + cos(xd1)
    # for ii in range(0, d):
    #     xi = position[ii]
    #     sum = sum + (xi**2)/4000
    #     prod = prod * cos(xi/sqrt(ii+1))

    return sum - prod + 1


def f_rastrigin(position):
    d = len(position)
    sum = 0

    for ii in range(1, d+1):
        xi = position[ii-1]
        sum = sum + (xi**2 - 10*cos(2*pi*xi) + 10)

    return sum


def f_rosenbrock(position):
    d = len(position)
    sum = 0

    for ii in range(1, d):
        xi = position[ii]    #x i+1
        xii = position[ii-1] #x i
        sum += 100*((xi**2)-xii)**2+(1-xi)**2
    
    return sum
    
def f_schwefel(position):
    d = len(position)
    sum = 0
    prod = 1

    for ii in range(1, d+1):
        xi = position[ii-1]
        sum = sum + xi**2
        prod = prod * abs(xi)

    return sum + prod


def f_sphere(position):
    d = len(position)
    sum = 0

    for ii in range (1, d+1):
        xi = position[ii-1]
        sum = sum + xi**2

    return sum

    
def f_zakharov(position):
    d = len(position)
    sum1 = 0
    sum2 = 0

    for ii in range(1, d+1):
        xi = position[ii-1]
        sum1 = sum1 + xi**2
        sum2 = sum2 + 0.5*ii*xi
    
    return sum1 + sum2**2 + sum2**4




    
draw(f_sphere, 100, "Funkcja Sphere")
draw(f_f2, 100, "Funkcja F2")
draw(f_rosenbrock, 2.048, "Funkcja Rosenbrock")
# draw(fitnessFunc, 600, "Funkcja Griewank")
# draw(f_rastrigin, 5.12, "Funkcja Rastrigin")
# draw(f_ackley, 32, "Funkcja Ackley")
draw(f_schwefel, 10, "Funkcja Schwefel")
draw(f_zakharov, 10, "Funkcja Zakharov")