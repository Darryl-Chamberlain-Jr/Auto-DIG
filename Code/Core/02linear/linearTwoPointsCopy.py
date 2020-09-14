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

### DEFINITIONS ###
def generateProblem():
    numerator=0
    denominator=0
    while (numerator==0 or denominator==0 or slope==1):
        pointOne = [maybeMakeNegative(random.randint(2, 11)), maybeMakeNegative(random.randint(2, 11))]
        pointTwo = [maybeMakeNegative(random.randint(2, 11)), maybeMakeNegative(random.randint(2, 11))]
        numerator = float(pointTwo[1]-pointOne[1])
        denominator = float(pointTwo[0]-pointOne[0])
        slope=numerator/denominator
    return [pointOne, pointTwo]
def generateSolutionAndDistractors(problem):
    pointOne, pointTwo = problem
    slope = float(pointTwo[1]-pointOne[1])/float(pointTwo[0]-pointOne[0])
    yInt = float(pointTwo[1]-slope*pointTwo[0])
    solution = [slope, yInt]
    distractor1 = [-slope, float(pointTwo[1]+slope*pointTwo[0])]
    distractor2 = [slope, -yInt]
    distractor3 = [slope, -pointOne[0] + pointOne[1]]
    distractor4 = [slope, -pointTwo[0] + pointTwo[1]]
    return [solution, distractor1, distractor2, distractor3, distractor4]
def cleanDisplayOfEquation(coefficients):
    displayCleanEquation = "y = %s" %generatePolynomialDisplay([round(coefficients[0], 2), round(coefficients[1], 2)])
    return displayCleanEquation
### VARIABLE DECLARATIONS ###
problem = generateProblem()
pointOne, pointTwo = problem
solution, distractor1, distractor2, distractor3, distractor4 = generateSolutionAndDistractors(problem)
### CREATE INTERVAL OPTIONS ###
solutionList = [solution, distractor1, distractor2, distractor3, distractor4]
intervalOptions = createIntervalOptions(solutionList, 5, 1)
### DEFINE ANSWER LIST AND DISPLAY SOLUTION
displaySolution = cleanDisplayOfEquation(solution)
c1 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[0][0][0], intervalOptions[0][0][1], intervalOptions[0][1][0], intervalOptions[0][1][1])
c2 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[1][0][0], intervalOptions[1][0][1], intervalOptions[1][1][0], intervalOptions[1][1][1])
c3 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[2][0][0], intervalOptions[2][0][1], intervalOptions[2][1][0], intervalOptions[2][1][1])
c4 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[3][0][0], intervalOptions[3][0][1], intervalOptions[3][1][0], intervalOptions[3][1][1])
c5 = "m \\in [%s, %s] \\hspace*{3mm} b \\in [%s, %s]" %(intervalOptions[4][0][0], intervalOptions[4][0][1], intervalOptions[4][1][0], intervalOptions[4][1][1])
option1 = [c1, "* $%s$, which is the correct option." %displaySolution, 1]
option2 = [c2, " $%s$, which corresponds to using the negative slope and the correct equation." %cleanDisplayOfEquation(distractor1), 0]
option3 = [c3, " $%s$, which corresponds to using the correct slope and getting the negative y-intercept." %cleanDisplayOfEquation(distractor2), 0]
option4 = [c4, " $%s$, which corresponds to using the correct slope/equation but not distributing correctly using the first point." %cleanDisplayOfEquation(distractor3), 0]
option5 = [c5, " $%s$, which corresponds to using the correct slope/equation but not distributing correctly using the second point." %cleanDisplayOfEquation(distractor4), 0]
answerList = [option1, option2, option3, option4, option5]
random.shuffle(answerList)
### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)
### DEFINE STEM, PROBLEM, GENERAL COMMENT AS STRINGS ###
displayStem = 'First, find the equation of the line containing the two points below. Then, write the equation as $ y=mx+b $ and choose the intervals that contain $m$ and $b$.'
displayProblem = "(%s, %s) \\text{ and } (%s, %s)" %(pointOne[0], pointOne[1], pointTwo[0], pointTwo[1])
generalComment = "Remember to keep your points in order when plugging in to the slope formula."

thisQuestion="linearTwoPointsCopy"
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
