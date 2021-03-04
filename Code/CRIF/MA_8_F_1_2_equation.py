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
def construct_polynomial_function(degree):
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
    return equation
def cubeRootThis(value):
    if value > 0:
        return (value)**(1./3.)
    else:
        return -(-value)**(1./3.)
def construct_rational_function(rootDegree):
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
    return equation
def construct_absolute_value_function():
    a = (-1)**random.randint(0,1) * random.randint(1, 5)
    h = (-1)**random.randint(0,1) * random.randint(1, 5)
    k = (-1)**random.randint(0,1) * random.randint(1, 5)
    if k > 0:
        equation = f"{a}|{generatePolynomialDisplay([1, -h])}|+{k}"
    else:
        equation = f"{a}|{generatePolynomialDisplay([1, -h])}|-{-k}"
    return equation
def construct_exponential_function(base):
    a = (-1)**random.randint(0,1) * random.randint(1, 5)
    h = (-1)**random.randint(0,1) * random.randint(1, 5)
    k = (-1)**random.randint(0,1) * random.randint(1, 5)
    if base == 0.5:
        display_base = "\\left( \\dfrac{1}{2} \\right)"
    else:
        display_base = "(2)"
    if k > 0:
        equation = "%d %s^{x-%d}+%d" %(a, display_base, h, k)
    else:
        equation = "%d %s^{x-%d}-%d" %(a, display_base, h, -k)
    return equation

### VARIABLE DECLARATIONS ###
# Declare the necessary variables.
equation_is_linear = random.randint(0, 1)
if equation_is_linear == 0:
    solution="no, the equation is not linear."
    answerLetter = "B"
    non_linear_choice = random.choice(["polynomial", "rational", "absolute_value", "exponential"])
    if non_linear_choice == "polynomial":
        degree = random.randint(2, 5)
        equation=construct_polynomial_function(degree)
        equation_description=f"degree-{degree} polynomial"
    elif non_linear_choice == "rational":
        rootDegree = random.randint(2, 3)
        equation=construct_rational_function(rootDegree)
        if rootDegree == 2:
            equation_description="square root function"
        else:
            equation_description="cube root function"
    elif non_linear_choice == "absolute_value":
        equation=construct_absolute_value_function()
        equation_description="absolute value function"
    else:
        base = random.choice([0.5, 2])
        equation=construct_exponential_function(base)
        equation_description=f"base-{base} exponential function"
    yes_comment=f"A linear equation is a degree-1 polynomial. {equation} is a {equation_description}"
    no_comment=f"* Correct! {equation} is not a degree-1 polynomial."
else:
    solution="yes, the graph is linear."
    answerLetter = "A"
    equation=construct_polynomial_function(1)
    yes_comment="* Correct! The equation is a degree-1 polynomial and is thus a linear function."
    no_comment="A linear function is a degree-1 polynomial. Polynomial equations have all variables with positive integer exponents."

displayStem = "Is the equation below a linear function?"
displayProblem = f"f(x) = {equation}"
displaySolution = solution

choices=["Yes, the equation is linear", "No, the equation is not linear."]
choiceComments=[f"{yes_comment}", f"{no_comment}"]
generalComment=f"The equation graphed was {equation}. A linear function is a degree-1 polynomial. Polynomial equations have all variables with positive integer exponents, like $f(x) = 3x^2-2x+4$. Square root and cube root functions have rational exponents (1/2 and 1/3)."

### Define display variables ###
# Options are: "String", "Math Mode", "Graph", or "Table"
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="String"

### Writes important information to database. ###
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
