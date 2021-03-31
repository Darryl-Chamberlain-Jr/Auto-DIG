import sys
from sympy import primerange
import numpy
import random
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

def generateFactors(minimumPrime, maximumPrime, numberOfFactors):
    listPrimes = list(primerange(minimumPrime, maximumPrime))
    bFactors = [random.sample(listPrimes, 1) for i in range(numberOfFactors)]
    dFactors = [random.sample(listPrimes, 1) for i in range(numberOfFactors)]
    return [bFactors, dFactors]
def generateSolution(minimum, maximum, factors):
    bFactors = factors[0]
    dFactors = factors[1]
    b = maybeMakeNegative(numpy.prod(bFactors))
    d = maybeMakeNegative(numpy.prod(dFactors))
    a = random.randint(minimum, maximum)
    c = random.randint(minimum, maximum)
    # This makes sure the middle coefficient does not cancel out and allow the student to solve without the quadratic formula or factoring.
    while (a*d+b*c==0) or (gcd(a, b) > 1) or (gcd(c, d) > 1):
        bFactors = factors[0]
        dFactors = factors[1]
        b = maybeMakeNegative(numpy.prod(bFactors))
        d = maybeMakeNegative(numpy.prod(dFactors))
        a = random.randint(minimum, maximum)
        c = random.randint(minimum, maximum)
    #This will guarantee that we always generate solutions with b < d
    if(b < d):
        return [a, b, c, d]
    else:
        return[c, d, a, b]

def generateProblem(solution):
    a, b, c, d = solution
    return [a*c, a*d + b*c, b*d]

#def distractorA1(solution):
#    a = float(solution[0])
#    b = float(solution[1])
#    c = float(solution[2])
#    d = float(solution[3])
#
#    z0 = -b
#    z1 = float(-d/(a*c))
#
#    if (z0<=z1):
#        return [z0, z1]
#    else:
#        return [z1, z0]

def generateAnswer(solution):
    s0 = float(solution[0])
    s1 = float(solution[1])
    s2 = float(solution[2])
    s3 = float(solution[3])
    z0 = float(-s1/s0)
    z1 = float(-s3/s2)
    if (z0 < z1):
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([solution[0], solution[1]]), generatePolynomialDisplay([solution[2], solution[3]]))
        answer = [z0, z1, factoredPolynomial]
    else:
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([solution[2], solution[3]]), generatePolynomialDisplay([solution[0], solution[1]]))
        answer = [z1, z0, factoredPolynomial]
    return answer

def distractorFatorWithA1(solution):
    a, b, c, d = solution
    if -a*d < -b*c:
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([1, a*d]), generatePolynomialDisplay([1, b*c]))
        return [-a*d, -b*c, factoredPolynomial]
    else:
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([1, b*c]), generatePolynomialDisplay([1, a*d]))
        return [-b*c, -a*d, factoredPolynomial]

def distractorC1(solution):
    a = float(solution[0])
    b = float(solution[1])
    c = float(solution[2])
    d = float(solution[3])
    z0 = float(-b/(a*c))
    z1 = -d
    if (z0<=z1):
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([solution[0]*solution[2], solution[1]]), generatePolynomialDisplay([1, solution[3]]))
        return [z0, z1, factoredPolynomial]
    else:
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([1, solution[3]]), generatePolynomialDisplay([solution[0]*solution[2], solution[1]]))
        return [z1, z0, factoredPolynomial]

def distractorLumpedCFactors(solution, factors):
    bFactors = factors[0]
    dFactors = factors[1]
    a = float(solution[0])
    b = float(solution[1])
    c = float(solution[2])
    d = float(solution[3])
    index = random.randint(0,len(bFactors)-1)
    b = float(b/(bFactors[index][0]))
    d = d*bFactors[index][0]
    z0 = float(-b/a)
    z1 = float(-d/c)
    intA = int(a)
    intB = int(b)
    intC = int(c)
    intD = int(d)
    if (z0<=z1):
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([intA, intB]), generatePolynomialDisplay([intC, intD]))
        return [z0, z1, factoredPolynomial]
    else:
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([intC, intD]), generatePolynomialDisplay([intA, intB]))
        return [z1, z0, factoredPolynomial]

