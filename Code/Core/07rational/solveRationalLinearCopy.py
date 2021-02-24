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
#import fractions

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

def generateCoefficients(numberOfSolutions):
    # structure: (a/bx+c) - d = e/f(bx+c)
    if (numberOfSolutions==0):
        mask = random.randint(5, 14)
        a = maybeMakeNegative(random.randint(2, 9)) * mask
        d = -1
        f = 1
        e = a
        b = maybeMakeNegative(random.randint(2, 9)) * mask
        c = maybeMakeNegative(random.randint(2, 9)) * mask
        return [a, b, c, d, e, f]
    else:
        a = float(maybeMakeNegative(random.randint(2, 9)))
        b = float(maybeMakeNegative(random.randint(2, 9)))
        c = float(maybeMakeNegative(random.randint(2, 9)))
        d = float(maybeMakeNegative(random.randint(2, 9)))
        e = float(maybeMakeNegative(random.randint(2, 9)))
        f = float(maybeMakeNegative(random.randint(2, 9)))
        makeSolutionExist = float((-f*a +e + d*c*f)/(-d*f*b) + c/b)
        while (makeSolutionExist==0):
            a = float(maybeMakeNegative(random.randint(2, 9)))
            b = float(maybeMakeNegative(random.randint(2, 9)))
            c = float(maybeMakeNegative(random.randint(2, 9)))
            d = float(maybeMakeNegative(random.randint(2, 9)))
            e = float(maybeMakeNegative(random.randint(2, 9)))
            f = float(maybeMakeNegative(random.randint(2, 9)))
            makeSolutionExist = float((-f*a + e + d*c*f)/(-d*f*b) + c/b)
    return [Integer(a), Integer(b), Integer(c), Integer(d), Integer(e), Integer(f)]

def generateSolution(coefficients, numberOfSolutions):
    a = float(coefficients[0])
    b = float(coefficients[1])
    c = float(coefficients[2])
    d = float(coefficients[3])
    e = float(coefficients[4])
    f = float(coefficients[5])
    if (numberOfSolutions == 0):
        return float(-c/b)
    else:
        return float((-f*a +e +d*c*f)/(-d*f*b))

def generateSolutionInterval(solution, intervalRange):
    interval = createInterval(solution, intervalRange)
    return interval

# Distractors
# No solution when there is a solution / Solution when there is no solution
# Single and doubles
def distractorMisDistributeC(coefficients):
    a, b, c, d, e, f = coefficients
    return [a, b, -c, d, e, f]

def distractorForgetF(coefficients):
    a, b, c, d, e, f = coefficients
    return [a, b, c, d, e, int(1)]

def distractorForgetA(coefficients):
    a, b, c, d, e, f = coefficients
    return [int(1), b, c, d, e, f]

def intervalToString(interval):
    return ['x \\in [%s,%s]' %(interval[0], interval[1])]

def stringForAnswersWithTwoIntervals(leftInterval, rightInterval):
    leftL, leftR = leftInterval
    rightL, rightR = rightInterval
    return ['x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s,%s]' %(leftL, leftR, rightL, rightR)]

# Two types of questions:
    # Rational -> Linear with no solutions
    # Rational -> Linear with one soltion

intervalRange = 2

numberOfSolutions = random.randint(0, 1)
coefficients = generateCoefficients(numberOfSolutions)
solution = generateSolution(coefficients, numberOfSolutions)

factorNumerator1 = coefficients[0]
factorDenominator1 = generatePolynomialDisplay([coefficients[1], coefficients[2]])
factorNumerator2 = coefficients[3]
factorNumerator3 = coefficients[4]
factorDenominator3 = generatePolynomialDisplay([coefficients[1]*coefficients[5], coefficients[5]*coefficients[2]])

if coefficients[3] < 0:
    leftSide = "\\frac{%s}{%s} + %s" %(coefficients[0], factorDenominator1, -coefficients[3])
