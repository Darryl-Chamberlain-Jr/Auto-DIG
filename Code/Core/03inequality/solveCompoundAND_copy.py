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
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

def createAllCoefficientsAndEndpoints():
    c0 = maybeMakeNegative(random.randint(3, 9))
    c1 = maybeMakeNegative(random.randint(3, 9))
    c3 = maybeMakeNegative(random.randint(3, 9))
    c4 = random.randint(3, 9)
    c5 = maybeMakeNegative(random.randint(3, 9))
    c6 = maybeMakeNegative(random.randint(3, 9))
    # Need 1, 4, and 6 set before 2
    c2 = (max(c1, c6)*c4) + random.randint(2, 5) # This flips the inequalities
    smallerEndpoint = float((-c0*c4-c3) / (c1*c4-c2))
    largerEndpoint = float((c4*c5+c3) / (c2-c4*c6))
    # Makes sure we get a solution interval
    while  (largerEndpoint <= smallerEndpoint):
        c0 = maybeMakeNegative(random.randint(3, 9))
        c1 = maybeMakeNegative(random.randint(3, 9))
        c3 = maybeMakeNegative(random.randint(3, 9))
        c4 = random.randint(3, 9)
        c5 = maybeMakeNegative(random.randint(3, 9))
        c6 = maybeMakeNegative(random.randint(3, 9))
        # Need 1, 4, and 6 set before 2
        c2 = (max(c1, c6)*c4) + random.randint(2, 5) # This flips the inequalities
        smallerEndpoint = float((-c0*c4-c3) / (c1*c4-c2))
        largerEndpoint = float((c4*c5+c3) / (c2-c4*c6))
    coefficients=[c0, c1, c2, c3, c4, c5, c6]
    solutionEndpoints = [smallerEndpoint, largerEndpoint]
    return [coefficients, solutionEndpoints]

coefficients, solutionEndpoints = createAllCoefficientsAndEndpoints()
while (abs(solutionEndpoints[0])==abs(solutionEndpoints[1]) or abs(solutionEndpoints[0])<1 or abs(solutionEndpoints[1])<1 or abs(abs(solutionEndpoints[0])-abs(solutionEndpoints[1])) < 1 ):
    coefficients, solutionEndpoints = createAllCoefficientsAndEndpoints()

c0, c1, c2, c3, c4, c5, c6 = coefficients

if c1 < 0:
    AndInequalityLeft = "%s - %s x" %(c0, -c1)
else:
    AndInequalityLeft = "%s + %s x" %(c0, c1)

if c3 < 0:
    AndInequalityMiddle = "\\frac{%s x + %s}{%s}" %(c2, -c3, c4)
else:
    AndInequalityMiddle = "\\frac{%s x - %s}{%s}" %(c2, c3, c4)

if c6 < 0:
    AndInequalityRight = "%s - %s x" %(c5, -c6)
else:
    AndInequalityRight = "%s + %s x" %(c5, c6)

precision = 0.75
solutionAndNegative = [ [round(solutionEndpoints[0], 3), round(solutionEndpoints[1], 3)], [-round(solutionEndpoints[0], 3), -round(solutionEndpoints[1], 3)] ]
intervalOptions1 = createIntervalOptions(solutionAndNegative, 4, precision)
intervalOptions2 = createIntervalOptions(solutionAndNegative, 4, precision)
intervalOptions3 = createIntervalOptions(solutionAndNegative, 4, precision)
intervalOptions4 = createIntervalOptions(solutionAndNegative, 4, precision)

displayStem = 'Solve the linear inequality below. Then, choose the constant and interval combination that describes the solution set.'

problemType = random.randint(0,3)