def distractorLumpedAFactors(solution, factors):
    bFactors = factors[0]
    dFactors = factors[1]
    a = float(solution[0])
    b = float(solution[1])
    c = float(solution[2])
    d = float(solution[3])
    index = random.randint(0,len(bFactors)-1)
    d = float(d/(dFactors[index][0]))
    b = b*dFactors[index][0]
    z0 = float(-b/a)
    z1 = float(-d/c)
    intA = int(a)
    intB = int(b)
    intC = int(c)
    intD = int(d)
    if (z0<=z1):
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([intA, intB]), generatePolynomialDisplay([intC, intD]))
        return [z0, z1, factoredPolynomial]
    else:
        factoredPolynomial = "(%s)(%s)" %(generatePolynomialDisplay([intC, intD]), generatePolynomialDisplay([intA, intB]))
        return [z1, z0, factoredPolynomial]

def generateSolutionAndDistractors():
    factors = generateFactors(minimum, maximum, numberOfFactors)
    solution = generateSolution(minimum, maximum, factors)
    distractor1 = distractorFatorWithA1(solution)
    distractor2 = distractorC1(solution)
    distractor3 = distractorLumpedCFactors(solution, factors)
    distractor4 = distractorLumpedAFactors(solution, factors)
    while ( (distractor1[0] == distractor2[0]) or (distractor1[0] == distractor3[0]) or (distractor1[0] == distractor4[0]) or (distractor2[0] == distractor3[0]) or (distractor2[0] == distractor4[0]) or (distractor3[0] == distractor4[0]) ):
        factors = generateFactors(minimum, maximum, numberOfFactors)
        solution = generateSolution(minimum, maximum, factors)
        distractor1 = distractorFatorWithA1(solution)
        distractor2 = distractorC1(solution)
        distractor3 = distractorLumpedCFactors(solution, factors)
        distractor4 = distractorLumpedAFactors(solution, factors)
    return [factors, solution, distractor1, distractor2, distractor3, distractor4]

intervalRange = 5
minimum = 2
maximum = 5
numberOfFactors = 2

factors, solution, distractor1, distractor2, distractor3, distractor4 = generateSolutionAndDistractors()
problem = generateProblem(solution)
answer = generateAnswer(solution)

solutionList = [[answer[0], answer[1]], [distractor1[0], distractor1[1]], [distractor2[0], distractor2[1]], [distractor3[0], distractor3[1]], [distractor4[0], distractor4[1]]]
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

if response_type=="Multiple-Choice":
    displayStem = 'Solve the quadratic equation below. Then, choose the intervals that the solutions $x_1$ and $x_2$ belong to, with $x_1 \\leq x_2$.'
else:
    displayStem = 'Solve the quadratic equation below.'
displayProblem = "%s = 0" %generatePolynomialDisplay(problem)
displaySolution = "x_1 = %.3f \\text{ and } x_2 = %.3f" %(answer[0], answer[1])
generalComment = "This question can be factored, but it may be faster to find the solutions via the Quadratic Equation."

solutionInterval = [intervalOptions[0], "* $x_1 = %.3f \\text{ and } x_2 = %.3f$, which is the correct option. Obtained by solving the factored version $%s$" %(answer[0], answer[1], answer[2]), 1]
distractor1Interval = [intervalOptions[1], "$x_1 = %.3f \\text{ and } x_2 = %.3f$, which corresponds to solving the factored version $%s$" %(distractor1[0], distractor1[1], distractor1[2]), 0]
distractor2Interval = [intervalOptions[2], "$x_1 = %.3f \\text{ and } x_2 = %.3f$, which corresponds to solving the factored version $%s$" %(distractor2[0], distractor2[1], distractor2[2]), 0]
distractor3Interval = [intervalOptions[3], "$x_1 = %.3f \\text{ and } x_2 = %.3f$, which corresponds to solving the factored version $%s$" %(distractor3[0], distractor3[1], distractor3[2]), 0]
distractor4Interval = [intervalOptions[4], "$x_1 = %.3f \\text{ and } x_2 = %.3f$, which corresponds to solving the factored version $%s$" %(distractor4[0], distractor4[1], distractor4[2]), 0]

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

c0 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[0][0][0][0], answerList[0][0][0][1], answerList[0][0][1][0], answerList[0][0][1][1])
c1 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[1][0][0][0], answerList[1][0][0][1], answerList[1][0][1][0], answerList[1][0][1][1])
c2 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[2][0][0][0], answerList[2][0][0][1], answerList[2][0][1][0], answerList[2][0][1][1])
c3 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[3][0][0][0], answerList[3][0][0][1], answerList[3][0][1][0], answerList[3][0][1][1])
c4 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[4][0][0][0], answerList[4][0][0][1], answerList[4][0][1][0], answerList[4][0][1][1])
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