else:
    leftSide = "\\frac{%s}{%s} - %s" %(coefficients[0], factorDenominator1, coefficients[3])

if (numberOfSolutions==0):
    solutionInterval = [['\\text{All solutions lead to invalid or complex values in the equation.}'], "*$x = %.3f$ leads to dividing by 0 in the original equation and thus is not a valid solution, which is the correct option." %solution, 1]
    solutionLength = 0
    distractor1 = solution
    distractor1Length = 1
    distractor1Interval = [intervalToString(generateSolutionInterval(float(solution), intervalRange)), "$x = %.3f$, which corresponds to not checking if this value leads to dividing by 0 in the original equation and thus is not a valid solution." %solution, 0]
else:
    solutionInterval = [intervalToString(generateSolutionInterval(solution, intervalRange)), "* $x = %.3f$, which is the correct option." %solution, 1]
    solutionLength = 1
    distractor1 = '\\text{All solutions are invalid or lead to complex values in the equation.}'
    distractor1Length = 0
    distractor1Interval = [["\\text{All solutions lead to invalid or complex values in the equation.}"], "This corresponds to thinking $x = %.3f$ leads to dividing by zero in the original equation, which it does not." %solution, 0]

distractor2 = generateSolution(distractorMisDistributeC(coefficients), 1)
distractor2Length = 1
if (distractor1 == distractor2):
    distractor2 = distractor2 + 1
else:
    distractor2 = distractor2
displayStem = 'Solve the rational equation below. Then, choose the interval(s) that the solution(s) belongs to.'
displayProblem = '\\frac{%s}{%s} + %s = \\frac{%s}{%s}' %(factorNumerator1, factorDenominator1, -factorNumerator2, factorNumerator3, factorDenominator3)
if (numberOfSolutions==0):
    displaySolution = '\\text{all solutions are invalid or lead to complex values in the equation.}'
else:
    displaySolution = "x = %.3f" %solution
distractor3 = [min(generateSolution(distractorMisDistributeC(coefficients), 1), solution), max(generateSolution(distractorMisDistributeC(coefficients), 1), solution)]
distractor4 = [min(generateSolution(distractorForgetF(coefficients), 1), solution), max(generateSolution(distractorForgetF(coefficients), 1), solution)]

if(solutionLength == 0):
    firstSolutionSet = [distractor1, distractor2, distractor3[0], distractor4[0]]
else:
    firstSolutionSet = [solution, distractor2, distractor3[0], distractor4[0]]
precision = 1
intervalOptionsFirstSet = createIntervalOptions(firstSolutionSet, intervalRange, precision)
secondSolutionSet = [distractor3[1], distractor4[1]]
intervalOptionsSecondSet = createIntervalOptions(secondSolutionSet, intervalRange, precision)

distractor2Interval = [intervalToString(intervalOptionsFirstSet[1]), "$x = %.3f$, which corresponds to not distributing the factor $%s$ correctly when trying to eliminate the fraction." %(distractor2, generatePolynomialDisplay([coefficients[1], coefficients[2]])), 0]
distractor3Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[2], intervalOptionsSecondSet[0]), "$x = %.3f \\text{ and } x = %.3f$, which corresponds to getting the correct solution and believing there should be a second solution to the equation." %(distractor3[0], distractor3[1]), 0]
distractor4Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[3], intervalOptionsSecondSet[1]), "$x = %.3f \\text{ and } x = %.3f$, which corresponds to getting the correct solution and believing there should be a second solution to the equation." %(distractor4[0], distractor4[1]), 0]

generalComment = "Distractors are different based on the number of solutions. Remember that after solving, we need to make sure our solution does not make the original equation divide by zero!"

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

c0 = answerList[0][0][0]
c1 = answerList[1][0][0]
c2 = answerList[2][0][0]
c3 = answerList[3][0][0]
c4 = answerList[4][0][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [ answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1] ]

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
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
