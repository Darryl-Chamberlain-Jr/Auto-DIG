import sys
import random

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

def generateDisplayAndSolution():
    #Goal: (a0*x+b0)*(a1*x+b1)*(x-z)+r
    # This can be improved in the future with numpy.poly1d as it provides quotient and remainder with poly division.
    a0 = random.randint(2, 5)
    b0 = maybeMakeNegative(random.randint(2, 5))
    a1 = random.randint(2, 5)
    b1 = maybeMakeNegative(random.randint(2, 5))
    z = maybeMakeNegative(random.randint(2, 5))
    r = maybeMakeNegative(random.randint(2, 5))
    #numeratorPoly = (a0*a1)*x**3 + (-a0*a1*z + a0*b1 + a1*b0)*x**2+ (-a0*b1*z - a1*b0*z + b0*b1)*x + (-b0*b1*z + r)
    numCo1 = a0*a1
    numCo2 = -a0*a1*z + a0*b1 + a1*b0
    numCo3 = -a0*b1*z - a1*b0*z + b0*b1
    numCo4 = -b0*b1*z + r
    numeratorPoly = generatePolynomialDisplay([numCo1, numCo2, numCo3, numCo4])
    denominator = generatePolynomialDisplay([1, -z])
    term1 = a0*a1
    term2 = a0*b1+a1*b0
    term3 = b0*b1
    quotient = generatePolynomialDisplay([term1, term2, term3])
    remainder = r
    #
    while (numCo1==0 or numCo2==0 or numCo3==0 or numCo4==0):
        a0 = random.randint(2, 5)
        b0 = maybeMakeNegative(random.randint(2, 5))
        a1 = random.randint(2, 5)
        b1 = maybeMakeNegative(random.randint(2, 5))
        z = maybeMakeNegative(random.randint(2, 5))
        r = maybeMakeNegative(random.randint(2, 5))
        #
        numCo1 = a0*a1
        numCo2 = -a0*a1*z + a0*b1 + a1*b0
        numCo3 = -a0*b1*z - a1*b0*z + b0*b1
        numCo4 = -b0*b1*z + r
        numeratorPoly = generatePolynomialDisplay([numCo1, numCo2, numCo3, numCo4])
        denominator = generatePolynomialDisplay([1, -z])
        term1 = a0*a1
        term2 = a0*b1+a1*b0
        term3 = b0*b1
        quotient = generatePolynomialDisplay([term1, term2, term3])
        remainder = r
    solutionValues = [term1, term2, term3, remainder]
    coefficients = [a0, b0, a1, b1, z, r]
    return [numeratorPoly, denominator, quotient, solutionValues, coefficients]

def syntheticDivision(polyCoefficients, syntheticNumber):
    a, b, c, d = polyCoefficients
    n = syntheticNumber
    term1 = a
    term2 = term1*n + b
    term3 = term2*n + c
    remainder = term3*n + d
    return [term1, term2, term3, remainder]

def subtractSyntheticDivision(polyCoefficients, syntheticNumber):
    a, b, c, d = polyCoefficients
    n = syntheticNumber
    term1 = a
    term2 = b - term1*n
    term3 = c - term2*n
    remainder = d - term3*n
    return [term1, term2, term3, remainder]

# There aren't great distractors. Will need to see students' work to make better ones.
def generateDistractors(coefficients):
    a0, b0, a1, b1, z, r = coefficients
    # Synthetically divided by the negative of the zero
    polyCoefficients = [a0*a1, -a0*a1*z + a0*b1 + a1*b0, -a0*b1*z - a1*b0*z + b0*b1, -b0*b1*z + r]
    distractor1 = syntheticDivision(polyCoefficients, -z)
    # Multiplies the first term rather than bringing it down.
    badPolyCoefficients = [z*a0*a1, -a0*a1*z + a0*b1 + a1*b0, -a0*b1*z - a1*b0*z + b0*b1, -b0*b1*z + r]
    distractor2 = syntheticDivision(badPolyCoefficients, z)
    distractor3 = syntheticDivision(badPolyCoefficients, -z)
    distractor4 = syntheticDivision(polyCoefficients, z-1)
    return [distractor1, distractor2, distractor3, distractor4]

