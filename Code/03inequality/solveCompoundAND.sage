import random
from sympy.abc import x
from sympy import solve
from sympy import Symbol
import math

# OBJECTIVE 3 - Solve Compound Inequalities
# Types: "or" and "and" Inequalities

# Type 2 - "and" Inequalities
# andBlocks[0] + andBlocks[1] * x leq (andBlocks[2]*x - andBlocks[3])/andBlocks[4] < andBlocks[5] + andBlocks[6] * x
# Some conditions to make it nicer
    # andBlocks[1]*andBlocks[4] - andBlocks[2] < 0
        # andBlocks[1] * andBlocks[4] < andBlocks[2]
    # andBlocks[2] - andBlocks[4]*andBlocks[6] > 0
        # andBlocks[6] * andBlocks[4]  < andBlocks[2]
# To make these two conditions true:
    # Randomize 1, 4, and 6,
    # take the max(andBlocks[1] * andBlocks[4], andBlocks[6] * andBlocks[4]),
    # then randomly add to the max to make 2.

def createAllCoefficientsAndEndpoints():
    coefficients = [0, 0, 0, 0, 0, 0, 0]
    coefficients[0] = float(maybeMakeNegative(random.randint(3, 9)))
    coefficients[1] = float(maybeMakeNegative(random.randint(3, 9)))
    coefficients[3] = float(maybeMakeNegative(random.randint(3, 9)))
    coefficients[4] = float(random.randint(3, 9))
    coefficients[5] = float(maybeMakeNegative(random.randint(3, 9)))
    coefficients[6] = float(maybeMakeNegative(random.randint(3, 9)))
    # Need 1, 4, and 6 set before 2
    coefficients[2] = float((max(coefficients[1], coefficients[6])*coefficients[4]) + random.randint(2, 5))
    # This flips the inequalities

    smallerEndpoint = float((-coefficients[0]*coefficients[4] - coefficients[3]) / (coefficients[1]*coefficients[4] - coefficients[2]))
    largerEndpoint = float((coefficients[4]*coefficients[5] + coefficients[3]) / (coefficients[2] - coefficients[4] * coefficients[6]))

    # Makes sure we get a solution interval
    while  (largerEndpoint <= smallerEndpoint):
        coefficients[0] = float(maybeMakeNegative(random.randint(3, 9)))
        coefficients[1] = float(maybeMakeNegative(random.randint(3, 9)))
        coefficients[3] = float(maybeMakeNegative(random.randint(3, 9)))
        coefficients[4] = float(random.randint(3, 9))
        coefficients[5] = float(maybeMakeNegative(random.randint(3, 9)))
        coefficients[6] = float(maybeMakeNegative(random.randint(3, 9)))
        # Need 1, 4, and 6 set before 2
        coefficients[2] = float((max(coefficients[1], coefficients[6])*coefficients[4]) + random.randint(2, 5))
        # This flips the inequalities

        smallerEndpoint = float((-coefficients[0]*coefficients[4] - coefficients[3]) / (coefficients[1]*coefficients[4] - coefficients[2]))
        largerEndpoint = float((coefficients[4]*coefficients[5] + coefficients[3]) / (coefficients[2] - coefficients[4] * coefficients[6]))

    a, b, c, d, e, f, g = coefficients

    return [a, b, c, d, e, f, g, smallerEndpoint, largerEndpoint]

def generateSolutionInterval(solution, intervalRange):
    intervalList = [[]]*len(solution)
    for i in xrange(0, len(solution)):
        intervalList[i] = createInterval(solution[i], intervalRange)
    return intervalList

intervalRange = 4
allCoefficientsAndEndpoints = createAllCoefficientsAndEndpoints()

coefficients = [allCoefficientsAndEndpoints[0], allCoefficientsAndEndpoints[1], allCoefficientsAndEndpoints[2], allCoefficientsAndEndpoints[3], allCoefficientsAndEndpoints[4], allCoefficientsAndEndpoints[5], allCoefficientsAndEndpoints[6]]
solutionEndpoints = [allCoefficientsAndEndpoints[7], allCoefficientsAndEndpoints[8]]

