### NECESSARY IMPORTS ###
import sys
import numpy
import random
import matplotlib.pyplot as plt

### System variables ###
DIR=sys.argv[1]
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
    OS_type=sys.argv[7]
    response_type=sys.argv[8]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

### DEFINITIONS ###
# This should list all definitions used. Be sure to check the commonly used functions file before creating a new one.
def graph_polynomial_function(degree):
    a = (-1)**random.randint(0,1) * random.randint(1, 5)
    h = (-1)**random.randint(0,1) * random.randint(1, 5)
    k = (-1)**random.randint(0,1) * random.randint(1, 5)
    if degree == 1:
        if k > 0:
            equation = f"{a}({generatePolynomialDisplay([1, -h])})+{k}"
        else:
            equation = f"{a}({generatePolynomialDisplay([1, -h])})-{-k}"
    else:
        if k > 0:
            equation = f"{a}({generatePolynomialDisplay([1, -h])})^{degree}+{k}"
        else:
            equation = f"{a}({generatePolynomialDisplay([1, -h])})^{degree}-{-k}"
    SMALL_SIZE = 24
    MEDIUM_SIZE = 28
    BIGGER_SIZE = 32
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.figure(1)
    graphX = numpy.arange(h-3, h+3, 0.01)
    graphY = a*(graphX-h)**degree+k
    plt.plot(graphX, graphY, linewidth = 5, color = '#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.close()
    return equation
def cubeRootThis(value):
    if value > 0:
        return (value)**(1./3.)
    else:
        return -(-value)**(1./3.)
def graph_rational_function():
    rootDegree = random.randint(2, 3)
    coefficient = (-1)**random.randint(0, 1) * random.randint(1, 4)
    h1 = maybeMakeNegative(random.randint(3, 7))
    h2 = maybeMakeNegative(random.randint(3, 7))
    k = maybeMakeNegative(random.randint(3, 7))
    fixed_point = [float(h2/h1), k]
    if rootDegree == 2:
        if h1 > 0:
            xPlot = numpy.arange(fixed_point[0], fixed_point[1]+4, 0.05)
        else:
            xPlot = numpy.arange(fixed_point[0]-4, fixed_point[1], 0.05)
        yPlot = [coefficient*(h1*xPlot[i]-h2)**0.5+k for i in range(len(xPlot))]
        if k > 0:
            equation = "{%d}\\sqrt{%s}+%d" %(coefficient, generatePolynomialDisplay([h1, -h2]), k)
        else:
            equation = "{%d}\\sqrt{%s}-%d" %(coefficient, generatePolynomialDisplay([h1, -h2]), -k)
    else:
        xPlot = numpy.arange(fixed_point[0]-3, fixed_point[0]+3, 0.05)
        yPlot = [coefficient*cubeRootThis(h1*xPlot[i]-h2)+k for i in range(len(xPlot))]
        if k > 0:
            equation = "{%d}\\sqrt[3]{%s}+%d" %(coefficient, generatePolynomialDisplay([h1, -h2]), k)
        else:
            equation = "{%d}\\sqrt[3]{%s}-%d" %(coefficient, generatePolynomialDisplay([h1, -h2]), -k)
    SMALL_SIZE = 24
    MEDIUM_SIZE = 28
    BIGGER_SIZE = 32
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.figure(1)
    plt.plot(xPlot, yPlot, linewidth = 5, color = '#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.close()
    return equation
def graph_absolute_value_function():
    a = (-1)**random.randint(0,1) * random.randint(1, 5)
    h = (-1)**random.randint(0,1) * random.randint(1, 5)
    k = (-1)**random.randint(0,1) * random.randint(1, 5)
    if k > 0:
        equation = f"{a}|{generatePolynomialDisplay([1, -h])}|+{k}"
    else:
        equation = f"{a}|{generatePolynomialDisplay([1, -h])}|-{-k}"
    SMALL_SIZE = 24
    MEDIUM_SIZE = 28
    BIGGER_SIZE = 32
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.figure(1)
    graphX = numpy.arange(h-3, h+3, 0.01)
    graphY = a*abs(graphX-h)+k
    plt.plot(graphX, graphY, linewidth = 5, color = '#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.close()
    return equation
def graph_exponential_function():
    a = (-1)**random.randint(0,1) * random.randint(1, 5)
    h = (-1)**random.randint(0,1) * random.randint(1, 5)
    k = (-1)**random.randint(0,1) * random.randint(1, 5)
    base = random.choice([0.5, 2])
    if base == 0.5:
        display_base = "\\left( \\dfrac{1}{2} \\right)"
    else:
        display_base = "(2)"
    if k > 0:
        equation = "%d %s^{x-%d}+%d" %(a, display_base, h, k)
    else:
        equation = "%d %s^{x-%d}-%d" %(a, display_base, h, -k)
    SMALL_SIZE = 24
    MEDIUM_SIZE = 28
    BIGGER_SIZE = 32
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.figure(1)
    graphX = numpy.arange(h-3, h+3, 0.01)
    graphY = a*(base)**(graphX-h)+k
    plt.plot(graphX, graphY, linewidth = 5, color = '#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.close()
    return equation

### VARIABLE DECLARATIONS ###
# Declare the necessary variables.
graph_is_linear = random.randint(0, 1)
if graph_is_linear == 0:
    solution="no, the graph is not linear."
    answerLetter = "B"
    yes_comment="A linear function has a constant rate of growth. As $x$ increases/decreases, $y$ increases/decreases at the same rate. The graph in this example does not have a constant rate of change."
    no_comment="* Correct! The graph does not have a constant rate of change and thus is not a linear function."
    non_linear_choice = random.choice(["polynomial", "rational", "absolute_value", "exponential"])
    if non_linear_choice == "polynomial":
        degree = random.randint(2, 5)
        equation=graph_polynomial_function(degree)
    elif non_linear_choice == "rational":
        equation=graph_rational_function()
    elif non_linear_choice == "absolute_value":
        equation=graph_absolute_value_function()
    else:
        equation=graph_exponential_function()
else:
    solution="yes, the graph is linear."
    answerLetter = "A"
    equation=graph_polynomial_function(1)
    yes_comment="* Correct! The graph has a constant rate of change and is thus a linear function."
    no_comment="A linear function has a constant rate of growth. As $x$ increases/decreases, $y$ increases/decreases at the same rate. The graph in this example does have a constant rate of change."

displayStem = "Is the graph below a linear function?"
displayProblem = f"{thisQuestion}{version}"
displaySolution = solution

choices=["Yes, the graph is linear", "No, the graph is not linear."]
choiceComments=[f"{yes_comment}", f"{no_comment}"]
generalComment=f"The equation graphed was {equation}. A linear function has a constant rate of growth. This means that as $x$ increases or decreases, $y$ increase or decreases at the same rate. For example, $x^2$ is NOT a linear function. As $x$ increases, the $y$ increases faster and faster. From $x=1$ to $x=2$, the $y$ increases by 3. From $x=2$ to $x=3$, the $y$ increases by 5. From $x=3$ to $x=4$, the $y$ increases by 7. A linear function would have the same change in $y$ for any change in $x$."

### Define display variables ###
# Options are: "String", "Math Mode", "Graph", or "Table"
displayStemType="String"
displayProblemType="Graph"
displayOptionsType="String"

### Writes important information to database. ###
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
