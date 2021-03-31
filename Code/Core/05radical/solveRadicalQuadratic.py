import sys
import random
import numpy
from math import gcd

DIR=sys.argv[1]
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
    OS_type=sys.argv[7]
    response_type=sys.argv[8]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

def smallerFirst(twoValuesToCompare):
    if twoValuesToCompare[0] < twoValuesToCompare[1]:
        return twoValuesToCompare
    else:
        return [twoValuesToCompare[1], twoValuesToCompare[0]]

def radicalCheck(coefficients):
    a, b, c, d = coefficients
    eq1 = numpy.poly1d([a, b])
    eq2 = numpy.poly1d([c, d])
    equation_to_solve=eq1*eq2
    solution = equation_to_solve.r
    if len(solution) == 0:
        return [0, 0, 0, 0]
    else:
        # radical 1 = a*c*x**2+b*d
        if (a*c*solution[0]**2+b*d < 0):
            r0SolutionA = 0
        else:
            r0SolutionA = 1
        #radical 2 = -(a*d+b*c)*x
        if (-(a*d+b*c)*solution[0] < 0):
            r0SolutionB = 0
        else:
            r0SolutionB = 1
        #################################
        if (a*c*solution[1]**2+b*d < 0):
            r1SolutionA = 0
        else:
            r1SolutionA = 1
        if (-(a*d+b*c)*solution[1] < 0):
            r1SolutionB = 0
        else:
            r1SolutionB = 1
        return [r0SolutionA, r0SolutionB, r1SolutionA, r1SolutionB]

def generateCoefficients(numberOfSolutions):
    # Converted to Quadratic Equation = (a*x+b)*(c*x+d)
    # a*c*x**2+(a*d+b*c)*x+bd
    # Force a fail so numbers are generated below.
    checkDiscriminant = 0
    check = [0, 0, 0, 0]
    #
    if (numberOfSolutions==0):
        # Makes sure each solution fails at least one of the radicals
        while (check[0]*check[1]+check[2]*check[3] > 0) or (checkDiscriminant<=0) or (gcd(gcd(a, c), gcd(b, d)) > 1):
            a = maybeMakeNegative(random.randint(2, 9))
            b = maybeMakeNegative(random.randint(2, 9))
            c = maybeMakeNegative(random.randint(2, 9))
            d = maybeMakeNegative(random.randint(2, 9))
            check = radicalCheck([a, b, c, d])
            checkDiscriminant = float((a*d+b*c)**2 - 4*a*c*b*d)
    elif (numberOfSolutions==1):
        while (check[0]*check[1]+check[2]*check[3] !=1) or (checkDiscriminant<=0) or (gcd(gcd(a, c), gcd(b, d)) > 1):
            a = maybeMakeNegative(random.randint(2, 9))
            b = maybeMakeNegative(random.randint(2, 9))
            c = maybeMakeNegative(random.randint(2, 9))
            d = maybeMakeNegative(random.randint(2, 9))
            check = radicalCheck([a, b, c, d])
            checkDiscriminant = float((a*d+b*c)**2 - 4*a*c*b*d)
    else:
        while (check[0]*check[1]+check[2]*check[3] < 2) or (checkDiscriminant<=0) or (gcd(gcd(a, c), gcd(b, d)) > 1):
            a = maybeMakeNegative(random.randint(2, 9))
            b = maybeMakeNegative(random.randint(2, 9))
            c = maybeMakeNegative(random.randint(2, 9))
            d = maybeMakeNegative(random.randint(2, 9))
            check = radicalCheck([a, b, c, d])
            checkDiscriminant = float((a*d+b*c)**2 - 4*a*c*b*d)
    return [a, b, c, d]

def generateSolutionToQuadratic(coefficients):
    a, b, c, d = coefficients
    eq1 = numpy.poly1d([a, b])
    eq2 = numpy.poly1d([c, d])
    equation_to_solve=eq1*eq2
    solution = equation_to_solve.r
    return [min(solution[0], solution[1]), max(solution[0], solution[1])]

def intervalToString(interval):
    return 'x \\in [%s,%s]' %(interval[0], interval[1])

def stringForAnswersWithTwoIntervals(leftInterval, rightInterval):
    leftL, leftR = leftInterval
    rightL, rightR = rightInterval
    return 'x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s,%s]' %(leftL, leftR, rightL, rightR)

