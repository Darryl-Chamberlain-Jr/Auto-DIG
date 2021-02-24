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
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

def generateFunctionAndImportantCoefficients():
    degree = int(random.randint(2, 4))
    an = int(random.randint(2, 7))
    a0 = int(random.randint(2, 7))
    if degree == 4:
        coefficients = [an, int(random.randint(2, 7)), int(random.randint(2, 7)), int(random.randint(2, 7)), a0]
    elif degree == 3:
        coefficients = [an, int(random.randint(2, 7)), int(random.randint(2, 7)), a0]
    else:
      coefficients = [an, int(random.randint(2, 7)), a0]
    function = generatePolynomialDisplay(coefficients)
    return [function, a0, an]

def generateFactors(num):
    factors = []
    counter = 1
    while (counter<=abs(num)):
        if (abs(num) % counter == 0):
            factors.append(counter)
        else:
            placeHolder = "I'm a dead placeholder!"
        counter = counter + 1
    return factors

def generateFactorsList(factors):
    factorsList = ""
    for i in range(len(factors) - 1):
        factorsList += "\\pm %d," %factors[i]
    factorsList += "\\pm %d" %factors[len(factors)-1]
    return factorsList

def generateSolutionAndDistractors(type, a0, an):
    # * This is the solution.
    # Distractor 1: Corresponds to the plus or minus factors of a1 only.
    # Distractor 2: Corresponds to the plus or minus of the quotient of the factors
    # Distractor 3: Corresponds to the plus or minus of the inverse quotient (an/a0) of the factors.
    # Distractor 4: Corresponds to not recognizing Integers as a subset of Rationals.
    factorsA0 = generateFactors(a0)
    factorsA0List = generateFactorsList(factorsA0)
    factorsAn = generateFactors(an)
    factorsAnList = generateFactorsList(factorsAn)
    #
    if type == "Rational":
        solution = ["\\text{ All combinations of: }\\frac{%s}{%s}" %(factorsA0List, factorsAnList), "* This is the solution \\textbf{since we asked for the possible Rational roots}!", 1]
        distractor1 = [factorsAnList, " Distractor 1: Corresponds to the plus or minus factors of a1 only.", 0]
        distractor2 = [factorsA0List, "This would have been the solution \\textbf{if asked for the possible Integer roots}!", 0]
        distractor3 = ["\\text{ All combinations of: }\\frac{%s}{%s}" %(factorsAnList, factorsA0List), " Distractor 3: Corresponds to the plus or minus of the inverse quotient (an/a0) of the factors. ", 0]
        distractor4 = ["\\text{ There is no formula or theorem that tells us all possible Rational roots.}", " Distractor 4: Corresponds to not recalling the theorem for rational roots of a polynomial.", 0]
    else:
        solution = [factorsA0List, "* This is the solution \\textbf{since we asked for the possible Integer roots}!", 1]
        distractor1 = [factorsAnList, " Distractor 1: Corresponds to the plus or minus factors of a1 only.", 0]
        distractor2 = ["\\text{ All combinations of: }\\frac{%s}{%s}" %(factorsA0List, factorsAnList), "This would have been the solution \\textbf{if asked for the possible Rational roots}!", 0]
        distractor3 = ["\\text{ All combinations of: }\\frac{%s}{%s}" %(factorsAnList, factorsA0List), " Distractor 3: Corresponds to the plus or minus of the inverse quotient (an/a0) of the factors. ", 0]
        distractor4 = ["\\text{There is no formula or theorem that tells us all possible Integer roots.}", " Distractor 4: Corresponds to not recognizing Integers as a subset of Rationals.", 0]
    preShuffle = [solution, distractor1, distractor2, distractor3]
    random.shuffle(preShuffle)
    answerList = [preShuffle[0], preShuffle[1], preShuffle[2], preShuffle[3], distractor4]
    return [answerList, solution[0]]

# Begin problem
info = generateFunctionAndImportantCoefficients()
while (info[1]==info[2]):
    info = generateFunctionAndImportantCoefficients()
displayPolynomial = info[0]
rationalOrIntegerList = ["Rational", "Integer"]
rationalOrInteger = rationalOrIntegerList[random.randint(0, 1)]
answerList, displaySolution = generateSolutionAndDistractors(rationalOrInteger, info[1], info[2])

displayStem = "What are the \\textit{possible %s} roots of the polynomial below?" %rationalOrInteger
displayProblem = "f(x) = %s" %displayPolynomial
generalComment = "We have a way to find the possible Rational roots. The possible Integer roots are the Integers in this list."

c0 = answerList[0][0]
c1 = answerList[1][0]
c2 = answerList[2][0]
c3 = answerList[3][0]
c4 = answerList[4][0]
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
if debug=="save":
    writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
