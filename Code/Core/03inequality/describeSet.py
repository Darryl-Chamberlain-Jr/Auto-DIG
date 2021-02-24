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
    OS_type=sys.argv[7]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

def generateDistanceAndFromNumber(minimum, maximum):
    distance = random.randint(minimum, maximum)
    fromNumber = random.randint(-maximum, maximum)
    while distance == fromNumber or fromNumber == 0:
        distance = random.randint(minimum, maximum)
        fromNumber = random.randint(-maximum, maximum)
    endValues = fromNumber - distance, fromNumber + distance
    return [distance, fromNumber, endValues]

def generateQuestion(values, questionType, distance, fromNumber):
    if questionType == 0:
        option1 = ["[%d, %d]" %(values[0], values[1]), 1, "This describes the values no more than %d from %d" %(distance, fromNumber)]
        option2 = ["(%d, %d)" %(values[0], values[1]), 0, "This describes the values less than %d from %d" %(distance, fromNumber)]
        option3 = ["(-\\infty, %d) \\cup (%d, \\infty)" %(values[0], values[1]), 0, "This describes the values more than %d from %d" %(distance, fromNumber)]
        option4 = ["(-\\infty, %d] \\cup [%d, \\infty)" %(values[0], values[1]), 0, "This describes the values no less than %d from %d" %(distance, fromNumber)]
        option5 = ["\\text{None of the above}", 0, "You likely thought the values in the interval were not correct."]
        displayProblem = "\\text{ No more than } %d \\text{ units from the number } %d." %(distance, fromNumber)
    elif questionType == 1:
        option1 = ["[%d, %d]" %(values[0], values[1]), 0, "This describes the values no more than %d from %d" %(distance, fromNumber)]
        option2 = ["(%d, %d)" %(values[0], values[1]), 1, "This describes the values less than %d from %d" %(distance, fromNumber)]
        option3 = ["(-\\infty, %d) \\cup (%d, \\infty)" %(values[0], values[1]), 0, "This describes the values more than %d from %d" %(distance, fromNumber)]
        option4 = ["(-\\infty, %d] \\cup [%d, \\infty)" %(values[0], values[1]), 0, "This describes the values no less than %d from %d" %(distance, fromNumber)]
        option5 = ["\\text{None of the above}", 0, "You likely thought the values in the interval were not correct."]
        displayProblem = "\\text{ Less than } %d \\text{ units from the number } %d." %(distance, fromNumber)
    elif questionType == 2:
        option1 = ["[%d, %d]" %(values[0], values[1]), 0, "This describes the values no more than %d from %d" %(distance, fromNumber)]
        option2 = ["(%d, %d)" %(values[0], values[1]), 0, "This describes the values less than %d from %d" %(distance, fromNumber)]
        option3 = ["(-\\infty, %d) \\cup (%d, \\infty)" %(values[0], values[1]), 1, "This describes the values more than %d from %d" %(distance, fromNumber)]
        option4 = ["(-\\infty, %d] \\cup [%d, \\infty)" %(values[0], values[1]), 0, "This describes the values no less than %d from %d" %(distance, fromNumber)]
        option5 = ["\\text{None of the above}", 0, "You likely thought the values in the interval were not correct."]
        displayProblem = "\\text{ More than } %d \\text{ units from the number } %d." %(distance, fromNumber)
    elif questionType == 3:
        option1 = ["[%d, %d]" %(values[0], values[1]), 0, "This describes the values no more than %d from %d" %(distance, fromNumber)]
        option2 = ["(%d, %d)" %(values[0], values[1]), 0, "This describes the values less than %d from %d" %(distance, fromNumber)]
        option3 = ["(-\\infty, %d) \\cup (%d, \\infty)" %(values[0], values[1]), 0, "This describes the values more than %d from %d" %(distance, fromNumber)]
        option4 = ["(-\\infty, %d] \\cup [%d, \\infty)" %(values[0], values[1]), 1, "This describes the values no less than %d from %d" %(distance, fromNumber)]
        option5 = ["\\text{None of the above}", 0, "You likely thought the values in the interval were not correct."]
        displayProblem = "\\text{ No less than } %d \\text{ units from the number } %d." %(distance, fromNumber)
    else:
        option1 = ["[%d, %d]" %(-values[0], values[1]), 0, "This describes the values no more than %d from %d" %(fromNumber, distance)]
        option2 = ["(%d, %d)" %(-values[0], values[1]), 0, "This describes the values less than %d from %d" %(fromNumber, distance)]
        option3 = ["(-\\infty, %d) \\cup (%d, \\infty)" %(-values[0], values[1]), 0, "This describes the values more than %d from %d" %(fromNumber, distance)]
        option4 = ["(-\\infty, %d] \\cup [%d, \\infty)" %(-values[0], values[1]), 0, "This describes the values no less than %d from %d" %(fromNumber, distance)]
        option5 = ["\\text{None of the above}", 1, "Options A-D described the values [more/less than] %d units from %d, which is the reverse of what the question asked." %(fromNumber, distance)]
        randomDisplay = random.randint(0, 3)
        if randomDisplay == 0:
            displayProblem = "\\text{ More than } %d \\text{ units from the number } %d." %(distance, fromNumber)
        elif randomDisplay == 1:
            displayProblem = "\\text{ No more than } %d \\text{ units from the number } %d." %(distance, fromNumber)
        elif randomDisplay == 2:
            displayProblem = "\\text{ Less than } %d \\text{ units from the number } %d." %(distance, fromNumber)
        else:
            displayProblem = "\\text{ No less than } %d \\text{ units from the number } %d." %(distance, fromNumber)
    answerListTemp = [option1, option2, option3, option4]
    random.shuffle(answerListTemp)
    answerList = [answerListTemp[0], answerListTemp[1], answerListTemp[2], answerListTemp[3], option5]
    return [answerList, displayProblem]
#################
distance, fromNumber, endValues = generateDistanceAndFromNumber(2, 10)
questionType = random.randint(0, 4)
while (questionType == 4 and fromNumber < 0):
    distance, fromNumber, endValues = generateDistanceAndFromNumber(2, 10)
answerList, displayProblem = generateQuestion(endValues, questionType, distance, fromNumber)

displayStem = 'Using an interval or intervals, describe all the $x$-values within or including a distance of the given values.'
generalComment = "When thinking about this language, it helps to draw a number line and try points."

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][1] == 1:
        answerLetter = letters[answerIndex]
        displaySolution = answerList[answerIndex][0]
        break
    answerIndex = answerIndex+1

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
