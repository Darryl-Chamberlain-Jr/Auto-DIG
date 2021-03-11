import sys
import random
import numpy
import math

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

def generateLineType():
    typeList = ['Parallel', 'Perpendicular']
    lineType = typeList[random.randint(0, len(typeList)-1)]
    return lineType
def generateProblemAndSolution(lineType):
    if lineType == 'Parallel':
        point = [maybeMakeNegative(random.randint(2, 10)), maybeMakeNegative(random.randint(2, 10))]
        A = random.randint(3, 9)
        B = maybeMakeNegative(random.randint(3, 9))
        while gcd(A, abs(B)) > 1:
            A = random.randint(3, 9)
            B = maybeMakeNegative(random.randint(3, 9))
        C = random.randint(3, 15)
        slope = float(-A)/float(B)
        yInt = float(point[1]-slope*point[0])
        return [[slope, yInt], point, [A,B,C]]
    else:
        point = [maybeMakeNegative(random.randint(2, 10)), maybeMakeNegative(random.randint(2, 10))]
        A = random.randint(3, 9)
        B = maybeMakeNegative(random.randint(3, 9))
        while gcd(A, abs(B)) > 1:
            A = random.randint(3, 9)
            B = maybeMakeNegative(random.randint(3, 9))
        C = float(random.randint(3, 15))
        slope = float(B)/float(A)
        yInt = float(point[1]-slope*point[0])
        return [[slope, yInt], point, [A,B,C]]
def generateDistractors(solution, point):
    slope, yInt = solution
    distractor1 = [-slope, point[1] + slope*point[0]]
    distractor2 = [slope, -yInt]
    distractor3 = [slope, -point[0] + point[1]]
    distractor4 = [1.0/slope, yInt]
    return [distractor1, distractor2, distractor3, distractor4]
def displayCleanEquation(coefficients):
    slope, yInt = coefficients
    if yInt < 0:
        equation = "y = %.2fx - %.2f" %(slope, -yInt)
    else:
        equation = "y = %.2fx + %.2f" %(slope, yInt)
    return equation
### VARIABLE DECLARATIONS ###
lineType = generateLineType()
solution, point, coefficients = generateProblemAndSolution(lineType)
A, B, C = coefficients
distractor1, distractor2, distractor3, distractor4 = generateDistractors(solution, point)
solutionList = [solution, distractor1, distractor2, distractor3, distractor4]
### CREATE INTERVAL OPTIONS ###
intervalOptions = createIntervalOptions(solutionList, 4, 1)
### DEFINE ANSWER LIST AND DISPLAY SOLUTION ###
c1 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[0][0][0], intervalOptions[0][0][1], intervalOptions[0][1][0], intervalOptions[0][1][1])
c2 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[1][0][0], intervalOptions[1][0][1], intervalOptions[1][1][0], intervalOptions[1][1][1])
c3 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[2][0][0], intervalOptions[2][0][1], intervalOptions[2][1][0], intervalOptions[2][1][1])
c4 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[3][0][0], intervalOptions[3][0][1], intervalOptions[3][1][0], intervalOptions[3][1][1])
c5 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[4][0][0], intervalOptions[4][0][1], intervalOptions[4][1][0], intervalOptions[4][1][1])
displaySolution = displayCleanEquation(solution)
option1 = [c1, "* $%s$, which is the correct option." %displaySolution, 1]
option2 = [c2, " $%s$, which corresponds to using the negative slope." %displayCleanEquation(distractor1), 0]
option3 = [c3, " $%s$, which corresponds to using the correct slope and getting the negative $y$-intercept." %displayCleanEquation(distractor2), 0]
option4 = [c4, " $%s$, which corresponds to correct slope and mis-distributing while simplifying to slope-intercept form." %displayCleanEquation(distractor3), 0]
option5 = [c5, " $%s$, which corresponds to using the reciprocal slope $(1/m)$." %displayCleanEquation(distractor4), 0]
answerList = [option1, option2, option3, option4, option5]
random.shuffle(answerList)
### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)
### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
displayStem = 'Find the equation of the line described below. Write the linear equation as $ y=mx+b $ and choose the intervals that contain $m$ and $b$.'
if B < 0:
    standardFormParOrPer = "%s x - %s y" %(A, -B)
else:
    standardFormParOrPer = "%s x + %s y" %(A, B)
displayProblem = '\\text{%s to } %s = %d \\text{ and passing through the point } (%s, %s).' %(lineType, standardFormParOrPer, C, point[0], point[1])
generalComment = "Parallel slope is the same and perpendicular slope is opposite reciprocal. Opposite reciprocal means flipping the fraction and changing the sign (positive to negative or negative to positive)."

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
