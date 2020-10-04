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

def generateSolution(coefficients):
    a, b, c = coefficients
    solveThisQuadratic = a*x**2+b*x+c
    solution = solve(solveThisQuadratic, x)
    return [min(float(solution[0]), float(solution[1])), max(float(solution[0]), float(solution[1]))]

def findDiscriminant(coefficients):
    a, b, c = coefficients
    return b**2 - 4*a*c

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

def distractorForgotA(coefficients):
    a, b, c = coefficients
    distractor = generateSolution([1, b, a*c])
    return [distractor, [1, b, a*c]]

def distractorPositiveB(coefficients):
    a, b, c = coefficients
    distractor = generateSolution([a, -b, c])
    return [distractor, [a, -b, c]]

def distractorBadDivision(coefficients):
    a, b, c = coefficients
    fA = float(a)
    fB = float(b)
    fC = float(c)
    distractor = [float(-fB/(2*fA) - math.sqrt(fB**2-4*fA*fC)), float(-fB/(2*fA) + math.sqrt(fB**2-4*fA*fC))]
    return [distractor, [1, -b, a*c]]

intervalRange = 3

coefficients = [maybeMakeNegative(random.randint(10, 20)), maybeMakeNegative(random.randint(7, 15)), maybeMakeNegative(random.randint(2, 9))]
discrim = findDiscriminant(coefficients)
while (discrim <= 0 or is_square(discrim)==true):
    coefficients = [maybeMakeNegative(random.randint(10, 20)), maybeMakeNegative(random.randint(7, 15)), maybeMakeNegative(random.randint(2, 9))]
    discrim = findDiscriminant(coefficients)

solution = generateSolution(coefficients)
distractor1 = distractorForgotA(coefficients)
distractor2 = distractorPositiveB(coefficients)
distractor3 = distractorBadDivision(coefficients)
# last distractor is "There are no Real solutions"

solutionList = [solution, distractor1[0], distractor2[0], distractor3[0]]
precision = 1

intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
solutionInterval = [intervalOptions[0], "* $x_1 = %.3f \\text{ and } x_2 = %.3f$, which is the correct option." %(float(solution[0]),  float(solution[1])), 1]
distractor1Interval = [intervalOptions[1], " $x_1 = %.3f \\text{ and } x_2 = %.3f$, which corresponds to using the Quadratic Formula with $a=1$" %(float(distractor1[0][0]), float(distractor1[0][1])), 0]
distractor2Interval = [intervalOptions[2], " $x_1 = %.3f \\text{ and } x_2 = %.3f$, which corresponds to writing the Quadratic Formula as $\\frac{b \\pm \\sqrt{b^2 - 4ac}}{2a}$" %(float(distractor2[0][0]), float(distractor2[0][1])), 0]
distractor3Interval = [intervalOptions[3], " $x_1 = %.3f \\text{ and } x_2 = %.3f$, which corresponds to writing the Quadratic Formula as $-\\frac{b}{2a} \\pm \\sqrt{b^2 - 4ac}$." %(float(distractor3[0][0]), float(distractor3[0][1])), 0]
distractor4Interval = ["\\text{There are no Real solutions}", "Corresponds to getting a negative under the radical or believing that since the quadratic cannot be factored, it has no Real solutions.", 0]

displayStem = 'Solve the quadratic equation below. Then, choose the intervals that the solutions belong to, with $x_1 \\leq x_2$ (if they exist).'
displayProblem = "%s = 0" %generatePolynomialDisplay(coefficients)
displaySolution = "x_1 = %.3f \\text{ and } x_2 = %.3f" %(float(solution[0]),  float(solution[1]))
generalComment = "This requires Quadratic Formula. Just be sure to use the correct formula and watch your signs."

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)
answerList.append(distractor4Interval)

c0 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[0][0][0][0], answerList[0][0][0][1], answerList[0][0][1][0], answerList[0][0][1][1])
c1 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[1][0][0][0], answerList[1][0][0][1], answerList[1][0][1][0], answerList[1][0][1][1])
c2 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[2][0][0][0], answerList[2][0][0][1], answerList[2][0][1][0], answerList[2][0][1][1])
c3 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[3][0][0][0], answerList[3][0][0][1], answerList[3][0][1][0], answerList[3][0][1][1])
c4 = "\\text{There are no Real solutions.}"
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]


answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

thisQuestion="quadraticFormula"
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
