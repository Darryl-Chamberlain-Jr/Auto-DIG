# Module 2 - Linear Functions
# Objective - Solve linear functions with rational coefficients
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
    if math.gcd(set[0], divisors[0]) > 1 or math.gcd(set[1], divisors[1]) > 1 or math.gcd(set[2], divisors[2]) > 1:
        setDivisible = 1
    else:
        setDivisible = 0
    return setDivisible
def createViableConstants():
    OneSolutionCheck = 0
    firstDivisible = 0
    secondDivisible = 0
    firstOrSecondDivisible = random.randint(0, 1)
    if firstOrSecondDivisible == 0:
        while (OneSolutionCheck == 0) or (firstDivisible == 0) or (secondDivisible==1):
            a, b, c = createThreeRandomIntegers() #in numerator factor, coefficient for x
            d, e, f = createThreeRandomIntegers() #in numerator factor, coefficient for x^0
            g, h, i = createThreeDistinctRandomNaturals() # denominators
            OneSolutionCheck = float(a/g) - float(b/h) - float(c/i) # checks that coefficients for x do not cancel to 0 and lead to infinitely many solutions
            firstDivisible = checkDivisibility([a,b,c], [g,h,i])
            secondDivisible = checkDivisibility([d,e,f], [g,h,i])
    else:
        while (OneSolutionCheck == 0) or (firstDivisible == 1) or (secondDivisible==0):
            a, b, c = createThreeRandomIntegers() #in numerator factor, coefficient for x
            d, e, f = createThreeRandomIntegers() #in numerator factor, coefficient for x^0
            g, h, i = createThreeDistinctRandomNaturals() # denominators
            OneSolutionCheck = float(a/g) - float(b/h) - float(c/i) # checks that coefficients for x do not cancel to 0 and lead to infinitely many solutions
            firstDivisible = checkDivisibility([a,b,c], [g,h,i])
            secondDivisible = checkDivisibility([d,e,f], [g,h,i])
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
    return solution[0]
def generateDistractors(constants):
    a, b, c, d, e, f, g, h, i = constants
    distractor1 = createSolution([a, b, c, d, -e, f, g, h, i]) # Student does not distribute negative in front of second fraction
    distractor2 = createSolution([a, b, c, g*d, h*e, i*f, g, h, i]) # Student divides x coefficients only
    distractor3 = createSolution([g*a, h*b, i*c, d, e, f, g, h, i]) # Student divides x^0 coefficients only
    return [distractor1, distractor2, distractor3]
### VARIABLE DECLARATIONS ###
solutionList = [0, 0, 0, 0]
while findMinDiff(solutionList) < 1 or numpy.prod(solutionList) == 0: # ensures solution/distractors are large enough so intervals are easier to read AND that all distractors lead to a solution
    constants = createViableConstants()
    solution = createSolution(constants)
    distractor1, distractor2, distractor3 = generateDistractors(constants)
    solutionList = [solution, distractor1, distractor2, distractor3]
intervalOptions = createIntervalOptions(solutionList, 3, 1)
### DEFINE ANSWER LIST AND DISPLAY SOLUTION ###
displaySolution = "x = %.3f" %solution
option1 = ["x \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1]), "* $x = %.3f$, which is the correct option." %solution, 1]
option2 = ["x \\in [%s, %s]" %(intervalOptions[1][0], intervalOptions[1][1]), " $x = %.3f$, which corresponds to not distributing the negative in front of the second fraction." %distractor1, 0]
option3 = ["x \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1]), " $x = %.3f$, which corresponds to dividing the coefficients in front of x by the denominator rather than dividing BOTH parts of the numerator by the denominator (or removing the fractions through multiplication)." %distractor2, 0]
option4 = ["x \\in [%s, %s]" %(intervalOptions[3][0], intervalOptions[3][1]), " $x = %.3f$, which corresponds to dividing the second number in the numerator by the denominator rather than dividing BOTH parts of the numerator by the denominator (or removing the fractions through multiplication)." %distractor3, 0]
option5 = ["\\text{There are no real solutions.}", "Corresponds to students thinking a fraction means there is no solution to the equation.", 0]
answerList = [option1, option2, option3, option4]
random.shuffle(answerList)
answerList.append(option5)
### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)
### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
displayStem = 'Solve the linear equation below. Then, choose the interval that contains the solution.'
displayProblem = "\\frac{%s}{%s} - \\frac{%s}{%s} = \\frac{%s}{%s}" %(generatePolynomialDisplay(  [constants[0], constants[3]]  ), constants[6], generatePolynomialDisplay(  [constants[1], constants[4]]  ), constants[7], generatePolynomialDisplay(  [constants[2], constants[5]]  ), constants[8]    )
generalComment = "If you are having trouble with this problem, try to remove a fraction at a time by multiplying each term by the denominator."
### WRITE TO KEY ###
writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
