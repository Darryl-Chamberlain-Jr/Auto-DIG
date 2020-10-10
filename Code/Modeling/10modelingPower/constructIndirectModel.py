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

thisQuestion="constructIndirectModel"

increasesOrDecreases = random.choice(["increases", "decreases"])
lengthExponent = random.randint(2, 4)
exponentDescriptions = ["square", "cube", "quartic"]
lengthDescription = exponentDescriptions[lengthExponent - 2]
stringLength = random.randint(2, 5)
vibrationRate = random.randint(20, 40)

constant = vibrationRate * float( ((stringLength)/10.0)**lengthExponent)
noConversion = float(vibrationRate * (stringLength)**lengthExponent )
wrongConversion = float(vibrationRate * (stringLength)**lengthExponent * 10 )
wrongModel = float(vibrationRate) / float( (((stringLength)/10.0)**lengthExponent) )
wrongModelNoConversion = float(vibrationRate) / float( ((stringLength)**lengthExponent) )

displayStem = "For the scenario below, model the rate of vibration (cm/s) of the string in terms of the length of the string. Then determine the variation constant $k$ of the model (if possible). The constant should be in terms of cm and s."
displayProblem = "The rate of vibration of a string under constant tension varies based on the type of string and the length of the string. The rate of vibration of string $\\omega$ %s as the %s length of the string %s. For example, when string $\\omega$ is %d mm long, the rate of vibration is %d cm/s." %(increasesOrDecreases, lengthDescription, increasesOrDecreases, stringLength, vibrationRate)
generalComment = "The most common mistake on this question is to not convert mm to cm! When modeling, you need to make sure all of the units for your variables are compatible."

option1 = ["k = %.2f" %constant, "* This is the correct option, which corresponds to the model $R = \\frac{k}{l^{%d}}$ AND converts from mm to cm."%lengthExponent, 1]
option2 = ["k = %.2f" %noConversion, "This option uses the correct model, $R = \\frac{k}{l^{%d}}$, but does not convert from mm to cm so that the units match." %lengthExponent, 0]
option3 = ["k = %.2f" %wrongModel, "This option uses the model $R = kl^{%d}$ as if this is a direct variation." %lengthExponent, 0]
option4 = ["k = %.2f" %wrongModelNoConversion, "This option uses the model $R = kl^{%d}$ as if this is a direct variation AND does not convert from mm to cm so that the units match." %lengthExponent, 0]
option5 = ["\\text{None of the above.}", "Talk with the coordinator if you chose this option.", 0]

displaySolution = option1[0]
answerListTemp = [option1, option2, option3, option4]
random.shuffle(answerListTemp)
answerList = [answerListTemp[0], answerListTemp[1], answerListTemp[2], answerListTemp[3], option5]


choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
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
