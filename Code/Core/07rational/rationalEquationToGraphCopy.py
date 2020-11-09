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
thisQuestion=sys.argv[5]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

def sketchRationalFunction(vertAsy, leadingCoeff, power, horShift, figureName, optionLetter):
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
    plt.savefig('/' + str(DIR) + '/Figures/' + str(figureName) + str(optionLetter) + str(version) + '.png', bbox_inches='tight')
    plt.close()
def createFunction():
    vertAsy = random.randint(1, 3)*(-1)**random.randint(0, 1)
    horShift = random.randint(1, 3)*(-1)**random.randint(0, 1)
    leadingCoeff = (-1)**random.randint(0, 1)
    power = random.randint(1, 2)
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
def createDistractors(vertAsy, leadingCoeff, power, horShift, figureName, optionList):
    if power == 1:
        distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{x+h}+k$ and the opposite leading coefficient."]
        sketchRationalFunction(-vertAsy, -leadingCoeff, power, horShift, figureName, optionList[1])
        distractor2 = [displayEquation(vertAsy, leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$."]
        sketchRationalFunction(vertAsy, leadingCoeff, power+1, horShift, figureName, optionList[2])
        distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power+1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x^2}$, using the general form $f(x) = \\frac{a}{x+h}+k$, and the opposite leading coefficient."]
        sketchRationalFunction(-vertAsy, -leadingCoeff, power+1, horShift, figureName, optionList[3])
    else:
        distractor1 = [displayEquation(-vertAsy, -leadingCoeff, power, horShift), "Corresponds to using the general form $f(x) = \\frac{a}{(x+h)^2}+k$ and the opposite leading coefficient."]
        sketchRationalFunction(-vertAsy, -leadingCoeff, power, horShift, figureName, optionList[1])
        distractor2 = [displayEquation(vertAsy, leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$."]
        sketchRationalFunction(vertAsy, leadingCoeff, power-1, horShift, figureName, optionList[2])
        distractor3 = [displayEquation(-vertAsy, -leadingCoeff, power-1, horShift), "Corresponds to thinking the graph was a shifted version of $\\frac{1}{x}$, using the general form $f(x) = \\frac{a}{(x+h)^2}+k$, and the opposite leading coefficient."]
        sketchRationalFunction(-vertAsy, -leadingCoeff, power-1, horShift, figureName, optionList[3])
    return [distractor1, distractor2, distractor3]

##### END OF DEFINITIONS #####
graphedRightOrWrong = random.randint(0, 1)
figureName = thisQuestion
optionList = ["A", "B", "C", "D"]
unshuffledOptionList = optionList
random.shuffle(optionList)
choices = [ "%sA%s" %(figureName, version), "%sB%s" %(figureName, version), "%sC%s" %(figureName, version), "%sD%s" %(figureName, version)]
figureNameShuffledList = [ "%s%s%s" %(figureName, optionList[0], version), "%s%s%s" %(figureName, optionList[1], version), "%s%s%s" %(figureName, optionList[2], version), "%s%s%s" %(figureName, optionList[3], version)]
vertAsy, leadingCoeff, power, horShift = createFunction()

if graphedRightOrWrong == 0:
    sketchRationalFunction(vertAsy, leadingCoeff, power, horShift, figureName, "E")
    displaySolution = f"{thisQuestion}E{version}"
    otherWrongThings = random.randint(0, 2)
    if otherWrongThings == 0:
        sketchRationalFunction(-vertAsy, leadingCoeff, power, horShift, figureName, optionList[0])
        solution = [displayEquation(-vertAsy, leadingCoeff, power, horShift), "Incorrect due to $x$-value."]
        distractor1, distractor2, distractor3 = createDistractors(-vertAsy, leadingCoeff, power, horShift, figureName, optionList)
    elif otherWrongThings == 1:
        sketchRationalFunction(vertAsy, leadingCoeff, power, -horShift, figureName, optionList[0])
        solution = [displayEquation(vertAsy, leadingCoeff, power, -horShift), "Incorrect due to $y$-value."]
        distractor1, distractor2, distractor3 = createDistractors(vertAsy, leadingCoeff, power, -horShift, figureName, optionList)
    else:
        sketchRationalFunction(-vertAsy, leadingCoeff, power, -horShift, figureName, optionList[0])
        solution = [displayEquation(-vertAsy, leadingCoeff, power, -horShift), "Incorrect due to $x$- and $y$-value."]
        distractor1, distractor2, distractor3 = createDistractors(-vertAsy, leadingCoeff, power, -horShift, figureName, optionList)
    answerLetter = "E"
    shuffledCommentsList = [solution[1], distractor1[1], distractor2[1], distractor3[1]]
else:
    sketchRationalFunction(vertAsy, leadingCoeff, power, horShift, figureName, optionList[0])
    solution = [displayEquation(vertAsy, leadingCoeff, power, horShift), "This is the correct option."]
    displaySolution = f"{thisQuestion}{version}{optionList[0]}"
    distractor1, distractor2, distractor3 = createDistractors(vertAsy, leadingCoeff, power, horShift, figureName, optionList)
    shuffledCommentsList = [solution[1], distractor1[1], distractor2[1], distractor3[1]]
    answerLetter = optionList[0]

choiceComments = commentsForGraphs(unshuffledOptionList, optionList, shuffledCommentsList)
if graphedRightOrWrong == 0:
    choiceComments.append("None of the graph options are correct, so this is the correct answer.")
else:
    choiceComments.append("You likely thought the vertex was not correct for any of the graphs.")

displayStem = "Choose the graph of the equation below."
displayProblem = displayEquation(vertAsy, leadingCoeff, power, horShift)
generalComment = "Remember that the general form of a basic rational equation is $ f(x) = \\frac{a}{(x-h)^n} + k$, where $a$ is the leading coefficient (and in this case, we assume is either $1$ or $-1$), $n$ is the degree (in this case, either $1$ or $2$), and $(h, k)$ is the intersection of the asymptotes."

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Graph"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
