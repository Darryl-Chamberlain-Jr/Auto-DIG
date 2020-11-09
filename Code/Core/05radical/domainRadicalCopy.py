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

precision = 1
intervalRange = 5

def displayInterval(direction):
    if direction == "Right":
        interval = "[a, \\infty)"
    else:
        interval = "(-\\infty, a]"
    return interval
def displayForKey(direction, value):
    if direction == "Right":
        interval = "[%.3f, \\infty)" %float(value)
    else:
        interval = "(-\\infty, %.3f]" %float(value)
    return interval

def displayFactor(a, b):
    if b < 0:
        display = "%s x - %s" %(int(a), -int(b))
    else:
        display = "%s x + %s" %(int(a), int(b))
    return display

def solutionAndDistractorsEven():
    # Generates pivot
    a = float(maybeMakeNegative(random.randint(3, 9)))
    b = float(maybeMakeNegative(random.randint(3, 9)))
    while abs(a) == abs(b):
        a = float(maybeMakeNegative(random.randint(3, 9)))
        b = float(maybeMakeNegative(random.randint(3, 9)))
    factor = displayFactor(a, b)
    pivot = -b/a
    #
    # Checks direction of domain
    if a > 0:
        direction = "Right"
        reverseDirection = "Left"
    else:
        direction = "Left"
        reverseDirection = "Right"
    #
    # Generate false pivot
    falsePivot = float(-a/b)
    #
    # Creates intervals for options
    optionList = [pivot, falsePivot]
    intervalOptions1 = createIntervalOptions(optionList, intervalRange, precision)
    intervalOptions2 = createIntervalOptions(optionList, intervalRange, precision)
    #
    # Sets up display of solution
    displaySolution = displayForKey(direction, pivot)
    solution = ["%s, \\text{ where } a \\in [%s, %s]" %(displayInterval(direction), intervalOptions1[0][0], intervalOptions1[0][1]), "* $%s$, which is the correct option." %displaySolution, 1]
    #
    # Sets up display of other options
    distractor1 = ["%s, \\text{where } a \\in [%s, %s]" %(displayInterval(reverseDirection), intervalOptions2[0][0], intervalOptions2[0][1]), " $%s$, which corresponds to reversing the direction of the domain." %displayForKey(reverseDirection, pivot), 0]
    distractor2 = ["%s, \\text{where } a \\in [%s, %s]" %(displayInterval(direction), intervalOptions1[1][0], intervalOptions1[1][1]), "$%s$, which corresponds to using the negative of the correct pivot value." %displayForKey(direction, falsePivot), 0]
    distractor3 = ["%s, \\text{where } a \\in [%s, %s]" %(displayInterval(reverseDirection), intervalOptions2[1][0], intervalOptions2[1][1]), "$%s$, which corresponds to reversing the direction of the domain AND using the negative of the correct pivot value." %displayForKey(reverseDirection, falsePivot), 0]
    distractor4 = ["(-\\infty, \\infty)", "This corresponds to the radical having an odd power, but the radical for this question is even.", 0]
    #
    # Shuffles options
    allOptions = [solution, distractor1, distractor2, distractor3, distractor4]
    random.shuffle(allOptions)
    choices = [allOptions[0][0], allOptions[1][0], allOptions[2][0], allOptions[3][0], allOptions[4][0]]
    choiceComments = [allOptions[0][1], allOptions[1][1], allOptions[2][1], allOptions[3][1], allOptions[4][1]]
    answerIndex = 0
    letters = ["A", "B", "C", "D", "E"]
    for checkLetter in letters:
        if allOptions[answerIndex][2] == 1:
            answerLetter = letters[answerIndex]
            break
        answerIndex = answerIndex+1
    return [factor, displaySolution, choices, choiceComments, answerLetter]

def solutionAndDistractorsOdd():
    # Generates pivot
    a = float(maybeMakeNegative(random.randint(3, 9)))
    b = float(maybeMakeNegative(random.randint(3, 9)))
    while abs(a) == abs(b):
        a = float(maybeMakeNegative(random.randint(3, 9)))
        b = float(maybeMakeNegative(random.randint(3, 9)))
    factor = displayFactor(a, b)
    pivot = -b/a
    #
    # Checks direction of domain
    if a > 0:
        direction = "Right"
        reverseDirection = "Left"
    else:
        direction = "Left"
        reverseDirection = "Right"
    #
    # Generate false pivot
    falsePivot = float(-a/b)
    #
    # Creates intervals for options
    optionList = [pivot, falsePivot]
    intervalOptions1 = createIntervalOptions(optionList, intervalRange, precision)
    intervalOptions2 = createIntervalOptions(optionList, intervalRange, precision)
    #
    # Sets up display of solution
    solution = ["(-\\infty, \\infty)", "* This is the correct option since the radical has an odd power.", 1]
    displaySolution = solution[0]
    #
    # Sets up display of other options
    distractor1 = ["\\text{The domain is } %s, \\text{   where } a \\in [%s, %s]" %(displayInterval(direction), intervalOptions1[0][0], intervalOptions1[0][1]), "$%s$, which corresponds to if the radical had an even power." %displayForKey(direction, pivot), 0]
    distractor2 = ["\\text{The domain is } %s, \\text{   where } a \\in [%s, %s]" %(displayInterval(reverseDirection), intervalOptions2[0][0], intervalOptions2[0][1]), "$%s$, which corresponds to if the radical had an even power AND reversing the direction of the domain." %displayForKey(reverseDirection, pivot), 0]
    distractor3 = ["\\text{The domain is } %s, \\text{   where } a \\in [%s, %s]" %(displayInterval(direction), intervalOptions1[1][0], intervalOptions1[1][1]),
    "$%s$, which corresponds to if the radical had an even power AND using the negative of the correct pivot value." %displayForKey(direction, falsePivot), 0]
    distractor4 = ["\\text{The domain is } %s, \\text{   where } a \\in [%s, %s]" %(displayInterval(reverseDirection), intervalOptions2[1][0], intervalOptions2[1][1]), "$%s$, which corresponds to if the radical had an even power AND reversing the direction of the domain AND using the negative of the correct pivot value." %displayForKey(reverseDirection, falsePivot), 0]
    #
    # Shuffles options
    allOptions = [solution, distractor1, distractor2, distractor3, distractor4]
    random.shuffle(allOptions)
    choices = [allOptions[0][0], allOptions[1][0], allOptions[2][0], allOptions[3][0], allOptions[4][0]]
    choiceComments = [allOptions[0][1], allOptions[1][1], allOptions[2][1], allOptions[3][1], allOptions[4][1]]
    answerIndex = 0
    letters = ["A", "B", "C", "D", "E"]
    for checkLetter in letters:
        if allOptions[answerIndex][2] == 1:
            answerLetter = letters[answerIndex]
            break
        answerIndex = answerIndex+1
    return [factor, displaySolution, choices, choiceComments, answerLetter]

rootDegree = random.randint(3, 8)
if rootDegree % 2 == 0:
    factor, displaySolution, choices, choiceComments, answerLetter = solutionAndDistractorsEven()
else:
    factor, displaySolution, choices, choiceComments, answerLetter = solutionAndDistractorsOdd()

displayStem = "What is the domain of the function below?"
displayProblem = "f(x) = \\sqrt[%d]{%s}" %(rootDegree, factor)
generalComment = "Remember that we cannot take the even root of a negative number - this is why the domain is only sometimes restricted! If we have an even root, we solve $%s \\geq 0$. Since this is an inequality, remember to flip the inequality if we divide by a negative number." %factor

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
