import sys
import random
from sympy.abc import x
from sympy.solvers import solve

DIR=sys.argv[1]
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
    OS_type=sys.argv[7]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

def generate1SolutionCoefficients():
    whichFactor = random.randint(0,1)
    if whichFactor == 0:
        b = random.randint(2, 3)
        c = random.randint(4, 7)
        while gcd(b, c) > 1:
            b = random.randint(2, 3)
            c = random.randint(4, 7)
        makeSameSign = maybeMakeNegative(1)
        a = random.randint(2, 3)
        d = makeSameSign * b * a* random.randint(2, 7)
        f = makeSameSign * b * random.randint(2, 7)
        e = maybeMakeNegative(random.randint(2, 7))
        g = (c*f)/b - (c*d)/(a*b)
        A = a*f-d
        B = a*g - b*e
        C = -c*e
        discriminant = B**2 - 4*A*C
        quadraticSolutions = solve(A*x**2+B*x+C)
        while (abs(g) > 10) or (discriminant < 0) or (len(quadraticSolutions) < 2):
            b = random.randint(2, 3)
            c = random.randint(4, 7)
            if gcd(b, c) > 1:
                b = random.randint(2, 3)
                c = random.randint(4, 7)
            makeSameSign = maybeMakeNegative(1)
            a = random.randint(2, 3)
            d = makeSameSign * b * a* random.randint(2, 7)
            f = makeSameSign * b * random.randint(2, 7)
            e = maybeMakeNegative(random.randint(2, 7))
            g = (c*f)/b - (c*d)/(a*b)
            A = a*f-d
            B = a*g - b*e
            C = -c*e
            discriminant = B**2 - 4*A*C
            quadraticSolutions = solve(A*x**2+B*x+C)
    else:
        f = random.randint(2, 7)
        g = maybeMakeNegative(random.randint(2, 7))
        while gcd(f, abs(g)) > 1:
            f = random.randint(2, 7)
            g = maybeMakeNegative(random.randint(2, 7))
        e = maybeMakeNegative(random.randint(2, 7))
        d = e * f * maybeMakeNegative(random.randint(2, 7))
        c = g * maybeMakeNegative(random.randint(2, 7))
        a = random.randint(2, 7)
        b = (d*g)/(e*f) + (c*f)/g
        A = a*f-d
        B = a*g - b*e
        C = -c*e
        discriminant = B**2 - 4*A*C
        quadraticSolutions = solve(A*x**2+B*x+C)
        while (discriminant) < 0 or (abs(b) > 10) or (len(quadraticSolutions) < 2):
            f = random.randint(2, 7)
            g = maybeMakeNegative(random.randint(2, 7))
            while gcd(f, abs(g)) > 1:
                f = random.randint(2, 7)
                g = maybeMakeNegative(random.randint(2, 7))
            e = maybeMakeNegative(random.randint(2, 7))
            d = e * f * maybeMakeNegative(random.randint(2, 7))
            c = g * maybeMakeNegative(random.randint(2, 7))
            a = random.randint(2, 7)
            b = (d*g)/(e*f) + (c*f)/g
            A = a*f-d
            B = a*g - b*e
            C = -c*e
            discriminant = B**2 - 4*A*C
            quadraticSolutions = solve(A*x**2+B*x+C)
    return [a, b, c, d, e, f, g]

def generateCoefficients(numberOfSolutions):
    a = maybeMakeNegative(random.randint(2, 7))
    b = maybeMakeNegative(random.randint(2, 7))
    c = maybeMakeNegative(random.randint(2, 7))
    d = -random.randint(2, 7)
    e = maybeMakeNegative(random.randint(2, 7))
    f = maybeMakeNegative(random.randint(2, 7))
    g = maybeMakeNegative(random.randint(2, 7))
    discrim = (a*g-e*b)**2 - 4*(a*f+d)*(-e*c)
    leadingCoefficient = a*f+d
    if (numberOfSolutions == 0):
        while (leadingCoefficient==0 or discrim >= 0):
            a = maybeMakeNegative(random.randint(2, 7))
            b = maybeMakeNegative(random.randint(2, 7))
            c = maybeMakeNegative(random.randint(2, 7))
            d = -random.randint(2, 7)
            e = maybeMakeNegative(random.randint(2, 7))
            f = maybeMakeNegative(random.randint(2, 7))
            g = maybeMakeNegative(random.randint(2, 7))
            discrim = (a*g-e*b)**2 - 4*(a*f+d)*(-e*c)
            leadingCoefficient = a*f+d
    elif (numberOfSolutions==1):
        a, b, c, d, e, f, g = generate1SolutionCoefficients()
    else:
        while (leadingCoefficient==0 or discrim <= 0):
            a = maybeMakeNegative(random.randint(2, 7))
            b = maybeMakeNegative(random.randint(2, 7))
            c = maybeMakeNegative(random.randint(2, 7))
            d = -random.randint(2, 7)
            e = maybeMakeNegative(random.randint(2, 7))
            f = maybeMakeNegative(random.randint(2, 7))
            g = maybeMakeNegative(random.randint(2, 7))
            discrim = (a*g-e*b)**2 - 4*(a*f+d)*(-e*c)
            leadingCoefficient = a*f+d
    return [a, b, c, d, e, f, g]

