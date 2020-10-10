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

thisQuestion="evaluateLimitGraphically"

stemType = random.randint(0, 2)

if stemType == 0:
    xApproaches = random.choice([-4, -2, 1, 3])
    displayStem = "For the graph below, evaluate the limit: $ \\displaystyle \\lim_{x \\rightarrow %d} f(x)$." %xApproaches
    if xApproaches == -4:
        option1 = ["0", "", 1]
        option2 = ["-\\infty", "", 0]
        option3 = ["-6", "", 0]
        option4 = ["\\text{The limit does not exist}", "", 0]
        option5 = ["\\text{None of the above}", "", 0]
    elif xApproaches == -2:
        option1 = ["3", "", 1]
        option2 = ["-2", "", 0]
        option3 = ["-\\infty", "", 0]
        option4 = ["\\text{The limit does not exist}", "", 0]
        option5 = ["\\text{None of the above}", "", 0]
    elif xApproaches == 1:
        option1 = ["6", "", 0]
        option2 = ["3", "", 0]
        option3 = ["-\\infty", "", 0]
        option4 = ["\\text{The limit does not exist}", "", 1]
        option5 = ["\\text{None of the above}", "", 0]
    else:
        option1 = ["-\\infty", "", 1]
        option2 = ["-2", "", 0]
        option3 = ["1", "", 0]
        option4 = ["\\text{The limit does not exist}", "", 0]
        option5 = ["\\text{None of the above}", "", 0]
    generalComment = "\\textbf{General Comments:} Remember that the limit does not exist if the left-hand and right-hand limits do not match."
elif stemType == 1:
    limit = random.choice([0, 3, -8])
    if limit == -8:
        displayStem = "For the graph below, find the value(s) $a$ that makes the statement true: $ \\displaystyle \\lim_{x \\rightarrow a} f(x) = -\\infty$."
        option1 = ["3", "", 0]
        option2 = ["-2", "", 0]
        option3 = ["-\\infty", "", 0]
        option4 = ["\\text{Multiple } a \\text{ make the statement true}.", "", 1]
        option5 = ["\\text{No } a \\text{ make the statement true}.", "", 0]
    else:
        displayStem = "For the graph below, find the value(s) $a$ that makes the statement true: $ \\displaystyle \\lim_{x \\rightarrow a} f(x) = %d$." %limit
        if limit == 0:
            option1 = ["3", "", 0]
            option2 = ["0", "", 0]
            option3 = ["-4", "", 0]
            option4 = ["\\text{Multiple } a \\text{ make the statement true}.", "", 1]
            option5 = ["\\text{No } a \\text{ make the statement true}.", "", 0]
        else:
            option1 = ["-2", "", 0]
            option2 = ["-\\infty", "", 0]
            option3 = ["1", "", 0]
            option4 = ["\\text{Multiple } a \\text{ make the statement true}.", "", 1]
            option5 = ["\\text{No } a \\text{ make the statement true}.", "", 0]
    generalComment = "\\textbf{General Comments:} There can be multiple $a$ values that make the statement true! For the limit, draw a horizontal line and determine if an $x$ value makes the limit exist."
else:
    displayStem = "For the graph below, find the value(s) $a$ that makes the statement true: $ \\displaystyle \\lim_{x \\rightarrow a} f(x)$ does not exist."
    option1 = ["-2", "", 0]
    option2 = ["1", "", 1]
    option3 = ["3", "", 0]
    option4 = ["\\text{Multiple } a \\text{ make the statement true}.", "", 0]
    option5 = ["\\text{No } a \\text{ make the statement true}.", "", 0]
    generalComment = "\\textbf{General Comments:} Remember that the limit does not exist if the left-hand and right-hand limits do not match."

displayProblem = f"{thisQuestion}{version}"

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
displayProblemType="Graph"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
