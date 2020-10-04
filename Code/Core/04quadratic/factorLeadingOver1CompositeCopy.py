import sys
from sympy import *
import numpy
import random
import math
from decimal import Decimal
import decimal
import traceback
import cmath
import matplotlib.pyplot as plt
from sympy.abc import x, y
from sympy.solvers import solve

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

def generateFactors(minimumPrime, maximumPrime, numberOfFactors):
    listPrimes = list(primerange(minimumPrime, maximumPrime))
    aFactors = [random.sample(listPrimes, 1) for i in range(numberOfFactors)]
    cFactors = [random.sample(listPrimes, 1) for i in range(numberOfFactors)]
    return [aFactors, cFactors]

def generateSolution(minimum, maximum, factors):
    aFactors = factors[0]
    cFactors = factors[1]
    a = numpy.prod(aFactors)
    c = numpy.prod(cFactors)
    b = maybeMakeNegative(random.randint(minimum, maximum))
    d = maybeMakeNegative(random.randint(minimum, maximum))

    # This makes sure we can't factor out a constant and the middle coefficient doesn't cancel.
    while ((gcd(a, b)*gcd(c, d)>1) or (a==c and b==-d) or (a*d+b*c==0)):
        aFactors = factors[0]
        cFactors = factors[1]
        a = numpy.prod(aFactors)
        c = numpy.prod(cFactors)
        b = maybeMakeNegative(random.randint(minimum, maximum))
        d = maybeMakeNegative(random.randint(minimum, maximum))

    #This will guarantee that we always generate solutions with b <= d
    if(b <= d):
        return [a, b, c, d]
    else:
        return[c, d, a, b]

def generateProblem(solution):
    a, b, c, d = solution
    return [a*c, a*d + b*c, b*d]

def distractorA1(solution):
    a, b, c, d = solution
    if a*d < b*c:
        return [1, a*d, 1, b*c]
    else:
        return [1, b*c, 1, a*d]

def distractorLumpedCFactors(solution, factors):
    aFactors = factors[0]
    cFactors = factors[1]
    a, b, c, d = solution
    index = random.randint(0,len(aFactors)-1)

    a = int(a/(aFactors[index][0]))
    c = c*aFactors[index][0]
    if(b <= d):
        return [a, b, c, d]
    else:
        return [c, d, a, b]
def distractorLumpedAFactors(solution, factors):
    aFactors = factors[0]
    cFactors = factors[1]
    a, b, c, d = solution
    index = random.randint(0,len(aFactors)-1)
    c = int(c/(cFactors[index][0]))
    a = a*cFactors[index][0]
    if(b <= d):
        return [a, b, c, d]
    else:
        return [c, d, a, b]

# Type 3 - a and c are fairly composite (ac has at least 6 factors)
intervalRange = 5
minimum = 2
maximum = 5
numberOfFactors = 2

factors = generateFactors(minimum, maximum, numberOfFactors)
solution = generateSolution(minimum, maximum, factors)
distractor1 = distractorA1(solution)
distractor2 = distractorLumpedCFactors(solution, factors)
distractor3 = distractorLumpedAFactors(solution, factors)
solutionList = [solution, distractor1, distractor2, distractor3]

while (solutionList[0]==solutionList[1] or solutionList[0]==solutionList[2] or solutionList[0]==solutionList[3] or solutionList[1]==solutionList[2] or solutionList[1]==solutionList[3] or solutionList[2]==solutionList[3]):
    factors = generateFactors(minimum, maximum, numberOfFactors)
    solution = generateSolution(minimum, maximum, factors)
    distractor1 = distractorA1(solution)
    distractor2 = distractorLumpedCFactors(solution, factors)
    distractor3 = distractorLumpedAFactors(solution, factors)
    solutionList = [solution, distractor1, distractor2, distractor3]

precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
problem = generateProblem(solution)
displayStem = 'Factor the quadratic below. Then, choose the intervals that contain the constants in the form $(ax+b)(cx+d); b \\leq d.$'

displayProblem = generatePolynomialDisplay(problem)

displaySolution = '(%s)(%s)' %(generatePolynomialDisplay([solution[0], solution[1]]), generatePolynomialDisplay([solution[2], solution[3]]))
displayDistractor1 = '(%s)(%s)' %(generatePolynomialDisplay([distractor1[0], distractor1[1]]), generatePolynomialDisplay([distractor1[2], distractor1[3]]))
displayDistractor2 = '(%s)(%s)' %(generatePolynomialDisplay([distractor2[0], distractor2[1]]), generatePolynomialDisplay([distractor2[2], distractor2[3]]))
displayDistractor3 = '(%s)(%s)' %(generatePolynomialDisplay([distractor3[0], distractor3[1]]), generatePolynomialDisplay([distractor3[2], distractor3[3]]))

generalComment = "$ac$ had many factors in this problem. It is best to list out the possible pairs in order to make sure you don't miss any."

solutionInterval = [intervalOptions[0], "* $%s$, which is the correct option." %displaySolution, 1]
distractor1Interval = [intervalOptions[1], " $%s$, which corresponds to factoring $%s$." %(displayDistractor1, generatePolynomialDisplay([1, problem[1], problem[0]*problem[2]])), 0]
distractor2Interval = [intervalOptions[2], " $%s$, which corresponds to associating some factor of c to a." %displayDistractor2, 0]
distractor3Interval = [intervalOptions[3], " $%s$, which corresponds to associating some factor of a to c." %displayDistractor3, 0]
distractor4Interval = ["", " Corresponds to a different factoring than any of the predicted options. If you get this, please let the coordinator know so they can work with you to figure out what went wrong with your factoring.", 0]

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)

c0 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\hspace*{5mm} c \\in [%s, %s], \\text{ and } \\hspace*{5mm} d \\in [%s, %s]" %(answerList[0][0][0][0], answerList[0][0][0][1], answerList[0][0][1][0], answerList[0][0][1][1], answerList[0][0][2][0], answerList[0][0][2][1], answerList[0][0][3][0], answerList[0][0][3][1])
c1 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\hspace*{5mm} c \\in [%s, %s], \\text{ and } \\hspace*{5mm} d \\in [%s, %s]" %(answerList[1][0][0][0], answerList[1][0][0][1], answerList[1][0][1][0], answerList[1][0][1][1], answerList[1][0][2][0], answerList[1][0][2][1], answerList[1][0][3][0], answerList[1][0][3][1])
c2 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\hspace*{5mm} c \\in [%s, %s], \\text{ and } \\hspace*{5mm} d \\in [%s, %s]" %(answerList[2][0][0][0], answerList[2][0][0][1], answerList[2][0][1][0], answerList[2][0][1][1], answerList[2][0][2][0], answerList[2][0][2][1], answerList[2][0][3][0], answerList[2][0][3][1])
c3 = "a \\in [%s, %s], \\hspace*{5mm} b \\in [%s, %s], \\hspace*{5mm} c \\in [%s, %s], \\text{ and } \\hspace*{5mm} d \\in [%s, %s]" %(answerList[3][0][0][0], answerList[3][0][0][1], answerList[3][0][1][0], answerList[3][0][1][1], answerList[3][0][2][0], answerList[3][0][2][1], answerList[3][0][3][0], answerList[3][0][3][1])
c4 = "\\text{None of the above.}"
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], distractor4Interval[1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

thisQuestion="factorLeadingOver1CompositeCopy"
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