def generateSolution(coefficients):
    a, b, c, d, e, f, g = coefficients
    quadraticEquation = (a*x)/(b*x+c) + (d*x**2)/(b*f*x**2 + (b*g+c*f)*x+c*g) - e/(f*x+g)
    solution = solve(quadraticEquation)
    return solution

def generateSolution1Case(coefficients):
    a, b, c, d, e, f, g = coefficients
    potentialHoleSolution1 = float(-c)/float(b)
    potentialHoleSolution2 = float(-g)/float(f)
    A = a*f-d
    B = a*g - b*e
    C = -c*e
    quadraticSolutions = solve(A*x**2+B*x+C)
    if round(float(quadraticSolutions[0]), 3) == round(potentialHoleSolution1, 3):
        holeSolution = potentialHoleSolution1
        trueSolution = quadraticSolutions[1]
    elif round(float(quadraticSolutions[1]), 3) == round(potentialHoleSolution1, 3):
        holeSolution = potentialHoleSolution1
        trueSolution = quadraticSolutions[0]
    elif round(float(quadraticSolutions[0]), 3) == round(potentialHoleSolution2, 3):
        holeSolution = potentialHoleSolution2
        trueSolution = quadraticSolutions[1]
    else:
        holeSolution = potentialHoleSolution2
        trueSolution = quadraticSolutions[0]
    return [trueSolution, holeSolution, [A, B, C]]

def distractorDomainError1(coefficients):
    a, b, c, d, e, f, g = coefficients
    return float(-c)/float(b)

def distractorDomainError2(coefficients):
    a, b, c, d, e, f, g = coefficients
    return float(-g)/float(f)

def distractorAbsoluteValueForDiscriminant(coefficients):
    a, b, c, d, e, f, g = coefficients
    A = a*f-d
    B = a*g - b*e
    C = -c*e
    return [float((-B - sqrt(abs(B**2 - 4*A*C)))/(2*A)), float((-B + sqrt(abs(B**2 - 4*A*C)))/(2*A)), [A, B, C]]

def intervalToString(interval):
    return ['x \\in [%s,%s]' %(interval[0], interval[1])]

def stringForAnswersWithTwoIntervals(leftInterval, rightInterval):
    leftL, leftR = leftInterval
    rightL, rightR = rightInterval
    return ['x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s,%s]' %(leftL, leftR, rightL, rightR)]

intervalRange = 6
#numberOfSolutions = random.randint(0, 2)
numberOfSolutions = 2
coefficients = generateCoefficients(numberOfSolutions)

factorNumerator1 = generatePolynomialDisplay([coefficients[0], 0])
factorDenominator1 = generatePolynomialDisplay([coefficients[1], coefficients[2]])
firstTerm = "\\frac{%s}{%s}" %(factorNumerator1, factorDenominator1)
factorNumerator2 = generatePolynomialDisplay([coefficients[3], 0, 0])
factorDenominator2 = generatePolynomialDisplay( [coefficients[1]*coefficients[5], coefficients[1]*coefficients[6]+coefficients[2]*coefficients[5], coefficients[2]*coefficients[6]] )
secondTerm = "\\frac{%s}{%s}" %(factorNumerator2, factorDenominator2)
factorNumerator3 = coefficients[4]
factorDenominator3 = generatePolynomialDisplay([coefficients[5], coefficients[6]])
thirdTerm = "\\frac{%s}{%s}" %(factorNumerator3, factorDenominator3)

if (numberOfSolutions==0):
    solution = '\\text{All solutions are invalid or lead to complex values in the equation.}'
    displaySolution = solution
    complexSolutions = distractorAbsoluteValueForDiscriminant(coefficients)
    solutionInterval = [['\\text{All solutions lead to invalid or complex values in the equation.}'], "* The equation leads to solving $%s=0$, which leads to complex solutions. This is the correct option." %generatePolynomialDisplay(complexSolutions[2]), 1]
    distractor1 = float(distractorDomainError1(coefficients))
    distractor2 = float(distractorDomainError2(coefficients))
    distractor3 = [float(distractorDomainError1(coefficients)), float(distractorDomainError2(coefficients))]
    distractor4 = complexSolutions
    firstSolutionSet = [distractor1, distractor2, distractor3[0], distractor4[0]]

    precision = 1
    intervalOptionsFirstSet = createIntervalOptions(firstSolutionSet, intervalRange, precision)
    secondSolutionSet = [distractor3[1], distractor4[1]]
    intervalOptionsSecondSet = createIntervalOptions(secondSolutionSet, intervalRange, precision)

    distractor1Interval = [intervalToString(intervalOptionsFirstSet[0]), "$x = %.3f$, which corresponds to solving $%s = 0$ and treating it as a solution to the equation." %(distractor1, factorDenominator1), 0]
    distractor2Interval = [intervalToString(intervalOptionsFirstSet[1]), "$x = %.3f$, which corresponds to solving $%s = 0$ and treating it as a solution to the equation." %(distractor2, factorDenominator3), 0]
    distractor3Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[2], intervalOptionsSecondSet[0]), "$x = %.3f \\text{ and } x = %.3f$, which corresponds to solving $%s = 0$ and $%s = 0$ and treating them as solutions to the equation." %(distractor3[0], distractor3[1], factorDenominator1, factorDenominator3), 0]
    distractor4Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[3], intervalOptionsSecondSet[1]), "$x = %.3f \\text{ and } x = %.3f$, which corresponds to making the discriminant from the Quadratic Formula positive to avoid complex solutions." %(distractor4[0], distractor4[1]), 0]

