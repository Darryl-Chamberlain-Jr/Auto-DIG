import sys
from sympy import *
import numpy
import random
import math
from decimal import Decimal
import decimal
import traceback
import cmath
import matplotlib.pyplot as plt
from sympy.abc import x, y
from sympy.solvers import solve

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

thisQuestion="functionCompositionCopy"

intervalRange = 5
precision = 1

def generateFunction(functionClass):
    #functionClass = {"Polynomial", "Radical", "Rational"}
    degree = int(random.randint(2, 3))
    counter = degree
    functionCoefficients = [0, 0, 0, 0]
    while (counter>=0):
        index = degree - counter
        functionCoefficients[index] = int(maybeMakeNegative(random.randint(1, 4)))
        counter = counter - 1
    return functionCoefficients

def evaluateValue(functionCoefficients, evaluateAt):
    degree = len(functionCoefficients)
    countdown = degree
    value = float(0)
    while (countdown>=1):
        index = degree - countdown
        value = float(value + functionCoefficients[index]*(evaluateAt)**(countdown-1))
        countdown = countdown - 1
    return float(value)

# In the future, we can make this more nuanced and pull from different classes of functions.
#functionClasses = generateFunctionClasses()

function1 = generateFunction("Polynomial")
function2 = generateFunction("Polynomial")
evaluateAt = maybeMakeNegative(random.randint(1, 2))

intermediate = evaluateValue(function2, evaluateAt)
output = evaluateValue(function1, intermediate)
solution = output

# Student reversed the composition
distractor1 = evaluateValue(function2, evaluateValue(function1, evaluateAt))

while (abs(solution) > 100 or abs(distractor1) > 100):
    function1 = generateFunction("Polynomial")
    function2 = generateFunction("Polynomial")
    evaluateAt = maybeMakeNegative(random.randint(1, 2))
    intermediate = evaluateValue(function2, evaluateAt)
    output = evaluateValue(function1, intermediate)
    solution = output
    distractor1 = evaluateValue(function2, evaluateValue(function1, evaluateAt))

# Shift from correct solution (needs to be revised)
distractor2 = solution + maybeMakeNegative(random.randint(5, 10))

# Shift from distractor solution (needs to be revised)
distractor3 = distractor1 + maybeMakeNegative(random.randint(5, 10))

solutionList = [solution, distractor1, distractor2, distractor3]
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = [intervalOptions[0], "* This is the correct solution", 1]
distractor1Interval = [intervalOptions[1], " Distractor 1: Corresponds to reversing the composition.", 0]
distractor2Interval = [intervalOptions[2], " Distractor 2: Corresponds to being slightly off from the solution.", 0]
distractor3Interval = [intervalOptions[3], " Distractor 3: Corresponds to being slightly off from the solution.", 0]

a1, a2, a3, a4 = function1
b1, b2, b3, b4 = function2
displayFunction1 = generatePolynomialDisplay(function1)
displayFunction2 = generatePolynomialDisplay(function2)

displayStem = "Choose the interval below that $f$ composed with $g$ at $x=%d$ is in." %evaluateAt
displayProblem = "f(x) = %s \\text{ and } g(x) = %s" %(displayFunction1, displayFunction2)
displaySolution = solution
generalComment = "$f$ composed with $g$ at $x$ means $f(g(x))$. The order matters!"

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)

c0 = "(f \\circ g)(%d) \\in [%s, %s]" %(evaluateAt, answerList[0][0][0], answerList[0][0][1])
c1 = "(f \\circ g)(%d) \\in [%s, %s]" %(evaluateAt, answerList[1][0][0], answerList[1][0][1])
c2 = "(f \\circ g)(%d) \\in [%s, %s]" %(evaluateAt, answerList[2][0][0], answerList[2][0][1])
c3 = "(f \\circ g)(%d) \\in [%s, %s]" %(evaluateAt, answerList[3][0][0], answerList[3][0][1])
c4 = "\\text{It is not possible to compose the two functions.}"
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], ""]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
