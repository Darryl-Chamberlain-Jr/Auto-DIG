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
thisQuestion=sys.argv[5]
sys.path.insert(1, f"/{DIR}/PythonScripts")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
from storeQuestionData import *

timeExponent = random.randint(2, 4)
distanceExponent = random.randint(2, 4)
exponentDescriptions = ["square", "cube", "quartic"]
timeDescription = exponentDescriptions[timeExponent - 2]
distanceDescription = exponentDescriptions[distanceExponent - 2]
increasesOrDecreases = random.choice(["increases", "decreases"])
averageDistance = random.randint(2, 10)
orbitTime = random.randint(50, 100)

constant = float(orbitTime**timeExponent) / float(averageDistance**distanceExponent)
homeworkConstant = float( (4.0*pi**2) / (9.8) )
indirectConstant = float(orbitTime**timeExponent * averageDistance**distanceExponent)
reversePowers = float(orbitTime**(1/float(timeExponent))) / float(averageDistance**(1/float(distanceExponent)))
displayStem = "For the scenario below, find the variation constant $k$ of the model (if possible)."
displayProblem = "In an alternative galaxy, the %s of the time, $T$ (Earth years), required for a planet to orbit Sun $\\chi$ %s as the %s of the distance, $d$ (AUs), that the planet is from Sun $\\chi$ %s. For example, when Ea's average distance from Sun $\\chi$ is %d, it takes %d Earth days to complete an orbit." %(timeDescription, increasesOrDecreases, distanceDescription, increasesOrDecreases, averageDistance, orbitTime)

# Solution
option1 = ["k = %.3f" %constant, "* This is the correct option corresponding to the model $T^{%d} = k d^{%d}$." %(timeExponent, distanceExponent), 1]
# Copying from homework: (4*pi**2) / (9.8)
option2 = ["k = %.3f" %homeworkConstant, "This copies the constant used in the homework.", 0]
# Indirect relation
option3 = ["k = %.3f" %indirectConstant, "This corresponds to the model $T^{%d} = \\frac{k}{d^{%d}}$." %(timeExponent, distanceExponent), 0]
# Reverse powers
option4 = ["k = %.3f" %reversePowers, "This corresponds to the model $T^{1/%d} = k d^{1/%d}$." %(timeExponent, distanceExponent), 0]
# Unable to determine based on info
option5 = ["\\text{Unable to compute the constant based on the information given.}", "This corresponds to believing you cannot determine the type of model from the information given.", 0]

displaySolution = option1[0]
generalComment = "Since $T$ %s proportionally as $d$ %s, we know this is a direct variation model." %(increasesOrDecreases, increasesOrDecreases)
answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

answerIndex = 0
letters = ["A", "B", "C", "D"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="String"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
