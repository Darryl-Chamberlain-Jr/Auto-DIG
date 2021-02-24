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
# Type 2 - Function to graph

def putChoicesInOrder(choiceAndComment):
    if choiceAndComment[0] == "A":
        place = 0
    elif choiceAndComment[0] == "B":
        place = 1
    elif choiceAndComment[0] == "C":
        place = 2
    elif choiceAndComment[0] == "D":
        place = 3
    else:
        place = 4
    return place

aCoeffFtG = maybeMakeNegative(random.randint(1, 4))
vertexFtG = [int(0), int(0)]
vertexFtG[0] = maybeMakeNegative(random.randint(1, 4))
vertexFtG[1] = maybeMakeNegative(random.randint(10, 20))
functionToGraph = aCoeffFtG* (x-vertexFtG[0])**2 + vertexFtG[1]

def generateGraphs(aCoeffFtG, vertexFtG):
    figureAnswerList = [["A", '', 1], ["B", '', 0], ["C", '', 0], ["D", '', 0]]
    random.shuffle(figureAnswerList)
    xPlot = numpy.arange(-5, 5, 0.01)
    graphX = numpy.arange(-5, 5, 0.01)

    solutionGraph = aCoeffFtG* (xPlot-vertexFtG[0])**2 + vertexFtG[1]
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
    showPlot = plt.plot(graphX, solutionGraph, linewidth = 5, color = 	'#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + figureAnswerList[0][0] + str(version) + '.png', bbox_inches='tight')
    plt.close()
    figureAnswerList[0][1] = "This is the correct option."
    answerLetter = figureAnswerList[0][0]

    # a(x+h)^2+k
    postiveHdistractor = aCoeffFtG* (xPlot+vertexFtG[0])**2 + vertexFtG[1]
    showPlot = plt.plot(graphX, postiveHdistractor, linewidth = 5, color = 	'#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + figureAnswerList[1][0] + str(version) + '.png', bbox_inches='tight')
    plt.close()
    figureAnswerList[1][1] = "Used the incorrect general form $f(x) = a(x+h)^2 + k$"

    # -a(x-h)^2+k
    negativeAdistractor = -aCoeffFtG* (xPlot-vertexFtG[0])**2 + vertexFtG[1]
    showPlot = plt.plot(graphX, negativeAdistractor, linewidth = 5, color = 	'#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + figureAnswerList[2][0] + str(version) + '.png', bbox_inches='tight')
    plt.close()
    figureAnswerList[2][1] = "Used the incorrect general form $f(x) = -a(x-h)^2 + k$"

    #-a(x+h)^2+k
    negativeApositiveHdistractor = -aCoeffFtG* (xPlot+vertexFtG[0])**2 + vertexFtG[1]
    showPlot = plt.plot(graphX, negativeApositiveHdistractor, linewidth = 5, color = 	'#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + figureAnswerList[3][0] + str(version) + '.png', bbox_inches='tight')
    plt.close()
    figureAnswerList[3][1] = "Used the incorrect general form $f(x) = -a(x+h)^2 + k$"
    #
    return figureAnswerList

figureAnswerList = generateGraphs(aCoeffFtG, vertexFtG)
answerLetter = figureAnswerList[0][0]

displayStem = 'Graph the equation below.'
if aCoeffFtG < 0:
    if vertexFtG[0] < 0:
        if vertexFtG[1] < 0:
            displayProblem = 'f(x) = -(x+%s)^2 - %s' %(-vertexFtG[0], -vertexFtG[1])
        else:
            displayProblem = 'f(x) = -(x+%s)^2 + %s' %(-vertexFtG[0], vertexFtG[1])
    else:
        if vertexFtG[1] < 0:
            displayProblem = 'f(x) = -(x-%s)^2 - %s' %(vertexFtG[0], -vertexFtG[1])
        else:
            displayProblem = 'f(x) = -(x-%s)^2 + %s' %(vertexFtG[0], vertexFtG[1])
else:
    if vertexFtG[0] < 0:
        if vertexFtG[1] < 0:
            displayProblem = 'f(x) = (x+%s)^2 - %s' %(-vertexFtG[0], -vertexFtG[1])
        else:
            displayProblem = 'f(x) = (x+%s)^2 + %s' %(-vertexFtG[0], vertexFtG[1])
    else:
        if vertexFtG[1] < 0:
            displayProblem = 'f(x) = (x-%s)^2 - %s' %(vertexFtG[0], -vertexFtG[1])
        else:
            displayProblem = 'f(x) = (x-%s)^2 + %s' %(vertexFtG[0], vertexFtG[1])

displaySolution = f"{thisQuestion}{figureAnswerList[0][0]}{version}"
generalComment = "Remember that Vertex Form is $y = a(x-h)^2+k$, where the vertex is $(h, k)$."

c0 = f"{thisQuestion}A{version}"
c1 = f"{thisQuestion}B{version}"
c2 = f"{thisQuestion}C{version}"
c3 = f"{thisQuestion}D{version}"
c4 = "None of the above"
choices = [c0, c1, c2, c3]

choiceComments = ["", "", "", "", ""]

placement0 = putChoicesInOrder(figureAnswerList[0])
placement1 = putChoicesInOrder(figureAnswerList[1])
placement2 = putChoicesInOrder(figureAnswerList[2])
placement3 = putChoicesInOrder(figureAnswerList[3])
placements = [placement0, placement1, placement2, placement3]

choiceComments[placement0] = figureAnswerList[0][1]
choiceComments[placement1] = figureAnswerList[1][1]
choiceComments[placement2] = figureAnswerList[2][1]
choiceComments[placement3] = figureAnswerList[3][1]
choiceComments[4] = "You likely thought the vertex did not correspond to the equation."

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Graph"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
