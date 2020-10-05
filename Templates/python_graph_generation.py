# Use this as a general template to help generate dynamic graphs via python.

### To test this example, use the following imports, functions, and variables. Remember: You should be using the pre-set list of imports for any code you write to insert into the program! "DIR" will need to be manually changed to the root Auto-DIG folder.
import numpy
from numpy import *
from sympy.abc import x
import random
import matplotlib.pyplot as plt
DIR="home/dchamberlain31/git-repos/Auto-DIG"
def random_power(type):
    if type == 1:
        power = random.randint(2, 5)*2+1
    elif type == 2:
        power = random.randint(2, 5)*2
    else:
        power = 0
    return power
def displayEquation(a, z1, e1, z2, e2, z3, e3):
    if z2 == 0:
        equation = "%d%s^{%s} %s^{%s} %s^{%s}" %(a*random.randint(2, 20), displayFactor(z2), e2, displayFactor(z1), e1, displayFactor(z3), e3)
    elif z3 == 0:
        equation = "%d%s^{%s} %s^{%s} %s^{%s}" %(a*random.randint(2, 20), displayFactor(z3), e3, displayFactor(z1), e1, displayFactor(z2), e2)
    else:
        equation = "%d%s^{%s} %s^{%s} %s^{%s}" %(a*random.randint(2, 20), displayFactor(z1), e1, displayFactor(z2), e2, displayFactor(z3), e3)
    return equation
def displayFactor(a):
    if a == 0:
        factor = "x"
    elif a < 0:
        factor = "(x + %d)" %-a
    else:
        factor = "(x - %d)" %a
    return factor
list_random_zeros = range(-4, 4)
a_coeff = (-1)**random.randint(0, 1)
random_zeros = random.sample(list_random_zeros, 3)
x_minimum = min(random_zeros)-0.5
x_maximum = max(random_zeros)+0.5

# Normally should be defined by name of the file. In this case we are using it as the name of our test image.
thisQuestion="test_graphing"
version="A"

# This equation is used to actually graph the function. x was defined as a variable. This is just an example
equation_of_graph = a_coeff*(x-random_zeros[0])**2 * (x-random_zeros[1])**2 * (x-random_zeros[2])**2
# This displays the equation you are graphing. You'll likely display this on the key.
display_equation_of_graph = displayEquation(a_coeff, random_zeros[0],  random_power(2), random_zeros[1], random_power(2), random_zeros[2], random_power(2))

# This defines the x-values that will be plotted. This is a collection of points from min to max counting by the value defined.
count_by=0.05
x_plot = numpy.arange(x_minimum, x_maximum, count_by)

#This creates a series of points that will be smoothly connected by python.
solution_graph = a_coeff*(x_plot-random_zeros[0])**2 * (x_plot-random_zeros[1])**2 * (x_plot-random_zeros[2])**2
# This makes sure the graphs are large enough to read easily.
plt.rcParams.update({'font.size': 36})

# This actually graphs the points defined earlier.
show_plot = plt.plot(x_plot, solution_graph, linewidth = 5, color = 	'#02325f')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
# Saves the figure. "thisQuestion" is a variable defined at the beginning of each code file.
plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
# IMPORTANT! Don't forget to close the plot.
plt.close()
