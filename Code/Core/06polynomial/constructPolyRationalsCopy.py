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

def generateFactor():
    a = random.randint(1, 5)
    b = maybeMakeNegative(random.randint(1, 7))
    while gcd(abs(a), abs(b)) > 1:
        a = random.randint(1, 5)
        b = maybeMakeNegative(random.randint(1, 7))
    return [a, b]

def listZeros(factor1, factor2):
    z1 = factor1[1]/factor1[0]
    z2 = - factor1[1]/factor1[0]
    z3 =  factor2[1]/factor2[0]
    z4 = - factor2[1]/factor2[0]
    return [z1, z2, z3, z4]

def generateSolution(factor1, factor2, factor3):
    f10, f11 = factor1
    f20, f21 = factor2
    f30, f31 = factor3
    a = f10*f20*f30
    b = -f11*f20*f30 - f10*f21*f30 - f10*f20*f31
    c = f11*f20*f31 + f10*f21*f31 + f11*f21*f30
    d = -f11*f21*f31
    return [a, b, c, d]

def distractorConjugateAllZeros(factor1, factor2, factor3):
    f10, f11 = factor1
    f20, f21 = factor2
    f30, f31 = factor3
    #
    f11 = -f11
    f21 = -f21
    f31 = -f31
    #
    a = f10*f20*f30
    b = -f11*f20*f30 - f10*f21*f30 - f10*f20*f31
    c = f11*f20*f31 + f10*f21*f31 + f11*f21*f30
    d = -f11*f21*f31
    return [a, b, c, d]

def distractorOppositeD(factor1, factor2, factor3):
    f10, f11 = factor1
    f20, f21 = factor2
    f30, f31 = factor3

    a = f10*f20*f30
    b = -f11*f20*f30 - f10*f21*f30 - f10*f20*f31
    c = f11*f20*f31 + f10*f21*f31 + f11*f21*f30
    d = f11*f21*f31

    return [a, b, c, d]

def distractorConjugateOneZero(factor1, factor2, factor3):
    f10, f11 = factor1
    f20, f21 = factor2
    f30, f31 = factor3

    f11 = -f11

    a = f10*f20*f30
    b = -f11*f20*f30 - f10*f21*f30 - f10*f20*f31
    c = f11*f20*f31 + f10*f21*f31 + f11*f21*f30
    d = -f11*f21*f31

    return [a, b, c, d]

def distractorConjugateTwoZeros(factor1, factor2, factor3):
    f10, f11 = factor1
    f20, f21 = factor2
    f30, f31 = factor3

    f11 = -f11
    f21 = -f21

    a = f10*f20*f30
    b = -f11*f20*f30 - f10*f21*f30 - f10*f20*f31
    c = f11*f20*f31 + f10*f21*f31 + f11*f21*f30
    d = -f11*f21*f31

    return [a, b, c, d]

def generateSolutionInterval(solution, intervalRange):
    intervalList = [[]]*len(solution)
    for i in xrange(0, len(solution)):
        intervalList[i] = createInterval(solution[i], intervalRange)
    return intervalList

intervalRange = 6

factor1 = generateFactor()
factor2 = generateFactor()
factor3 = generateFactor()
zero1 = float(factor1[1])/float(factor1[0])
zero2 = float(factor2[1])/float(factor2[0])
zero3 = float(factor3[1])/float(factor3[0])

while (abs(zero1) == abs(zero2) or abs(zero1) == abs(zero3) or abs(zero2) == abs(zero3)):
    factor1 = generateFactor()
    factor2 = generateFactor()
    factor3 = generateFactor()
    zero1 = float(factor1[1])/float(factor1[0])
    zero2 = float(factor2[1])/float(factor2[0])
    zero3 = float(factor3[1])/float(factor3[0])

#polynomial = (factor1[0]*x-factor1[1])*(factor2[0]*x-factor2[1])*(factor3[0]*x-factor3[1])

solution = generateSolution(factor1, factor2, factor3)
displaySolution = generatePolynomialDisplay(solution)

distractor1 = distractorConjugateAllZeros(factor1, factor2, factor3)
distractor2 = distractorOppositeD(factor1, factor2, factor3)
distractor3 = distractorConjugateOneZero(factor1, factor2, factor3)
distractor4 = distractorConjugateTwoZeros(factor1, factor2, factor3)