while (abs(solutionEndpoints[0])==abs(solutionEndpoints[1]) or abs(solutionEndpoints[0])<1 or abs(solutionEndpoints[1])<1 or abs(abs(solutionEndpoints[0])-abs(solutionEndpoints[1])) < 1 ):
    allCoefficientsAndEndpoints = createAllCoefficientsAndEndpoints()
    coefficients = [allCoefficientsAndEndpoints[0], allCoefficientsAndEndpoints[1], allCoefficientsAndEndpoints[2], allCoefficientsAndEndpoints[3], allCoefficientsAndEndpoints[4], allCoefficientsAndEndpoints[5], allCoefficientsAndEndpoints[6]]
    solutionEndpoints = [float(allCoefficientsAndEndpoints[7]), float(allCoefficientsAndEndpoints[8])]

# Display for LaTeX
c0 = Integer(coefficients[0])
c1 = Integer(coefficients[1])
c2 = Integer(coefficients[2])
c3 = Integer(coefficients[3])
c4 = Integer(coefficients[4])
c5 = Integer(coefficients[5])
c6 = Integer(coefficients[6])

if c1 < 0:
    AndInequalityLeft = "%s - %s x" %(c0, -c1)
else:
    AndInequalityLeft = "%s + %s x" %(c0, c1)

if c3 < 0:
    AndInequalityMiddle = "\\frac{%s x + %s}{%s}" %(c2, -c3, c4)
else:
    AndInequalityMiddle = "\\frac{%s x - %s}{%s}" %(c2, c3, c4)

if c6 < 0:
    AndInequalityRight = "%s - %s x" %(c5, -c6)
else:
    AndInequalityRight = "%s + %s x" %(c5, c6)

precision = 1

solutionAndNegative = [solutionEndpoints, [-solutionEndpoints[0], -solutionEndpoints[1]]]
intervalOptions1 = createIntervalOptions(solutionAndNegative, intervalRange, precision)
intervalOptions2 = createIntervalOptions(solutionAndNegative, intervalRange, precision)
intervalOptions3 = createIntervalOptions(solutionAndNegative, intervalRange, precision)
intervalOptions4 = createIntervalOptions(solutionAndNegative, intervalRange, precision)

displayStem = 'Solve the linear inequality below. Then, choose the constant and interval combination that describes the solution set.'

problemType = random.randint(0,3)

