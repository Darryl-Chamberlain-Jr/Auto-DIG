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

thisQuestion="identifyGraphOfRationalFunctionCopy"

# Graph A: VAs at -1, 2, 5
# Graph B: VAs at 1, -2
# Graph C: VAs at -5, -2, 1
# Graph D: VAs at -1, 2

def coefficientsForPoly(zeros):
    a, b, c = zeros
    #(x-a)(x-b)(x-c)
    return [1, -c-a-b, a*b+a*c+b*c, -a*b*c]

#typeList = ["A", "B", "C", "D"]
#type = random.choice(typeList)

displayStem = "Which of the following functions \\textit{could} be the graph below?"
displayProblem = f"{thisQuestion}{version}"

denomGraphA = generatePolynomialDisplay(coefficientsForPoly([-1, 2, 5]))
denomGraphC = generatePolynomialDisplay(coefficientsForPoly([1, -2, -5]))
randomHole = random.choice([-6, -4, -3, 3, 4, 6])
denomGraphB = generatePolynomialDisplay(coefficientsForPoly([1, -2, randomHole]))
denomGraphD = generatePolynomialDisplay(coefficientsForPoly([-1, 2, randomHole]))
possibleNumeratorZerosGraphA = [-6, -5, -4, -3, -2, 1, 3, 4, 6]
possibleNumeratorZerosGraphB = [-6, -5, -4, -3, -1, 2, 3, 4, 5, 6]
possibleNumeratorZerosGraphC = [-6, -4, -3, -1, 2, 3, 4, 5, 6]
possibleNumeratorZerosGraphD = [-6, -5, -4, -3, -2, 1, 3, 4, 5, 6]
numGraphA = generatePolynomialDisplay(coefficientsForPoly(random.sample(possibleNumeratorZerosGraphA, 3)))
numGraphB = generatePolynomialDisplay(coefficientsForPoly(random.sample(possibleNumeratorZerosGraphB, 3)))
numGraphC = generatePolynomialDisplay(coefficientsForPoly(random.sample(possibleNumeratorZerosGraphC, 3)))
numGraphD = generatePolynomialDisplay(coefficientsForPoly(random.sample(possibleNumeratorZerosGraphD, 3)))

option1 = ["f(x) = \\frac{%s}{%s}" %(numGraphA, denomGraphA), "This function has vertical asymptotes at $x=-1$, $x=2$, and $x=5$.", 0]
option2 = ["f(x) = \\frac{%s}{%s}" %(numGraphB, denomGraphB), "This function has vertical asymptotes at $x=-2$, and $x=1$.", 0]
option3 = ["f(x) = \\frac{%s}{%s}" %(numGraphC, denomGraphC), "This function has vertical asymptotes at $x=-5$, $x=-2$, and $x=1$.", 0]
option4 = ["f(x) = \\frac{%s}{%s}" %(numGraphD, denomGraphD), "This function has vertical asymptotes at $x=-1$, and $x=2$.", 0]
option5 = ["\\text{None of the above are possible equations for the graph.}", "If you believe none of the functions above could be the graph, please contact the coordinator.", 0]

if version == "A":
    displaySolution = option1[0]
    option1[2] = 1
if version == "B":
    displaySolution = option2[0]
    option2[2] = 1
if version == "C":
    displaySolution = option3[0]
    option3[2] = 1
else:
    displaySolution = option4[0]
    option4[2] = 1

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "To determine whether the function could be the graph, determine the vertical asymptotes of the graph."

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Graph"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