if problemType == 0:
    displayProblem = '%s < %s \\leq %s' %(AndInequalityLeft, AndInequalityMiddle, AndInequalityRight)
    solution = ["(a, b]", "* $(%.2f, %.2f]$, which is the correct option." %(solutionEndpoints[0], solutionEndpoints[1]), 1]
    displaySolution =  "(%.2f, %.2f]" %(solutionEndpoints[0], solutionEndpoints[1])
    distractor1 = ["[a, b)", "$[%.2f, %.2f)$, which corresponds to flipping the inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor2 = ["(-\\infty, a) \\cup [b, \\infty)", "$(-\\infty, %.2f) \\cup [%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor3 = ["(-\\infty, a] \\cup (b, \\infty)", "$(-\\infty, %.2f] \\cup (%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality AND flipping the inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor4 = ["\\text{None of the above.}", "", "This corresponds to thinking that the values were not correct.", 0]
    answerList = [solution, distractor1, distractor2, distractor3]
    random.shuffle(answerList)
    answerList.append(distractor4)
elif problemType == 1:
    displayProblem = '%s \\leq %s < %s' %(AndInequalityLeft, AndInequalityMiddle, AndInequalityRight)
    solution = ["[a, b)", "$[%.2f, %.2f)$, which is the correct option." %(solutionEndpoints[0], solutionEndpoints[1]), 1]
    displaySolution =  "[%.2f, %.2f)" %(solutionEndpoints[0], solutionEndpoints[1])
    distractor1 = ["(a, b]", "$(%.2f, %.2f]$, which corresponds to flipping the inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor2 = ["(-\\infty, a] \\cup (b, \\infty)", "$(-\\infty, %.2f] \\cup (%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor3 = ["(-\\infty, a) \\cup [b, \\infty)", "$(-\\infty, %.2f) \\cup [%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality AND flipping the inequality." %(solutionEndpoints[0], solutionEndpoints[1]), 0]
    distractor4 = ["\\text{None of the above.}", "", "This corresponds to thinking that the values were not correct.", 0]
    answerList = [solution, distractor1, distractor2, distractor3]
    random.shuffle(answerList)
    answerList.append(distractor4)
elif problemType == 2:
    displayProblem = '%s < %s \\leq %s' %(AndInequalityLeft, AndInequalityMiddle, AndInequalityRight)
    distractor4 = ["(a, b]", "$(%.2f, %.2f]$, which is the correct interval but negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor1 = ["[a, b)", "$[%.2f, %.2f)$, which corresponds to flipping the inequality and getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor2 = ["(-\\infty, a) \\cup [b, \\infty)", "$(-\\infty, %.2f) \\cup [%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality and getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor3 = ["(-\\infty, a] \\cup (b, \\infty)", "$(-\\infty, %.2f] \\cup (%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality AND flipping the inequality AND getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    solution = ["\\text{None of the above.}", "* This is correct as the answer should be $(%.2f, %.2f]$." %(solutionEndpoints[0], solutionEndpoints[1]), 1]
    displaySolution = solution[0]
    answerList = [distractor4, distractor1, distractor2, distractor3]
    random.shuffle(answerList)
    answerList.append(solution)
else:
    displayProblem = '%s \\leq %s < %s' %(AndInequalityLeft, AndInequalityMiddle, AndInequalityRight)
    distractor4 = ["[a, b)", "$[%.2f, %.2f)$, which is the correct interval but negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor1 = ["(a, b]", "$(%.2f, %.2f]$, which corresponds to flipping the inequality and getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor2 = ["(-\\infty, a] \\cup (b, \\infty)", "$(-\\infty, %.2f] \\cup (%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality and getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    distractor3 = ["(-\\infty, a) \\cup [b, \\infty)", "$(-\\infty, %.2f) \\cup [%.2f, \\infty)$, which corresponds to displaying the and-inequality as an or-inequality AND flipping the inequality AND getting negatives of the actual endpoints." %(-solutionEndpoints[0], -solutionEndpoints[1]), 0]
    solution = ["\\text{None of the above.}", "* This is correct as the answer should be $[%.2f, %.2f)$." %(solutionEndpoints[0], solutionEndpoints[1]), 1]
    displaySolution = solution[0]
    answerList = [distractor4, distractor1, distractor2, distractor3]
    random.shuffle(answerList)
    answerList.append(solution)

generalComment = "To solve, you will need to break up the compound inequality into two inequalities. Be sure to keep track of the inequality! It may be best to draw a number line and graph your solution."

if problemType == 0 or problemType == 1:
    c0 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[0][0], intervalOptions1[0][0][0], intervalOptions1[0][0][1], intervalOptions1[0][1][0], intervalOptions1[0][1][1])
    c1 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[1][0], intervalOptions2[0][0][0], intervalOptions2[0][0][1], intervalOptions2[0][1][0], intervalOptions2[0][1][1])
    c2 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[2][0], intervalOptions3[0][0][0], intervalOptions3[0][0][1], intervalOptions3[0][1][0], intervalOptions3[0][1][1])
    c3 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0], intervalOptions4[0][0][0], intervalOptions4[0][0][1], intervalOptions4[0][1][0], intervalOptions4[0][1][1])
    c4 = "%s" %answerList[4][0]
else:
    c0 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[0][0], intervalOptions1[1][0][0], intervalOptions1[1][0][1], intervalOptions1[1][1][0], intervalOptions1[1][1][1])
    c1 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[1][0], intervalOptions2[1][0][0], intervalOptions2[1][0][1], intervalOptions2[1][1][0], intervalOptions2[1][1][1])
    c2 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[2][0], intervalOptions3[1][0][0], intervalOptions3[1][0][1], intervalOptions3[1][1][0], intervalOptions3[1][1][1])
    c3 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0], intervalOptions4[1][0][0], intervalOptions4[1][0][1], intervalOptions4[1][1][0], intervalOptions4[1][1][1])
    c4 = "%s" %answerList[4][0]

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