solutionList = [solution, distractor1, distractor2, distractor3, distractor4]
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
solutionInterval = [intervalOptions[0], "* $%s$, which is the correct option." %displaySolution, 1]
distractor1Interval = [intervalOptions[1],"$%s$, which corresponds to multiplying out $(%s)(%s)(%s)$." %( generatePolynomialDisplay(distractor1), generatePolynomialDisplay([factor1[0], factor1[1]]), generatePolynomialDisplay([factor2[0], factor2[1]]), generatePolynomialDisplay([factor3[0], factor3[1]]) ), 0]
distractor2Interval = [intervalOptions[2], "$%s$, which corresponds to multiplying everything correctly except the constant term." %generatePolynomialDisplay(distractor2), 0]
distractor3Interval = [intervalOptions[3], "$%s$, which corresponds to multiplying out $(%s)(%s)(%s)$." %(generatePolynomialDisplay(distractor3), generatePolynomialDisplay([factor1[0], factor1[0]]), generatePolynomialDisplay([factor2[0], -factor2[0]]),generatePolynomialDisplay([factor3[0], -factor3[0]])), 0]
distractor4Interval = [intervalOptions[4], "$%s$, which corresponds to multiplying out $(%s)(%s)(%s)$." %(generatePolynomialDisplay(distractor4), generatePolynomialDisplay([factor1[0], factor1[0]]), generatePolynomialDisplay([factor2[0], factor2[0]]),generatePolynomialDisplay([factor3[0], -factor3[0]])), 0]

displayStem = 'Construct the lowest-degree polynomial given the zeros below. Then, choose the intervals that contain the coefficients of the polynomial in the form $ax^3+bx^2+cx+d$.'

if factor1[0] == 1:
    displayZero1 = factor1[1]
else:
    displayZero1 = "\\frac{%s}{%s}" %(factor1[1], factor1[0])
#
if factor2[0] == 1:
    displayZero2 = factor2[1]
else:
    displayZero2 = "\\frac{%s}{%s}" %(factor2[1], factor2[0])
#
if factor3[0] == 1:
    displayZero3 = factor3[1]
else:
    displayZero3 = "\\frac{%s}{%s}" %(factor3[1], factor3[0])
#
displayProblem = "%s, %s, \\text{ and } %s" %(displayZero1, displayZero2, displayZero3)
answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

displayFactor1 = generatePolynomialDisplay([factor1[0], -factor1[1] ])
displayFactor2 = generatePolynomialDisplay([factor2[0], -factor2[1] ])
displayFactor3 = generatePolynomialDisplay([factor3[0], -factor3[1] ])
generalComment = "To construct the lowest-degree polynomial, you want to multiply out $(%s)(%s)(%s)$" %(displayFactor1, displayFactor2, displayFactor3)
c0 = "a \\in [%s, %s], b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[0][0][0][0], answerList[0][0][0][1], answerList[0][0][1][0], answerList[0][0][1][1], answerList[0][0][2][0], answerList[0][0][2][1], answerList[0][0][3][0], answerList[0][0][3][1])
c1 = "a \\in [%s, %s], b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[1][0][0][0], answerList[1][0][0][1], answerList[1][0][1][0], answerList[1][0][1][1], answerList[1][0][2][0], answerList[1][0][2][1], answerList[1][0][3][0], answerList[1][0][3][1])
c2 = "a \\in [%s, %s], b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[2][0][0][0], answerList[2][0][0][1], answerList[2][0][1][0], answerList[2][0][1][1], answerList[2][0][2][0], answerList[2][0][2][1], answerList[2][0][3][0], answerList[2][0][3][1])
c3 = "a \\in [%s, %s], b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[3][0][0][0], answerList[3][0][0][1], answerList[3][0][1][0], answerList[3][0][1][1], answerList[3][0][2][0], answerList[3][0][2][1], answerList[3][0][3][0], answerList[3][0][3][1])
c4 = "a \\in [%s, %s], b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[4][0][0][0], answerList[4][0][0][1], answerList[4][0][1][0], answerList[4][0][1][1], answerList[4][0][2][0], answerList[4][0][2][1], answerList[4][0][3][0], answerList[4][0][3][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
