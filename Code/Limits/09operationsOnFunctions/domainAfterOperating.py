import sys
import random
from math import gcd

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

def generateFunctionClasses(operation):
    functionClass = ["Polynomial", "Radical", "Rational"]
    random.shuffle(functionClass)

    function1Class = functionClass[int(random.randint(0, 2))]
    function2Class = functionClass[int(random.randint(0, 2))]

    if (operation == "Multiply"):
        # Removes Poly x Rational or Rational x Poly
        while ((function1Class=="Polynomial" and function2Class == "Rational") or (function1Class=="Rational" and function2Class == "Polynomial")):
            function1Class = functionClass[int(random.randint(0, 2))]
            function2Class = functionClass[int(random.randint(0, 2))]
    #For the future
    elif (operation == "Divide"):
        # Removes Rational equations from function options
        function1Class = functionClass[int(random.randint(0, 1))]
        function2Class = functionClass[int(random.randint(0, 1))]
    else:
        function1Class = functionClass[int(random.randint(0, 2))]
        function2Class = functionClass[int(random.randint(0, 2))]

    return [function1Class, function2Class]

def generateFunctionAndDomain(functionClass):
    #functionClass = {"Polynomial", "Radical", "Rational"}
    if (functionClass=="Polynomial"):
        degree = random.randint(1, 4)
        if degree == 1:
            coefficients = [random.randint(1, 9), random.randint(0, 9)]
            function = generatePolynomialDisplay(coefficients)
        elif degree == 2:
            coefficients = [random.randint(1, 9), random.randint(0, 9), random.randint(0, 9)]
            function = generatePolynomialDisplay(coefficients)
        elif degree == 3:
            coefficients = [random.randint(1, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
            function = generatePolynomialDisplay(coefficients)
        else:
            coefficients = [random.randint(1, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
            function = generatePolynomialDisplay(coefficients)
        return [function, "RR"]

    elif (functionClass == "Rational"):
        numerator = random.randint(1, 5)
        a = random.randint(3, 6)
        b = maybeMakeNegative(a*random.randint(3, 6) + random.randint(1, 6))
        while (not(gcd(a, b)==1)):
            a = random.randint(3, 6)
            b = maybeMakeNegative(a*random.randint(3, 6) + random.randint(1, 6))
        excludeFromDomain = float(-b)/float(a)
        if (b<0):
            function = "\\frac{%d}{%dx-%d}" %(numerator, a, -b)
        else:
            function = "\\frac{%d}{%dx+%d}" %(numerator, a, b)
        return [function, excludeFromDomain]

    else:
        a = float(maybeMakeNegative(random.randint(3, 6)))
        b = float(maybeMakeNegative(a*random.randint(3, 6) + random.randint(1, 6)))
        excludeFromDomain = float(-b)/float(a)
        if (a>0):
            inequalityDirection = "geq"
        else:
            inequalityDirection = "leq"
        if (b<0):
            function = "\\sqrt{%dx-%d} " %(a, -b)
        else:
            function = "\\sqrt{%dx+%d} " %(a, b)
        return [function, excludeFromDomain, inequalityDirection]

def determineOperatedFunctionsInfo(function1, function2):
#Possibilities:
    #Poly, Poly
    if (function1[1]=="RR" and function2[1]=="RR"):
        return ["RR"]

    #Poly, Radical or Poly, Rational
    elif (function1[1]=="RR" and not(function2[1]=="RR")):
        return function2

    #Radical, Poly or Rational, Poly
    elif (function2[1]=="RR" and not(function1[1]=="RR")):
        return function1

    #Radical, Radical excluded
    #Radical, Rational
    #Excluded for now

    #Rational, Radical
    #Excluded for now

    #Rational, Rational
    else:
        # We need to include placeholders to make the return long enough to be distinct from the others
        return [function1, function2, 0, 0]

def domainOfFunctions(operatedFunctionInfo):
    #Poly/Poly
    if (len(operatedFunctionInfo)==1):
        message = "\\text{ The domain is all Real numbers. }"
        return [message]

    #Poly/Rational, Rational/Poly
    elif (len(operatedFunctionInfo)==2):
        message = "\\text{ The domain is all Real numbers except } x = a"
        interval = createIntervalOptions([float(operatedFunctionInfo[1])], 5, 1)
        return [message, operatedFunctionInfo[1], interval]

    #Poly/Radical, Radical/Poly
    elif (len(operatedFunctionInfo)==3):
        if (operatedFunctionInfo[2] == "geq"):
            message = "\\text{ The domain is all Real numbers greater than or equal to } x = a"
            interval = createIntervalOptions([float(operatedFunctionInfo[1])], 5, 1)
            return [message, operatedFunctionInfo[1], interval]
        else:
            message = "\\text{ The domain is all Real numbers less than or equal to } x = a"
            interval = createIntervalOptions([operatedFunctionInfo[1]], 5, 1)
            return [message, operatedFunctionInfo[1], interval]

    #Rational/Rational
    else:
        message1 = "\\text{ The domain is all Real numbers except } x = a \\text{ and } x = b"
        message2 = "\\text{ and } b \\in "
        interval1 = createIntervalOptions([float(operatedFunctionInfo[0][1])], 5, 1)
        interval2 = createIntervalOptions([float(operatedFunctionInfo[1][1])], 5, 1)
        return [message1, message2, operatedFunctionInfo[0][1], operatedFunctionInfo[1][1], interval1, interval2]

def randomRationalDomain():
    f = generateFunctionAndDomain("Rational")
    domain = domainOfFunctions(f)
    return domain

def randomRadicalDomain(inequalityDirection):
    f = generateFunctionAndDomain("Radical")
    while (not (f[2] == inequalityDirection) ):
        f = generateFunctionAndDomain("Radical")
    domain = domainOfFunctions(f)
    return domain

def randomDoubleRationalDomain():
    f = generateFunctionAndDomain("Rational")
    g = generateFunctionAndDomain("Rational")

    info = [f, g, 0, 0]
    domain = domainOfFunctions(info)
    return domain

# BEGIN
#For now, remove "Divide"
operationList = ["Add", "Subtract", "Multiply"]
random.shuffle(operationList)

operation = operationList[int(random.randint(0, 2))]
functionClasses = generateFunctionClasses(operation)
while ((functionClasses[0] == "Radical" and functionClasses[1] == "Radical") or (functionClasses[0] == "Rational" and functionClasses[1] == "Radical") or (functionClasses[0] == "Radical" and functionClasses[1] == "Rational")):
    functionClasses = generateFunctionClasses(operation)

function1 = generateFunctionAndDomain(functionClasses[0])
function2 = generateFunctionAndDomain(functionClasses[1])

operatedFunctionInfo = determineOperatedFunctionsInfo(function1, function2)
solution = domainOfFunctions(operatedFunctionInfo)
solution.append("* This is the solution!")

#Poly/Poly
if (len(operatedFunctionInfo)==1):
    distractor1 = randomRationalDomain()
    distractor2 = randomRadicalDomain("leq")
    distractor3 = randomRadicalDomain("geq")

    # Shuffles all answers that have a single interval to input
    answerList = [distractor1, distractor2, distractor3]
    random.shuffle(answerList)

    # 4th option always has 2 intervals to input
    distractor4 = randomDoubleRationalDomain()
    answerList.append(distractor4)

    # Final answer is Domain of all real numbers
    displaySolution = "(-\\infty, \\infty)"
    answerList.append(solution)
    answerLetter = "E"

#Poly/Rational, Rational/Poly
elif (len(operatedFunctionInfo)==2):
    distractor1 = randomRadicalDomain("leq")
    distractor2 = randomRadicalDomain("geq")
    displaySolution = "\\text{ The domain is all Real numbers except } x = %s" %round(solution[1], 2)

    # Shuffles all answers that have a single interval to input
    preparingAnswerList = [[distractor1, 0], [distractor2, 0], [solution, 1]]
    random.shuffle(preparingAnswerList)
    answerIndex = 0
    letters = ["A", "B", "C"]
    for checkLetter in letters:
        if preparingAnswerList[answerIndex][1] == 1:
            answerLetter = letters[answerIndex]
            break
        answerIndex = answerIndex+1
    answerList=[preparingAnswerList[0][0], preparingAnswerList[1][0], preparingAnswerList[2][0]]

    # 4th option always has 2 intervals to input
    distractor3 = randomDoubleRationalDomain()
    answerList.append(distractor3)

    # Final answer is Domain of all real numbers
    distractor4 = domainOfFunctions(["RR"])
    answerList.append(distractor4)

#Poly/Radical, Radical/Poly
elif (len(operatedFunctionInfo)==3):
    if (operatedFunctionInfo[2] == "geq"):
        distractor1 = randomRationalDomain()
        distractor2 = randomRadicalDomain("leq")
        displaySolution = "\\text{ The domain is all Real numbers greater than or equal to} x = %s." %round(solution[1], 2)

        # Shuffles all answers that have a single interval to input
        preparingAnswerList = [[distractor1, 0], [distractor2, 0], [solution, 1]]
        random.shuffle(preparingAnswerList)
        answerIndex = 0
        letters = ["A", "B", "C"]
        for checkLetter in letters:
            if preparingAnswerList[answerIndex][1] == 1:
                answerLetter = letters[answerIndex]
                break
            answerIndex = answerIndex+1
        answerList=[preparingAnswerList[0][0], preparingAnswerList[1][0], preparingAnswerList[2][0]]

        # 4th option always has 2 intervals to input
        distractor3 = randomDoubleRationalDomain()
        answerList.append(distractor3)

        # Final answer is Domain of all real numbers
        distractor4 = domainOfFunctions(["RR"])
        answerList.append(distractor4)

    else:
        distractor1 = randomRationalDomain()
        distractor2 = randomRadicalDomain("geq")
        displaySolution = "\\text{ The domain is all Real numbers less than or equal to} x = %s." %round(solution[1], 2)

        # Shuffles all answers that have a single interval to input
        preparingAnswerList = [[distractor1, 0], [distractor2, 0], [solution, 1]]
        random.shuffle(preparingAnswerList)
        answerIndex = 0
        letters = ["A", "B", "C"]
        for checkLetter in letters:
            if preparingAnswerList[answerIndex][1] == 1:
                answerLetter = letters[answerIndex]
                break
            answerIndex = answerIndex+1
        answerList=[preparingAnswerList[0][0], preparingAnswerList[1][0], preparingAnswerList[2][0]]

        # 4th option always has 2 intervals to input
        distractor3 = randomDoubleRationalDomain()
        answerList.append(distractor3)

        # Final answer is Domain of all real numbers
        distractor4 = domainOfFunctions(["RR"])
        answerList.append(distractor4)

#Rational/Rational
else:
    #In the future, this should grab functions from the double and put them into the singles.
    distractor1 = randomRationalDomain()
    distractor2 = randomRadicalDomain("leq")
    distractor3 = randomRadicalDomain("geq")

    # Shuffles all answers that have a single interval to input
    answerList = [distractor1, distractor2, distractor3]
    random.shuffle(answerList)

    # 4th option always has 2 intervals to input
    answerList.append(solution)
    displaySolution = "\\text{ The domain is all Real numbers except } x = %s \\text{ and } x = %s" %(round(solution[2], 2), round(solution[3], 2))
    answerLetter = "D"
    # Final answer is Domain of all real numbers
    distractor4 = domainOfFunctions(["RR"])
    answerList.append(distractor4)

displayFunction1 = function1[0]
displayFunction2 = function2[0]

# In the future, this should have 10 options
if response_type=="Multiple-Choice":
	displayStem = f"{operation} the following functions, then choose the domain of the resulting function from the list below." 
else:
	displayStem=f"{operation} the following functions and write the domain of the resulting function."
displayProblem = "f(x) = %s \\text{ and } g(x) = %s" %(displayFunction1, displayFunction2)
generalComment = "The new domain is the intersection of the previous domains."

c0 = "%s, \\text{ where } a \\in [%s, %s]" %(answerList[0][0], answerList[0][2][0][0], answerList[0][2][0][1])
c1 = "%s, \\text{ where } a \\in [%s, %s]" %(answerList[1][0], answerList[1][2][0][0], answerList[1][2][0][1])
c2 = "%s, \\text{ where } a \\in [%s, %s]" %(answerList[2][0], answerList[2][2][0][0], answerList[2][2][0][1])
c3 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0], answerList[3][4][0][0], answerList[3][4][0][1], answerList[3][5][0][0], answerList[3][5][0][1])
c4 = "%s" %answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = ["", "", "", "", ""]

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
