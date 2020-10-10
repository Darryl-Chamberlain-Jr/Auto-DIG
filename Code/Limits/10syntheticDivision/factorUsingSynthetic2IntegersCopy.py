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

thisQuestion="factorUsingSynthetic2IntegersCopy"

def generateDisplayAndZeros():
    #Goal: (a0*x+b0)*(a1*x+b1)*(x-z)
    a0 = random.randint(2, 5)
    b0 = maybeMakeNegative(random.randint(2, 5))
    a1 = random.randint(2, 5)
    b1 = maybeMakeNegative(random.randint(2, 5))
    z = maybeMakeNegative(random.randint(2, 5))

    while (gcd(a0, b0)>1 or gcd(a1, b1)>1) or (a0 == a1 and b0 == b1):
        a0 = random.randint(2, 5)
        b0 = maybeMakeNegative(random.randint(2, 5))
        a1 = random.randint(2, 5)
        b1 = maybeMakeNegative(random.randint(2, 5))
        z = maybeMakeNegative(random.randint(2, 5))

    numCo1 = a0*a1
    numCo2 = -a0*a1*z + a0*b1 + a1*b0
    numCo3 = -a0*b1*z - a1*b0*z + b0*b1
    numCo4 = -b0*b1*z
    displayPolynomial = generatePolynomialDisplay([numCo1, numCo2, numCo3, numCo4])
    a0f = float(a0)
    a1f = float(a1)
    b0f = float(b0)
    b1f = float(b1)
    #
    z1 = float(-b0f/a0f)
    z2 = float(-b1f/a1f)
    z3 = z
    #zeros = [float(-b0/a0), float(-b1/a1), z]
    zeros = descendingOrder(z1, z2, z3)
    coefficients = [a0, b0, a1, b1, z]

    return [displayPolynomial, zeros, coefficients]

def descendingOrder(z1, z2, z3):
    # We need to put these in order...
    if (z1 <= z2 and z1 <=z3):
        #Then z1 is the smallest
        if (z2 <= z3):
            zeros = [z1, z2, z3]
        else:
            zeros = [z1, z3, z2]
    # z1 is not the smallest
    elif (z2<=z3):
        if(z1<=z3):
            zeros = [z2, z1, z3]
        else:
            zeros = [z2, z3, z1]
    else:
        if(z1<=z2):
            zeros = [z3, z1, z2]
        else:
            zeros = [z3, z2, z1]
    return zeros

def generateDistractors(coefficients):
    a0, b0, a1, b1, z = coefficients
    a0f = float(a0)
    a1f = float(a1)
    b0f = float(b0)
    b1f = float(b1)
    # Distractor 1: Corresponds to negatives of all zeros.
    distractor1 = descendingOrder(float(b0f/a0f), float(b1f/a1f), -z)
    # Distractor 2: Corresponds to inversing rational roots.
    distractor2 = descendingOrder(float(-a0f/b0f), float(-a1f/b1f), z)
    # Distractor 3: Corresponds to negatives of all zeros AND inversing rational roots.
    distractor3 = descendingOrder(float(a0f/b0f), float(a1f/b1f), -z)
    # Distractor 4: Corresponds to moving factors from one rational to another.
    distractor4 = descendingOrder(b0, float(b1f/(a1f*a0f)), -z)

    distractors = [distractor1, distractor2, distractor3, distractor4]
    return distractors

intervalRange = 2
precision = 1

info = generateDisplayAndZeros()
displayPolynomial = info[0]
zeros = info[1]
coefficients = info[2]

distractors = generateDistractors(coefficients)
solution = zeros

solutionList = [solution, distractors[0], distractors[1], distractors[2], distractors[3]]
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = intervalOptions[0]
distractor1Interval = intervalOptions[1]
distractor2Interval = intervalOptions[2]
distractor3Interval = intervalOptions[3]
distractor4Interval = intervalOptions[4]

solutionInterval.append("* This is the solution!")
distractor1Interval.append(" Distractor 1: Corresponds to negatives of all zeros.")
distractor2Interval.append(" Distractor 2: Corresponds to inversing rational roots.")
distractor3Interval.append(" Distractor 3: Corresponds to negatives of all zeros AND inversing rational roots.")
distractor4Interval.append(" Distractor 4: Corresponds to moving factors from one rational to another.")

solutionInterval.append(1)
distractor1Interval.append(0)
distractor2Interval.append(0)
distractor3Interval.append(0)
distractor4Interval.append(0)

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

displayStem = "Factor the polynomial below completely. Then, choose the intervals the zeros of the polynomial belong to, where $z_1 \\leq z_2 \\leq z_3$. \\textit{To make the problem easier, all zeros are between -5 and 5.}"
displayProblem = "f(x) = %s" %displayPolynomial
displaySolution = solution
generalComment = "Remember to try the middle-most integers first as these normally are the zeros. Also, once you get it to a quadratic, you can use your other factoring techniques to finish factoring."

c0 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], \\text{   and   } z_3 \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1], answerList[0][1][0], answerList[0][1][1], answerList[0][2][0], answerList[0][2][1])
c1 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], \\text{   and   } z_3 \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1], answerList[1][1][0], answerList[1][1][1], answerList[1][2][0], answerList[1][2][1])
c2 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], \\text{   and   } z_3 \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1], answerList[2][1][0], answerList[2][1][1], answerList[2][2][0], answerList[2][2][1])
c3 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], \\text{   and   } z_3 \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1], answerList[3][1][0], answerList[3][1][1], answerList[3][2][0], answerList[3][2][1])
c4 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], \\text{   and   } z_3 \\in [%s, %s]" %(answerList[4][0][0], answerList[4][0][1], answerList[4][1][0], answerList[4][1][1], answerList[4][2][0], answerList[4][2][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][3], answerList[1][3], answerList[2][3], answerList[3][3], answerList[4][3]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][4] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
