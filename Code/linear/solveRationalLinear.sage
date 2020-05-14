import random
import numpy
from sympy.solvers import solve
from sympy.abc import x

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
    a = maybeMakeNegative(random.randint(3, 9))
    b = maybeMakeNegative(random.randint(3, 9))
    c = maybeMakeNegative(random.randint(3, 9))
    return [a, b, c]

def createThreeDistinctRandomNaturals():
    possibleNaturals= range(2,9)
    naturals = random.sample(possibleNaturals, 3)
    return naturals

def createThreeDistinctRandomIntegers():
    a, b, c = random.sample(range(3, 9), 3)
    return [maybeMakeNegative(a), maybeMakeNegative(b), maybeMakeNegative(c)]

def checkDivisibility(set, divisors):
    if gcd(set[0], divisors[0]) > 1 or gcd(set[1], divisors[1]) > 1 or gcd(set[2], divisors[2]) > 1:
        setDivisible = 1
    else:
        setDivisible = 0
    return setDivisible

def createViableConstants():
    coefficients = createThreeRandomIntegers()
    numerators = createThreeRandomIntegers()
    denominators = createThreeDistinctRandomNaturals()
    a, b, c = coefficients
    d, e, f = numerators
    g, h, i = denominators

    # Check that there is exactly one solution to the linear equation
    firstBlock = float(a/g)
    secondBlock = float(b/h)
    thirdBlock = float(c/i)
    OneSolutionCheck = firstBlock - secondBlock - thirdBlock

    # Forces just one set of coefficients to be divisible by denominator.
    firstDivisible = checkDivisibility(coefficients, denominators)
    secondDivisible = checkDivisibility(numerators, denominators)
    firstOrSecondDivisible = random.randint(0, 1)
    if firstOrSecondDivisible == 0:
        while (OneSolutionCheck == 0) or (firstDivisible == 0) or (secondDivisible==1):
            coefficients = createThreeRandomIntegers()
            numerators = createThreeRandomIntegers()
            denominators = createThreeDistinctRandomNaturals()
            #
            a, b, c = coefficients
            d, e, f = numerators
            g, h, i = denominators
            #
            firstBlock = float(a/g)
            secondBlock = float(b/h)
            thirdBlock = float(c/i)
            OneSolutionCheck = firstBlock - secondBlock - thirdBlock
            #
            firstDivisible = checkDivisibility(coefficients, denominators)
            secondDivisible = checkDivisibility(numerators, denominators)
    else:
        while (OneSolutionCheck == 0) or (firstDivisible == 1) or (secondDivisible==0):
            coefficients = createThreeRandomIntegers()
            numerators = createThreeRandomIntegers()
            denominators = createThreeDistinctRandomNaturals()
            #
            a, b, c = coefficients
            d, e, f = numerators
            g, h, i = denominators
            #
            firstBlock = float(a/g)
            secondBlock = float(b/h)
            thirdBlock = float(c/i)
            OneSolutionCheck = firstBlock - secondBlock - thirdBlock
            #
            firstDivisible = checkDivisibility(coefficients, denominators)
            secondDivisible = checkDivisibility(numerators, denominators)
    return [a, b, c, d, e, f, g, h, i]

def createSolution(constants):
    a, b, c, d, e, f, g, h, i = constants
    equationBlockOne = (a*x+d)/g
    equationBlockTwo = (b*x+e)/h
    equationBlockThree = (c*x+f)/i

    toSolve = equationBlockOne - equationBlockTwo - equationBlockThree
    solution = solve(toSolve)
    if len(solution)==0:
        solution = [0]
    else:
        print("Things went well.")
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
    return ['x_1 \\in [%d,%d]' %(interval[0], interval[1])]
intervalRange = 3

constants = createViableConstants()
solution = [createSolution(constants)[0]]
#solutionInterval = intervalToString(generateSolutionInterval(solution, intervalRange))

distractor1 = [createSolution(distractorMinorDistributionError(constants))[0]]
distractor2 = [createSolution(distractorBadNumeratorDivision(constants))[0]]
distractor3 = [createSolution(distractorBadCoefficientDivision(constants))[0]]
#distractor4 = createSolution(distractorNegativeSolution(constants))[0]

