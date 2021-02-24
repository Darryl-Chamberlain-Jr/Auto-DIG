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

# Evaluate a one-sided limit that is easy to graph (rational function) f(x)= a(1/x-h)^n + k
shift = [maybeMakeNegative(random.randint(1, 9)), random.randint(1, 9)]
a = maybeMakeNegative(random.randint(1, 9))
while len(set(shift)) != len(shift):
    shift = [maybeMakeNegative(random.randint(1, 9)), random.randint(1, 9)]
exponent = random.randint(3, 9)
if shift[0] < 0:
    rationalFunction = "\\frac{%d}{(x+%d)^%d}+%d" %(a, -shift[0], exponent, shift[1])
else:
    rationalFunction = "\\frac{%d}{(x-%d)^%d}+%d" %(a, shift[0], exponent, shift[1])

atOrAwayFromVA = random.randint(0, 1)
if atOrAwayFromVA == 0:
    xApproaches = shift[0]
else:
    xApproaches = -shift[0]

displayStem = "Evaluate the one-sided limit of the function $f(x)$ below, if possible."
option1 = ["\\infty", "", 0]
option2 = ["-\\infty", "", 0]
option3 = ["f(%d)" %xApproaches, "", 0]
option4 = ["\\text{The limit does not exist}", "", 0]
option5 = ["\\text{None of the above}", "", 0]

leftOrRightLimit = random.randint(0, 1)

if leftOrRightLimit == 0:
    displayProblem = "\\lim_{x \\rightarrow %d^-} %s" %(xApproaches, rationalFunction)
    if atOrAwayFromVA == 0:
        if exponent % 2 == 0:
           if a < 0:
                option2[2] = 1
           else:
                option1[2] = 1
        else:
            if a < 0:
                option1[2] = 1
            else:
                option2[2] = 1
    else:
        option3[2] = 1
else:
    displayProblem = "\\lim_{x \\rightarrow %d^+} %s" %(xApproaches, rationalFunction)
    if atOrAwayFromVA == 0:
        if exponent % 2 == 0:
           if a < 0:
                option2[2] = 1
           else:
                option1[2] = 1
        else:
            if a < 0:
                option2[2] = 1
            else:
                option1[2] = 1
    else:
        option3[2] = 1

generalComment = "\\textbf{General comments:} You should be able to graph the rational function displayed. If not, go back to Module 7 to learn about the general shape of rational functions."

answerList = [option1, option2, option3]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], option4[0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], option4[1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], option4[2], option5[2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        displaySolution = choices[answerIndex]
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
