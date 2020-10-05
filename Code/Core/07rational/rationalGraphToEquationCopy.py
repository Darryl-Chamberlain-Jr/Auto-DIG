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

thisQuestion="rationalGraphToEquationCopy"

def sketchRationalFunction(vertAsy, leadingCoeff, power, horShift, figureName):
    ### Defines x-values to avoid asymptote
    plt.rcParams.update({'font.size': 36})
    stepSize = 0.01
    xLeftMin = vertAsy - 2.5
    xLeftMax = vertAsy - stepSize
    xRightMin = vertAsy + stepSize
    xRightMax = vertAsy + 2.5
    ### x-values for graphing
    xLeft = numpy.arange(xLeftMin, xLeftMax, stepSize)
    xPlotLeft = leadingCoeff/(xLeft-vertAsy)**power + horShift
    xRight = numpy.arange(xRightMin, xRightMax, stepSize)
    xPlotRight = leadingCoeff/(xRight-vertAsy)**power + horShift
    ### Lines to plot
    plt.plot(xLeft, xPlotLeft, linewidth=5, color='blue')
    plt.plot(xRight, xPlotRight, linewidth=5, color='blue')
    plt.axvline(x=vertAsy, ls=('dashed'), color='black')
    plt.axhline(y=horShift, ls=('dashed'), color='black')
    ### x and y bounds to make pretty picture
    yMin = horShift - 2.5
    yMax = horShift + 2.5
    #plt.xlim(xMin, xMax)
    plt.ylim([float(yMin),float(yMax)])
    ### Saves and closes picture
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.close()

def createFunction():
    vertAsy = random.randint(1, 3)*(-1)**random.randint(0, 1)
    horShift = random.randint(1, 3)*(-1)**random.randint(0, 1)
    leadingCoeff = (-1)**random.randint(0, 1)
    power = random.randint(1, 2)
    #
    figureName = thisQuestion
    sketchRationalFunction(vertAsy, leadingCoeff, power, horShift, figureName)
    return [vertAsy, leadingCoeff, power, horShift]

def displayEquation(vertAsy, leadingCoeff, power, horShift):
    if power == 1:
        if vertAsy < 0:
            if horShift < 0:
                equation = "f(x) = \\frac{%s}{x + %s} - %s" %(leadingCoeff, -vertAsy, -horShift)
            else:
                equation = "f(x) = \\frac{%s}{x + %s} + %s" %(leadingCoeff, -vertAsy, horShift)
        else:
            if horShift < 0:
                equation = "f(x) = \\frac{%s}{x - %s} - %s" %(leadingCoeff, vertAsy, -horShift)
            else:
                equation = "f(x) = \\frac{%s}{x - %s} + %s" %(leadingCoeff, vertAsy, horShift)
    else:
        if vertAsy < 0:
            if horShift < 0:
                equation = "f(x) = \\frac{%s}{(x + %s)^2} - %s" %(leadingCoeff, -vertAsy, -horShift)
            else:
                equation = "f(x) = \\frac{%s}{(x + %s)^2} + %s" %(leadingCoeff, -vertAsy, horShift)
        else:
            if horShift < 0:
                equation = "f(x) = \\frac{%s}{(x - %s)^2} - %s" %(leadingCoeff, vertAsy, -horShift)
            else:
                equation = "f(x) = \\frac{%s}{(x - %s)^2} + %s" %(leadingCoeff, vertAsy, horShift)
    return equation

