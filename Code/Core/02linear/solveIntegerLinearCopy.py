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

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

### DEFINITIONS ###
def generateBlocks():    # Create an array of 6 distinct naturals, then make some integers
    blocks = [0,0,0,0,0,0]
    OneSolutionCheck = 0
    while (OneSolutionCheck == 0):    # Makes sure there is exactly one solution
        listNaturals = range(2, 20)
        blocks = random.sample(listNaturals, 6)
        blocks[0] = -blocks[0]
        blocks[1] = maybeMakeNegative(blocks[1])
        blocks[2] = maybeMakeNegative(blocks[2])
        blocks[3] = -blocks[3]
        blocks[4] = maybeMakeNegative(blocks[4])
        blocks[5] = maybeMakeNegative(blocks[5])
        OneSolutionCheck = blocks[0]*blocks[2] - blocks[3]*blocks[4]
    return blocks
def generateSolution(blocks):
    a, b, c, d, e, f = blocks
    basicLinearEquation = a * (b + c * x) - d * ( x * e - f)
    solution = solve(basicLinearEquation, x)
    if len(solution) == 0:
        solution=[0]
    return solution[0]
def generateDistractors(blocks):
    a, b, c, d, e, f = blocks
    distractor1 = generateSolution([a, b, -c, d, e, f])    # not distributing the negative in front of the first parentheses correctly
    distractor2 = generateSolution([a, b, c, d, e, -f])    # not distributing the negative in front of the second parentheses correctly
    distractor3 = generateSolution([-a, b, c, d, e, f])    # negative of the actual solution
    return [distractor1, distractor2, distractor3]
### VARIABLE DECLARATIONS ###
blocks = generateBlocks()
solution = generateSolution(blocks)
distractor1, distractor2, distractor3 = generateDistractors(blocks)
solutionList = [solution, distractor1, distractor2, distractor3]
### CREATE INTERVAL OPTIONS ###
intervalOptions = createIntervalOptions(solutionList, 3, 1)
### DEFINE ANSWER LIST AND DISPLAY SOLUTION ###
displaySolution = "x = %.3f" %solution
option1 = ["x \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1]), "* $x = %.3f$, which is the correct option." %solution, 1]
option2 = ["x \\in [%s, %s]" %(intervalOptions[1][0], intervalOptions[1][1]), "* $x = %.3f$, which corresponds to not distributing the negative in front of the first parentheses correctly." %distractor1, 0]
option3 = ["x \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1]), "* $x = %.3f$, which corresponds to not distributing the negative in front of the second parentheses correctly." %distractor2, 0]
option4 = ["x \\in [%s, %s]" %(intervalOptions[3][0], intervalOptions[3][1]), "* $x = %.3f$, which corresponds to getting the negative of the actual solution." %distractor3, 0]
option5 = ["\\text{There are no real solutions.}", "Corresponds to students thinking a fraction means there is no solution to the equation.", 0]
answerList = [option1, option2, option3, option4]
random.shuffle(answerList)
answerList.append(option5)
### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)
### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
displayStem = 'Solve the equation below. Then, choose the interval that contains the solution.'
displayProblem = "%d(%s) = %d(%s)" %(blocks[0], generatePolynomialDisplay([blocks[1], blocks[2]]), blocks[3], generatePolynomialDisplay([blocks[4], blocks[5]]))
generalComment = "The most common mistake on this question is to not distribute the negative in front of the second fraction correctly. The best way to avoid this is putting the numerator in parentheses, which will help you remember to distribute the negative correctly."

thisQuestion="solveIntegerLinearCopy"
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
