# Module 1 - Real & Complex Numbers
# Objective - Multiply two complex numbers.

### DEFINITIONS ###
def generateProblemCoefficients():
    listIntegers = range(2, 11)
    constants = random.sample(listIntegers, 4)
    constants = [maybeMakeNegative(i) for i in constants]
    a1, b1, a2, b2 = constants
    while (a1*b2 + b1*a2) == 0:
        constants = random.sample(listIntegers, 4)
        constants = [maybeMakeNegative(i) for i in constants]
        a1, b1, a2, b2 = constants
    return constants
def generateSolutionAndDistractors(coefficients):
    a1, b1, a2, b2 = coefficients
    complex1 = complex(a1, b1)
    complex2 = complex(a2, b2)
    product = complex1*complex2
    solution = [int(product.real), int(product.imag)]
    distractor1Product = complex(a1, -b1)*complex(a2, b2)
    distractor1 = [int(distractor1Product.real), int(distractor1Product.imag)]
    distractor2Product = complex(a1, b1)*complex(a2, -b2)
    distractor2 = [int(distractor2Product.real), int(distractor2Product.imag)]
    distractor3Product = complex(a1, -b1)*complex(a2, -b2)
    distractor3 = [int(distractor3Product.real), int(distractor3Product.imag)]
    distractor4Product = complex(a1*a2, b1*b2)
    distractor4 = [distractor4Product.real, distractor4Product.imag]
    return [solution, distractor1, distractor2, distractor3, distractor4]

### VARIABLE DECLARATIONS ###
problemCoefficients = generateProblemCoefficients()
solutionList = generateSolutionAndDistractors(problemCoefficients)

### CREATE INTERVAL OPTIONS ###
intervalOptions = createIntervalOptions(solutionList, 5, 1)

### DEFINE ANSWER LIST, DISPLAY SOLUTION, DISPLAY DISTRACTORS ###
displaySolution = displayComplexFactor(solutionList[0])
c0 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[0][0][0], intervalOptions[0][0][1], intervalOptions[0][1][0], intervalOptions[0][1][1])
c1 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[1][0][0], intervalOptions[1][0][1], intervalOptions[1][1][0], intervalOptions[1][1][1])
c2 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[2][0][0], intervalOptions[2][0][1], intervalOptions[2][1][0], intervalOptions[2][1][1])
c3 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[3][0][0], intervalOptions[3][0][1], intervalOptions[3][1][0], intervalOptions[3][1][1])
c4 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[4][0][0], intervalOptions[4][0][1], intervalOptions[4][1][0], intervalOptions[4][1][1])

solutionInterval = [c0, "* $%s$, which is the correct option." %displaySolution, 1]
distractor1Interval = [c1, " $%s$, which corresponds to adding a minus sign in the first term." %displayComplexFactor(solutionList[1]), 0]
distractor2Interval = [c2, " $%s$, which corresponds to adding a minus sign in the second term." %displayComplexFactor(solutionList[2]), 0]
distractor3Interval = [c3, " $%s$, which corresponds to adding a minus sign in both terms." %displayComplexFactor(solutionList[3]), 0]
distractor4Interval = [c4, " $%s$, which corresponds to just multiplying the real terms to get the real part of the solution and the coefficients in the complex terms to get the complex part."%displayComplexFactor(solutionList[4]), 0]

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
displayStem = 'Simplify the expression below into the form $a+bi$. Then, choose the intervals that $a$ and $b$ belong to.'
displayProblem = "(%s)(%s)" %(displayComplexFactor([problemCoefficients[0], problemCoefficients[1]]), displayComplexFactor([problemCoefficients[2], problemCoefficients[3]]))
generalComment = "You can treat $i$ as a variable and distribute. Just remember that $i^2=-1$, so you can continue to reduce after you distribute."

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)

### DEFINE XRONOS VARIABLES ###
xronosSolution = solutionList[0]
xronosDistractors = [solutionList[1], solutionList[2], solutionList[3], solutionList[4]]
displayXronosStem = "Simplify the expression below into the form $a+bi$."
xronosHint="You can treat $i$ as a variable and distribute. Just remember that $i^2=-1$, so you can continue to reduce after you distribute."

### WRITE TO KEY ###
writeToKey(HWorEXAM, keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
