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

def chooseDomainOrRange():
    listChoices = ["Domain", "Range"]
    random.shuffle(listChoices)
    return listChoices[0]

def chooseSignOfLeadingCoefficient():
    sign = (-1)**random.randint(0, 1)
    return sign

def generateShifting():
    h = 0
    k = 0
    while (h==0 or k==0 or h==k):
        h = random.randint(-9, 9)
        k = random.randint(-9, 9)
    return [h, k]

def intervalWithInfinity(solutionInterval, inclusion):
    a, b = solutionInterval
    if (a == 0) and (inclusion == "yes"):
        display = "(-\\infty, a]"
        key = "(-\\infty, %d]" %b
    elif (b == 0) and (inclusion == "yes"):
        display = "[a, \\infty)"
        key = "[%d, \\infty)" %a
    elif (a == 0) and (inclusion == "no"):
        display = "(-\\infty, a)"
        key = "(-\\infty, %d)" %b
    elif (b == 0) and (inclusion == "no"):
        display = "(a, \\infty)"
        key = "(%d, \\infty)" %a
    else:
       display = "Error"
       key = "Error"
    return [display, key]

def distractorNegateDomain(intervalPresentation):
    a, b = intervalPresentation
    return [-a, -b]

def extractValue(solutionInterval):
    a, b = solutionInterval
    if(a == 0):
        return b
    else:
        return a

# Type 1 - Logarithmic

# a * log_2 (x-h) + k
    # a Positive
        # Domain: (h, infty)
        # Range: (-infty, infty)
    # a Negative
        # Domain: (h, infty)
        # Range: (-infty, infty)
intervalRange = 5
domainOrRange = chooseDomainOrRange()
#domainOrRange = "Domain"
a = chooseSignOfLeadingCoefficient()
shift = generateShifting()
h = shift[0]
k = shift[1]

if (domainOrRange == "Domain"):
    intervalPresentation = [h, 0]
    solution = h
    distractor1 = k
    distractor2 = -h
    distractor3 = -k

    displaySolution = "(%d, \\infty)" %h
    solutionList = [solution, distractor1, distractor2, distractor3]
    precision = 1
    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

    solutionInterval = [intervalWithInfinity([h, 0], "no")[0], intervalOptions[0], "* $%s$, which is the correct option." %intervalWithInfinity([h, 0], "no")[1], 1]
    distractor1Interval = [intervalWithInfinity([k, 0], "yes")[0], intervalOptions[1], "$%s$, which corresponds to using the vertical shift when shifting the Domain AND including the endpoint." %intervalWithInfinity([k, 0], "yes")[1], 0]
    distractor2Interval = [intervalWithInfinity([0, h], "no")[0], intervalOptions[2], "$%s$, which corresponds to flipping the Domain. Remember: the general for is $a*\\log(x-h)+k$, \\textbf{where $a$ does not affect the domain}." %intervalWithInfinity([0, -h], "no")[1], 0]
    distractor3Interval = [intervalWithInfinity([0, -k], "yes")[0], intervalOptions[3], "$%s$, which corresponds to using the negative vertical shift AND including the endpoint AND flipping the domain." %intervalWithInfinity([0, -k], "yes")[1], 0]
    distractor4Interval = ["(-\\infty, \\infty)", ["", ""], "This corresponds to thinking of the range of the log function (or the domain of the exponential function).", 0]

    answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
    random.shuffle(answerList)
    answerList.append(distractor4Interval)
    answerIndex = 0
    letters = ["A", "B", "C", "D", "E"]
    for checkLetter in letters:
        if answerList[answerIndex][3] == 1:
            answerLetter = letters[answerIndex]
            break
        answerIndex = answerIndex+1
else:
    displaySolution = "(\\infty, \\infty)"
    distractor1 = h
    distractor2 = -k
    distractor3 = k
    distractor4 = -h

    solutionList = [distractor1, distractor2, distractor3, distractor4]

    precision = 1
    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
    solutionInterval = ["(-\\infty, \\infty)", ["", ""], "*This is the correct option.", 1]
    distractor1Interval = [intervalWithInfinity([k, 0], "yes")[0], intervalOptions[0], "$%s$, which corresponds to using the flipped Domain AND including the endpoint." %intervalWithInfinity([k, 0], "yes")[1], 0]
    distractor2Interval = [intervalWithInfinity([0, -k], "no")[0], intervalOptions[1], "$%s$, which corresponds to using the using the negative of vertical shift on $(0, \\infty)$." %intervalWithInfinity([0, -k], "no")[1], 0]
    distractor3Interval = [intervalWithInfinity([0, k], "no")[0], intervalOptions[2], "$%s$, which corresponds to using the vertical shift while the Range is $(-\\infty, \\infty)$." %intervalWithInfinity([0, k], "no")[1], 0]
    distractor4Interval = [intervalWithInfinity([-h, 0], "yes")[0], intervalOptions[3], "$%s$, which corresponds to using the negative of the horizontal shift AND including the endpoint." %intervalWithInfinity([-h, 0], "yes")[1], 0]

    answerList = [distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
    random.shuffle(answerList)
    answerList.append(solutionInterval)
    answerLetter = "E"

displayStem = 'Which of the following intervals describes the %s of the function below?' %domainOrRange
# Makes the function display correctly.
if (a<0):
    if (h<0):
        if(k<0):
            displayProblem = 'f(x) = -\\log_2{(x+%d)}-%d' %(-h, -k)
        else:
            displayProblem = 'f(x) = -\\log_2{(x+%d)}+%d' %(-h, k)
    else:
        if(k<0):
            displayProblem = 'f(x) = -\\log_2{(x-%d)}-%d' %(h, -k)
        else:
            displayProblem = 'f(x) = -\\log_2{(x-%d)}+%d' %(h, k)
else:
    if (h<0):
        if(k<0):
            displayProblem = 'f(x) = \\log_2{(x+%d)}-%d' %(-h, -k)
        else:
            displayProblem = 'f(x) = \\log_2{(x+%d)}+%d' %(-h, k)
    else:
        if(k<0):
            displayProblem = 'f(x) = \\log_2{(x-%d)}-%d' %(h, -k)
        else:
            displayProblem = 'f(x) = \\log_2{(x-%d)}+%d' %(h, k)

generalComment = "\\textbf{General Comments}: The domain of a basic logarithmic function is $(0, \\infty)$ and the Range is $(-\\infty, \\infty)$. We can use shifts when finding the Domain, but the Range will always be all Real numbers."

c0 = "%s, a \\in [%s, %s]" %(answerList[0][0], answerList[0][1][0], answerList[0][1][1])
c1 = "%s, a \\in [%s, %s]" %(answerList[1][0], answerList[1][1][0], answerList[1][1][1])
c2 = "%s, a \\in [%s, %s]" %(answerList[2][0], answerList[2][1][0], answerList[2][1][1])
c3 = "%s, a \\in [%s, %s]" %(answerList[3][0], answerList[3][1][0], answerList[3][1][1])
c4 = "%s" %answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
