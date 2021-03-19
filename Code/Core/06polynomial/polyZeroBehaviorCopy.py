import sys
import random

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

def generateFactor():
    a = 1
    b = maybeMakeNegative(random.randint(2, 9))
    c = random.randint(2, 9)
    return [a, b, c]

def listZeros(factor1, factor2):
    z1 = factor1[1]
    z2 = - factor1[1]
    z3 =  factor2[1]
    z4 = - factor2[1]
    return [z1, z2, z3, z4]

def displayFactor(a):
    if a == 0:
        factor = "x"
    elif a < 0:
        factor = "x + %d" %-a
    else:
        factor = "x - %d" %a
    return factor

def determineZeroBehavior(a, zeros, exponents, zeroDisplayed):
    a0, b0, c0, d0 = zeros
    ae, be, ce, de = exponents
    floatDisplayed = float(zeroDisplayed)
    checkSmaller = float(floatDisplayed - 0.5)
    checkLarger = float(floatDisplayed + 0.5)
    smallerValue = float(a * (checkSmaller - a0)**ae * (checkSmaller - b0)**be * (checkSmaller - c0)**ce * (checkSmaller -d0)**de)
    largerValue = float(a * (checkLarger - a0)**ae * (checkLarger - b0)**be * (checkLarger - c0)**ce * (checkLarger -d0)**de)
    if smallerValue < 0 and largerValue < 0:
        behavior = "negativeEven"
    elif smallerValue < 0 and largerValue > 0:
        behavior = "positiveOdd"
    elif smallerValue > 0 and largerValue > 0:
        behavior = "positiveEven"
    else:
        behavior = "negativeOdd"
    return behavior

leadingCoefficient = maybeMakeNegative(random.randint(2, 9))
factor1 = generateFactor()
factor2 = generateFactor()

while (abs(factor1[1]) == abs(factor2[1])):
    factor1 = generateFactor()
    factor2 = generateFactor()

# Makes sure the conjugate of the zero on display has opposite multiplicity of the zero on display.
e0 = factor1[2]
e1 = factor1[2] + 2*random.randint(1, 3)-1
e2 = factor2[2]
e3 = factor2[2] + 2*random.randint(1, 3)-1

chooseZero = random.choice([0, 1, 2, 3])
if chooseZero == 0:
    zeroOnDisplay = factor1[1]
    e0 = factor1[2]
    e1 = factor1[2] + 2*random.randint(1, 3)-1
    e2 = factor2[2]
    e3 = factor2[2] + random.randint(1, 4)
    expoenentOnDisplay = e1
elif chooseZero == 1:
    zeroOnDisplay = -factor1[1]
    e0 = factor1[2]
    e1 = factor1[2] + 2*random.randint(1, 3)-1
    e2 = factor2[2]
    e3 = factor2[2] + random.randint(1, 4)
    expoenentOnDisplay = e0
elif chooseZero == 2:
    zeroOnDisplay = factor2[1]
    e0 = factor1[2] + random.randint(1, 4)
    e1 = factor1[2]
    e2 = factor2[2] + 2*random.randint(1, 3)-1
    e3 = factor2[2]
    expoenentOnDisplay = e3
else:
    zeroOnDisplay = -factor2[1]
    e0 = factor1[2] + random.randint(1, 4)
    e1 = factor1[2]
    e2 = factor2[2] + 2*random.randint(1, 3)-1
    e3 = factor2[2]
    expoenentOnDisplay = e2

displayProblem = "f(x) = %s(%s)^{%d}(%s)^{%d}(%s)^{%d}(%s)^{%d}" %(leadingCoefficient, displayFactor(-factor1[1]), e0, displayFactor(factor1[1]), e1, displayFactor(-factor2[1]), e2, displayFactor(factor2[1]), e3)

zeros = [-factor1[1], factor1[1], -factor2[1], factor2[1]]
exponents = [e0, e1, e2, e3]
behavior = determineZeroBehavior(leadingCoefficient, zeros, exponents, zeroOnDisplay)
if behavior == "positiveEven":
    displaySolution = f"{thisQuestion}C{version}"
    answerLetter="C"
elif behavior == "negativeEven":
    displaySolution = f"{thisQuestion}B{version}"
    answerLetter="B"
elif behavior == "positiveOdd":
    displaySolution = f"{thisQuestion}D{version}"
    answerLetter="D"
else:
    displaySolution = f"{thisQuestion}A{version}"
    answerLetter="A"

choices = [f"{thisQuestion}A{version}", f"{thisQuestion}B{version}", f"{thisQuestion}C{version}", f"{thisQuestion}D{version}"]

displayStem = 'Describe the zero behavior of the zero $x = %s$ of the polynomial below.' %zeroOnDisplay
generalComment = "You will need to sketch the entire graph, then zoom in on the zero the question asks about."
choiceComments = ["", "", "", ""]

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Graph"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
