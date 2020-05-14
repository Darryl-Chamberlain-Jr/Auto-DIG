import random
import numpy
from sympy.solvers import solve
from sympy.abc import x

#load("../Code/generalPurposeMethods.sage")
print "Starting Objective 2 Type 2"
load("../generalPurposeMethods.sage")
# OBJECTIVE 2 - Solve linear equations.
# Types of questions:
    # Type 1 - Linear equations with Integers only
    # Type 2 - Linear equations with Rationals

# Type 2 - Solve Advanced linear equations (fractions)
#(coefficients[0]*x + numerators[0])/denominators[0]
    # - (coefficients[1]*x+numerators[1])/denominators[1]
    # = (coefficients[2]*x+numerators[2])/denominators[2]

#No restrictions on coefficients or numerators
def createThreeRandomIntegers():
    a = maybeMakeNegative(random.randint(3, 8))
    b = maybeMakeNegative(random.randint(3, 8))
    c = maybeMakeNegative(random.randint(3, 8))
    return [a, b, c]

def createThreeDistinctRandomNaturals():
    possibleNaturals= range(2,7)
    naturals = random.sample(possibleNaturals, 3)
    return naturals

def createThreeDistinctRandomIntegers():
    a, b, c = random.sample(range(3, 8), 3)
    return [maybeMakeNegative(a), maybeMakeNegative(b), maybeMakeNegative(c)]

def createViableConstants(coefficients, numerators, denominators):
    a, b, c = coefficients
    d, e, f = numerators
    g, h, i = denominators

    # Check that there is exactly one solution to the linear equation
    firstBlock = float(a/g)
    secondBlock = float(b/h)
    thirdBlock = float(c/i)
    OneSolutionCheck = firstBlock - secondBlock - thirdBlock

    while (OneSolutionCheck == 0):
        print "Help, I'm trapped in this fucking while loop"
        coefficients = createThreeRandomIntegers()
        numerators = createThreeRandomIntegers()
        denominators = createThreeDistinctRandomIntegers()

        a, b, c = coefficients
        d, e, f = numerators
        g, h, i = denominators

        firstBlock = float(a/g)
        secondBlock = float(b/h)
        thirdBlock = float(c/i)
        OneSolutionCheck = firstBlock - secondBlock - thirdBlock
    return [a, b, c, d, e, f, g, h, i]

def createSolution(constants):
    a, b, c, d, e, f, g, h, i = constants
    equationBlockOne = (a*x+d)/g
    equationBlockTwo = (b*x+e)/h
    equationBlockThree = (c*x+f)/i

    toSolve = equationBlockOne - equationBlockTwo - equationBlockThree
    solution = solve(toSolve)
    print "Solution: %s" %solution
    if len(solution)==0:
        solution = [0]
        print "One of the distractors does not have a solution."
    else:
        print "Things went well."
    return solution

def distractorMinorDistributionError(constants):
    a, b, c, d, e, f, g, h, i = constants
    return [a, b, c, d, -e, f, g, h, i]

#Student divides coefficients only
def distractorBadNumeratorDivision(constants):
    a, b, c, d, e, f, g, h, i = constants
    return [a, b, c, g*d, h*e, i*f, g, h, i]

#Student divides numerators only
def distractorBadCoefficientDivision(constants):
    a, b, c, d, e, f, g, h, i = constants
    return [g*a, h*b, i*c, d, e, f, g, h, i]

#Student leaves off negative at end of problem (sometimes will be a good distractor)
def distractorNegativeSolution(constants):
    a, b, c, d, e, f, g, h, i = constants
    return [a, b, c, -d, -e, -f, g, h, i]

def generateSolutionInterval(solution, intervalRange):
    intervalList = createInterval(solution, intervalRange)
    return intervalList
def intervalToString(interval):
    return ['x_1 \in [%d,%d]' %(interval[0], interval[1])]
intervalRange = 3
coefficients = createThreeRandomIntegers()
numerators = createThreeRandomIntegers()
denominators = createThreeDistinctRandomNaturals()

constants = createViableConstants(coefficients, numerators, denominators)

solution = [createSolution(constants)[0]]
#solutionInterval = intervalToString(generateSolutionInterval(solution, intervalRange))

distractor1 = [createSolution(distractorMinorDistributionError(constants))[0]]
distractor2 = [createSolution(distractorBadNumeratorDivision(constants))[0]]
distractor3 = [createSolution(distractorBadCoefficientDivision(constants))[0]]
#distractor4 = createSolution(distractorNegativeSolution(constants))[0]

