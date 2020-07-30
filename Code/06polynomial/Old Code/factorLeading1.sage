# OBJECTIVE 2 - Factor a trinomial with leading coefficient 1.
from sympy.abc import x
import random

load("../Code/generalPurposeMethods.sage")
#load("generalPurposeMethods.sage")
def generateNumber(maxRange):
    return 2*(random.randint(2, maxRange))

def createZeros(maxRange):
    c = maybeMakeNegative(generateNumber(maxRange))
    d = maybeMakeNegative(generateNumber(maxRange))
    while (c==-d):
        c = maybeMakeNegative(generateNumber(maxRange))
        d = maybeMakeNegative(generateNumber(maxRange))
    if (c<=d):
        return [c, d]
    else:
        return [d, c]

def generateSolutionInterval(solution, intervalRange):
    intervalList = [[]]*len(solution)
    for i in xrange(0, len(solution)):
        intervalList[i] = createInterval(solution[i], intervalRange)
    return intervalList

def distractorWrongProduct(zeros):
    product = zeros[0]*zeros[1]
    divisor = gcd(zeros[0], zeros[1])
    output = [product/divisor, divisor]
    if (product/divisor <= divisor):
        return output
    else:
        return [divisor, product/divisor]

def distractorWrongProduct2(zeros):
    product = zeros[0]*zeros[1]
    divisor = 2
    output = [product/divisor, divisor]
    if (product/divisor <= divisor):
        return output
    else:
        return [divisor, product/divisor]

def distractorWrongSum(zeros):
    zeroSum = zeros[0] + zeros[1]
    divisor = gcd(zeros[0], zeros[1])
    output = [zeroSum - divisor, divisor]
    if (zeroSum - divisor <= divisor):
        return output
    else:
        return [divisor, zeroSum - divisor]

def distractorWrongSum2(zeros):
    zeroSum = zeros[0] + zeros[1]
    divisor = 2
    output = [zeroSum - divisor, divisor]
    if (zeroSum - divisor <= divisor):
        return output
    else:
        return [divisor, zeroSum - divisor]

solution = createZeros(14)
zeros = solution
quadratic = x**2 + (zeros[0] + zeros[1]) * x + zeros[0]*zeros[1]

distractor1 = distractorWrongProduct(zeros)
distractor2 = distractorWrongSum(zeros)
distractor3 = distractorWrongProduct2(zeros)
distractor4 = distractorWrongSum2(zeros)
distractors = [distractor1, distractor2, distractor3, distractor4]

while (distractor1==distractor2 or distractor1 == distractor3 or distractor1 == distractor4 or distractor1 == solution or distractor2 == distractor3 or distractor2 == distractor4 or distractor2 == solution or distractor3==distractor4 or distractor3==solution or distractor4==solution):
    solution = createZeros(14)
    zeros = solution

    distractor1 = distractorWrongProduct(zeros)
    distractor2 = distractorWrongSum(zeros)
    distractor3 = distractorWrongProduct2(zeros)
    distractor4 = distractorWrongSum2(zeros)
    distractors = [distractor1, distractor2, distractor3, distractor4]

solutionList = [solution, distractor1, distractor2, distractor3, distractor4]

intervalRange = 5
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

quadratic = x**2 + (zeros[0] + zeros[1]) * x + zeros[0]*zeros[1]

displayStem = 'Factor the quadratic below. Then, choose the intervals that contain the constants in the form $(x+a)(x+b); a \\leq b.$'

constantB = zeros[0] + zeros[1]
constantC = zeros[0] * zeros[1]

if constantB < 0 and constantC < 0:
    displayProblem = "x^2 - %s x - %s" %(-constantB, -constantC)
elif constantB < 0 and constantC > 0:
    displayProblem = "x^2 - %s x + %s" %(-constantB, constantC)
elif constantB > 0 and constantC < 0:
    displayProblem = "x^2 + %s x - %s" %(constantB, -constantC)
else:
    displayProblem = "x^2 + %s x + %s" %(constantB, constantC)

solutionFactor0 = x + zeros[0]
solutionFactor1 = x + zeros[1]
displaySolution = '(%s)(%s)' %(solutionFactor0, solutionFactor1)
generalComment = "General Comments: We are looking for two numbers that multiple to be $%s$ and add to be $%s$. When in doubt, list the products in order!" %(constantC, constantB)

solutionInterval = intervalOptions[0]
distractor1Interval = intervalOptions[1]
distractor2Interval = intervalOptions[2]
distractor3Interval = intervalOptions[3]
distractor4Interval = intervalOptions[4]

solutionInterval.append("* Correct option.")
distractor1Interval.append(" Distractor 1: Corresponds to using the wrong product of c based on the gcd.")
distractor2Interval.append(" Distractor 2: Corresponds to miscalculating the sum of the products of c based on the gcd of the zeros.")
distractor3Interval.append(" Distractor 3: Corresponds to using the wrong product of c by 2.")
distractor4Interval.append(" Distractor 4: Corresponds to miscalculating the sum of the products of c by 2.")

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

c0 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1], answerList[0][1][0], answerList[0][1][1])
c1 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1], answerList[1][1][0], answerList[1][1][1])
c2 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1], answerList[2][1][0], answerList[2][1][1])
c3 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1], answerList[3][1][0], answerList[3][1][1])
c4 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[4][0][0], answerList[4][0][1], answerList[4][1][0], answerList[4][1][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)

print "Finished running factorLeading1.sage"
