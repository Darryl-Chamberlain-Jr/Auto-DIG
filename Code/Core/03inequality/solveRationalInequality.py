import sys
import numpy
import random

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

def createIntervalToDisplay(direction, inclusion, value):
    if direction == "left" and inclusion == "yes":
        intervalToDisplay = "(-\\infty, %s]" %value
    elif direction == "left" and inclusion == "no":
        intervalToDisplay = "(-\\infty, %s)" %value
    elif direction == "right" and inclusion == "yes":
        intervalToDisplay = "[%s, \\infty)" %value
    elif direction == "right" and inclusion == "no":
        intervalToDisplay = "(%s, \\infty)" %value
    else:
        intervalToDisplay = "\\text{An error occured when creating this interval look.}"
    return intervalToDisplay
def createNumerators():
    numerators = [0, 0, 0, 0]
    while (numerators[1] >= numerators[2] or numerators[0] == numerators[3]):
        n0 = maybeMakeNegative(random.randint(3, 10))
        n1 = maybeMakeNegative(random.randint(3, 10))
        n2 = maybeMakeNegative(random.randint(3, 10))
        n3 = maybeMakeNegative(random.randint(3, 10))
        numerators=[n0, n1, n2, n3]
    return numerators
def createCoefficients():
    numerators = createNumerators()
    denominators = random.sample(range(2, 10), 4)
    n0, n1, n2, n3 = numerators
    d0, d1, d2, d3 = denominators
    left=numpy.poly1d([n1/d1, n0/d0])
    right=numpy.poly1d([n2/d2, n3/d3])
    diff_of_left_right=left-right
    endpoint = diff_of_left_right.r
    while (len(endpoint)==0 or abs(endpoint[0])<1 ):
        numerators = createNumerators()
        denominators = random.sample(range(2, 10), 4)
        n0, n1, n2, n3 = numerators
        d0, d1, d2, d3 = denominators
        left=numpy.poly1d([n1/d1, n0/d0])
        right=numpy.poly1d([n2/d2, n3/d3])
        diff_of_left_right=left-right
        endpoint = diff_of_left_right.r
    return [numerators, denominators, endpoint[0]]

numerators, denominators, endpoint = createCoefficients()
n0, n1, n2, n3 = numerators
d0, d1, d2, d3 = denominators
endpointCleaned = round(float(endpoint), 3)
checkingToFlipInequality = n1*d2-n2*d1

allProblemTypes = ["less", "leq", "greater", "geq"]
random.shuffle(allProblemTypes)
problemType = allProblemTypes[0]

if problemType == "less":
    if (checkingToFlipInequality > 0):
        solutionDirections = ["left", "no", endpointCleaned]
    else:
        solutionDirections = ["right", "no", endpointCleaned]
elif problemType == "leq":
    if (checkingToFlipInequality > 0):
        solutionDirections = ["left", "yes", endpointCleaned]
    else:
        solutionDirections = ["right", "yes", endpointCleaned]
elif problemType == "greater":
    if (checkingToFlipInequality < 0):
        solutionDirections = ["left", "no", endpointCleaned]
    else:
        solutionDirections = ["right", "no", endpointCleaned]
else:
    if (checkingToFlipInequality < 0):
        solutionDirections = ["left", "yes", endpointCleaned]
    else:
        solutionDirections = ["right", "yes", endpointCleaned]
solutionAnswer = createIntervalToDisplay(solutionDirections[0], solutionDirections[1], solutionDirections[2])
solutionDisplay = createIntervalToDisplay(solutionDirections[0], solutionDirections[1], "a")
### Distractor 1 is the inverse of the solution ###
if solutionDirections[0] == "left":
    distractor1Answer = createIntervalToDisplay("right", solutionDirections[1], endpointCleaned)
    distractor1Display = createIntervalToDisplay("right", solutionDirections[1], "a")
    distractor3Answer = createIntervalToDisplay("right", solutionDirections[1], -endpointCleaned)
else:
    distractor1Answer = createIntervalToDisplay("left", solutionDirections[1], endpointCleaned)
    distractor1Display = createIntervalToDisplay("left", solutionDirections[1], "a")
    distractor3Answer = createIntervalToDisplay("left", solutionDirections[1], -endpointCleaned)
### Distractor 2 is the negation of the solution endpoint ###
distractor2Answer = createIntervalToDisplay(solutionDirections[0], solutionDirections[1], -endpointCleaned)
distractor2Display = solutionDisplay
### Distractor 3 is the negation AND inverse of the solution ###
distractor3Display = distractor1Display
# Creates the intervals to hide the endpoints
solutionList1 = [round(endpointCleaned, 3), -round(endpointCleaned, 3)]
solutionList2 = [round(endpointCleaned, 3), -round(endpointCleaned, 3)]
intervalOptions1 = createIntervalOptions(solutionList1, 3, 0.75)
intervalOptions2 = createIntervalOptions(solutionList2, 3, 0.75)

solution = [solutionAnswer, solutionDisplay, intervalOptions1[0], "* $%s$, which is the correct option." %solutionAnswer, 1]
displaySolution = solutionAnswer
distractor1 = [distractor1Answer, distractor1Display, intervalOptions2[0], " $%s$, which corresponds to switching the direction of the interval. You likely did this if you did not flip the inequality when dividing by a negative!" %distractor1Answer, 0]
distractor2 = [distractor2Answer, distractor2Display, intervalOptions1[1], " $%s$, which corresponds to negating the endpoint of the solution." %distractor2Answer, 0]
distractor3 = [distractor3Answer, distractor3Display, intervalOptions2[1], " $%s$, which corresponds to switching the direction of the interval AND negating the endpoint. You likely did this if you did not flip the inequality when dividing by a negative as well as not moving values over to a side properly." %distractor3Answer, 0]
distractor4 = ["\\text{None of the above}.", "You may have chosen this if you thought the inequality did not match the ends of the intervals."]

