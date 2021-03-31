import sys
import random
from sympy.abc import x

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

intervalRange = 5
precision = 1

def defineFunctionAndMaybeInverse():
    classesOfFunctions = ["degree2Poly", "radical", "degree3Poly"]
    # degree3Poly broken right now. Getting ValueError: non-integer stop for randrange()
    type = classesOfFunctions[random.randint(0, 1)]
    a = random.randint(2, 5)
    b = maybeMakeNegative(random.randint(2, 5))
    while (abs(a)==abs(b)):
        a = random.randint(2, 5)
        b = maybeMakeNegative(random.randint(2, 5))
    if (type=="degree2Poly"):
        if b < 0:
            function = "%d x^2 - %d" %(a, -b)
        else:
            function = "%d x^2 + %d" %(a, b)
        return [function, "no", a, b]
    elif (type=="degree3Poly"):
        if b < 0:
            function = "%d x^3 - %d" %(a, -b)
        else:
            function = "%d x^3 + %d" %(a, b)
        inverseFunction = ((x-b)/a)**(1/3)
        return [function, "yes", inverseFunction, a, b, "poly"]
    elif (type == "radical"):
        function = (a*x + b)**(1/3)
        if b < 0:
            function = "\\sqrt[3]{%d x - %d}" %(a, -b)
        else:
            function = "\\sqrt[3]{%d x + %d}" %(a, b)
        inverseFunction = (x**3-b)/a
        return [function, "yes", inverseFunction, a, b, "radical"]
    else:
        return "You done fucked up this time."

# Generates distractors together
def distractorsDegree2Poly(a, b, evaluateAt):
    # Not invertible
    distractor1 = float( abs ( ( (evaluateAt-b)/a)**(1/2) ) )
    distractor2 = float( abs( ((evaluateAt+b)/a)**(1/2) ) )
    distractor3 = distractor1 + random.randint(1, 3)
    while (distractor3 == distractor1 or distractor3 == distractor2):
        distractor3 = distractor1 + random.randint(1, 3)
    distractor4 = distractor3 + random.randint(1, 3)
    while (distractor4 == distractor1 or distractor4 == distractor2 or distractor4 == distractor3):
        distractor4 = distractor3 + random.randint(1, 3)

    return [distractor1, distractor2, distractor3, distractor4]

def distractorsDegree3Poly(a, b, evaluateAt):
    # solution = ((x-b)/a)**(1/3)
    v1 = float( (evaluateAt+b)/a )
    if ( v1 < 0):
        distractor1 = -(-v1)**(1/3)
    else:
        distractor1 = (v1)**(1/3)

    v2 = float((evaluateAt-b)/(a))
    if (v2 < 0):
        distractor2 = -(-v2)**(1/3)
    else:
        distractor2 = (v2)**(1/3)

    v3 = float((evaluateAt+b)/(-a))
    if (v3<0):
        distractor3 = -(-v3)**(1/3)
    else:
        distractor3 = (v3)**(1/3)
    return [distractor1, distractor2, distractor3]

def distractorsRadical(a, b, evaluateAt):
    # solution = (x**3-b)/a
    distractor1 = float((evaluateAt**3 +b)/a)
    distractor2 = float( (evaluateAt**3 -b)/(-a) )
    distractor3 = float( (evaluateAt**3 +b)/(-a) )
    return [distractor1, distractor2, distractor3]

functionAndMaybeInverse = defineFunctionAndMaybeInverse()
evaluateAt = float(maybeMakeNegative(random.randint(10, 15)))
intervalRange = 5
precision = 1

if (functionAndMaybeInverse[1]=="no"):
    a = float(functionAndMaybeInverse[2])
    b = float(functionAndMaybeInverse[3])

    solution = ["\\text{ The function is not invertible for all Real numbers. }", "* This is the correct option.", 1]
    distractors = distractorsDegree2Poly(a, b, evaluateAt)
    solutionList = distractors
    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

    distractor1Interval = [intervalOptions[0]]
    distractor2Interval = [intervalOptions[1]]
    distractor3Interval = [intervalOptions[2]]
    distractor4Interval = [intervalOptions[3]]

    distractor1Interval.append(" Distractor 1: This corresponds to trying to find the inverse even though the function is not 1-1. ")
    distractor2Interval.append(" Distractor 2: This corresponds to finding the (nonexistent) inverse and not subtracting by the vertical shift.")
    distractor3Interval.append(" Distractor 3: This corresponds to finding the (nonexistent) inverse and dividing by a negative.")
    distractor4Interval.append(" Distractor 4: This corresponds to both distractors 2 and 3.")
    distractor1Interval.append(0)
    distractor2Interval.append(0)
    distractor3Interval.append(0)
    distractor4Interval.append(0)

    answerList = [distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
    displaySolution = solution[0]

    random.shuffle(answerList)
    answerList.append(solution)

else:
    a = float(functionAndMaybeInverse[3])
    b = float(functionAndMaybeInverse[4])

    if (functionAndMaybeInverse[5]=="poly"):
        value = float( (evaluateAt-b)/a )
        if (value<0):
            solution = float( -(-value)**(1/3) )
        else:
            solution = float( (value)**(1/3) )
        distractors = distractorsDegree3Poly(a, b, evaluateAt)

    else:
        solution = float( (evaluateAt**3-b) /a )
        distractors = distractorsRadical(a, b, evaluateAt)

    solutionList = [solution, distractors[0], distractors[1], distractors[2]]
    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

    solutionInterval = [intervalOptions[0]]
    distractor1Interval = [intervalOptions[1]]
    distractor2Interval = [intervalOptions[2]]
    distractor3Interval = [intervalOptions[3]]
    distractor4Interval = ["\\text{ The function is not invertible for all Real numbers. }"]

    solutionInterval.append("* This is the correct solution.")
    distractor1Interval.append(" Distractor 1: This corresponds to ")
    distractor2Interval.append(" This solution corresponds to distractor 2.")
    distractor3Interval.append(" This solution corresponds to distractor 3.")
    distractor4Interval.append(" This solution corresponds to distractor 4.")

    solutionInterval.append(1)
    distractor1Interval.append(0)
    distractor2Interval.append(0)
    distractor3Interval.append(0)
    distractor4Interval.append(0)

    answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
    displaySolution = solution

    random.shuffle(answerList)
    answerList.append(distractor4Interval)

evaluateAt=int(evaluateAt)
if response_type=="Multiple-Choice":
	displayStem=f"Find the inverse of the function below (if it exists). Then, evaluate the inverse at $x = {evaluateAt}$ and choose the interval that $f^{-1}({evaluateAt})$ belongs to." 
else:
	displayStem=f"Find the inverse of the function below (if it exists). If the inverse exists, evaluate the inverse at $x = {evaluateAt}$"
displayProblem = f"f(x) = {functionAndMaybeInverse[0]}" 
generalComment = "Be sure you check that the function is 1-1 before trying to find the inverse!"

c0 = "f^{-1}(%d) \\in [%s, %s]" %(evaluateAt, answerList[0][0][0], answerList[0][0][1])
c1 = "f^{-1}(%d) \\in [%s, %s]" %(evaluateAt, answerList[1][0][0], answerList[1][0][1])
c2 = "f^{-1}(%d) \\in [%s, %s]" %(evaluateAt, answerList[2][0][0], answerList[2][0][1])
c3 = "f^{-1}(%d) \\in [%s, %s]" %(evaluateAt, answerList[3][0][0], answerList[3][0][1])
c4 = answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
