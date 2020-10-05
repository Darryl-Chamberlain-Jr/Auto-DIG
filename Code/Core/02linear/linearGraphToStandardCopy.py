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

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

thisQuestion="linearGraphToStandardCopy"

### DEFINITIONS ###
def simplifySolution(A, B, C):
    if(A < 0):
        A = -A
        B = -B
        C = -C
    aBGCD = math.gcd(A, B)
    bCGCD = math.gcd(B, C)
    mixedGCD = math.gcd(aBGCD, bCGCD)
    while(mixedGCD > 1):
        A = int(A/mixedGCD)
        B = int(B/mixedGCD)
        C = int(C/mixedGCD)
        aBGCD = math.gcd(A, B)
        bCGCD = math.gcd(B, C)
        mixedGCD = math.gcd(aBGCD, bCGCD)
    return [A, B, C]
def generateProblemAndSolution(numeratorMax, interceptMax):
    numeratorSlope = maybeMakeNegative(random.randint(2, numeratorMax))
    denominatorSlope = random.randint(2, numeratorMax)
    # Makes sure slope is rational
    while math.gcd(numeratorSlope, denominatorSlope) > 1:
        numeratorSlope = maybeMakeNegative(random.randint(2, numeratorMax))
        denominatorSlope = random.randint(2, numeratorMax)
    slopeGraph = float(numeratorSlope)/float(denominatorSlope)
    yInt = random.randint(-interceptMax, interceptMax)
    point2 = [denominatorSlope, slopeGraph*denominatorSlope + yInt]
    point3 = [-denominatorSlope, -slopeGraph*denominatorSlope + yInt]
    # Converts to Stadard Form
    if slopeGraph > 0:
        aOfGraph = -numeratorSlope
        bOfGraph = denominatorSlope
        cOfGraph = denominatorSlope*yInt
    else:
        aOfGraph = numeratorSlope
        bOfGraph = -denominatorSlope
        cOfGraph = -denominatorSlope*yInt
    return [simplifySolution(aOfGraph, bOfGraph, cOfGraph), [slopeGraph, yInt], point2, point3]
def generateDistractors(solution):
    A, B, C = solution
    distractor1 = [-A, -B, -C]
    distractor2 = [A, -B, -C]
    distractor3 = [round(float(A/B), 3), 1, round(float(C)/float(B), 3)]
    distractor4 =  [round(float(A/B), 3), -1, round(-float(C)/float(B), 3)]
    return [distractor1, distractor2, distractor3, distractor4]
def displayStandardForm(coefficients):
    A, B, C = coefficients
    if B < 0:
        standardForm = "%sx - %sy = %s" %(A, -B, C)
    else:
        standardForm = "%sx + %sy = %s" %(A, B, C)
    return standardForm
#########################
def plotGraph(slopeGraph, yInt, point2, point3):
    graphX = numpy.arange(-5.0, 5.0, 0.01)
    graphY = slopeGraph*graphX + yInt
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
    plt.subplot(111)
    plt.plot(graphX, graphY, linewidth = 5, color = '#02325f')
    #
    #plt.subplot(111)
    #plt.plot([0], [yInt], 'bo')
    #
    plt.subplot(111)
    plt.plot([point2[0]], [point2[1]], 'bo', markersize=20)
    #
    plt.subplot(111)
    plt.plot([point3[0]], [point3[1]], 'bo', markersize=20)
    #
    if slopeGraph > 0:
        #plt.text(0, yInt, "[0, %s]" %yInt, fontsize=28, horizontalalignment='right')
        plt.text(point2[0], point2[1], "[%d, %d]" %(point2[0], point2[1]), fontsize=28, horizontalalignment='right')
        plt.text(point3[0], point3[1], "[%d, %d]" %(point3[0], point3[1]), fontsize=28, horizontalalignment='right')
    else:
        #plt.text(0, yInt, "[0, %s]" %yInt, fontsize=28)
        plt.text(point2[0], point2[1], "[%d, %d]" %(point2[0], point2[1]), fontsize=28)
        plt.text(point3[0], point3[1], "[%d, %d]" %(point3[0], point3[1]), fontsize=28)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.close()
    return
### VARIABLE DECLARATIONS ###
numeratorMax = 5
interceptMax = 5
solution, slopeInt, point2, point3 = generateProblemAndSolution(numeratorMax, interceptMax)
plotGraph(slopeInt[0], slopeInt[1], point2, point3)
### CREATE INTERVAL OPTIONS ###
distractor1, distractor2, distractor3, distractor4 = generateDistractors(solution)
solutionList = [solution, distractor1, distractor2, distractor3, distractor4]
intervalOptions = createIntervalOptions(solutionList, 5, 1)
### DEFINE ANSWER LIST, DISPLAY SOLUTION
c0 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(intervalOptions[0][0][0], intervalOptions[0][0][1], intervalOptions[0][1][0], intervalOptions[0][1][1], intervalOptions[0][2][0], intervalOptions[0][2][1])
c1 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(intervalOptions[1][0][0], intervalOptions[1][0][1], intervalOptions[1][1][0], intervalOptions[1][1][1], intervalOptions[1][2][0], intervalOptions[1][2][1])
c2 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(intervalOptions[2][0][0], intervalOptions[2][0][1], intervalOptions[2][1][0], intervalOptions[2][1][1], intervalOptions[2][2][0], intervalOptions[2][2][1])
c3 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(intervalOptions[3][0][0], intervalOptions[3][0][1], intervalOptions[3][1][0], intervalOptions[3][1][1], intervalOptions[3][2][0], intervalOptions[3][2][1])
c4 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(intervalOptions[4][0][0], intervalOptions[4][0][1], intervalOptions[4][1][0], intervalOptions[4][1][1], intervalOptions[4][2][0], intervalOptions[4][2][1])
displaySolution = displayStandardForm(solution)
option1 = [c0, "* $%s$, which is the correct option." %displaySolution, 1]
option2 = [c1, " $%s$, which corresponds to not making $A$ positive (by multiplying the equation by $-1$)." %displayStandardForm(distractor1), 0]
option3 = [c2, " $%s$, which corresponds to using the opposite (negative) slope of the graph, but did everything else correctly." %displayStandardForm(distractor2), 0]
option4 = [c3, " $%s$, which corresponds to not removing rational values for Standard Form." %displayStandardForm(distractor3), 0]
option5 = [c4, " $%s$, which corresponds to using the opposite (negative) slope of the graph and not removing rational values." %displayStandardForm(distractor4), 0]
answerList = [option1, option2, option3, option4, option5]
random.shuffle(answerList)
### DEFINE CHOICES, CHOICE COMMENTS, ANSWER LETTER
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)
### DEFINE STEM, PROBLEM, GENERAL COMMENT AS STRINGS
displayStem = 'Write the equation of the line in the graph below in Standard form $Ax+By=C$. Then, choose the intervals that contain $A, B, \\text{ and } C$.'
displayProblem = "\\text{Equation that was graphed:} f(x)= %s" %generatePolynomialDisplay(slopeInt)
generalComment = "Standard form is supposed to have $A > 0$ and all fractions removed."

displayStemType="String"
displayProblemType="Graph"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
