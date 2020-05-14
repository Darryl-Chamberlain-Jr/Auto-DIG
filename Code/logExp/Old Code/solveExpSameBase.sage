import random
import numpy
import math
from sympy.solvers import solve
from sympy.abc import x
from sympy import Symbol
x = Symbol('x')

#load("../Code/generalPurposeMethods.sage")
print "Starting Module 9 Objective 2"
#load("generalPurposeMethods.sage")


# Ideas for forms of this question:
    # b**(a0*x+a1) = (b**power)**(c0*x+c1)
    # b**(a0*x+a1) = (b**(\frac{1}{power}))**(c0*x+c1)
    # FUTURE: b**(a0*x+a1) = - (b**power)**(c0*x+c1)

# OBJECTIVE 2 - Solving Exponential Equations (with same bases)
intervalRange = 5
precision = 1

problemNumber1 = 42
problemNumber2 = 43

def createCoefficients(type):
    b = random.randint(2, 5)
    a0 = maybeMakeNegative(random.randint(2, 5))
    a1 = maybeMakeNegative(random.randint(2, 5))
    c0 = maybeMakeNegative(random.randint(2, 5))
    c1 = maybeMakeNegative(random.randint(2, 5))
    exponent1 = float(abs(-a1/a0))
    exponent2 = float(abs(-c1/c0))

    while ((c1==a1) or (c0==a0) or exponent1==exponent2):
        b = random.randint(2, 5)
        a0 = maybeMakeNegative(random.randint(2, 5))
        a1 = maybeMakeNegative(random.randint(2, 5))
        c0 = maybeMakeNegative(random.randint(2, 5))
        c1 = maybeMakeNegative(random.randint(2, 5))
        exponent1 = float(abs(-a1/a0))
        exponent2 = float(abs(-c1/c0))

    if (type=="Natural"):
        power = random.randint(2, 4)
    else:
        power = -random.randint(2, 4)

    return [b, a0, a1, power, c0, c1]

def displayEquation(coefficients):
    b, a0, a1, power, c0, c1 = coefficients
    if (power>0):
        bToThePower = b**power
        if (a1<0):
            if (c1<0):
                equation = "%d^{%dx-%d} = %d^{%dx-%d}" %(b, a0, -a1, bToThePower, c0, -c1)
            else:
                equation = "%d^{%dx-%d} = %d^{%dx+%d}" %(b, a0, -a1, bToThePower, c0, c1)
        else:
            if (c1<0):
                equation = "%d^{%dx+%d} = %d^{%dx-%d}" %(b, a0, a1, bToThePower, c0, -c1)
            else:
                equation = "%d^{%dx+%d} = %d^{%dx+%d}" %(b, a0, a1, bToThePower, c0, c1)

    else:
        bToThePower = b**abs(power)
        if (a1<0):
            if (c1<0):
                equation = "%d^{%dx-%d} = \\left(\\frac{1}{%d}\\right)^{%dx-%d}" %(b, a0, -a1, bToThePower, c0, -c1)
            else:
                equation = "%d^{%dx-%d} = \\left(\\frac{1}{%d}\\right)^{%dx+%d}" %(b, a0, -a1, bToThePower, c0, c1)
        else:
            if (c1<0):
                equation = "%d^{%dx+%d} = \\left(\\frac{1}{%d}\\right)^{%dx-%d}" %(b, a0, a1, bToThePower, c0, -c1)
            else:
                equation = "%d^{%dx+%d} = \\left(\\frac{1}{%d}\\right)^{%dx+%d}" %(b, a0, a1, bToThePower, c0, c1)

    return equation

def solveEquation(coefficients):
    #b**(a0*x+a1) = (b**power)**(c0*x+c1)
    b, a0, a1, power, c0, c1 = coefficients
    bf = float(b)
    a0f = float(a0)
    a1f = float(a1)
    powerf = float(power)
    c0f = float(c0)
    c1f = float(c1)
    solution = float((powerf*c1f-a1f)/(a0f-powerf*c0f))
    return solution

def createSolutionAndDistractors(coefficients):
    b, a0, a1, power, c0, c1 = coefficients

    solution = solveEquation(coefficients)
    distractor1 = solveEquation([b, a0, c1, power, c0, a1])
    distractor2 = solveEquation([b, a0, a1, 1, c0, c1])
    distractor3 = solveEquation([b, a0, c1, 1, c0, a1])
    #distractor4 will be that there is no Real solution to the equation.
    solutionList = [solution, distractor1, distractor2, distractor3]

    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

    solutionInterval = intervalOptions[0]
    distractor1Interval = intervalOptions[1]
    distractor2Interval = intervalOptions[2]
    distractor3Interval = intervalOptions[3]
    distractor4Interval = ["\\text{There is no Real solution to the equation.}"]

    solutionInterval.append("* This is the solution!")
    distractor1Interval.append(" Corresponds to getting the negative of the actual solution.")
    distractor2Interval.append(" Correponds to ignoring that the bases are different.")
    distractor3Interval.append(" Corresponds to ignoring that the basses are different and reversing that solution.")
    distractor4Interval.append(" Corresponds to believing there is no solution since the bases are not exactly the same.")

    answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
    random.shuffle(answerList)
    answerList.append(distractor4Interval)

    return [solutionList, answerList]

