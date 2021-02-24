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

# Ideas for forms of this question:
    # math.log(x, b) = \frac{a0}{a1}, solve for x
    # math.log(a0*x+a1, b)+k = num, solve for x

# OBJECTIVE 1 - Solving Logarithmic Equations
intervalRange = 5
precision = 1

# STRUCTURE FOR NOW
    # math.log(a0*x+a1, b)+k = N

def createEquation():
    a0 = maybeMakeNegative(random.randint(2, 4))
    a1 = (random.randint(5, 8))
    b = random.randint(2, 5)
    k = maybeMakeNegative(random.randint(4, 6))
    N = random.randint(2, 3)

    while (k==N or N-k>5 or b == N-k):
        a0 = maybeMakeNegative(random.randint(2, 4))
        a1 = (random.randint(5, 8))
        b = random.randint(4, 5)
        k = maybeMakeNegative(random.randint(4, 6))
        N = random.randint(2, 3)

    if (a1<0):
        if (k<0):
            equation = "\\log_{%d}{(%dx-%d)}-%d = %d" %(b, a0, -a1, -k, N)
        else:
            equation = "\\log_{%d}{(%dx-%d)}+%d = %d" %(b, a0, -a1, k, N)
    else:
        if (k<0):
            equation = "\\log_{%d}{(%dx+%d)}-%d = %d" %(b, a0, a1, -k, N)
        else:
            equation = "\\log_{%d}{(%dx+%d)}+%d = %d" %(b, a0, a1, k, N)

    return [equation, b, a0, a1, k, N]

def solveEquation(coefficients):
    b, a0, a1, k, N = coefficients
    bf = float(b)
    a0f = float(a0)
    a1f = float(a1)
    solution = float( (bf**(N-k) - a1)/a0 )
    return solution

def createSolutionAndDistractors(coefficients):
    b, a0, a1, k, N = coefficients

    solution = solveEquation(coefficients)
    distractor1 = solveEquation([b, a0, a1, 0, N])
    distractor2 = solveEquation([N-k, a0, a1, 0, b])
    distractor3 = solveEquation([N-k, a0, -a1, 0, b])
    #distractor4 will be that there is no Real solution to the equation.
    solutionList = [solution, distractor1, distractor2, distractor3]

    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
    solutionInterval = [intervalOptions[0], "* $x = %.3f$, which is the correct option." %solution, 1]
    distractor1Interval = [intervalOptions[1], "$x = %.3f$, which corresponds to ignoring the vertical shift when converting to exponential form." %distractor1, 0]
    distractor2Interval = [intervalOptions[2], "$x = %.3f$, which corresponds to reversing the base and exponent when converting." %distractor2, 0]
    distractor3Interval = [intervalOptions[3], "$x = %.3f$, which corresponds to reversing the base and exponent when converting and reversing the value with $x$." %distractor3, 0]
    distractor4Interval = [["\\text{There is no Real solution to the equation.}", ""], "Corresponds to believing a negative coefficient within the log equation means there is no Real solution.", 0]

    answerList= [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
    random.shuffle(answerList)
    answerList.append(distractor4Interval)
    return [solutionList, answerList, solution]

###################

equationAndCoefficients = createEquation()
coefficients = [equationAndCoefficients[1], equationAndCoefficients[2], equationAndCoefficients[3], equationAndCoefficients[4], equationAndCoefficients[5]]
solutionAndAnswers = createSolutionAndDistractors(coefficients)

displayEquation = equationAndCoefficients[0]
answerList = solutionAndAnswers[1]

displayStem = 'Solve the equation for $x$ and choose the interval that contains the solution (if it exists).'
displayProblem = displayEquation
displaySolution = "x = %.3f" %solutionAndAnswers[2]

generalComment = "\\textbf{General Comments:} First, get the equation in the form $\\log_b{(cx+d)} = a$. Then, convert to $b^a = cx+d$ and solve."

c0 = "x \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1])
c1 = "x \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1])
c2 = "x \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1])
c3 = "x \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1])
c4 = "%s" %answerList[4][0][0]

choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

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
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
