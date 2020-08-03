def generateSolution(complexZero, realZero):
    a, b = complexZero
    k = realZero
    c3 = 1
    c2 = -2*a-k
    c1 = a**2+b**2 + 2*a*k
    c0 = (a**2+b**2)*(-k)
    return [c3, c2, c1, c0]

def generateDistractors(complexZero, realZero):
    a, b = complexZero
    k = realZero
    # Distractor 1: This distractor corresponds to using (x+z) for zeros.
    a1 = 1
    b1 = 2*a+k
    c1 = a**2+b**2 + 2*a*k
    d1 = (a**2+b**2)*k
    distractor1 = [a1, b1, c1, d1]

    # Distractor 2: This distractor corresponds to using a from the complex and the other zero to make a quadratic.
    a2 = 1
    b2 = 1
    c2 = -a-k
    d2 = a*k
    distractor2 = [a2, b2, c2, d2]

    # Distractor 3: This distractor corresponds to using b from the complex and the other zero to make a quadratic.
    a3 = 1
    b3 = 1
    c3 = -b-k
    d3 = b*k
    distractor3 = [a3, b3, c3, d3]

    # Distractor 4: This distractor corresponds to negatives for each of the coefficients in the solution.
    #a4 = 1
    #b4 = 2*a+k
    #c4 = -a**2 - b**2 - 2*a*k
    #d4 = (a**2+b**2)*k
    #distractor4 = [a4, b4, c4, d4]
    return [distractor1, distractor2, distractor3]

intervalRange = 6
precision = 1

complexZero = [maybeMakeNegative(random.randint(2, 5)), maybeMakeNegative(random.randint(2, 5))]
realZero = maybeMakeNegative(random.randint(1, 4))

while (complexZero[0] == complexZero[1]):
    complexZero = [maybeMakeNegative(random.randint(2, 5)), maybeMakeNegative(random.randint(2, 5))]

if (complexZero[1]<0):
    displayZero1 = "%d - %di" %(complexZero[0], -complexZero[1])
    displayZero1Conjugate = "%d + %di" %(complexZero[0], -complexZero[1])
    displayZero2 = "%d" %realZero
else:
    displayZero1 = "%d + %di" %(complexZero[0], complexZero[1])
    displayZero1Conjugate = "%d - %di" %(complexZero[0], complexZero[1])
    displayZero2 = "%d" %realZero

solution = generateSolution(complexZero, realZero)
displaySolution = generatePolynomialDisplay(solution)

distractor1, distractor2, distractor3 = generateDistractors(complexZero, realZero)
solutionList = [solution, distractor1, distractor2, distractor3]

intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = [intervalOptions[0], "* $%s$, which is the correct option." %displaySolution, 1]
distractor1Interval = [intervalOptions[1], "$%s$, which corresponds to multiplying out $(x-(%s))(x-(%s))(%s)$." %(generatePolynomialDisplay(distractor1), displayZero1, displayZero1Conjugate, generatePolynomialDisplay([1, realZero])), 0]
distractor2Interval = [intervalOptions[2], "$%s$, which corresponds to multiplying out $(%s)(%s)$." %(generatePolynomialDisplay(distractor2), generatePolynomialDisplay([1, -complexZero[0]]), generatePolynomialDisplay([1, -realZero])), 0]
distractor3Interval = [intervalOptions[3], "$%s$, which corresponds to multiplying out $(%s)(%s)$." %(generatePolynomialDisplay(distractor3), generatePolynomialDisplay([1, -complexZero[1]]), generatePolynomialDisplay([1, -realZero])), 0]

displayStem = 'Construct the lowest-degree polynomial given the zeros below. Then, choose the intervals that contain the coefficients of the polynomial in the form $x^3+bx^2+cx+d$.'
displayProblem = '%s \\text{ and } %s' %(displayZero1, displayZero2)
generalComment = "Remember that the conjugate of $a+bi$ is $a-bi$. Since these zeros always come in pairs, we need to multiply out $(x-(%s))(x-(%s))(x-(%s))$." %(displayZero1, displayZero1Conjugate, displayZero2)

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)

c0 = "b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[0][0][1][0], answerList[0][0][1][1], answerList[0][0][2][0], answerList[0][0][2][1], answerList[0][0][3][0], answerList[0][0][3][1])
c1 = "b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[1][0][1][0], answerList[1][0][1][1], answerList[1][0][2][0], answerList[1][0][2][1], answerList[1][0][3][0], answerList[1][0][3][1])
c2 = "b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[2][0][1][0], answerList[2][0][1][1], answerList[2][0][2][0], answerList[2][0][2][1], answerList[2][0][3][0], answerList[2][0][3][1])
c3 = "b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(answerList[3][0][1][0], answerList[3][0][1][1], answerList[3][0][2][0], answerList[3][0][2][1], answerList[3][0][3][0], answerList[3][0][3][1])
c4 = "\\text{None of the above.}"
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], "This corresponds to making an unanticipated error or not understanding how to use nonreal complex numbers to create the lowest-degree polynomial. If you chose this and are not sure what you did wrong, please contact the coordinator for help."]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
