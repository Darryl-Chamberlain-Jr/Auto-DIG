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

a = random.randint(2, 9)
f = random.randint(2, 9)
while a == f:
    a = random.randint(2, 9)
    f = random.randint(2, 9)
g = random.randint(2, 9)
d = f*g
perfectSquares = [16, 25, 36, 49, 64, 81]
c = int(math.sqrt(random.choice(perfectSquares)))
b = a*g - c**2
while b < 1:
    a = random.randint(2, 9)
    f = random.randint(2, 9)
    while a == f:
        a = random.randint(2, 9)
        f = random.randint(2, 9)
    g = random.randint(2, 9)
    d = f*g
    perfectSquares = [16, 25, 36, 49, 64, 81]
    c = int(sqrt(random.choice(perfectSquares)))
    b = a*g - c**2
limit = float(a)/float(2*f*c)
xApproaches = int(float(d) / float(f))
# Distractors
hwLimit = 1.0/float(2*c)
naiveLimit = float(math.sqrt(a))/float(f)
badLHospital = limit / float(a)

displayStem = "Evaluate the limit below, if possible."
displayProblem = "\\lim_{x \\rightarrow %d} \\frac{\\sqrt{%dx - %d} - %d}{%dx - %d}" %(xApproaches, a, b, c, f, d)
generalComment = "\\textbf{General comments:} It is difficult to imagine the graph of this function, so you need to test values close to $x = %d$." %xApproaches

showCorrectValue = random.randint(0, 1)

if showCorrectValue == 0:
    option1 = ["%.3f" %hwLimit, "You likely memorized how to solve the similar homework problem and used the same formula here.", 0]
    option2 = ["%.3f" %naiveLimit, "You likely tried to use a shortcut to find the limit of a function that only works for when the numerator/denominator are polynomials.", 0]
    option3 = ["%.3f" %badLHospital, "You likely learned L'Hospital's Rule in a previous course, but misapplied it here.", 0]
    option4 = ["\\infty", "You likely believed that since the denominator is equal to 0, the limit is infinity.", 0]
    option5 = ["\\text{None of the above}", "* This is the correct option as the limit is %.3f." %limit, 1]
else:
    naiveOrBadLHospital = random.randint(0, 1)
    if naiveOrBadLHospital == 0:
        option1 = ["%.3f" %limit, "* This is the correct option.", 1]
        option2 = ["%.3f" %hwLimit, "You likely memorized how to solve the similar homework problem and used the same formula here.", 0]
        option3 = ["%.3f" %naiveLimit, "You likely tried to use a shortcut to find the limit of a function that only works for when the numerator/denominator are polynomials.", 0]
        option4 = ["\\infty", "You likely believed that since the denominator is equal to 0, the limit is infinity.", 0]
        option5 = ["\\text{None of the above}", "If you got a limit that does not match any of the above, please contact the coordinator.", 0]
    else:
        option1 = ["%.3f" %limit, "", 1]
        option2 = ["%.3f" %hwLimit, "You likely memorized how to solve the similar homework problem and used the same formula here.", 0]
        option3 = ["%.3f" %badLHospital, "You likely learned L'Hospital's Rule in a previous course, but misapplied it here.", 0]
        option4 = ["\\infty", "You likely believed that since the denominator is equal to 0, the limit is infinity.", 0]
        option5 = ["\\text{None of the above}", "If you got a limit that does not match any of the above, please contact the coordinator.", 0]
answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

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
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