#Make sure to update this while loop if you add back distractor 4!
#while (abs(distractor1[0])<=1 or abs(distractor2[0])<=1 or abs(distractor3[0])<=1 or abs(distractor4[0])<=1):
while (abs(distractor1[0])<=1 or abs(distractor2[0])<=1 or abs(distractor3[0])<=1):
    coefficients = createThreeRandomIntegers()
    numerators = createThreeRandomIntegers()
    denominators = createThreeDistinctRandomNaturals()

    constants = createViableConstants(coefficients, numerators, denominators)

    solution = [createSolution(constants)[0]]
    #solutionInterval = intervalToString(generateSolutionInterval(solution, intervalRange))

    distractor1 = [createSolution(distractorMinorDistributionError(constants))[0]]
    distractor2 = [createSolution(distractorBadNumeratorDivision(constants))[0]]
    distractor3 = [createSolution(distractorBadCoefficientDivision(constants))[0]]
    # distractor4 = createSolution(distractorNegativeSolution(constants))[0]

solutionList = [solution, distractor1, distractor2, distractor3]
print solutionList
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = [intervalOptions[0][0]]
distractor1Interval = [intervalOptions[1][0]]
distractor2Interval = [intervalOptions[2][0]]
distractor3Interval = [intervalOptions[3][0]]

displayStem = 'Solve the linear equation below. Then, choose the interval that contains the solution.'

if numerators[0] < 0:
    if numerators[1] < 0:
        if numerators[2] < 0:
            displayProblem = "\\frac{%d x - %d}{%s} - \\frac{%d x - %d}{%d} = \\frac{%d x - %d}{%d}" %(constants[0], -constants[3], constants[6], constants[1], -constants[4], constants[7], constants[2], -constants[5], constants[8])
        else:
            displayProblem = "\\frac{%d x - %d}{%s} - \\frac{%d x - %d}{%d} = \\frac{%d x + %d}{%d}" %(constants[0], -constants[3], constants[6], constants[1], -constants[4], constants[7], constants[2], constants[5], constants[8])
    else:
        if numerators[2] < 0:
            displayProblem = "\\frac{%d x - %d}{%s} - \\frac{%d x + %d}{%d} = \\frac{%d x - %d}{%d}" %(constants[0], -constants[3], constants[6], constants[1], constants[4], constants[7], constants[2], -constants[5], constants[8])
        else:
            displayProblem = "\\frac{%d x - %d}{%s} - \\frac{%d x + %d}{%d} = \\frac{%d x + %d}{%d}" %(constants[0], -constants[3], constants[6], constants[1], constants[4], constants[7], constants[2], constants[5], constants[8])
else:
    if numerators[1] < 0:
        if numerators[2] < 0:
            displayProblem = "\\frac{%d x + %d}{%s} - \\frac{%d x - %d}{%d} = \\frac{%d x - %d}{%d}" %(constants[0], constants[3], constants[6], constants[1], -constants[4], constants[7], constants[2], -constants[5], constants[8])
        else:
            displayProblem = "\\frac{%d x + %d}{%s} - \\frac{%d x - %d}{%d} = \\frac{%d x + %d}{%d}" %(constants[0], constants[3], constants[6], constants[1], -constants[4], constants[7], constants[2], constants[5], constants[8])
    else:
        if numerators[2] < 0:
            displayProblem = "\\frac{%d x + %d}{%s} - \\frac{%d x + %d}{%d} = \\frac{%d x - %d}{%d}" %(constants[0], constants[3], constants[6], constants[1], constants[4], constants[7], constants[2], -constants[5], constants[8])
        else:
            displayProblem = "\\frac{%d x + %d}{%s} - \\frac{%d x + %d}{%d} = \\frac{%d x + %d}{%d}" %(constants[0], constants[3], constants[6], constants[1], constants[4], constants[7], constants[2], constants[5], constants[8])

displaySolution = round(float(solution[0]), 3)
comments = "General Comments: If you are having trouble with this problem, try to remove a fraction at a time by multiplying each term by the denominator."

solutionInterval.append("* Correct option.")
distractor1Interval.append(" Corresponds to not distributing the negative correctly for the second fraction.")
distractor2Interval.append(" Corresponds to dividing only the first term for each fraction (rather than multiplying to remove the fractions).")
distractor3Interval.append(" Corresponds to dividing only the second term for each fraction (rather than multiplying to remove the fractions).")

solutionInterval.append(1)
distractor1Interval.append(0)
distractor2Interval.append(0)
distractor3Interval.append(0)

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)
toAppendAnswer = '\\text{There are no real solutions.}'
toAppendComment = "Corresponds to students thinking a fraction means there is no solution to the equation."
answerList.append([toAppendAnswer, toAppendComment, 0])

c0 = "x \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1])
c1 = "x \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1])
c2 = "x \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1])
c3 = "x \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1])
c4 = "\\text{There are no Real solutions.}"
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

#writeQuestionToFile(moduleNumber, version, problemNumber, displayStem, displayProblem)
#writeSolutionAndOptionsToFile(moduleNumber, version, displaySolution, choices, choiceComments)
#writeToMasterAnswerKeys(moduleNumber, version, answerLetter)
#writeCommentsToFile(moduleNumber, version, comments)
