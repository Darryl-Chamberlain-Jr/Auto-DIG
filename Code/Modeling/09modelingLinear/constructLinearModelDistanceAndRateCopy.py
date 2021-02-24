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

speedFlat = random.randint(5, 8)
speedUp = speedFlat - random.randint(1, 3)
speedDown = speedFlat + random.randint(2, 4)
distanceUp = float(1/speedUp)
distanceDown = float(1/speedDown)
distanceFlat = float(1/speedFlat)
totalDistance = speedFlat + speedUp + speedDown
distractorDistance = speedFlat * speedUp * speedDown
totalTime = distanceUp + distanceDown + distanceFlat
distractorTime = distanceUp * distanceDown * distanceFlat


# ASK EITHER LINEAR MODEL FOR TOTAL DISTANCE OR TOTAL TIME
distanceOrTime = random.randint(0, 2)
modelShown = random.randint(0, 2)
if distanceOrTime == 0:
    # DISTANCE
    if modelShown == 0:
        displayStem = "For the information provided below, construct a linear model that describes the total distance of the path, $D$, in terms of the time spent on a particular path \\textit{if we know that all parts of the path are equal length}."
        displaySolution = "\\text{The model can be found with the information provided, but isn't options 1-3.}"
        option1 = ["%d t" %totalDistance, "This would be correct if we knew the time spent on each path was equal.", 0]
        option2 = ["%.3f t" %totalTime, "The coefficient here is calculated as if you were trying to model the time on the total path.", 0]
        option3 = ["%d t" %distractorDistance, "The coefficient here is calculated by multiplying the speeds together rather than adding them.", 0]
        option4 = ["\\text{The model can be found with the information provided, but isn't options 1-3.}", "* This is the correct option. Since the paths are equal length and the bike can travel different speeds on each part, the time spent on each path is not equal! The model would be $%dt_u + %dt_d +%dt_f$, where $t_u$ is time traveling up, $t_d$ is time traveling down, and $t_f$ is time traveling on a flat portion." %(speedUp, speedDown, speedFlat), 1]
        option5 = ["\\text{The model cannot be found with the information provided.}", "If you chose this option, please contact the coordinator to discuss why you think we cannot model the situation.", 0]
    else:
        displayStem = "For the information provided below, construct a linear model that describes the total distance of the path, $D$, in terms of the time spent on a particular path \\textit{if we know that the time spent on each path was equal}."
        displaySolution = "%d t" %totalDistance
        option1 = ["%d t" %totalDistance, "* This is the correct option since time spent on each path is equal.", 1]
        option2 = ["%.3f t" %totalTime, "The coefficient here is calculated as if you were trying to model the time on the total path.", 0]
        option3 = ["%d t" %distractorDistance, "The coefficient here is calculated by multiplying the speeds together rather than adding them.", 0]
        option4 = ["\\text{The model can be found with the information provided, but isn't options 1-3.}", "Since the time spent on each path was equal, we can treat all time variables as the same variable, $t$.", 0]
        option5 = ["\\text{The model cannot be found with the information provided.}", "If you chose this option, please contact the coordinator to discuss why you think we cannot model the situation.", 0]
else:
    # TIME
    if modelShown == 0:
        displayStem = "For the information below, construct a linear model that describes the total time $T$ spent on the path in terms of the distance of a particular part of the path \\textit{if we know that the time spent on each path was equal}."
        displaySolution = "\\text{The model can be found with the information provided, but isn't options 1-3.}"
        option1 = ["%.3f D" %totalTime, "This would be correct if we knew all parts of the path are equal length.", 0]
        option2 = ["%.3f D" %totalDistance, "The coefficient here is calculated as if you were trying to model the distance on the total path.", 0]
        option3 = ["%.3f D" %distractorDistance, "The coefficient here is calculated by multiplying the distances together rather than adding.", 0]
        option4 = ["\\text{The model can be found with the information provided, but isn't options 1-3.}", "* This is the correct option. Since the time spent on each path was equal, the distance of each path must be different. The model would be $%.3fD_u + %.3fD_d + %.3fD_f$, where $D_u$ is distance traveling up the hill, $D_d$ is distance traveling down, and $D_f$ is distance traveling on a flat part." %(distanceUp, distanceDown, distanceFlat), 1]
        option5 = ["\\text{The model cannot be found with the information provided.}", "If you chose this option, please contact the coordinator to discuss why you think we cannot model the situation.", 0]
    else:
        displayStem = "For the information below, construct a linear model that describes the total time $T$ spent on the path in terms of the distance of a particular part of the path \\textit{if we know that all parts of the path are equal length}."
        displaySolution = "%.3f D" %totalTime
        option1 = ["%.3f D" %totalTime, "* This is the correct option.", 1]
        option2 = ["%.3f D" %totalDistance, "The coefficient here is calculated as if you were trying to model the distance on the total path.", 0]
        option3 = ["%.3f D" %distractorDistance, "The coefficient here is calculated by multiplying the distances together rather than adding.", 0]
        option4 = ["\\text{The model can be found with the information provided, but isn't options 1-3.}", "Since we know all parts of the path are equal length, we can treat all distance variables as the same variable, $D$.", 0]
        option5 = ["\\text{The model cannot be found with the information provided.}", "If you chose this option, please contact the coordinator to discuss why you think we cannot model the situation.", 0]

displayProblem = "A bicyclist is training for a race on a hilly path. Their bike keeps track of their speed at any time, but not the distance traveled. Their speed traveling up a hill is %d mph, %d mph when traveling down a hill, and %d mph when traveling along a flat portion." %(speedUp, speedDown, speedFlat)

answerList = [option1, option2, option3]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], option4[0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], option4[1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], option4[2], option5[2]]

generalComment = "Be sure you pay attention to the variable we are writing the model in terms of. To create the model with a single variable, we have to know that variable is the same throughout each path!"

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1


# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="String"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
