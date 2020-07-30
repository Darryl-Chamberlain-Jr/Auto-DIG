import random
from sympy import *
import numpy

# OBJECTIVE 2 - Identify the end behavior and zero behavior of a polynomial equation

# behaviorOfPolynomial = a*(factor1[0]*x+factor1[1])**factor1[2] *(factor1[0]*x-factor1[1])**(factor1[2]+1) *(factor2[0]*x+factor2[1])**factor2[2]*(factor2[0]*x+factor2[1])**(factor2[2]+1)
# This allows us to see if they know which factor is correct.

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

firstTerm = (x+factor1[1])**e0
secondTerm = (x-factor1[1])**e1
thirdTerm = (x+factor2[1])**e2
fourthTerm = (x-factor2[1])**e3

behaviorOfPolynomial = leadingCoefficient*( firstTerm * secondTerm * thirdTerm * fourthTerm )

displayPolynomial = leadingCoefficient * (x+factor1[1])**e0 *(x-factor1[1])**e1 *(x+factor2[1])**e2 *(x-factor2[1])**e3
displayProblem = "f(x) = %s(%s)^{%d}(%s)^{%d}(%s)^{%d}(%s)^{%d}" %(leadingCoefficient, displayFactor(-factor1[1]), e0, displayFactor(factor1[1]), e1, displayFactor(-factor2[1]), e2, displayFactor(factor2[1]), e3)

zeros = [-factor1[1], factor1[1], -factor2[1], factor2[1]]
exponents = [e0, e1, e2, e3]
behavior = determineZeroBehavior(leadingCoefficient, zeros, exponents, zeroOnDisplay)
print("\n", zeros, "\n")
print(exponents, "\n")
print(behavior, "\n")
if behavior == "positiveEven":
    displaySolution = "zeroBehaviorPositiveEven%s" %version
    answerLetter="C"
elif behavior == "negativeEven":
    displaySolution = "zeroBehaviorNegativeEven%s" %version
    answerLetter="B"
elif behavior == "positiveOdd":
    displaySolution = "zeroBehaviorPositiveOdd%s" %version
    answerLetter="D"
else:
    displaySolution = "zeroBehaviorNegativeOdd%s" %version
    answerLetter="A"

choices = ["zeroBehaviorNegativeOdd%s" %version, "zeroBehaviorNegativeEven%s" %version, "zeroBehaviorPositiveEven%s" %version, "zeroBehaviorPositiveOdd%s" %version]

displayStem = 'Describe the zero behavior of the zero $x = %s$ of the polynomial below.' %zeroOnDisplay
generalComment = "\\textbf{General Comments:} You will need to sketch the entire graph, then zoom in on the zero the question asks about."
choiceComments = ["", "", "", ""]

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "Graphs", displaySolution, answerLetter, choices, choiceComments, generalComment)