if problemType == 0:
    displayProblem = '%s < %s \\leq %s' %(AndInequalityLeft, AndInequalityMiddle, AndInequalityRight)
    solution = ["(a, b]", "* $(%.2f, %.2f]$, which is the correct option." %(solutionEndpoints[0], solutionEndpoints[1]), 1]
    displaySolution =  "(%.2f, %.2f]" %(solutionEndpoints[0], solutionEndpoints[1])
    distractor1 = ["[a, b)", "$[%.2f, %.2f)$, which corresponds to flipping the inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor2 = ["(-\\infty, a) \\cup [b, \\infty)", "$(-\\infty, %.2f) \\cup [%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor3 = ["(-\\infty, a] \\cup (b, \\infty)", "$(-\\infty, %.2f] \\cup (%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality AND flipping the inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor4 = ["\\text{None of the above.}", "", "This corresponds to thinking that the values were not correct.", 0]
    answerList = [solution, distractor1, distractor2, distractor3]
    random.shuffle(answerList)
    answerList.append(distractor4)
elif problemType == 1:
    displayProblem = '%s \\leq %s < %s' %(AndInequalityLeft, AndInequalityMiddle, AndInequalityRight)
    solution = ["[a, b)", "$[%.2f, %.2f)$, which is the correct option." %(solutionEndpoints[0], solutionEndpoints[1]), 1]
    displaySolution =  "[%.2f, %.2f)" %(solutionEndpoints[0], solutionEndpoints[1])
    distractor1 = ["(a, b]", "$(%.2f, %.2f]$, which corresponds to flipping the inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor2 = ["(-\\infty, a] \\cup (b, \\infty)", "$(-\\infty, %.2f] \\cup (%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor3 = ["(-\\infty, a) \\cup [b, \\infty)", "$(-\\infty, %.2f) \\cup [%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality AND flipping the inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor4 = ["\\text{None of the above.}", "", "This corresponds to thinking that the values were not correct.", 0]
    answerList = [solution, distractor1, distractor2, distractor3]
    random.shuffle(answerList)
    answerList.append(distractor4)
elif problemType == 2:
    displayProblem = '%s < %s \\leq %s' %(AndInequalityLeft, AndInequalityMiddle, AndInequalityRight)
    distractor4 = ["(a, b]", "$(%.2f, %.2f]$, which is the correct interval but negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor1 = ["[a, b)", "$[%.2f, %.2f)$, which corresponds to flipping the inequality and getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor2 = ["(-\\infty, a) \\cup [b, \\infty)", "$(-\\infty, %.2f) \\cup [%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality and getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor3 = ["(-\\infty, a] \\cup (b, \\infty)", "$(-\\infty, %.2f] \\cup (%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality AND flipping the inequality AND getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    solution = ["\\text{None of the above.}", "* This is correct as the answer should be $(%.2f, %.2f]$." %(solutionEndpoints[0], solutionEndpoints[1]), 1]
    displaySolution = solution[0]
    answerList = [distractor4, distractor1, distractor2, distractor3]
    random.shuffle(answerList)
    answerList.append(solution)
else:
    displayProblem = '%s \\leq %s < %s' %(AndInequalityLeft, AndInequalityMiddle, AndInequalityRight)
    distractor4 = ["[a, b)", "$[%.2f, %.2f)$, which is the correct interval but negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor1 = ["(a, b]", "$(%.2f, %.2f]$, which corresponds to flipping the inequality and getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor2 = ["(-\\infty, a] \\cup (b, \\infty)", "$(-\\infty, %.2f] \\cup (%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality and getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor3 = ["(-\\infty, a) \\cup [b, \\infty)", "$(-\\infty, %.2f) \\cup [%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality AND flipping the inequality AND getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    solution = ["\\text{None of the above.}", "* This is correct as the answer should be $[%.2f, %.2f)$." %(solutionEndpoints[0], solutionEndpoints[1]), 1]
    displaySolution = solution[0]
    answerList = [distractor4, distractor1, distractor2, distractor3]
    random.shuffle(answerList)
    answerList.append(solution)

generalComment = "To solve, you will need to break up the compound inequality into two inequalities. Be sure to keep track of the inequality! It may be best to draw a number line and graph your solution."

if problemType == 0 or problemType == 1:
    c0 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[0][0], intervalOptions1[0][0][0], intervalOptions1[0][0][1], intervalOptions1[0][1][0], intervalOptions1[0][1][1])
    c1 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[1][0], intervalOptions2[0][0][0], intervalOptions2[0][0][1], intervalOptions2[0][1][0], intervalOptions2[0][1][1])
    c2 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[2][0], intervalOptions3[0][0][0], intervalOptions3[0][0][1], intervalOptions3[0][1][0], intervalOptions3[0][1][1])
    c3 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0], intervalOptions4[0][0][0], intervalOptions4[0][0][1], intervalOptions4[0][1][0], intervalOptions4[0][1][1])
    c4 = "%s" %answerList[4][0]
else:
    c0 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[0][0], intervalOptions1[1][0][0], intervalOptions1[1][0][1], intervalOptions1[1][1][0], intervalOptions1[1][1][1])
    c1 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[1][0], intervalOptions2[1][0][0], intervalOptions2[1][0][1], intervalOptions2[1][1][0], intervalOptions2[1][1][1])
    c2 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[2][0], intervalOptions3[1][0][0], intervalOptions3[1][0][1], intervalOptions3[1][1][0], intervalOptions3[1][1][1])
    c3 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0], intervalOptions4[1][0][0], intervalOptions4[1][0][1], intervalOptions4[1][1][0], intervalOptions4[1][1][1])
    c4 = "%s" %answerList[4][0]

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
