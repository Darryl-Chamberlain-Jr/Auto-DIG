# Module 6 - Polynomial Functions
# Objective: Construct a lowest-degree polynomial given the roots.

### DEFINITIONS ###
def generateSolutionAndDistractors(complexZero, realZero):
    a, b = complexZero
    k = realZero
    solution = [1, -2*a-k, a**2+b**2 + 2*a*k, (a**2+b**2)*(-k)]
    distractor1 = [1, 2*a+k, a**2+b**2 + 2*a*k, (a**2+b**2)*k] # Distractor 1: This distractor corresponds to using (x+z) for zeros.
    distractor2 = [1, 1, -a-k, a*k] # Distractor 2: This distractor corresponds to using a from the complex and the other zero to make a quadratic.
    distractor3 = [1, 1, -b-k, b*k] # Distractor 3: This distractor corresponds to using b from the complex and the other zero to make a quadratic.
    return [solution, distractor1, distractor2, distractor3]

### VARIABLE DECLARATIONS ###
realZero = maybeMakeNegative(random.randint(1, 4))
complexZero = [0, 0]
while (complexZero[0] == complexZero[1]):
    complexZero = [maybeMakeNegative(random.randint(2, 5)), maybeMakeNegative(random.randint(2, 5))]
displayZero1 = displayComplexFactor(complexZero)
displayZero1Conjugate = displayComplexFactor([complexZero[0], -complexZero[1]])
displayZero2 = realZero

### CREATE INTERVAL OPTIONS ###
solution, distractor1, distractor2, distractor3 = generateSolutionAndDistractors(complexZero, realZero)
solutionList = [solution, distractor1, distractor2, distractor3]
intervalOptions = createIntervalOptions(solutionList, 6, 1)

### DEFINE ANSWERLIIST AND DISPLAYSOLUTION ###
c0 = "b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(intervalOptions[0][1][0], intervalOptions[0][1][1], intervalOptions[0][2][0], intervalOptions[0][2][1], intervalOptions[0][3][0], intervalOptions[0][3][1])
c1 = "b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(intervalOptions[1][1][0], intervalOptions[1][1][1], intervalOptions[1][2][0], intervalOptions[1][2][1], intervalOptions[1][3][0], intervalOptions[1][3][1])
c2 = "b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(intervalOptions[2][1][0], intervalOptions[2][1][1], intervalOptions[2][2][0], intervalOptions[2][2][1], intervalOptions[2][3][0], intervalOptions[2][3][1])
c3 = "b \\in [%s, %s], c \\in [%s, %s], \\text{ and } d \\in [%s, %s]" %(intervalOptions[3][1][0], intervalOptions[3][1][1], intervalOptions[3][2][0], intervalOptions[3][2][1], intervalOptions[3][3][0], intervalOptions[3][3][1])
c4 = "\\text{None of the above.}"
displaySolution = generatePolynomialDisplay(solution)
solutionInterval = [c0, "* $%s$, which is the correct option." %displaySolution, 1]
distractor1Interval = [c1, "$%s$, which corresponds to multiplying out $(x-(%s))(x-(%s))(%s)$." %(generatePolynomialDisplay(distractor1), displayZero1, displayZero1Conjugate, generatePolynomialDisplay([1, realZero])), 0]
distractor2Interval = [c2, "$%s$, which corresponds to multiplying out $(%s)(%s)$." %(generatePolynomialDisplay(distractor2), generatePolynomialDisplay([1, -complexZero[0]]), generatePolynomialDisplay([1, -realZero])), 0]
distractor3Interval = [c3, "$%s$, which corresponds to multiplying out $(%s)(%s)$." %(generatePolynomialDisplay(distractor3), generatePolynomialDisplay([1, -complexZero[1]]), generatePolynomialDisplay([1, -realZero])), 0]
distractor4Interval = [c4, "This corresponds to making an unanticipated error or not understanding how to use nonreal complex numbers to create the lowest-degree polynomial. If you chose this and are not sure what you did wrong, please contact the coordinator for help.", 0]

### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
displayStem = 'Construct the lowest-degree polynomial given the zeros below. Then, choose the intervals that contain the coefficients of the polynomial in the form $x^3+bx^2+cx+d$.'
displayProblem = '%s \\text{ and } %s' %(displayZero1, displayZero2)
generalComment = "Remember that the conjugate of $a+bi$ is $a-bi$. Since these zeros always come in pairs, we need to multiply out $(x-(%s))(x-(%s))(x-(%s))$." %(displayZero1, displayZero1Conjugate, displayZero2)

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)
answerList.append(distractor4Interval)
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)

### WRITE TO KEY ###
writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
