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

# \\frac{(a0*x-b0)(a1*x-b1)(x-b3)}{(a0*x-b0)(a2*x-b2)}

def generateRationalFactor():
    a = random.randint(2, 6)
    b = maybeMakeNegative(random.randint(2, 5))
    while (gcd(abs(a), abs(b)) > 1):
        a = random.randint(2, 6)
        b = maybeMakeNegative(random.randint(2, 5))
    return [a, b]

def createNumAndDenom0():
    a0, b0 = generateRationalFactor()
    a1, b1 = generateRationalFactor()
    a2, b2 = [1, maybeMakeNegative(random.randint(2, 5))]
    z0 = float(b0)/float(a0)
    z1 = float(b1)/float(a1)
    z2 = float(b2)/float(a2)
    while (z0 == z1) or (z0 == z2) or (z1 == z2):
        a0, b0 = generateRationalFactor()
        a1, b1 = generateRationalFactor()
        a2, b2 = [1, maybeMakeNegative(random.randint(2, 5))]
        z0 = float(b0)/float(a0)
        z1 = float(b1)/float(a1)
        z2 = float(b2)/float(a2)
    b3 = maybeMakeNegative(random.randint(1, 4))
    coeffNumA = a0*a1
    coeffNumB = -a0*b1 - a1*b0 - a0*a1*b3
    coeffNumC = b0*b1 + a0*b1*b3 + a1*b0*b3
    coeffNumD = -b0*b1*b3
    numerator = generatePolynomialDisplay([coeffNumA, coeffNumB, coeffNumC, coeffNumD])
    #(a0*x-b0)(a2*x-b2)
    coeffDenA = a0*a2
    coeffDenB = -a0*b2 - a2*b0
    coeffDenC = b0*b2
    denominator = generatePolynomialDisplay([coeffDenA, coeffDenB, coeffDenC])
    #
    falseHorizontalAsy = float(a1) / float(a2)
    hole = z0
    verticalAsy = z2
    obliqueAsyA = a1
    obliqueAsyB = -a1*b3 - b1 + b2*a1
    obliqueAsy = generatePolynomialDisplay([obliqueAsyA, obliqueAsyB])
    #
    return [numerator, denominator, obliqueAsy, verticalAsy, hole, falseHorizontalAsy]

def createNumAndDenomNon0():
    a0, b0 = generateRationalFactor()
    a1, b1 = generateRationalFactor()
    a2, b2 = [maybeMakeNegative(random.randint(2, 5)), maybeMakeNegative(random.randint(2, 5))]
    z0 = float(b0)/float(a0)
    z1 = float(b1)/float(a1)
    z2 = float(b2)/float(a2)
    b3 = maybeMakeNegative(random.randint(1, 4))
    while (z0 == z1) or (z0 == z2) or (z1 == z2) or (z2 == float(b3)):
        a0, b0 = generateRationalFactor()
        a1, b1 = generateRationalFactor()
        a2, b2 = [1, maybeMakeNegative(random.randint(2, 5))]
        z0 = float(b0)/float(a0)
        z1 = float(b1)/float(a1)
        z2 = float(b2)/float(a2)
        b3 = maybeMakeNegative(random.randint(1, 4))
    coeffNumA = a0*a1
    coeffNumB = -a0*b1 - a1*b0 - a0*a1*b3
    coeffNumC = b0*b1 + a0*b1*b3 + a1*b0*b3
    coeffNumD = -b0*b1*b3
    numerator = generatePolynomialDisplay([coeffNumA, coeffNumB, coeffNumC, coeffNumD])
    #(a0*x-b0)(a2*x-b2)(x-b3)
    coeffDenA = a0*a2
    coeffDenB = -a0*b2 - a2*b0 - a2*b0
    coeffDenC = b0*b2 + a0*b2*b3 + a2*b0*b3
    coeffDenD = -b0*b2*b3
    denominator = generatePolynomialDisplay([coeffDenA, coeffDenB, coeffDenC, coeffDenD])
    #
    horizontalAsy = float(a1) / float(a2)
    hole = z0
    verticalAsy1 = z2
    verticalAsy2 = b3
    #
    return [numerator, denominator, verticalAsy1, verticalAsy2, hole, horizontalAsy]
############################################
HA = random.randint(0, 1)

if HA == 0:
    numerator, denominator, obliqueAsy, verticalAsy, hole, falseHorizontalAsy = createNumAndDenom0()
    option1 = ["\\text{Oblique Asymptote of } y = %s." %(obliqueAsy), "This corresponds to flipping the numerator and denominator, then using synthetic division to find the oblique asymptote.", 0]
    option2 = ["\\text{Horizontal Asymptote of } y = %.3f " %falseHorizontalAsy, "This corresponds to using rule for Horizontal Asymptote when degree of numerator and denominator match.", 0]
    option3 = ["\\text{Horizontal Asymptote at } y = %.3f" %verticalAsy, "This corresponds to considering where the denominator is equal to 0 as horizontal asymptote.", 0]
    option4 = ["\\text{Horizontal Asymptote of } y = %.3f \\text{ and Oblique Asymptote of } y = %s" %(falseHorizontalAsy, obliqueAsy), "This corresponds to believing there can be both a horizontal and oblique asymptote.", 0]
    option5 = ["\\text{Horizontal Asymptote of } y = 0", "* This is the correct option.", 1]
    displaySolution = option5[0]
else:
    numerator, denominator, verticalAsy1, verticalAsy2, hole, horizontalAsy = createNumAndDenomNon0()
    option1 = ["\\text{Horizontal Asymptote of } y = %.3f " %horizontalAsy, "* This is the correct option.", 1]
    option2 = ["\\text{Horizontal Asymptote of } y = 0 ", "This corresponds to using the rule for Horizontal Asymptote when the degree of the denominator is larger than the numerator.", 0]
    option3 = ["\\text{Vertical Asymptote of } y = %.3f " %verticalAsy1, "This corresponds to the hole at $x = %.3f$." %verticalAsy1, 0]
    option4 = ["\\text{Vertical Asymptote of } y = %d " %verticalAsy2, "This corresponds to the hole at $x = %d$." %verticalAsy2, 0]
    option5 = ["\\text{None of the above}", "This corresponds to believing there should be an oblique asymptote.", 0]
    displaySolution = option1[0]

displayStem = "Determine the horizontal and/or oblique asymptotes in the rational function below."
displayProblem = "f(x) = \\frac{%s}{%s}" %(numerator, denominator)
generalComment = "We have a Horizontal Asymptote if the degree of the numerator is smaller than or equal to the degree of the denominator. We have an Oblique Asymptote if the degree of the numerator is larger than the degree of the denominator. We cannot have both!"

answerList = [option1, option2, option3, option4, option5]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
