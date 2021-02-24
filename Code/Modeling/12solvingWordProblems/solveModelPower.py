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

percentMore = random.randint(20, 50)
increaseEach = int(round((((1+0.01*float(percentMore))**(1/3.0)) - 1)*100, 0))
increaseSQRT = int(round((((1+0.01*float(percentMore))**(1/2.0)) - 1)*100, 0))
increaseHalf = int(round(float(percentMore)/2.0, 0))
incorrectSolve = int(round(float(percentMore**(1/3.0)), 0))
test_list = [increaseEach, increaseSQRT, increaseHalf, incorrectSolve]
while len(set(test_list)) != len(test_list):
    percentMore = random.randint(20, 50)
    increaseEach = int(round((((1+0.01*float(percentMore))**(1/3.0)) - 1)*100, 0))
    increaseSQRT = int(round((((1+0.01*float(percentMore))**(1/2.0)) - 1)*100, 0))
    increaseHalf = int(round(float(percentMore)/2.0, 0))
    incorrectSolve = int(round(float(percentMore)/3.0, 0))
    test_list = [increaseEach, increaseSQRT, increaseHalf, incorrectSolve]

displayStem = "For the scenario below, use the model for the volume of a cylinder as $V = \\pi r^2 h$."

displayProblem = "Pringles wants to add %d \\text{percent} more chips to their cylinder cans and minimize the design change of their cans. They've decided that the best way to minimize the design change is to increase the radius and height by the same percentage. What should this increase be?" %percentMore

option1 = ["\\text{About } %d \\text{ percent}" %increaseEach, "* This is the correct option.", 1]
option2 = ["\\text{About } %d \\text{ percent}" %increaseSQRT, "This corresponds to solving correctly but treating both radius and height as equal contributors to the volume.", 0]
option3 = ["\\text{About } %d \\text{ percent}" %increaseHalf, "This corresponds to treating both radius and height as equal contributors and not solving correctly.", 0]
option4 = ["\\text{About } %d \\text{ percent}" %incorrectSolve, "This corresponds to not solving for the increase properly.", 0]
option5 = ["\\text{None of the above}", "If you chose this, please contact the coordinator to discus how you solved the problem.", 0]

displaySolution = option1[0]
answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "Remember that when plugging the increases of values in, you need to treat it as that percentage above 100. For example, a 5 percent increase means 105 percent."

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
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
