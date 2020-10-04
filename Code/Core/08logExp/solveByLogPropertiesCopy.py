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

thisQuestion="solveByLogPropertiesCopy"

def generateSolutionAndDistractorsType1(rootDegree, numerator, coefficient, a):
    solution = float(ln(numerator) - rootDegree*a) / float(coefficient)
    distractor1 = -float(ln(numerator)+rootDegree*ln(a))/float(coefficient)
    distractor2 = float(ln(numerator)-2*a) / float(coefficient)
    distractor3 = "\\text{There is no Real solution to the equation.}"
    distractor4 = "\\text{None of the above.}"
    intervalOptions = createIntervalOptions([solution, distractor1, distractor2], 3, 1)
    solutionOption = ["x \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1]), "* $x = %.3f$, which is the correct option." %solution, 1]
    distractor1Option = ["x \\in [%s, %s]" %(intervalOptions[1][0], intervalOptions[1][1]), "$x = %.3f$, which corresponds to thinking you need to take the natural log of on the left before reducing." %distractor1, 0]
    distractor2Option = ["x \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1]), "$x = %.3f$, which corresponds to treating any root as a square root." %distractor2, 0]
    distractor3Option = [distractor3, "This corresponds to believing you cannot solve the equation.", 0]
    distractor4Option = [distractor4, "This corresponds to making an unexpected error.", 0]
    shuffleFirstThree = [solutionOption, distractor1Option, distractor2Option]
    random.shuffle(shuffleFirstThree)
    answerList = [shuffleFirstThree[0], shuffleFirstThree[1], shuffleFirstThree[2], distractor3Option, distractor4Option]
    displaySolution = "x = %s" %round(solution, 3)
    return [answerList, displaySolution]

def generateSolutionAndDistractorsType2(rootDegree, numerator, coefficient, a):
    solution = float( ln(numerator) - rootDegree*ln(a) )  /  float(coefficient)
    distractor1 = - float(ln(numerator)+rootDegree*a) / float(coefficient)
    distractor2 = float(ln(numerator)-2*ln(a)) / float(coefficient)
    distractor3 = "\\text{There is no Real solution to the equation.}"
    distractor4 = "\\text{None of the above.}"
    intervalOptions = createIntervalOptions([solution, distractor1, distractor2], 3, 1)
    solutionOption = ["x \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1]), "* $x = %.3f$, which is the correct option." %solution, 1]
    distractor1Option = ["x \\in [%s, %s]" %(intervalOptions[1][0], intervalOptions[1][1]), "$x = %.3f$, which corresponds to thinking you don't need to take the natural log of both sides before reducing, as if the equation already had a natural log on the right side." %distractor1, 0]
    distractor2Option = ["x \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1]), "$x = %.3f$, which corresponds to treating any root as a square root." %distractor2, 0]
    distractor3Option = [distractor3, "This corresponds to believing you cannot solve the equation.", 0]
    distractor4Option = [distractor4, "This corresponds to making an unexpected error.", 0]
    shuffleFirstThree = [solutionOption, distractor1Option, distractor2Option]
    random.shuffle(shuffleFirstThree)
    answerList = [shuffleFirstThree[0], shuffleFirstThree[1], shuffleFirstThree[2], distractor3Option, distractor4Option]
    displaySolution = "x = %s" %round(solution, 3)
    return [answerList, displaySolution]

def generateSolutionAndDistractorsType3(rootDegree, numerator, coefficient, a):
    solution = float(ln(numerator) - rootDegree*a) / float(coefficient)
    negSolution = float(ln(numerator) - rootDegree*a) / float(-coefficient)
    distractor1 = -float(ln(numerator)+rootDegree*ln(a)) / float(coefficient)
    distractor2 = float(ln(numerator)-2*a) / float(coefficient)
    distractor3 = "\\text{There is no Real solution to the equation.}"
    distractor4 = "\\text{None of the above.}"
    intervalOptions = createIntervalOptions([negSolution, distractor1, distractor2, solution], 3, 1)
    negSolutionOption = ["x \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1]), "$x = %.3f$, which is the negative of the correct solution." %negSolution, 0]
    distractor1Option = ["x \\in [%s, %s]" %(intervalOptions[1][0], intervalOptions[1][1]), "$x = %.3f$, which corresponds to thinking you need to take the natural log of the left side before reducing." %distractor1, 0]
    distractor2Option = ["x \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1]), "$x = %.3f$, which corresponds to treating any root as a square root." %distractor2, 0]
    distractor3Option = [distractor3, "This corresponds to believing you cannot solve the equation.", 0]
    distractor4Option = [distractor4, "*$x = %.3f$ is the correct solution and does not fit in any of the other intervals." %solution, 1]
    shuffleFirstThree = [negSolutionOption, distractor1Option, distractor2Option]
    random.shuffle(shuffleFirstThree)
    answerList = [shuffleFirstThree[0], shuffleFirstThree[1], shuffleFirstThree[2], distractor3Option, distractor4Option]
    displaySolution = "x = %s, \\text{ which does not fit in any of the interval options.}" %round(solution, 3)
    return [answerList, displaySolution]

def generateSolutionAndDistractorsType4(rootDegree, numerator, coefficient, a):
    solution = float(ln(numerator) - rootDegree*ln(a)) / float(coefficient)
    negSolution = float(ln(numerator) - rootDegree*ln(a)) / float(-coefficient)
    distractor1 = -float(ln(numerator)+rootDegree*a) / float(coefficient)
    distractor2 = float(ln(numerator)-2*ln(a)) / float(coefficient)
    distractor3 = "\\text{There is no Real solution to the equation.}"
    distractor4 = "\\text{None of the above.}"
    intervalOptions = createIntervalOptions([negSolution, distractor1, distractor2, solution], 3, 1)
    negSolutionOption = ["x \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1]), "$x = %.3f$, which is the negative of the correct solution." %negSolution, 0]
    distractor1Option = ["x \\in [%s, %s]" %(intervalOptions[1][0], intervalOptions[1][1]), "$x = %.3f$, which corresponds to thinking you don't need to take the natural log of both sides before reducing, as if the right side already has a natural log." %distractor1, 0]
    distractor2Option = ["x \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1]), "$x = %.3f$, which corresponds to treating any root as a square root." %distractor2, 0]
    distractor3Option = [distractor3, "This corresponds to believing you cannot solve the equation.", 0]
    distractor4Option = [distractor4, "* $x = %.3f$ is the correct solution and does not fit in any of the other intervals." %solution, 1]
    shuffleFirstThree = [negSolutionOption, distractor1Option, distractor2Option]
    random.shuffle(shuffleFirstThree)
    answerList = [shuffleFirstThree[0], shuffleFirstThree[1], shuffleFirstThree[2], distractor3Option, distractor4Option]
    displaySolution = "x = %s, \\text{ which does not fit in any of the interval options.}" %round(solution, 3)
    return [answerList, displaySolution]

# THIS WILL NOW HAVE TWO DIFFERENT PROBLEMS:
    # a = \ln(\sqrt[rootDegree]{\frac{ \sage{numerator} }{ e^{\sage{coefficient}x} } } )
        # a = (1/rootDegree) ln(\frac{ \sage{numerator} }{ e^{\sage{coefficient}x} } )
        # rootDegree*a = ln(numerator) - coefficient*x
        # coefficient*x = ln(numerator) - rootDegree*a
        # x = ( ln(numerator) - rootDegree*a )/( coefficient )
    # a = \sqrt[rootDegree]{\frac{\sage{numerator}}{e^{\sage{coefficient}x}}}
        # x = ( ln(numerator) - rootDegree*ln(a) )/( coefficient )

rootDegree = random.randint(3, 7)
numerator = random.randint(5, 30)
coefficient = random.randint(3,9)
a = random.randint(5, 25)
questionType = random.randint(1, 4)

if questionType == 1:
     answerList, displaySolution = generateSolutionAndDistractorsType1(rootDegree, numerator, coefficient, a)
     displayProblem = ' %s = \\ln{\\sqrt[%d]{\\frac{%d}{e^{%dx}}}}' %(a, rootDegree, numerator, coefficient)
elif questionType == 2:
    answerList, displaySolution = generateSolutionAndDistractorsType2(rootDegree, numerator, coefficient, a)
    displayProblem = ' %s = \\sqrt[%d]{\\frac{%d}{e^{%dx}}}' %(a, rootDegree, numerator, coefficient)
elif questionType == 3:
    answerList, displaySolution = generateSolutionAndDistractorsType3(rootDegree, numerator, coefficient, a)
    displayProblem = ' %s = \\ln{\\sqrt[%d]{\\frac{%d}{e^{%dx}}}}' %(a, rootDegree, numerator, coefficient)
else:
    answerList, displaySolution = generateSolutionAndDistractorsType4(rootDegree, numerator, coefficient, a)
    displayProblem = ' %s = \\sqrt[%d]{\\frac{%d}{e^{%dx}}}' %(a, rootDegree, numerator, coefficient)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

displayStem = ' Solve the equation for $x$ and choose the interval that contains $x$ (if it exists).'
generalComment = "\\textbf{General Comments}: After using the properties of logarithmic functions to break up the right-hand side, use $\\ln(e) = 1$ to reduce the question to a linear function to solve. You can put $\\ln(%d)$ into a calculator if you are having trouble." %numerator

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
