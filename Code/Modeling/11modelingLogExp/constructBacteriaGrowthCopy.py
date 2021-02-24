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
    OS_type=sys.argv[7]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

rateList = ["doubles", "triples", "quadruples"]
rateBase = random.randint(2, 4)
rateDescription = rateList[rateBase-2]
initialPop = random.randint(2, 4)
timePassed = random.randint(1, 3)
convertedTime = timePassed*60
tempReplicationRate = random.uniform(20, 40)
finalPop = initialPop * (rateBase)**(float(1.0/tempReplicationRate)*convertedTime)
ratio = float(finalPop)/float(initialPop)
approximateReplicationRate = int( 1.0 / ( log(ratio)/(float(convertedTime)*log(rateBase)) ) )
noConversionApproxReplicationRate = int( 360.0 / ( log(ratio)/(float(timePassed)*log(rateBase)) ) )
incorrectPropertiesApproxReplicationRate = int( 1.0 / ( log(finalPop)/(float(convertedTime)*log(rateBase*initialPop)) ) )
incorrectPropertiesAndNoConversionApproxRepRate = int( 360.0 / ( log(finalPop)/(float(timePassed)*log(rateBase*initialPop)) ) )
if rateBase == 2:
    wrongRateBase = 3
else:
    wrongRateBase = 2
WBapproximateReplicationRate = int( 1.0 / ( log(ratio)/(float(convertedTime)*log(wrongRateBase)) ) )
WBnoConversionApproxReplicationRate = int( 360.0 / ( log(ratio)/(float(timePassed)*log(wrongRateBase)) ) )
WBincorrectPropertiesApproxReplicationRate = int( 1.0 / ( log(finalPop)/(float(convertedTime)*log(wrongRateBase*initialPop)) ) )
WBincorrectPropertiesAndNoConversionApproxRepRate = int( 360.0 / ( log(finalPop)/(float(timePassed)*log(wrongRateBase*initialPop)) ) )

displayStem = "Using the scenario below, model the population of bacteria $\\alpha$ in terms of the number of minutes, $t$ that pass. Then, choose the correct approximate \\textit{(rounded to the nearest minute)} replication rate of bacteria-$\\alpha$."
displayProblem = "A newly discovered bacteria, $\\alpha$, is being examined in a lab. The lab started with a petri dish of %d bacteria-$\\alpha$. After %d hours, the petri dish has %d bacteria-$\\alpha$. Based on similar bacteria, the lab believes bacteria-$\\alpha$ %s after some undetermined number of minutes." %(initialPop, timePassed, finalPop, rateDescription)

listedOrNot = random.randint(0, 1)
if listedOrNot == 0:
    option1 = ["\\text{About } %d \\text{ minutes}" %WBapproximateReplicationRate, "This uses the wrong base.", 0]
    option2 = ["\\text{About } %d \\text{ minutes}" %WBnoConversionApproxReplicationRate, "This uses the wrong base and solves for the constant correctly but converted incorrectly.", 0]
    option3 = ["\\text{About } %d \\text{ minutes}" %WBincorrectPropertiesApproxReplicationRate, "This uses the wrong base and does not solve for the constant correctly.", 0]
    option4 = ["\\text{About } %d \\text{ minutes}" %WBincorrectPropertiesAndNoConversionApproxRepRate, "This uses the wrong base, does not solve for the constant correctly, AND converted incorrectly.", 0]
    option5 = ["\\text{None of the above}", "* This is the correct option as all other options used the wrong base in their model.", 1]
    displaySolution = option5[0]
else:
    option1 = ["\\text{About } %d \\text{ minutes}" %approximateReplicationRate, "* This is the correct option.", 1]
    option2 = ["\\text{About } %d \\text{ minutes}" %noConversionApproxReplicationRate, "This solves for the constant correctly but converted incorrectly.", 0]
    option3 = ["\\text{About } %d \\text{ minutes}" %incorrectPropertiesApproxReplicationRate, "This does not solve for the constant correctly.", 0]
    option4 = ["\\text{About } %d \\text{ minutes}" %incorrectPropertiesAndNoConversionApproxRepRate, "This does not solve for the constant correctly AND converted incorrectly.", 0]
    option5 = ["\\text{None of the above}", "Please contact the coordinator to discuss why you believe none of the answers above are correct.", 0]
    displaySolution = option1[0]

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "Your model should be $P(t) = P_0(b)^{kt}$, where $P(t)$ is the population at some time $t$, $P_0$ is the initial population, and $k$ is the replication rate. Be sure you convert the hours into minutes!"

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
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
