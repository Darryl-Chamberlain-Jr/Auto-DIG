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

def generateFactor():
    a = 1
    b = maybeMakeNegative(random.randint(2, 9))
    c = random.randint(2, 5)
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

leadingCoefficient = Integer(maybeMakeNegative(random.randint(2, 9)))
factor1 = generateFactor()
factor2 = generateFactor()

while (abs(factor1[1]) == abs(factor2[1])):
    factor1 = generateFactor()
    factor2 = generateFactor()

# Makes sure the conjugate of the zero on display has opposite multiplicity of the zero on display.

e0 = factor1[2]
e1 = factor1[2] + 2*random.randint(1, 3)-1
e2 = factor2[2]
e3 = factor2[2] + random.randint(0, 2)

displayPolynomial = leadingCoefficient * (x+factor1[1])**e0 *(x-factor1[1])**e1 *(x+factor2[1])**e2 *(x-factor2[1])**e3
displayProblem = "f(x) = %s(%s)^{%d}(%s)^{%d}(%s)^{%d}(%s)^{%d}" %(leadingCoefficient, displayFactor(-factor1[1]), e0, displayFactor(factor1[1]), e1, displayFactor(-factor2[1]), e2, displayFactor(factor2[1]), e3)

sumOfExponents = e0 + e1 + e2 + e3

if leadingCoefficient < 0 and sumOfExponents % 2 == 0:
    displaySolution = f"{thisQuestion}B{version}"
    answerLetter="B"
elif leadingCoefficient > 0 and sumOfExponents % 2 == 0:
    displaySolution = f"{thisQuestion}C{version}"
    answerLetter="C"
elif leadingCoefficient > 0 and sumOfExponents % 2 == 1:
    displaySolution = f"{thisQuestion}D{version}"
    answerLetter="D"
else:
    displaySolution = f"{thisQuestion}A{version}"
    answerLetter="A"

choices = [f"{thisQuestion}A{version}", f"{thisQuestion}B{version}", f"{thisQuestion}C{version}", f"{thisQuestion}D{version}"]
choiceComments = ["The function is above the $x$-axis, then passes through.", "The function is below the $x$-axis, then touches.", "The function is above the $x$-axis, then touches.", "The function is below the $x$-axis, then passes through."]

displayStem = 'Describe the end behavior of the polynomial below.'
generalComment = "Remember that end behavior is determined by the leading coefficient AND whether the \\textbf{sum} of the multiplicities is positive or negative."

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Graph"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
