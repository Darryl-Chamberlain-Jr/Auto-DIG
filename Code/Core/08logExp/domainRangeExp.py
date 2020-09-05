from random import shuffle
from sympy import solve
from sympy.abc import x
import random

# OBJECTIVE 1 - Describe the domain/range of Logarithmic and Exponential functions.
#load("../Code/generalPurposeMethods.sage")
def chooseDomainOrRange():
    #shuffle wasn't working...
    listChoices = ["Domain", "Range"]
    choice = listChoices[random.randint(0, 1)]
    return choice

def chooseSignOfLeadingCoefficient():
    sign = (-1)**random.randint(0, 1)
    return sign

def generateShifting():
    h = 0
    k = 0
    while (h==0 or k==0):
        h = random.randint(-9, 9)
        k = random.randint(-9, 9)
    return [h, k]

def distractorNegateSolution(intervalPresentation):
    a, b = intervalPresentation
    return [-a, -b]

def intervalWithInfinity(solutionInterval, inclusion):
    a, b = solutionInterval
    if (a == 0) and (inclusion == "yes"):
        display = "(-\\infty, a]"
        key = "(-\\infty, %d]" %b
    elif (b == 0) and (inclusion == "yes"):
        display = "[a, \\infty)"
        key = "[%d, \\infty)" %a
    elif (a == 0) and (inclusion == "no"):
        display = "(-\\infty, a)"
        key = "(-\\infty, %d)" %b
    elif (b == 0) and (inclusion == "no"):
        display = "(a, \\infty)"
        key = "(%d, \\infty)" %a
    else:
       display = "Error"
       key = "Error"
    return [display, key]

def extractValue(solutionInterval):
    a, b = solutionInterval
    if(a == 0):
        return b
    else:
        return a

#Type 2 - Exponential
# a*e^(x-h) + k
    # a Positive
        # Domain: (-infty, infty)
        # Range: (k, infty)

    # a Negative
        # Domain: (-infty, infty)
        # Range: (-infty, -k)
intervalRange = 5
domainOrRange = chooseDomainOrRange()

a = chooseSignOfLeadingCoefficient()
shift = generateShifting()
h = shift[0]
k = shift[1]

if (domainOrRange == "Range"):
    if (a>0):
        intervalPresentation = [k, 0]
        inverseIntervalPresentation = [0, k]
        displaySolution = "(%d, \\infty)" %k
    else:
        intervalPresentation = [0, k]
        inverseIntervalPresentation = [k, 0]
        displaySolution = "(-\\infty, %d)" %k
    solution = k
    distractor1 = -k
    distractor2 = -k
    distractor3 = k
    #
    solutionList = [solution, distractor1, distractor2, distractor3]
    precision = 1
    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
    #
    solutionInterval = [intervalWithInfinity(intervalPresentation, "no")[0], intervalOptions[0], "* $%s$, which is the correct option." %intervalWithInfinity(intervalPresentation, "no")[1], 1]
    distractor1Interval = [intervalWithInfinity(distractorNegateSolution(inverseIntervalPresentation), "yes")[0], intervalOptions[1], "$%s$, which corresponds to using the negative vertical shift AND flipping the Range interval AND including the endpoint." %intervalWithInfinity(distractorNegateSolution(inverseIntervalPresentation), "yes")[1], 0]
    distractor2Interval = [intervalWithInfinity(distractorNegateSolution(inverseIntervalPresentation), "no")[0], intervalOptions[2], "$%s$, which corresponds to using the negative vertical shift AND flipping the Range interval." %intervalWithInfinity(distractorNegateSolution(inverseIntervalPresentation), "no")[1], 0]
    distractor3Interval = [intervalWithInfinity(intervalPresentation, "yes")[0], intervalOptions[3], "$%s$, which corresponds to including the endpoint." %intervalWithInfinity(intervalPresentation, "yes")[1], 0]
    distractor4Interval = ['(-\\infty, \\infty)', [' ', ' '], "This corresponds to confusing range of an exponential function with the domain of an exponential function.", 0]
    #
    answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
    random.shuffle(answerList)
    answerList.append(distractor4Interval)
    answerIndex = 0
    letters = ["A", "B", "C", "D", "E"]
    for checkLetter in letters:
        if answerList[answerIndex][3] == 1:
            answerLetter = letters[answerIndex]
            break
        answerIndex = answerIndex+1
    #
