import random
from sympy import *
import numpy

# OBJECTIVE 2 - Identify the end behavior and zero behavior of a polynomial equation

# behaviorOfPolynomial = a*(factor1[0]*x+factor1[1])**factor1[2] *(factor1[0]*x-factor1[1])**(factor1[2]+1) *(factor2[0]*x+factor2[1])**factor2[2]*(factor2[0]*x+factor2[1])**(factor2[2]+1)
# This allows us to see if they know which factor is correct.

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
    displaySolution = "polyEndBehaviorB%s" %version
    answerLetter="B"
elif leadingCoefficient > 0 and sumOfExponents % 2 == 0:
    displaySolution = "polyEndBehaviorC%s" %version
    answerLetter="C"
elif leadingCoefficient > 0 and sumOfExponents % 2 == 1:
    displaySolution = "polyEndBehaviorD%s" %version
    answerLetter="D"
else:
    displaySolution = "polyEndBehaviorA%s" %version
    answerLetter="A"

choices = ["polyEndBehaviorA%s" %version, "polyEndBehaviorB%s" %version, "polyEndBehaviorC%s" %version, "polyEndBehaviorD%s" %version]
choiceComments = ["The function is above the $x$-axis, then passes through.", "The function is below the $x$-axis, then touches.", "The function is above the $x$-axis, then touches.", "The function is below the $x$-axis, then passes through."]

displayStem = 'Describe the end behavior of the polynomial below.'
generalComment = "\\textbf{General Comments:} Remember that end behavior is determined by the leading coefficient AND whether the \\textbf{sum} of the multiplicities is positive or negative."

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "Graphs", displaySolution, answerLetter, choices, choiceComments, generalComment)
