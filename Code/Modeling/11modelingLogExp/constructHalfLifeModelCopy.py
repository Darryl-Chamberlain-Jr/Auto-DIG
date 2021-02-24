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

timePassed = random.randint(2, 20)
initialAmount = random.randint(500, 1000)
finalAmount = int( float(initialAmount) * (1.0 / random.randint(4, 10)) )
k = log( float(finalAmount) / float(initialAmount) ) / (float(timePassed)*log(0.5))
# Correct answer
halfLife = int(1.0/k)*365
# Correct model but solved incorrectly
kBadSolve = log(finalAmount) / ( float(timePassed)*log(0.5*initialAmount) )
halfLifeBadSolve = int(1.0/kBadSolve) * 365
# Modeled as constant function A/A_0 = kt
constantModelHalfLife = int( float(finalAmount)/float(initialAmount) * float(timePassed) ) * 365
# Modeled with base of e rather than 1/2
kWithBaseE = log( float(finalAmount)/float(initialAmount) )  /  ( float(timePassed)*log(exp(1)) )
halfLifeWithBaseE = int(-1.0/kWithBaseE) * 365
###
### LATER, MAKE A BASE OF E ###
displayStem = "Using the scenario below, model the situation using an exponential function and a base of $\\frac{1}{2}$. Then, solve for the half-life of the element, rounding to the nearest day."
displayProblem = "The half-life of an element is the amount of time it takes for the element to decay to half of its initial starting amount. There is initially %d grams of element $X$ and after %d years there is %d grams remaining." %(initialAmount, timePassed, finalAmount)

option1 = ["\\text{About } %d \\text{ days}" %halfLife, "* This is the correct option.", 1]
option2 = ["\\text{About } %d \\text{ days}" %halfLifeBadSolve, "This uses the correct model but solves for the exponential constant incorrectly.", 0]
option3 = ["\\text{About } %d \\text{ days}" %constantModelHalfLife, "This models half-life as a linear function.", 0]
option4 = ["\\text{About } %d \\text{ days}" %halfLifeWithBaseE, "This uses the correct model but a base of $e$ rather than $\\frac{1}{2}$.", 0]
option5 = ["\\text{None of the above}", "Please contact the coordinator if you believe all the options above are incorrect.", 0]
displaySolution = option1[0]

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "The model should be $A(t) = A_0 (\\frac{1}{2})^{kt}$, where $A(t)$ is the amount after $t$ years, $A_0$ is the initial amount, and $k$ is decay constant. To find the half-life, you need to solve for $k$ by using the amount after $x$ years, then solve for the time $t$ when $A = \\frac{A_0}{2}$. Your answer would be in years, so convert to days."

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="String"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
