# Module 5 - Radical Equations
    # Objective 1 - Identify the domain on which a radical function is not defined.
    # Objective 2 - Identify the graph of a radical function.
        # Two types of questions:
            # Graph to equation
            # Equation to graph
    # Objective 3 - Solve radical equations that lead to linear equations.
    # Objective 4 - Solve radical equations that lead to quadratic equations.

import random
from sympy.abc import x
from sympy import solve

#This question should be updated. The most common mistake, squaring both sides, results in the same answer as the correct method.

def radicalCheck(coefficients):
    a, b, c, d = coefficients
    af = float(a)
    bf = float(b)
    cf = float(c)
    df = float(d)
    solution = float((df-bf)/(af-cf))
    if (af*solution + bf < 0):
        r0 = 0
    else:
        r0 = 1
    if (cf*solution + df < 0):
        r1 = 0
    else:
        r1 = 1
    return [r0, r1]

def generateCoefficients(numberOfSolutions):
    a = maybeMakeNegative(random.randint(2, 9))
    c = maybeMakeNegative(random.randint(2, 9))
    while(a==c):
        a = maybeMakeNegative(random.randint(2, 9))
        c = maybeMakeNegative(random.randint(2, 9))
    b = maybeMakeNegative(random.randint(2, 9))
    d = maybeMakeNegative(random.randint(2, 9))
    
    check = radicalCheck([a, b, c, d])
    if (numberOfSolutions==0):
        while (check[0]*check[1] > 0):
            a = maybeMakeNegative(random.randint(2, 9))
            c = maybeMakeNegative(random.randint(2, 9))
            while(a==c):
                a = maybeMakeNegative(random.randint(2, 9))
                c = maybeMakeNegative(random.randint(2, 9))
            b = maybeMakeNegative(random.randint(2, 9))
            d = maybeMakeNegative(random.randint(2, 9))
            check = radicalCheck([a, b, c, d])
        return [a, b, c, d]
    else:
        while (check[0]*check[1] == 0):
            a = maybeMakeNegative(random.randint(2, 9))
            c = maybeMakeNegative(random.randint(2, 9))
            while(a==c):
                a = maybeMakeNegative(random.randint(2, 9))
                c = maybeMakeNegative(random.randint(2, 9))
            b = maybeMakeNegative(random.randint(2, 9))
            d = maybeMakeNegative(random.randint(2, 9))
            check = radicalCheck([a, b, c, d])
        return [a, b, c, d]

def generateSolution(coefficients):
    a, b, c, d = coefficients
    fa = float(a)
    fb = float(b)
    fc = float(c)
    fd = float(d)
    solution = float((fd - fb)/(fa - fc))
    return solution

def intervalToString(interval):
    return ['x \\in [%s,%s]' %(interval[0], interval[1])]

def stringForAnswersWithTwoIntervals(leftInterval, rightInterval):
    leftL, leftR = leftInterval
    rightL, rightR = rightInterval
    return ['x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s,%s]' %(leftL, leftR, rightL, rightR)]

def distractorFreshmansDream(coefficients):
    a, b, c, d = coefficients
    return [a, b, c, -d]

def distractorSolvedRoot1(coefficients):
    a, b, c, d = coefficients
    fa = float(a)
    fb = float(b)
    return -fb/fa

def distractorSolvedRoot2(coefficients):
    a, b, c, d = coefficients
    fc = float(c)
    fd = float(d)
    return -fd/fc

def generateSolutionInterval(solution, intervalRange):
    interval = createInterval(solution, intervalRange)
    return interval

def smallerFirst(twoValuesToCompare):
    if twoValuesToCompare[0] < twoValuesToCompare[1]:
        return twoValuesToCompare
    else:
        return [twoValuesToCompare[1], twoValuesToCompare[0]]

intervalRange=4
numberOfSolutions = random.randint(0, 1)
coefficients = generateCoefficients(numberOfSolutions)
solution = generateSolution(coefficients)

