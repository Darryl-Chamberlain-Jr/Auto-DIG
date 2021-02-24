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

typeOfValues = random.randint(0, 2)
if typeOfValues == 0:
    x_0 = random.randint(0, 9)
    y_0 = round(random.uniform(0, 20), 3)
elif typeOfValues == 1:
    x_0 = "\\infty"
    y_0 = round(random.uniform(0, 20), 3)
else:
    x_0 = random.randint(0, 9)
    y_0 = "\\infty"

displayStem = "Based on the information below, which of the following statements is always true?"
xFirst = random.randint(0, 1)
if xFirst == 1:
    displayProblem = "As $x$ approaches $%s$, $f(x)$ approaches $%s$." %(x_0, y_0)
else:
    displayProblem = "$f(x)$ approaches $%s$ as $x$ approaches $%s$." %(y_0, x_0)

noneOfTheAboveOrNot = random.randint(0, 1)

if typeOfValues == 0:
    if noneOfTheAboveOrNot == 0:
        # No infinities - Correct answer
        option1 = ["f(x) \\text{ is close to or exactly } %s \\text{ when } x \\text{ is close to } %s" %(y_0, x_0), "", 1]
        option2 = ["f(x) \\text{ is close to or exactly } %s \\text{ when } x \\text{ is close to } %s" %(x_0, y_0), "", 0]
        option3 = ["f(x) = %s \\text{ when } x \\text{ is close to } %s" %(y_0, x_0), "", 0]
        option4 = ["f(x) = %s \\text{ when } x \\text{ is close to } %s" %(x_0, y_0), "", 0]
        option5 = ["\\text{None of the above are always true.}", "", 0]
    else:
        # No infinities - None of the above
        option1 = ["f(%d) \\text{ is close to or exactly } %d" %(x_0, y_0), "", 0]
        option2 = ["f(%d) = %d" %(x_0, y_0), "", 0]
        option3 = ["f(%d) = %d" %(y_0, x_0), "", 0]
        option4 = ["f(%d) \\text{ is close to or exactly } %d" %(y_0, x_0), "", 0]
        option5 = ["\\text{None of the above are always true.}", "", 1]
elif typeOfValues == 1:
    if noneOfTheAboveOrNot == 0:
        # x infinity - Correct answer
        option1 = ["f(x) \\text{ is close to or exactly } %s \\text{ when } x \\text{ is large enough}." %x_0, "", 0]
        option2 = ["f(x) \\text{ is close to or exactly } %s \\text{ when } x \\text{ is large enough}." %y_0, "", 1]
        option3 = ["f(x) \\text{ is undefined when } x \\text{ is large enough}.", "", 0]
        option4 = ["x \\text{ is undefined when } f(x) \\text{ is large enough}.", "", 0]
        option5 = ["\\text{None of the above are always true.}", "", 0]
    else:
        # x infinity - None of the above
        option1 = ["f(%d) \\text{ is close to or exactly } %d" %(x_0, y_0), "", 0]
        option2 = ["f(%d) \\text{ is close to or exactly } %d" %(y_0, x_0), "", 0]
        option3 = ["f(%d) \\text{ is undefined }" %(x_0), "", 0]
        option4 = ["f(%d) \\text{ is undefined }" %(y_0), "", 0]
        option5 = ["\\text{None of the above are always true.}", "", 1]
else:
    if noneOfTheAboveOrNot == 0:
        # y infinity - Correct answer
        option1 = ["f(x) \\text{ is close to or exactly } %s \\text{ when } x \\text{ is large enough}." %x_0, "", 0]
        option2 = ["f(x) \\text{ is close to or exactly } %s \\text{ when } x \\text{ is large enough}." %y_0, "", 0]
        option3 = ["f(x) \\text{ is undefined when } x \\text{ is close to or exactly } %s." %x_0, "", 1]
        option4 = ["x \\text{ is undefined when } f(x) \\text{ is close to or exactly } %s." %y_0, "", 0]
        option5 = ["\\text{None of the above are always true.}", "", 0]
    else:
        # y infinity - None of the above
        option1 = ["f(%d) \\text{ is close to or exactly } %d" %(x_0, y_0), "", 0]
        option2 = ["f(%d) \\text{ is close to or exactly } %d" %(y_0, x_0), "", 0]
        option3 = ["f(%d) \\text{ is undefined }" %(x_0), "", 0]
        option4 = ["f(%d) \\text{ is undefined }" %(y_0), "", 0]
        option5 = ["\\text{None of the above are always true.}", "", 1]

generalComment = "The limit tells you what happens as the $x$-values approach $%s$. It says \\textbf{absolutely nothing} about what is happening exactly at $f(%s)$!" %(x_0, x_0)

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        displaySolution = choices[answerIndex]
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
