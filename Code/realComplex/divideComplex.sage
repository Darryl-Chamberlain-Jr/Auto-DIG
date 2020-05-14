def generateProblem():
    listIntegers = [i for i in range(1, 7)]
    constants = random.sample(listIntegers, 4)
    constants = [maybeMakeNegative(i) for i in constants]
    return constants
def generateSolution(complex1, complex2):
    quotient = complex1/complex2
    return [quotient.real, quotient.imag]
def generateSolutionIntervals(solution, intervalRange):
    intervalList = [[]]*len(solution)
    for i in range(0, len(solution)):
        intervalList[i] = createInterval(solution[i], intervalRange)
    return intervalList

def generateDistractors(problem):
    a1, b1, a2, b2 = problem
    #Divide like terms
    distractor1 = [float(a1/a2), float(b1/b2)]

    # Multiply by non-conjugate and treat like conjugate in denominator
    numeratorD2 = complex(a1, b1) * complex(a2, b2)
    denominatorD2 = complex(a2, b2) * complex(a2, -b2)
    quotientD2 = numeratorD2/denominatorD2.real
    distractor2 = [quotientD2.real, quotientD2.imag]

    # Multiply by conjugate, only divide first term
    numeratorD3 = complex(a1, b1) * complex(a2, -b2)
    denominatorD3 = complex(a2, b2) * complex(a2, -b2)
    realTermD3 = float(numeratorD3.real / denominatorD3.real)
    imagTermD3 = float(numeratorD3.imag)
    distractor3 = [realTermD3, imagTermD3]

    # Multiply by conjugate, only divide second term
    numeratorD4 = complex(a1, b1) * complex(a2, -b2)
    denominatorD4 = complex(a2, b2) * complex(a2, -b2)
    realTermD4 = float(numeratorD4.real)
    imagTermD4 = float(numeratorD4.imag / denominatorD4.real)
    distractor4 = [realTermD4, imagTermD4]

    return [distractor1, distractor2, distractor3, distractor4]

def displayComplexFloat(problem):
    a, b = problem
    if b < 0:
        if b == -1:
            display = "%.2f  - i" %a
        else:
            display = "%.2f  - %.2f i" %(a, -b)
    else:
        if b == 1:
            display = "%.2f + i" %a
        else:
            display = "%.2f  + %.2f i" %(a, b)
    return display

def displayComplex(problem):
    a, b = problem
    if b < 0:
        if b == -1:
            display = "%d  - i" %a
        else:
            display = "%d  - %d i" %(a, -b)
    else:
        if b == 1:
            display = "%d + i" %a
        else:
            display = "%d  + %d i" %(a, b)
    return display

intervalRange = 5
precision = 1
# OBJECTIVE 4 - Add/Subtract/Multiply/Divide Complex numbers.
# Two complex numbers will be generated, which we can ask students to multiply or divide.

problem = generateProblem()
a1, b1, a2, b2 = problem
a1 = 9 * a1
b1 = 11 * b1

#This is just to check if the two complex numbers are equal. SageTeX doesn't want to show it in this way.
complex1 = CC(a1, b1)
complex2 = CC(a2, b2)

while complex1 == complex2:
    problem = generateProblem()
    a1, b1, a2, b2 = problem
    a1 = 9 * a1
    b1 = 11 * b1
    complex1 = CC(a1, b1)
    complex2 = CC(a2, b2)

solution = generateSolution(complex1, complex2)
coefficients = [a1, b1, a2, b2]

distractors = generateDistractors(coefficients)
solutionList = [solution, distractors[0], distractors[1], distractors[2], distractors[3]]
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

displaySolution = displayComplexFloat([solution[0], round(solution[1], 2)])
displayDistractor1 = displayComplexFloat([distractors[0][0], distractors[0][1]])
displayDistractor2 = displayComplexFloat([distractors[1][0], distractors[1][1]])
displayDistractor3 = displayComplexFloat([distractors[2][0], distractors[2][1]])
displayDistractor4 = displayComplexFloat([distractors[3][0], distractors[3][1]])

solutionInterval = [intervalOptions[0], "* $%s$, which is the correct option." %displaySolution, 1]
distractor1Interval = [intervalOptions[1], " $%s$, which corresponds to just dividing the first term by the first term and the second by the second." %displayDistractor1, 0]
distractor2Interval = [intervalOptions[2], " $%s$, which corresponds to forgetting to multiply the conjugate by the numerator and not computing the conjugate correctly." %displayDistractor2, 0]
distractor3Interval = [intervalOptions[3], " $%s$, which corresponds to forgetting to multiply the conjugate by the numerator." %displayDistractor3, 0]
distractor4Interval = [intervalOptions[4], " $%s$, which corresponds to forgetting to multiply the conjugate by the numerator and using a plus instead of a minus in the denominator." %displayDistractor4, 0]

displayStem = 'Simplify the expression below into the form $a+bi$. Then, choose the intervals that $a$ and $b$ belong to.'
# This makes sure the problem displays correctly in LaTeX.
displayProblem = "\\frac{%s}{%s}" %(displayComplex([a1, b1]), displayComplex([a2, b2]))

generalComment = "General Comment: Multiply the numerator and denominator by the *conjugate* of the denominator, then simplify. For example, if we have $2+3i$, the conjugate is $2-3i$."

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

c0 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[0][0][0][0], answerList[0][0][0][1], answerList[0][0][1][0], answerList[0][0][1][1])
c1 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[1][0][0][0], answerList[1][0][0][1], answerList[1][0][1][0], answerList[1][0][1][1])
c2 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[2][0][0][0], answerList[2][0][0][1], answerList[2][0][1][0], answerList[2][0][1][1])
c3 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0][0][0], answerList[3][0][0][1], answerList[3][0][1][0], answerList[3][0][1][1])
c4 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[4][0][0][0], answerList[4][0][0][1], answerList[4][0][1][0], answerList[4][0][1][1])
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