if response_type=="Multiple-Choice":
    displayStem = 'Solve the linear inequality below. Then, choose the constant and interval combination that describes the solution set.'
else:
    displayStem = 'Solve the linear inequality below.'

if n1 < 0 and n3 < 0:
    if problemType == "less":
        displayProblem = "\\frac{%d}{%d} - \\frac{%d}{%d} x < \\frac{%d}{%d} x - \\frac{%d}{%d}" %(n0, d0, -n1, d1, n2, d2, -n3, d3)
    elif problemType == "leq":
        displayProblem = "\\frac{%d}{%d} - \\frac{%d}{%d} x \\leq \\frac{%d}{%d} x - \\frac{%d}{%d}" %(n0, d0, -n1, d1, n2, d2, -n3, d3)
    elif problemType == "greater":
        displayProblem = "\\frac{%d}{%d} - \\frac{%d}{%d} x > \\frac{%d}{%d} x - \\frac{%d}{%d}" %(n0, d0, -n1, d1, n2, d2, -n3, d3)
    else:
        displayProblem = "\\frac{%d}{%d} - \\frac{%d}{%d} x \\geq \\frac{%d}{%d} x - \\frac{%d}{%d}" %(n0, d0, -n1, d1, n2, d2, -n3, d3)
#
elif n1 < 0 and n3 > 0:
    if problemType == "less":
        displayProblem = "\\frac{%d}{%d} - \\frac{%d}{%d} x < \\frac{%d}{%d} x + \\frac{%d}{%d}" %(n0, d0, -n1, d1, n2, d2, n3, d3)
    elif problemType == "leq":
        displayProblem = "\\frac{%d}{%d} - \\frac{%d}{%d} x \\leq \\frac{%d}{%d} x + \\frac{%d}{%d}" %(n0, d0, -n1, d1, n2, d2, n3, d3)
    elif problemType == "greater":
        displayProblem = "\\frac{%d}{%d} - \\frac{%d}{%d} x > \\frac{%d}{%d} x + \\frac{%d}{%d}" %(n0, d0, -n1, d1, n2, d2, n3, d3)
    else:
        displayProblem = "\\frac{%d}{%d} - \\frac{%d}{%d} x \\geq \\frac{%d}{%d} x + \\frac{%d}{%d}" %(n0, d0, -n1, d1, n2, d2, n3, d3)
#
elif n1 > 0 and n3 < 0:
    if problemType == "less":
        displayProblem = "\\frac{%d}{%d} + \\frac{%d}{%d} x < \\frac{%d}{%d} x - \\frac{%d}{%d}" %(n0, d0, n1, d1, n2, d2, -n3, d3)
    elif problemType == "leq":
        displayProblem = "\\frac{%d}{%d} + \\frac{%d}{%d} x \\leq \\frac{%d}{%d} x - \\frac{%d}{%d}" %(n0, d0, n1, d1, n2, d2, -n3, d3)
    elif problemType == "greater":
        displayProblem = "\\frac{%d}{%d} + \\frac{%d}{%d} x > \\frac{%d}{%d} x - \\frac{%d}{%d}" %(n0, d0, n1, d1, n2, d2, -n3, d3)
    else:
        displayProblem = "\\frac{%d}{%d} + \\frac{%d}{%d} x \\geq \\frac{%d}{%d} x - \\frac{%d}{%d}" %(n0, d0, n1, d1, n2, d2, -n3, d3)
#
else:
    if problemType == "less":
        displayProblem = "\\frac{%d}{%d} + \\frac{%d}{%d} x < \\frac{%d}{%d} x + \\frac{%d}{%d}" %(n0, d0, n1, d1, n2, d2, n3, d3)
    elif problemType == "leq":
        displayProblem = "\\frac{%d}{%d} + \\frac{%d}{%d} x \\leq \\frac{%d}{%d} x + \\frac{%d}{%d}" %(n0, d0, n1, d1, n2, d2, n3, d3)
    elif problemType == "greater":
        displayProblem = "\\frac{%d}{%d} + \\frac{%d}{%d} x > \\frac{%d}{%d} x + \\frac{%d}{%d}" %(n0, d0, n1, d1, n2, d2, n3, d3)
    else:
        displayProblem = "\\frac{%d}{%d} + \\frac{%d}{%d} x \\geq \\frac{%d}{%d} x + \\frac{%d}{%d}" %(n0, d0, n1, d1, n2, d2, n3, d3)

generalComment = "Remember that less/greater than or equal to includes the endpoint, while less/greater do not. Also, remember that you need to flip the inequality when you multiply or divide by a negative."

answerList = [solution, distractor1, distractor2, distractor3]
random.shuffle(answerList)

c0 = "%s, \\text{ where } a \\in [%s, %s]" %(answerList[0][1], answerList[0][2][0], answerList[0][2][1])
c1 = "%s, \\text{ where } a \\in [%s, %s]" %(answerList[1][1], answerList[1][2][0], answerList[1][2][1])
c2 = "%s, \\text{ where } a \\in [%s, %s]" %(answerList[2][1], answerList[2][2][0], answerList[2][2][1])
c3 = "%s, \\text{ where } a \\in [%s, %s]" %(answerList[3][1], answerList[3][2][0], answerList[3][2][1])
c4 = "%s" %distractor4[0]

choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][3], answerList[1][3], answerList[2][3], answerList[3][3], distractor4[1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][4] == 1:
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