# Begin problem
intervalRange = 5
precision = 1

displayAndSolution = generateDisplayAndSolution()
displayNumerator = displayAndSolution[0]
displayDenominator = displayAndSolution[1]
displayQuotient = displayAndSolution[2]

coefficients = displayAndSolution[4]

# Solution is coefficents of quotient and remainder
solution = [displayAndSolution[3][0], displayAndSolution[3][1], displayAndSolution[3][2], displayAndSolution[3][3]]
distractors = generateDistractors(coefficients)

solutionList = [solution, distractors[0], distractors[1], distractors[2], distractors[3]]
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = intervalOptions[0]
distractor1Interval = intervalOptions[1]
distractor2Interval = intervalOptions[2]
distractor3Interval = intervalOptions[3]
distractor4Interval = intervalOptions[4]

solutionInterval.append("* This is the solution!")
distractor1Interval.append(" You divided by the opposite of the factor.")
distractor2Interval.append(" You multiplied by the synthetic number rather than bringing the first factor down.")
distractor3Interval.append(" You divided by the opposite of the factor AND multiplied the first factor rather than just bringing it down.")
distractor4Interval.append(" You multiplied by the synthetic number and subtracted rather than adding during synthetic division.")

solutionInterval.append(1)
distractor1Interval.append(0)
distractor2Interval.append(0)
distractor3Interval.append(0)
distractor4Interval.append(0)

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

displayStem = "Perform the division below. Then, find the intervals that correspond to the quotient in the form $ax^2+bx+c$ and remainder $r$."
displayProblem = "\\frac{%s}{%s}" %(displayNumerator, displayDenominator)
displaySolution = "%s + \\frac{%s}{%s}" %(displayQuotient, coefficients[5], displayDenominator)
generalComment = "Be sure to synthetically divide by the zero of the denominator!"

c0 = "a \\in [%s, %s], \\text{   } b \\in [%s, %s], \\text{   } c \\in [%s, %s], \\text{   and   } r \\in [%s, %s]." %(answerList[0][0][0], answerList[0][0][1], answerList[0][1][0], answerList[0][1][1], answerList[0][2][0], answerList[0][2][1], answerList[0][3][0], answerList[0][3][1])
c1 = "a \\in [%s, %s], \\text{   } b \\in [%s, %s], \\text{   } c \\in [%s, %s], \\text{   and   } r \\in [%s, %s]." %(answerList[1][0][0], answerList[1][0][1], answerList[1][1][0], answerList[1][1][1], answerList[1][2][0], answerList[1][2][1], answerList[1][3][0], answerList[1][3][1])
c2 = "a \\in [%s, %s], \\text{   } b \\in [%s, %s], \\text{   } c \\in [%s, %s], \\text{   and   } r \\in [%s, %s]." %(answerList[2][0][0], answerList[2][0][1], answerList[2][1][0], answerList[2][1][1], answerList[2][2][0], answerList[2][2][1], answerList[2][3][0], answerList[2][3][1])
c3 = "a \\in [%s, %s], \\text{   } b \\in [%s, %s], \\text{   } c \\in [%s, %s], \\text{   and   } r \\in [%s, %s]." %(answerList[3][0][0], answerList[3][0][1], answerList[3][1][0], answerList[3][1][1], answerList[3][2][0], answerList[3][2][1], answerList[3][3][0], answerList[3][3][1])
c4 = "a \\in [%s, %s], \\text{   } b \\in [%s, %s], \\text{   } c \\in [%s, %s], \\text{   and   } r \\in [%s, %s]." %(answerList[4][0][0], answerList[4][0][1], answerList[4][1][0], answerList[4][1][1], answerList[4][2][0], answerList[4][2][1], answerList[4][3][0], answerList[4][3][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][4], answerList[1][4], answerList[2][4], answerList[3][4], answerList[4][4]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][5] == 1:
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