# One question for each type
typesOfPower = ["Natural", "Integer"]

coefficients1 = createCoefficients(typesOfPower[0])
equation1 = displayEquation(coefficients1)
solutionAndAnswers1 = createSolutionAndDistractors(coefficients1)
solutionList1 = solutionAndAnswers1[0]
answerList1 = solutionAndAnswers1[1]

while (abs(solutionList1[0]-solutionList1[1])<3 or abs(solutionList1[2]-solutionList1[3])<3):
    coefficients1 = createCoefficients(typesOfPower[0])
    equation1 = displayEquation(coefficients1)
    solutionAndAnswers1 = createSolutionAndDistractors(coefficients1)
    solutionList1 = solutionAndAnswers1[0]
    answerList1 = solutionAndAnswers1[1]

displayStem1 = 'Solve the equation for $x$ and choose the interval that contains the solution (if it exists).'
displayProblem1 = equation1
displaySolution1 = "x = %s" %(round(solutionList1[0], 3))
generalComments1 = "\\textbf{General Comments:} This question was written so that the bases could be the same. Try to write one base as the other so we can set the exponents equal and solve."

c0 = "x \\in [%s, %s]" %(answerList1[0][0], answerList1[0][1])
c1 = "x \\in [%s, %s]" %(answerList1[1][0], answerList1[1][1])
c2 = "x \\in [%s, %s]" %(answerList1[2][0], answerList1[2][1])
c3 = "x \\in [%s, %s]" %(answerList1[3][0], answerList1[3][1])
c4 = "%s" %answerList1[4][0]
choices1 = [c0, c1, c2, c3, c4]
choiceComments1 = [answerList1[0][2], answerList1[1][2], answerList1[2][2], answerList1[3][2], answerList1[4][1]]

writeQuestionToFile(moduleNumber, version, problemNumber1, displayStem1, displayProblem1)
writeSolutionAndOptionsToFile(moduleNumber, version, displaySolution1, choices1, choiceComments1)
writeCommentsToFile(moduleNumber, version, generalComments1)

###################
coefficients2 = createCoefficients(typesOfPower[1])
equation2 = displayEquation(coefficients2)
solutionAndAnswers2 = createSolutionAndDistractors(coefficients2)
solutionList2 = solutionAndAnswers2[0]
answerList2 = solutionAndAnswers2[1]

while (abs(solutionList2[0]-solutionList2[1])<1 or abs(solutionList2[2]-solutionList2[3])<1):
    coefficients2 = createCoefficients(typesOfPower[1])
    equation2 = displayEquation(coefficients2)
    solutionAndAnswers2 = createSolutionAndDistractors(coefficients2)
    solutionList2 = solutionAndAnswers2[0]
    answerList2 = solutionAndAnswers2[1]

displayStem2 = 'Solve the equation for $x$ and choose the interval that contains the solution (if it exists).'
displayProblem2 = equation2
displaySolution2 = "x = %s" %(round(solutionList2[0], 3))
generalComments2 = "\\textbf{General Comments:} This question was written so that the bases could be the same. Try to write one base as the other so we can set the exponents equal and solve."

c0 = "x \\in [%s, %s]" %(answerList2[0][0], answerList2[0][1])
c1 = "x \\in [%s, %s]" %(answerList2[1][0], answerList2[1][1])
c2 = "x \\in [%s, %s]" %(answerList2[2][0], answerList2[2][1])
c3 = "x \\in [%s, %s]" %(answerList2[3][0], answerList2[3][1])
c4 = "%s" %answerList2[4][0]
choices2 = [c0, c1, c2, c3, c4]
choiceComments2 = [answerList2[0][2], answerList2[1][2], answerList2[2][2], answerList2[3][2], answerList2[4][1]]

writeQuestionToFile(moduleNumber, version, problemNumber2, displayStem2, displayProblem2)
writeSolutionAndOptionsToFile(moduleNumber, version, displaySolution2, choices2, choiceComments2)
writeCommentsToFile(moduleNumber, version, generalComments2)

print "I have finished Module 9 Objective 2 Type 1, Master"
