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

def makeChoices(values):
    displayChoices = "\\{ %.4f, %.4f, %.4f, %.4f \\}" %(values[0], values[1], values[2], values[3])
    return displayChoices

a = float(random.randint(1, 10))
positiveValuesToTest = [a+0.1, a+0.01, a+0.001, a+0.0001]
negativeValuesToTest = [a-0.1, a-0.01, a-0.001, a-0.0001]
distractorPositiveValuesToTest = [a, a+0.1, a+0.01, a+0.001]
distractorNegativeValuesToTest = [a, a-0.1, a-0.01, a-0.001]
distractorBothValuesToTest = [a-0.1, a-0.01, a+0.01, a+0.1]

whichSide = random.randint(0,1)
if whichSide == 0:
    side = "+"
    option1 = [makeChoices(positiveValuesToTest), "This is correct!", 1]
    option2 = [makeChoices(negativeValuesToTest), "These values would estimate the limit of %d on the left." %a, 0]
    option3 = [makeChoices(distractorPositiveValuesToTest), "If we get $\\frac{0}{0}$ or $\\frac{\\infty}{\\infty}$, the value %d doesn't help us estimate the limit." %int(a), 0]
    option4 = [makeChoices(distractorNegativeValuesToTest), "If we get $\\frac{0}{0}$ or $\\frac{\\infty}{\\infty}$, the value %d doesn't help us estimate the limit." %int(a), 0]
    option5 = [makeChoices(distractorBothValuesToTest), "These values would estimate the limit at the point and not a one-sided limit.", 0]
    displaySolution = option1[0]
    descriptionOfSide = "right"
else:
    side = "-"
    option1 = [makeChoices(positiveValuesToTest), "These values would estimate the limit of %d on the right." %a, 0]
    option2 = [makeChoices(negativeValuesToTest), "This is correct!", 1]
    option3 = [makeChoices(distractorPositiveValuesToTest), "If we get $\\frac{0}{0}$ or $\\frac{\\infty}{\\infty}$, the value %d doesn't help us estimate the limit." %int(a), 0]
    option4 = [makeChoices(distractorNegativeValuesToTest), "If we get $\\frac{0}{0}$ or $\\frac{\\infty}{\\infty}$, the value %d doesn't help us estimate the limit." %int(a), 0]
    option5 = [makeChoices(distractorBothValuesToTest), "These values would estimate the limit at the point and not a one-sided limit.", 0]
    displaySolution = option2[0]
    descriptionOfSide = "left"

displayStem = "To estimate the one-sided limit of the function below as $x$ approaches %d from the %s, which of the following sets of numbers should you use?" %(int(a), descriptionOfSide)
displayProblem = "\\frac{\\frac{%d}{x} - 1}{x - %d}" %(a, a)

answerList = [option1, option2, option3, option4, option5]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

generalComment = "\\textbf{General Comments:} To evaluate a one-sided limit, we want to put numbers close to the limit. We can't use the limit value itself if it results in $\\frac{0}{0}$ or $\\frac{\\infty}{\\infty}$"

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