elif (numberOfSolutions==1):
    trueSolution, holeSolution, quadraticCoefficients = generateSolution1Case(coefficients)
    if holeSolution == float(distractorDomainError1(coefficients)):
        distractorHole = float(distractorDomainError2(coefficients))
    else:
        distractorHole = float(distractorDomainError1(coefficients))
    displaySolution = "x = %.3f \\text{ and \\textbf{NOT} } x = %.3f" %(trueSolution, holeSolution)
    distractor2 = holeSolution
    distractor3 = [min(trueSolution, holeSolution), max(trueSolution, holeSolution)]
    distractor4 = [min(trueSolution, distractorHole), max(trueSolution, distractorHole)]

    firstSolutionSet = [trueSolution, distractor2, distractor3[0], distractor4[0]]
    precision = 1
    intervalOptionsFirstSet = createIntervalOptions(firstSolutionSet, intervalRange, precision)
    secondSolutionSet = [distractor3[1], distractor4[1]]
    intervalOptionsSecondSet = createIntervalOptions(secondSolutionSet, intervalRange, precision)

    solutionInterval = [intervalToString(intervalOptionsFirstSet[0]), "* $x = %.3f$ is a solution and $x = %.3f$ is not a solution, which is the correct option." %(trueSolution, holeSolution), 1]
    distractor1Interval = [['\\text{All solutions lead to invalid or complex values in the equation.}'], "This corresponds to either getting a negative discriminant when trying to solve $%s=0$ or finding that one solution is not valid and thus thinking both solutions are not valid." %generatePolynomialDisplay(quadraticCoefficients), 0]
    distractor2Interval = [intervalToString(intervalOptionsFirstSet[1]), "$x = %.3f$ is a solution and $x = %.3f$ is not a solution, which throws out the good solution and keeps the solution that divides by 0 in the original equation." %(holeSolution, trueSolution), 0]
    distractor3Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[2], intervalOptionsSecondSet[0]), "$x = %.3f$ and $x = %.3f$ are solutions, which corresponds to not checking if your solutions lead to invalid values (dividing by zero) in the original equation." %(distractor3[0], distractor3[1]), 0]
    distractor4Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[3], intervalOptionsSecondSet[1]), "$x = %.3f$ and $x = %.3f$ are solutions, which corresponds to solving the equation correctly for $x = %.3f$, but including the other invalid value in the original equation." %(distractor4[0], distractor4[1], trueSolution), 0]

elif (numberOfSolutions==2):
    exactSolution = generateSolution(coefficients)
    solution = [round(float(generateSolution(coefficients)[0]), 3),  round(float(generateSolution(coefficients)[1]), 3)]
    displaySolution = "\\text{There are two solutions: } x = %.3f \\text{ and } x = %.3f" %(solution[0], solution[1])
    distractor1 = float(distractorDomainError2(coefficients))
    distractor2 = float(solution[1])
    distractor3 = [float(solution[0]), float(distractorDomainError1(coefficients))]
    firstSolutionSet = [float(solution[0]), distractor1, distractor2, distractor3[0]]
    precision = 1
    intervalOptionsFirstSet = createIntervalOptions(firstSolutionSet, intervalRange, precision)
    secondSolutionSet = [float(solution[1]), distractor3[1]]
    intervalOptionsSecondSet = createIntervalOptions(secondSolutionSet, intervalRange, precision)

    solutionInterval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[0], intervalOptionsSecondSet[0]), "* $x = %.3f \\text{ and } x = %.3f$, which is the correct option." %(solution[0], solution[1]), 1]
    distractor1Interval = [intervalToString(intervalOptionsFirstSet[1]), "", 0]
    distractor2Interval = [intervalToString(intervalOptionsFirstSet[2]), "", 0]
    distractor3Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[3], intervalOptionsSecondSet[1]), "", 0]
    distractor4Interval = [["\\text{All solutions lead to invalid or complex values in the equation.}"], "", 0]
#else:
#    print("Something went wrong, please try again.")
displayStem = 'Solve the rational equation below. Then, choose the interval(s) that the solution(s) belongs to.'
displayProblem = '%s + %s = %s' %(firstTerm, secondTerm, thirdTerm)
generalComment = "Distractors are different based on the number of solutions. Remember that after solving, we need to make sure our solution does not make the original equation divide by zero!"

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

choices = [answerList[0][0][0], answerList[1][0][0], answerList[2][0][0], answerList[3][0][0], answerList[4][0][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
