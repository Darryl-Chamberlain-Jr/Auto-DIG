import numpy
from sympy.abc import x
from sympy import Symbol
import random

def generateLineType():
    typeList = ['Parallel', 'Perpendicular']
    lineType = typeList[random.randint(0, len(typeList)-1)]
    return lineType

def generateProblemAndSolution(lineType):
    if lineType == 'Parallel':
        point = [maybeMakeNegative(random.randint(2, 10)), maybeMakeNegative(random.randint(2, 10))]
        aCoeff = random.randint(3, 9)
        bCoeff = maybeMakeNegative(random.randint(3, 9))
        while gcd(aCoeff, abs(bCoeff)) > 1:
            aCoeff = random.randint(3, 9)
            bCoeff = maybeMakeNegative(random.randint(3, 9))
        cCoeff = float(random.randint(3, 15))
        aFloat = float(aCoeff)
        bFloat = float(bCoeff)
        slope = float(-aFloat/bFloat)
        yInt = float(point[1]-slope*point[0])
        return [[slope, yInt], point, [aCoeff, bCoeff, cCoeff]]
    elif lineType == 'Perpendicular':
        point = [maybeMakeNegative(random.randint(2, 10)), maybeMakeNegative(random.randint(2, 10))]
        aCoeff = random.randint(3, 9)
        bCoeff = maybeMakeNegative(random.randint(3, 9))
        while gcd(aCoeff, abs(bCoeff)) > 1:
            aCoeff = random.randint(3, 9)
            bCoeff = maybeMakeNegative(random.randint(3, 9))
        cCoeff = float(random.randint(3, 15))
        aFloat = float(aCoeff)
        bFloat = float(bCoeff)
        slope = float(bFloat/aFloat)
        yInt = float(point[1]-slope*point[0])
        return [[slope, yInt], point, [aCoeff, bCoeff, cCoeff]]
    else:
        print("You did not input an appropriate line type, you entered " + str(lineType))

def generateSolutionInterval(solution, intervalRange):
    intervalList = [[]]*len(solution)
    for i in range(0, len(solution)):
        intervalList[i] = createInterval(solution[i], intervalRange)
    return intervalList

def distractorSlopeSign(solution, point):
    # (-slope, point[1]+slope*point[0])
    slope, yInt = solution
    distractorSlope = -slope
    distractorYInt = point[1] + slope*point[0]
    return [distractorSlope, distractorYInt]

def distractorYIntSign(solution):
    # (slope, -yInt)
    slope, yInt = solution
    distractorSlope = slope
    distractorYInt = -yInt
    return [distractorSlope, distractorYInt]
def distractorPointSlopeMisdistribute(solution, point):
    #(slope, -point[0]+point[1])
    #This is if the student used point-slope and did not distribute correctly.
    slope, yInt = solution
    pointOne, pointTwo = point
    distractorSlope = slope
    distractorYInt = -pointOne + pointOne
    return [distractorSlope, distractorYInt]
def distractorSlopeInverted(solution, point):
    # (1/slope, yInt)
    #Created when a student inverts the slope.
    slope, yInt = solution
    distractorSlope = 1.0/slope
    distractorYInt = yInt
    return [distractorSlope, distractorYInt]

def displayEquation(coefficients):
    slope, yInt = coefficients
    if yInt < 0:
        equation = "y = %.2fx - %.2f" %(slope, -yInt)
    else:
        equation = "y = %.2fx + %.2f" %(slope, yInt)
    return equation

# Type 2 - Parallel/Perpendicular line and a point
intervalRange = 2
lineType = generateLineType()
generateProblemAndSolution(lineType)
solution, point, coefficients = generateProblemAndSolution(lineType)

distractor1 = distractorSlopeSign(solution, point)
distractor2 = distractorYIntSign(solution)
distractor3 = distractorPointSlopeMisdistribute(solution, point)
distractor4 = distractorSlopeInverted(solution, point)

solutionList = [solution, distractor1, distractor2, distractor3, distractor4]
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = intervalOptions[0]
distractor1Interval = intervalOptions[1]
distractor2Interval = [createIntervalOptions([solutionList[2][0]], intervalRange, precision)[0], intervalOptions[2][1]]
distractor3Interval = [createIntervalOptions([solutionList[3][0]], intervalRange, precision)[0], intervalOptions[3][1]]
distractor4Interval = [intervalOptions[4][0], createIntervalOptions([solutionList[4][1]], intervalRange, precision)[0]]

aCoeff, bCoeff, cCoeff = coefficients
cCoeffInt = int(cCoeff)

if bCoeff < 0:
    standardFormParOrPer = "%s x - %s y" %(int(aCoeff), -int(bCoeff))
else:
    standardFormParOrPer = "%s x + %s y" %(int(aCoeff), int(bCoeff))

displayStem = 'Find the equation of the line described below. Write the linear equation as $ y=mx+b $ and choose the intervals that contain $m$ and $b$.'
displayProblem = '\\text{%s to } %s = %d \\text{ and passing through the point } (%s, %s).' %(lineType, standardFormParOrPer, cCoeffInt, point[0], point[1])
displaySolution = displayEquation(solution)
generalComment = "General Comments: Parallel slope is the same and perpendicular slope is opposite reciprocal. Opposite reciprocal means flipping the fraction and changing the sign (positive to negative or negative to positive)."

solutionInterval.append("* $%s$, which is the correct option." %displayEquation(solution))
distractor1Interval.append(" $%s$, which corresponds to using the negative slope." %displayEquation(distractor1))
distractor2Interval.append(" $%s$, which corresponds to using the correct slope and getting the negative $y$-intercept." %displayEquation(distractor2))
distractor3Interval.append(" $%s$, which corresponds to using the correct slope and mis-distributing while simplifying to slope-intercept form." %displayEquation(distractor3))
distractor4Interval.append(" $%s$, which corresponds to using the reciprocal slope $(1/m)$." %displayEquation(distractor4))

solutionInterval.append(1)
distractor1Interval.append(0)
distractor2Interval.append(0)
distractor3Interval.append(0)
distractor4Interval.append(0)

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

c0 = "m \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1], answerList[0][1][0], answerList[0][1][1])
c1 = "m \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1], answerList[1][1][0], answerList[1][1][1])
c2 = "m \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1], answerList[2][1][0], answerList[2][1][1])
c3 = "m \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1], answerList[3][1][0], answerList[3][1][1])
c4 = "m \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[4][0][0], answerList[4][0][1], answerList[4][1][0], answerList[4][1][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][3] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
