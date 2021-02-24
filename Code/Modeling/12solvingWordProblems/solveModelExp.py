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
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

initialPop = random.randint(3, 8)
growthRate = random.randint(2, 4)
growthDescriptionList = ["doubled", "tripled", "quadrupled"]
growthDescription = growthDescriptionList[growthRate - 2]
replicationRate = random.randint(1, 5)
thresholdConfirmedCases = 10**random.randint(3, 6)
#
daysUntilThreshold = int( math.ceil(    float( replicationRate*log(float(thresholdConfirmedCases) / float(initialPop)) ) / float(log(growthRate))    )   )
incorrectProperties = int( math.ceil(    float( replicationRate * log( thresholdConfirmedCases ) ) / float(log(growthRate*initialPop))    )    )
eAsBase = int( math.ceil(    float( replicationRate*log(float(thresholdConfirmedCases) / float(initialPop)) ) / float(log(exp(1)))    )   )
incorrectPropertiesEAsBase = int( math.ceil(    float( replicationRate * log( thresholdConfirmedCases ) ) / float(log(exp(1)*initialPop))    )   )
#
test_list = [daysUntilThreshold, incorrectProperties, eAsBase, incorrectPropertiesEAsBase]
while len(set(test_list)) != len(test_list):
    initialPop = random.randint(3, 8)
    growthRate = random.randint(2, 4)
    growthDescriptionList = ["doubled", "tripled", "quadrupled"]
    growthDescription = growthDescriptionList[growthRate - 2]
    replicationRate = random.randint(1, 5)
    thresholdConfirmedCases = 10**random.randint(3, 6)
    #
    daysUntilThreshold = int( math.ceil(    float( replicationRate*log(float(thresholdConfirmedCases) / float(initialPop)) ) / float(log(growthRate))    )   )
    incorrectProperties = int( math.ceil(    float( replicationRate * log( thresholdConfirmedCases ) ) / float(log(growthRate*initialPop))    )    )
    eAsBase = int( math.ceil(    float( replicationRate*log(float(thresholdConfirmedCases) / float(initialPop)) ) / float(log(exp(1)))    )   )
    incorrectPropertiesEAsBase = int( math.ceil(    float( replicationRate * log( thresholdConfirmedCases ) ) / float(log(exp(1)*initialPop))    )   )
    test_list = [daysUntilThreshold, incorrectProperties, eAsBase, incorrectPropertiesEAsBase]

displayStem = "Solve the modeling problem below, if possible."
displayProblem = "A new virus is spreading throughout the world. There were initially %d many cases reported, but the number of confirmed cases has %s every %d days. How long will it be until there are at least %d confirmed cases?" %(initialPop, growthDescription, replicationRate, thresholdConfirmedCases)

option1 = ["\\text{About } %d \\text{ days}" %daysUntilThreshold, "* This is the correct option.", 1]
option2 = ["\\text{About } %d \\text{ days}" %incorrectProperties, "You modeled the situation correctly but did not apply the properties of log correctly.", 0]
option3 = ["\\text{About } %d \\text{ days}" %eAsBase, "You modeled the situation with $e$ as the base, but solved correctly otherwise.", 0]
option4 = ["\\text{About } %d \\text{ days}" %incorrectPropertiesEAsBase, "You modeled the situation with $e$ as the base and did not apply the properties of log correctly.", 0]
option5 = ["\\text{There is not enough information to solve the problem.}", "If you chose this option, please contact the coordinator to discuss why you think this is the case.", 0]

displaySolution = option1[0]

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "Set up the model the same as in Module 11M. Then, plug in %d and solve for $d$ in your model." %thresholdConfirmedCases

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
if debug=="save":
    writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