#Make sure to update this while loop if you add back distractor 4!
#while (abs(distractor1[0])<=1 or abs(distractor2[0])<=1 or abs(distractor3[0])<=1 or abs(distractor4[0])<=1):
while (abs(distractor1[0])<=1 or abs(distractor2[0])<=1 or abs(distractor3[0])<=1):
    constants = createViableConstants()
    solution = [createSolution(constants)[0]]
    #solutionInterval = intervalToString(generateSolutionInterval(solution, intervalRange))

    distractor1 = [createSolution(distractorMinorDistributionError(constants))[0]]
    distractor2 = [createSolution(distractorBadNumeratorDivision(constants))[0]]
    distractor3 = [createSolution(distractorBadCoefficientDivision(constants))[0]]
    # distractor4 = createSolution(distractorNegativeSolution(constants))[0]

solutionList = [solution, distractor1, distractor2, distractor3]
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = [intervalOptions[0][0]]
distractor1Interval = [intervalOptions[1][0]]
distractor2Interval = [intervalOptions[2][0]]
distractor3Interval = [intervalOptions[3][0]]

displayStem = 'Solve the linear equation below. Then, choose the interval that contains the solution.'

if constants[3] < 0:
    if constants[4] < 0:
        if constants[5] < 0:
            displayProblem = "\\frac{%d x - %d}{%s} - \\frac{%d x - %d}{%d} = \\frac{%d x - %d}{%d}" %(constants[0], -constants[3], constants[6], constants[1], -constants[4], constants[7], constants[2], -constants[5], constants[8])
        else:
            displayProblem = "\\frac{%d x - %d}{%s} - \\frac{%d x - %d}{%d} = \\frac{%d x + %d}{%d}" %(constants[0], -constants[3], constants[6], constants[1], -constants[4], constants[7], constants[2], constants[5], constants[8])
    else:
        if constants[5] < 0:
            displayProblem = "\\frac{%d x - %d}{%s} - \\frac{%d x + %d}{%d} = \\frac{%d x - %d}{%d}" %(constants[0], -constants[3], constants[6], constants[1], constants[4], constants[7], constants[2], -constants[5], constants[8])
        else:
            displayProblem = "\\frac{%d x - %d}{%s} - \\frac{%d x + %d}{%d} = \\frac{%d x + %d}{%d}" %(constants[0], -constants[3], constants[6], constants[1], constants[4], constants[7], constants[2], constants[5], constants[8])
else:
    if constants[4] < 0:
        if constants[5] < 0:
            displayProblem = "\\frac{%d x + %d}{%s} - \\frac{%d x - %d}{%d} = \\frac{%d x - %d}{%d}" %(constants[0], constants[3], constants[6], constants[1], -constants[4], constants[7], constants[2], -constants[5], constants[8])
        else:
            displayProblem = "\\frac{%d x + %d}{%s} - \\frac{%d x - %d}{%d} = \\frac{%d x + %d}{%d}" %(constants[0], constants[3], constants[6], constants[1], -constants[4], constants[7], constants[2], constants[5], constants[8])
    else:
        if constants[5] < 0:
            displayProblem = "\\frac{%d x + %d}{%s} - \\frac{%d x + %d}{%d} = \\frac{%d x - %d}{%d}" %(constants[0], constants[3], constants[6], constants[1], constants[4], constants[7], constants[2], -constants[5], constants[8])
        else:
            displayProblem = "\\frac{%d x + %d}{%s} - \\frac{%d x + %d}{%d} = \\frac{%d x + %d}{%d}" %(constants[0], constants[3], constants[6], constants[1], constants[4], constants[7], constants[2], constants[5], constants[8])

displaySolution = "x = %.3f" %solution[0]
generalComment = "General Comments: If you are having trouble with this problem, try to remove a fraction at a time by multiplying each term by the denominator."

solutionInterval.append("* $x = %.3f$, which is the correct option." %solution[0])
distractor1Interval.append(" $x = %.3f$, which corresponds to not distributing the negative correctly for the second fraction." %distractor1[0])
distractor2Interval.append(" $x = %.3f$, which corresponds to dividing only the first term for each fraction (rather than multiplying to remove the fractions)." %distractor2[0])
distractor3Interval.append(" $x = %.3f$, which corresponds to dividing only the second term for each fraction (rather than multiplying to remove the fractions)." %distractor3[0])

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

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