def createDistractors(vertAsy, leadingCoeff, power, horShift, vertAsyOrHorAsyWrong):
    if vertAsyOrHorAsyWrong == 0:
        if power == 1:
            distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{x-h}+k$ and the opposite leading coefficient.", 0]
            distractor2 = [displayEquation(vertAsy, leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$.", 0]
            distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$, using the general form $f(x) = \\frac{a}{x-h}+k$, and the opposite leading coefficient.", 0]
        else:
            distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{(x-h)^2}+k$ and the opposite leading coefficient.", 0]
            distractor2 = [displayEquation(vertAsy, leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$.", 0]
            distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$, using the general form $f(x) = \\frac{a}{(x-h)^2}+k$, and the opposite leading coefficient.", 0]
    elif vertAsyOrHorAsyWrong == 1:
        if power == 1:
            distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{x+h}+k$, the opposite leading coefficient AND not noticing the $y$-value was wrong.", 0]
            distractor2 = [displayEquation(vertAsy, leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$ not noticing the $y$-value was wrong.", 0]
            distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$, using the general form $f(x) = \\frac{a}{x+h}+k$, the opposite leading coefficient, AND not noticing the $y$-value was wrong.", 0]
        else:
            distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{(x+h)^2}+k$, the opposite leading coefficient, AND not noticing the $y$-value was wrong.", 0]
            distractor2 = [displayEquation(vertAsy, leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$ AND not noticing the $y$-value was wrong.", 0]
            distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$, using the general form $f(x) = \\frac{a}{(x+h)^2}+k$, the opposite leading coefficient, AND not noticing the $y$-value was wrong.", 0]
    elif vertAsyOrHorAsyWrong == 2:
        if power == 1:
            distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{x-h}+k$, the opposite leading coefficient AND not noticing the $y$-value was wrong.", 0]
            distractor2 = [displayEquation(vertAsy, leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$ not noticing the $y$-value was wrong.", 0]
            distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$, using the general form $f(x) = \\frac{a}{x-h}+k$, the opposite leading coefficient, AND not noticing the $y$-value was wrong.", 0]
        else:
            distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{(x-h)^2}+k$, the opposite leading coefficient, AND not noticing the $y$-value was wrong.", 0]
            distractor2 = [displayEquation(vertAsy, leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$ AND not noticing the $y$-value was wrong.", 0]
            distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$, using the general form $f(x) = \\frac{a}{(x-h)^2}+k$, the opposite leading coefficient, AND not noticing the $y$-value was wrong.", 0]
    else:
        if power == 1:
            distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{x+h}+k$ and the opposite leading coefficient.", 0]
            distractor2 = [displayEquation(vertAsy, leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$.", 0]
            distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$, using the general form $f(x) = \\frac{a}{x+h}+k$, and the opposite leading coefficient.", 0]
        else:
            distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{(x+h)^2}+k$ and the opposite leading coefficient.", 0]
            distractor2 = [displayEquation(vertAsy, leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$.", 0]
            distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$, using the general form $f(x) = \\frac{a}{(x+h)^2}+k$, and the opposite leading coefficient.", 0]
    return [distractor1, distractor2, distractor3]

##### END OF DEFINITIONS #####
vertAsy, leadingCoeff, power, horShift = createFunction()
correctGraphOrNot = random.randint(0,1)
if correctGraphOrNot == 0:
    vertAsyOrHorAsyWrong = random.randint(0, 2)
    if vertAsyOrHorAsyWrong == 0:
        solution = [displayEquation(-vertAsy, leadingCoeff, power, horShift), "The $x$-value of the equation does not match the graph.", 0]
        displaySolution = "\\text{None of the above as it should be } %s" %displayEquation(vertAsy, leadingCoeff, power, horShift)
        distractor1, distractor2, distractor3 = createDistractors(-vertAsy, leadingCoeff, power, horShift, vertAsyOrHorAsyWrong)
    elif vertAsyOrHorAsyWrong == 1:
        yOffBy = random.randint(-7, 7)
        while yOffBy == 0:
            yOffBy = random.randint(-7, 7)
        solution = [displayEquation(vertAsy, leadingCoeff, power, horShift+yOffBy), "The $y$-value of the equation does not match the graph.", 0]
        displaySolution = "\\text{None of the above as it should be } %s" %displayEquation(vertAsy, leadingCoeff, power, horShift)
        distractor1, distractor2, distractor3 = createDistractors(vertAsy, leadingCoeff, power, horShift+yOffBy, vertAsyOrHorAsyWrong)
    else:
        yOffBy = random.randint(-7, 7)
        while yOffBy == 0:
            yOffBy = random.randint(-7, 7)
        solution = [displayEquation(-vertAsy, leadingCoeff, power, horShift+yOffBy), "The $x$- and $y$-value of the equation does not match the graph.", 0]
        displaySolution = "\\text{None of the above as it should be } %s" %displayEquation(vertAsy, leadingCoeff, power, horShift)
        distractor1, distractor2, distractor3 = createDistractors(-vertAsy, leadingCoeff, power, horShift+yOffBy, vertAsyOrHorAsyWrong)
else:
    vertAsyOrHorAsyWrong = 3
    solution = [displayEquation(vertAsy, leadingCoeff, power, horShift), "This is the correct option.", 1]
    displaySolution = displayEquation(vertAsy, leadingCoeff, power, horShift)
    distractor1, distractor2, distractor3 = createDistractors(vertAsy, leadingCoeff, power, horShift, vertAsyOrHorAsyWrong)

displayStem = "Choose the equation of the function graphed below."
displayProblem = f"{thisQuestion}{version}"
generalComment = "Remember that the general form of a basic rational equation is $ f(x) = \\frac{a}{(x-h)^n} + k$, where $a$ is the leading coefficient (and in this case, we assume is either $1$ or $-1$), $n$ is the degree (in this case, either $1$ or $2$), and $(h, k)$ is the intersection of the asymptotes."

optionList = [solution, distractor1, distractor2, distractor3]
random.shuffle(optionList)

choices = [optionList[0][0], optionList[1][0], optionList[2][0], optionList[3][0], "\\text{None of the above}"]

if correctGraphOrNot == 0:
    choiceComments = [optionList[0][1], optionList[1][1], optionList[2][1], optionList[3][1], "None of the equation options were the correct equation."]
    answerLetter = "E"
else:
    choiceComments = [optionList[0][1], optionList[1][1], optionList[2][1], optionList[3][1], "This corresponds to believing the vertex of the graph was not correct."]
    answerIndex = 0
    letters = ["A", "B", "C", "D", "E"]
    for checkLetter in letters:
        if optionList[answerIndex][2] == 1:
            answerLetter = letters[answerIndex]
            break
        answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Graph"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
