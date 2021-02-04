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

def generateStem(type):
    initialPop = random.randint(2, 10)*10000
    constant = random.randint(2, 5)*10
    populations = [0,0,0,0,0,0,0,0,0]
    posOrNegSlope = (-1)**random.randint(0, 1)
    if type == "linear":
        for k in range(0, 9):
            populations[k] = max(initialPop+posOrNegSlope*(k+1)*constant, 0)
    elif type == "direct":
        randomPower = random.randint(4, 6)
        for k in range(0, 9):
            populations[k] = max(initialPop+posOrNegSlope*constant*(k+1)^(randomPower), 0)
    elif type == "indirect":
        randomPower = random.randint(2, 4)
        for k in range(0, 9):
            populations[k] = max(int(initialPop+posOrNegSlope*constant*(k+1)^(-randomPower)), 0)
    elif type == "exponential":
        randomBase = random.randint(2, 4)
        for k in range(0, 9):
            populations[k] = max(int(initialPop+posOrNegSlope*constant*randomBase**(k+1)), 0)
    else:
        # Type is LOG
        for k in range(0, 9):
            populations[k] = max(int(initialPop+posOrNegSlope*constant*log((k+1))), 0)
    return [initialPop, populations]

# TYPE OF PROBLEM TO BE DETERMINED BY MODULE
typesToChooseFrom=["linear", "direct", "exponential", "logarithmic"]
problemType = typesToChooseFrom[random.randint(0, 3)]
initialPop, populations = generateStem(problemType)
displayStem = "A town has an initial population of %d. The town's population for the next 9 years is provided below. Which type of function would be most appropriate to model the town's population?" %initialPop
#header for the table
header_row = ['\\textbf{Year}', 1, 2, 3, 4, 5, 6, 7, 8, 9]
populations.insert(0, '\\textbf{Pop}')
population_row = populations
displayProblem = [header_row, population_row]
generalComment = "We are trying to compare the growth rate of the population. Growth rates can be characterized from slowest to fastest as: logarithmic, indirect, linear, direct, exponential. The best way to approach this is to first compare it to linear (is it linear, faster than linear, or slower than linear)? If faster, is it as fast as exponential? If slower, is it as slow as logarithmic?"

linearAnswer = 0
directAnswer = 0
indirectAnswer = 0
logAnswer = 0
expAnswer = 0

if problemType == 'linear':
    linearAnswer = 1
elif problemType == 'direct':
    directAnswer = 1
elif problemType == 'indirect':
    indirectAnswer = 1
elif problemType == 'exponential':
    expAnswer = 1
else:
    logAnswer = 1

c0 = ["\\text{Linear}", "This suggests a constant growth. You would be able to add or subtract the same amount year-to-year if this is the correct answer.", linearAnswer]
c1 = ["\\text{Non-Linear Power}", "This suggests a growth faster than constant but slower than exponential.", directAnswer]
#c2 = ["\\text{Indirect variation}", "This suggests a growth slower than constant but faster than logarithmic.", indirectAnswer]
c2 = ["\\text{Logarithmic}", "This suggests the slowest of growths that we know.", logAnswer]
c3 = ["\\text{Exponential}", "This suggests the fastest of growths that we know.", expAnswer]

choiceAndCommentList = [c0, c1, c2, c3]
random.shuffle(choiceAndCommentList)

choices = [0, 0, 0, 0]
choiceComments = [0, 0, 0, 0]

for k in range(0, 4):
    choices[k] = choiceAndCommentList[k][0]
    choiceComments[k] = choiceAndCommentList[k][1]

choices.append("\\text{None of the above}")
choiceComments.append("Please contact the coordinator to discuss why you believe none of the options model the population.")

answerIndex = 0
letters = ["A", "B", "C", "D"]
for checkLetter in letters:
    if choiceAndCommentList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        displaySolution = choiceAndCommentList[answerIndex][0]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Table"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