else:
    displaySolution= "(-\\infty, \\infty)"
    intervalPresentation = [0, k]
    inverseIntervalPresentation = [k, 0]
    distractor1 = -k
    distractor2 = -k
    distractor3 = k
    distractor4 = k
    #
    solutionList = [distractor1, distractor2, distractor3, distractor4]
    precision = 1
    intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)
    #
    solutionInterval = ['(-\\infty, \\infty)', [' ', ' '], "* This is the correct option.", 1]
    distractor1Interval = [intervalWithInfinity(distractorNegateSolution(inverseIntervalPresentation), "yes")[0], intervalOptions[0], "$%s$, which corresponds to using the negative vertical shift AND flipping the Range interval AND including the endpoint." %intervalWithInfinity(distractorNegateSolution(inverseIntervalPresentation), "yes")[1], 0]
    distractor2Interval = [intervalWithInfinity(distractorNegateSolution(inverseIntervalPresentation), "no")[0],intervalOptions[1], "$%s$, which corresponds to using the negative vertical shift AND flipping the Range interval." %intervalWithInfinity(distractorNegateSolution(inverseIntervalPresentation), "no")[1], 0]
    distractor3Interval = [intervalWithInfinity(intervalPresentation, "yes")[0], intervalOptions[2], "$%s$, which corresponds to using the correct vertical shift *if we wanted the Range* AND including the endpoint." %intervalWithInfinity(intervalPresentation, "yes")[1], 0]
    distractor4Interval = [intervalWithInfinity(intervalPresentation, "no")[0], intervalOptions[3], "$%s$, which corresponds to using the correct vertical shift *if we wanted the Range*." %intervalWithInfinity(intervalPresentation, "no")[1], 0]
    #
    answerList = [distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
    random.shuffle(answerList)
    answerList.append(solutionInterval)
    answerLetter = "E"

displayStem = 'Which of the following intervals describes the %s of the function below?' %domainOrRange
# Forced to display correctly
if (a<0):
    if (h<0):
        if(k<0):
            displayProblem = 'f(x) = -e^{x+%d}-%d' %(-h, -k)
        else:
            displayProblem = 'f(x) = -e^{x+%d}+%d' %(-h, k)
    else:
        if(k<0):
            displayProblem = 'f(x) = -e^{x-%d}-%d' %(h, -k)
        else:
            displayProblem = 'f(x) = -e^{x-%d}+%d' %(h, k)
else:
    if (h<0):
        if(k<0):
            displayProblem = 'f(x) = e^{x+%d}-%d' %(-h, -k)
        else:
            displayProblem = 'f(x) = e^{x+%d}+%d' %(-h, k)
    else:
        if(k<0):
            displayProblem = 'f(x) = e^{x-%d}-%d' %(h, -k)
        else:
            displayProblem = 'f(x) = e^{x-%d}+%d' %(h, k)

generalComment = "\\textbf{General Comments}: Domain of a basic exponential function is $(-\\infty, \\infty)$ while the Range is $(0, \\infty)$. We can shift these intervals [and even flip when $a<0$!] to find the new Domain/Range."
c0 = "%s, a \\in [%s, %s]" %(answerList[0][0], answerList[0][1][0], answerList[0][1][1])
c1 = "%s, a \\in [%s, %s]" %(answerList[1][0], answerList[1][1][0], answerList[1][1][1])
c2 = "%s, a \\in [%s, %s]" %(answerList[2][0], answerList[2][1][0], answerList[2][1][1])
c3 = "%s, a \\in [%s, %s]" %(answerList[3][0], answerList[3][1][0], answerList[3][1][1])
c4 = "%s" %answerList[4][0]
choices = [c0, c1, c2, c3, c4]

choiceComments = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