# Options
    # There should always be a 'There is no solution to the equation.'
    # Two with a single solution
        # One of the solutions from (a*x+b)*(c*x+d)
        # The other solution from (a*x+b)*(c*x+d)
    # Two with two solutions
        # Both solutions to the quadratic (a*x+b)*(c*x+d)
        # Solutions to the equation (a*x+b)*(-c*x-d)

intervalRange=4
numberOfSolutions = random.randint(0, 2)
coefficients = generateCoefficients(numberOfSolutions)

if coefficients[1]*coefficients[3] < 0:
    displayFactor1 = "%d x^2 - %d" %(coefficients[0]*coefficients[2], -coefficients[1]*coefficients[3])
else:
    displayFactor1 = "%d x^2 + %d" %(coefficients[0]*coefficients[2], coefficients[1]*coefficients[3])
displayFactor2 = "%d x" %(-(coefficients[0]*coefficients[3] + coefficients[1]*coefficients[2]))

# Different cases for each number of solutions
if (numberOfSolutions==0):
    badSolution = generateSolutionToQuadratic(coefficients)
    solutionInterval = ['\\text{All solutions lead to invalid or complex values in the equation.}', "* This is the correct option.", 1]
    #
    distractor1 = badSolution[0]
    distractor2 = badSolution[1]
    distractor3 = badSolution
    if (abs(badSolution[0])==badSolution[0] and abs(badSolution[1])==badSolution[1] ):
        distractor4 = [-badSolution[0], -badSolution[1]]
    else:
        distractor4 = [abs(badSolution[0]), abs(badSolution[1])]
    #
    firstSolutionSet = [distractor1, distractor2, distractor3[0], distractor4[0]]
    precision = 1
    intervalOptionsFirstSet = createIntervalOptions(firstSolutionSet, intervalRange, precision)
    secondSolutionSet = [distractor3[1], distractor4[1]]
    intervalOptionsSecondSet = createIntervalOptions(secondSolutionSet, intervalRange, precision)
    distractor1Interval = [intervalToString(intervalOptionsFirstSet[0]), "$x = %.3f$, which corresponds to not checking that this value makes at least one of the radicands negative." %badSolution[0], 0]
    distractor2Interval = [intervalToString(intervalOptionsFirstSet[1]), "$x = %.3f$, which corresponds to not checking that this value makes at least one of the radicands negative." %badSolution[1], 0]
    distractor3Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[2], intervalOptionsSecondSet[0]), "$x = %.3f \\text{ and } x = %.3f$, which corresponds to not checking that BOTH values make at least one of the radicands negative." %(badSolution[0], badSolution[1]), 0]
    distractor4Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[3], intervalOptionsSecondSet[1]), "$x = %.3f \\text{ and } x = %.3f$, which corresponds to getting the negatives of the values that make the equation 0." %(distractor4[0], distractor4[1]), 0]
    displaySolution = '\\text{all potential solutions lead to complex values in the equation.}'