if coefficients[1] < 0:
    displayFactor1 = "%d x - %d" %(coefficients[0], -coefficients[1])
else:
    displayFactor1 = "%d x + %d" %(coefficients[0], coefficients[1])

if coefficients[3] <0:
    displayFactor2 = "%d x - %d" %(coefficients[2], -coefficients[3])
else:
    displayFactor2 = "%d x + %d" %(coefficients[2], coefficients[3])

if (numberOfSolutions==1):
    solutionLength = 1
    distractor1Interval = ['\\text{All solutions lead to invalid or complex values in the equation.}']
    distractor1Interval.append('This corresponds to believing the solution $x = %.3f$ leads to a complex value in the original equation.' %solution)
else:
    solutionLength = 0
    solutionInterval = ['\\text{All solutions lead to invalid or complex values in the equation.}']
    solutionInterval.append('*$x = %.3f$ leads to a complex value in the equation, so this is the correct option.' %solution)
    distractor1 = solution

displayStem = 'Solve the radical equation below. Then, choose the interval(s) that the solution(s) belongs to.'
displayProblem = '\\sqrt{%s} - \\sqrt{%s} = 0' %(displayFactor1, displayFactor2)
if (numberOfSolutions==0):
    displaySolution = '\\text{All solutions lead to invalid or complex values in the equation.}'
else:
    displaySolution = 'x = %s' %solution
distractor2 = generateSolution(distractorFreshmansDream(coefficients))
distractor3 = smallerFirst([solution, distractorSolvedRoot1(coefficients)])
distractor4 = smallerFirst([distractorSolvedRoot1(coefficients), distractorSolvedRoot2(coefficients)])

if(solutionLength == 0):
    firstSolutionSet = [distractor1, distractor2, distractor3[0], distractor4[0]]
else:
    firstSolutionSet = [solution, distractor2, distractor3[0], distractor4[0]]
precision = 1
intervalOptionsFirstSet = createIntervalOptions(firstSolutionSet, intervalRange, precision)
secondSolutionSet = [distractor3[1], distractor4[1]]
intervalOptionsSecondSet = createIntervalOptions(secondSolutionSet, intervalRange, precision)
if(solutionLength == 0):
    distractor1Interval = intervalToString(intervalOptionsFirstSet[0])
    distractor1Interval.append('This corresponds to not checking that the potential solution $x = %.3f$ leads to a complex value in the original equation.' %solution)
else:
    solutionInterval = intervalToString(intervalOptionsFirstSet[0])
    solutionInterval.append('* $x = %.3f$, which is the correct option.' %solution)
distractor2Interval = intervalToString(intervalOptionsFirstSet[1])
distractor3Interval = stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[2], intervalOptionsSecondSet[0])
distractor4Interval = stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[3], intervalOptionsSecondSet[1])

distractor2Interval.append('$x = %.3f$, which corresponds to squaring each square root separately and assigning the negative to the third term.' %distractor2)
distractor3Interval.append('$x = %.3f$ and $x = %.3f$, which corresponds to solving the equation correctly and including the value that makes the first square root 0.' %(distractor3[0], distractor3[1]))
distractor4Interval.append('$x = %.3f$ and $x = %.3f$, which corresponds to solving each radical separately for 0.' %(distractor4[0], distractor4[1]))
#
# Assigns 1 to the solution.
solutionInterval.append(1)
distractor1Interval.append(0)
distractor2Interval.append(0)
distractor3Interval.append(0)
distractor4Interval.append(0)
#
answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

c0 = answerList[0][0]
c1 = answerList[1][0]
c2 = answerList[2][0]
c3 = answerList[3][0]
c4 = answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

generalComment = "General Comments: Distractors are different based on the number of solutions. For example, if the question is designed to have 0 options, then the distractors are solving the equation and not checking that the solution leads to complex numbers (because plugging them in makes the value under the square root negative). Remember that after solving, we need to make sure our solution does not make the original equation take the square root of a negative number!"

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
