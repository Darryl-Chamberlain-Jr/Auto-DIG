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
import matplotlib.pyplot as plt

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

x = var("x")

def generateSolutionAndDistractors(coefficients, vertex):
    a, b, c = coefficients
    solution = [[a, b, c], "* $f(x)=%s$, which is the correct option." %generatePolynomialDisplay([a, b, c]), 1]
    distractor1 = [[a, -b, c], "$f(x)=%s$, which corresponds to incorrectly using vertex form as $f(x) = a(x+h)^2+k$." %generatePolynomialDisplay([a, -b, c]), 0]
    distractor2 = [[-a, b, -c + 2*vertex[1]], "$f(x)=%s$, which corresponds to incorrectly using vertex form as $f(x) = a(x+h)^2+k$ AND making $a$ the opposite sign than it should be." %generatePolynomialDisplay([-a, b, -c + 2*vertex[1]]), 0]
    distractor3 = [[a, -b, c - 2*vertex[1]], "$f(x)=%s$, which corresponds to incorrectly using vertex form as $f(x) = a(x+h)^2 - k$." %generatePolynomialDisplay([a, -b, c - 2*vertex[1]]), 0]
    distractor4 = [[-a, -b, -c + 2*vertex[1]], "$f(x)=%s$, which corresponds to making $a$ the opposite sign than it should be." %generatePolynomialDisplay([-a, -b, -c + 2*vertex[1]]), 0]
    return [solution, distractor1, distractor2, distractor3, distractor4]

def graphTheFunctionAndReturnCoefficients(a, vertex):
    graphToFunction = a * (x-vertex[0])**2 + vertex[1]
    #
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
    graphX = numpy.arange(vertex[0] - 3, vertex[0] + 3, 0.01)
    graphY = a * (graphX-vertex[0])**2 + vertex[1]
    plt.plot(graphX, graphY, linewidth = 5, color = 	'#02325f')
    plt.plot( [ vertex[0] ], [ vertex[1] ], 'bs')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.close()
    return [a, -2*vertex[0]*a, a*(vertex[0])**2 +vertex[1]]

a = maybeMakeNegative(1)
vertex = [maybeMakeNegative(random.randint(1, 2))*2, maybeMakeNegative(random.randint(1, 5))*2]
coefficients = graphTheFunctionAndReturnCoefficients(a, vertex)
solution, distractor1, distractor2, distractor3, distractor4 = generateSolutionAndDistractors(coefficients, vertex)
solutionList = [ solution[0], distractor1[0], distractor2[0], distractor3[0], distractor4[0] ]
intervalRange = 3
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
answerList = [ [intervalOptions[0], solution[1], solution[2]], [intervalOptions[1], distractor1[1], distractor1[2]], [intervalOptions[2], distractor2[1], distractor2[2]], [intervalOptions[3], distractor3[1], distractor3[2]], [intervalOptions[4], distractor4[1], distractor4[2]] ]
random.shuffle(answerList)

displayStem = 'Write the equation of the graph presented below in the form $f(x)=ax^2+bx+c$, assuming  $a=1$ or $a=-1$. Then, choose the intervals that $a, b,$ and $c$ belong to.'
displayProblem = f"{thisQuestion}{version}"
displaySolution = "f(x) = %s" %generatePolynomialDisplay(solution[0])
generalComment = "When the graph is pointing up, $a=1$. When the graph is pointing down, $a=-1$. Be sure to use Vertex Form: $y = a(x-h)^2+k$."

c0 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\text{ and } \\hspace*{5mm} c \\in [%s, %s]" %(answerList[0][0][0][0], answerList[0][0][0][1], answerList[0][0][1][0], answerList[0][0][1][1], answerList[0][0][2][0], answerList[0][0][2][1])
c1 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\text{ and } \\hspace*{5mm} c \\in [%s, %s]" %(answerList[1][0][0][0], answerList[1][0][0][1], answerList[1][0][1][0], answerList[1][0][1][1], answerList[1][0][2][0], answerList[1][0][2][1])
c2 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\text{ and } \\hspace*{5mm} c \\in [%s, %s]" %(answerList[2][0][0][0], answerList[2][0][0][1], answerList[2][0][1][0], answerList[2][0][1][1], answerList[2][0][2][0], answerList[2][0][2][1])
c3 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\text{ and } \\hspace*{5mm} c \\in [%s, %s]" %(answerList[3][0][0][0], answerList[3][0][0][1], answerList[3][0][1][0], answerList[3][0][1][1], answerList[3][0][2][0], answerList[3][0][2][1])
c4 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\text{ and } \\hspace*{5mm} c \\in [%s, %s]" %(answerList[4][0][0][0], answerList[4][0][0][1], answerList[4][0][1][0], answerList[4][0][1][1], answerList[4][0][2][0], answerList[4][0][2][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

displayStemType="String"
displayProblemType="Graph"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
