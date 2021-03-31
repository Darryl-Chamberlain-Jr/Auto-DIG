import sys
import random
from math import gcd

DIR=sys.argv[1]
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
    OS_type=sys.argv[7]
    response_type=sys.argv[8]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

# Ideas for forms of this question [gcd(b0, b1)=1]:
    # b0**(a0*x+a1) = b1**(c0*x+c1)
    # b0**(a0*x+a1) = (b1**(\frac{1}{power}))**(c0*x+c1)
    # FUTURE: b0**(a0*x+a1) = - (b1**power)**(c0*x+c1)

intervalRange = 3
precision = 1

def createCoefficients(type):
    b0 = random.randint(2, 5)
    b1 = random.randint(3, 7)
    a0 = float(maybeMakeNegative(random.randint(2, 5)))
    a1 = float(maybeMakeNegative(random.randint(2, 5)))
    c0 = float(maybeMakeNegative(random.randint(2, 5)))
    c1 = float(maybeMakeNegative(random.randint(2, 5)))
    exponent1 = float(-a1/a0)
    exponent2 = float(-c1/c0)
    while ((c1==a1) or (c0==a0) or gcd(b0, b1)>1 or exponent1 == exponent2):
        b0 = random.randint(2, 5)
        b1 = random.randint(3, 7)
        a0 = float(maybeMakeNegative(random.randint(2, 5)))
        a1 = float(maybeMakeNegative(random.randint(2, 5)))
        c0 = float(maybeMakeNegative(random.randint(2, 5)))
        c1 = float(maybeMakeNegative(random.randint(2, 5)))
        exponent1 = float(-a1/a0)
        exponent2 = float(-c1/c0)
    if (type=="Natural"):
        power = random.randint(2, 3)
    else:
        power = -random.randint(2, 3)

    return [b0, a0, a1, b1, power, c0, c1]

def displayEquation(coefficients):
    b0, a0, a1, b1, power, c0, c1 = coefficients
    if (power>0):
        b1ToThePower = b1**power
        if (a1<0):
            if (c1<0):
                equation = "%d^{%dx-%d} = %d^{%dx-%d}" %(b0, a0, -a1, b1ToThePower, c0, -c1)
            else:
                equation = "%d^{%dx-%d} = %d^{%dx+%d}" %(b0, a0, -a1, b1ToThePower, c0, c1)
        else:
            if (c1<0):
                equation = "%d^{%dx+%d} = %d^{%dx-%d}" %(b0, a0, a1, b1ToThePower, c0, -c1)
            else:
                equation = "%d^{%dx+%d} = %d^{%dx+%d}" %(b0, a0, a1, b1ToThePower, c0, c1)

    else:
        b1ToThePower = b1**abs(power)
        if (a1<0):
            if (c1<0):
                equation = "%d^{%dx-%d} = \\left(\\frac{1}{%d}\\right)^{%dx-%d}" %(b0, a0, -a1, b1ToThePower, c0, -c1)
            else:
                equation = "%d^{%dx-%d} = \\left(\\frac{1}{%d}\\right)^{%dx+%d}" %(b0, a0, -a1, b1ToThePower, c0, c1)
        else:
            if (c1<0):
                equation = "%d^{%dx+%d} = \\left(\\frac{1}{%d}\\right)^{%dx-%d}" %(b0, a0, a1, b1ToThePower, c0, -c1)
            else:
                equation = "%d^{%dx+%d} = \\left(\\frac{1}{%d}\\right)^{%dx+%d}" %(b0, a0, a1, b1ToThePower, c0, c1)

    return equation

def createSolutionAndDistractors(coefficients):
    #b0**(a0*x+a1) = (b1**power)**(c0*x+c1)
    b0, a0, a1, b1, power, c0, c1 = coefficients
    b0f = float(b0)
    a0f = float(a0)
    a1f = float(a1)
    b1f = float(b1)
    powerf = float(power)
    c0f = float(c0)
    c1f = float(c1)
    L0 = float(math.log(b0f))
    L1 = float( math.log(b1f**powerf) )
    numerator = float(L1*c1f - a1f*L0)
    denominator = float(a0f*L0 - c0f*L1)
    solution = float(numerator/denominator)
    # D1 - Ignores bases and solves exponents equal.
    distractor1 = float(c1f - a1f)/float(a0f - c0f)
    # D2 - Distributes ln(base) to first term only.
    distractor2 = float(c1f - a1f)/float(a0f*L0 - c0f*L1)
    # D3 - Distributes ln(base) to second term only.
    distractor3 = float(L1*c1f - a1f*L0)/float(a0f - c0f)
    return [solution, distractor1, distractor2, distractor3]

def createAnswerList(solutionList):
    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
    solutionInterval = [intervalOptions[0], "* $x = %.3f$, which is the correct option." %solutionList[0], 1]
    distractor1Interval = [intervalOptions[1], "$x = %.3f$, which corresponds to solving the numerators as equal while ignoring the bases are different." %solutionList[1], 0]
    distractor2Interval = [intervalOptions[2], "$x = %.3f$, which corresponds to distributing the $\\ln(base)$ to the first term of the exponent only." %solutionList[2], 0]
    distractor3Interval = [intervalOptions[3], "$x = %.3f$, which corresponds to distributing the $\\ln(base)$ to the second term of the exponent only." %solutionList[3], 0]
    distractor4Interval = [["\\text{There is no Real solution to the equation.}"], "This corresponds to believing there is no solution since the bases are not powers of each other.", 0]
    answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
    random.shuffle(answerList)
    answerList.append(distractor4Interval)
    return answerList

# One question for each type
typesOfPower = ["Natural", "Integer"]
power = typesOfPower[random.randint(0, 1)]

coefficients = createCoefficients(power)
equation = displayEquation(coefficients)
solutionList = createSolutionAndDistractors(coefficients)

while (abs(solutionList[0]-solutionList[1]) < 1 or abs(solutionList[0]-solutionList[2]) < 1) or abs(solutionList[0]-solutionList[3]) < 1 or abs(solutionList[1]-solutionList[2]) < 1 or abs(solutionList[1]-solutionList[3]) < 1 or abs(solutionList[2]-solutionList[3]) < 1:
    coefficients = createCoefficients(power)
    equation = displayEquation(coefficients)
    solutionList = createSolutionAndDistractors(coefficients)
answerList = createAnswerList(solutionList)

if response_type=="Multiple-Choice":
	displayStem = 'Solve the equation for $x$ and choose the interval that contains the solution (if it exists).'
else:
	displayStem="Solve the equation below for $x$."
displayProblem = equation
displaySolution = "x = %.3f" %solutionList[0]
generalComment = "\\textbf{General Comments:} This question was written so that the bases could not be written the same. You will need to take the log of both sides."

c0 = "x \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1])
c1 = "x \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1])
c2 = "x \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1])
c3 = "x \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1])
c4 = "%s" %answerList[4][0][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
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