elif (numberOfSolutions==1):
    # Radical Check: Checks if the solution is allowed in the first (0) and second (1) radical
    # [r0SolutionA, r0SolutionB, r1SolutionA, r1SolutionB]
    findZeros = radicalCheck(coefficients)
    if (findZeros[0]*findZeros[1]==0): # This means the first zero failed at least one of the radicals
        solutionToQuadratic = generateSolutionToQuadratic(coefficients)
        solution = solutionToQuadratic[1] # Thus the one solution must be the other zero.
        distractor1 = solutionToQuadratic[0]
    else:
        solutionToQuadratic = generateSolutionToQuadratic(coefficients) # If it didn't fail, then it is the correct zero.
        solution = solutionToQuadratic[0]
        distractor1 = solutionToQuadratic[1]
    #
    badValuesSorted = smallerFirst(solutionToQuadratic)
    distractor3 = badValuesSorted
    badSolution = badValuesSorted
    if (abs(badSolution[0])==badSolution[0] and abs(badSolution[1])==badSolution[1] ):
        distractor4 = smallerFirst([-badSolution[0], -badSolution[1]])
    else:
        distractor4 = smallerFirst([abs(badSolution[0]), abs(badSolution[1])])
    distractor2Interval = ['\\text{All solutions lead to invalid or complex values in the equation.}', "This corresponds to believing both $x = %.3f \\text{ and } x = %.3f$ both lead to complex values." %(badValuesSorted[0], badValuesSorted[1]), 0]
    firstSolutionSet = [solution, distractor1, distractor3[0], distractor4[0]]
    precision = 1
    intervalOptionsFirstSet = createIntervalOptions(firstSolutionSet, intervalRange, precision)
    secondSolutionSet = [distractor3[1], distractor4[1]]
    intervalOptionsSecondSet = createIntervalOptions(secondSolutionSet, intervalRange, precision)
    solutionInterval = [intervalToString(intervalOptionsFirstSet[0]), "* This is the correct option.", 1]
    distractor1Interval = [intervalToString(intervalOptionsFirstSet[1]), "$x = %.3f$, which corresponds to thinking this value does not make either radicand negative AND the value $x = %.3f$ does." %(distractor1, solution), 0]
    distractor3Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[2], intervalOptionsSecondSet[0]), "$x = %.3f \\text{ and } x = %.3f$, which corresponds to not checking that $x = %.3f$ leads to a negative in at least one of the radicands." %(distractor3[0], distractor3[1], distractor1), 0]
    distractor4Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[3], intervalOptionsSecondSet[1]), "$x = %.3f \\text{ and } x = %.3f$, which corresponds to negatives or the absolute value of the values you would have gotten by solving the equation correctly." %(distractor4[0], distractor4[1]), 0]
    displaySolution = '\\text{that there is one solution and it is } x = %.3f.' %solution
else:
    solution = generateSolutionToQuadratic(coefficients)
    #
    distractor1 = solution[0]
    distractor2 = solution[1]
    if (abs(solution[0])==solution[0] and abs(solution[1])==solution[1] ):
        distractor3 = smallerFirst([-solution[0], -solution[1]])
    else:
        distractor3 = smallerFirst([abs(solution[0]), abs(solution[1])])
    #
    firstSolutionSet = [solution[0], distractor1, distractor2, distractor3[0]]
    precision = 1
    intervalOptionsFirstSet = createIntervalOptions(firstSolutionSet, intervalRange, precision)
    secondSolutionSet = [solution[1], distractor3[1]]
    intervalOptionsSecondSet = createIntervalOptions(secondSolutionSet, intervalRange, precision)
    solutionInterval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[0], intervalOptionsSecondSet[0]), "* $x = %.3f \\text{ and } x = %.3f$, which is the correct option." %(solution[0], solution[1]), 1]
    distractor1Interval = [intervalToString(intervalOptionsFirstSet[1]), "$x = %.3f$, which corresponds to thinking that $x = %.3f$ leads to a negative in at least one of the radicands." %(distractor1, distractor2), 0]
    distractor2Interval = [intervalToString(intervalOptionsFirstSet[2]), "$x = %.3f$, which corresponds to thinking that $x = %.3f$ leads to a negative in at least one of the radicands." %(distractor2, distractor1), 0]
    distractor3Interval = [stringForAnswersWithTwoIntervals(intervalOptionsFirstSet[3], intervalOptionsSecondSet[1]), "$x = %.3f \\text{ and } x = %.3f$, which are the negative or absolute values of the values you would have gotten by solving the equation correctly." %(distractor3[0], distractor3[1]), 0]
    distractor4Interval = ['\\text{All solutions lead to invalid or complex values in the equation.}', "Corresponds to thinking that $x = %.3f \\text{ and } x = %.3f$ lead to negatives in at least one of the radicands." %(solution[0], solution[1]), 0]
    displaySolution = '\\text{that there are two solutions and they are } x = %.3f \\text{ and } x = %.3f.' %(solution[0], solution[1])

if response_type=="Multiple-Choice":
	displayStem='Solve the radical equation below. Then, choose the interval(s) that the solution(s) belongs to.'
else:
	displayStem='Solve the radical equation below.'
displayProblem = '\\sqrt{%s} - \\sqrt{%s} = 0' %(displayFactor1, displayFactor2)
generalComment = "Distractors are different based on the number of solutions. For example, if the question is designed to have 0 options, then the distractors are solving the equation and not checking that the solutions lead to complex numbers (because plugging them in makes the value under the square root negative). Remember that after solving, we need to make sure our solution does not make the original equation take the square root of a negative number!"

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

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
