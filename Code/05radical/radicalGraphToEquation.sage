import numpy
import math
import random
import matplotlib.pyplot as plt

def cubeRootThis(value):
    if value > 0:
        return (value)**(1./3.)
    else:
        return -(-value)**(1./3.)

def sketchFunctionAndPoint(graphX, graphY, pointOfInterest, figureName):
    SMALL_SIZE = 24
    MEDIUM_SIZE = 28
    BIGGER_SIZE = 32

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.figure(1)
    plt.subplot(111)
    plt.plot(graphX, graphY, linewidth = 5)

    plt.subplot(111)
    plt.plot( [ pointOfInterest[0] ], [ pointOfInterest[1] ], 'bs')

    #plt.rcParams.update({'font.size': 22})
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('../Figures/' + str(figureName) + str(version) + '.png', bbox_inches='tight')
    plt.close()

def createFunctionAndPointOfInterest():
    rootDegree = random.randint(2, 3)
    #rootDegree = 2
    coefficient = maybeMakeNegative(1)
    a = 1
    b = maybeMakeNegative(random.randint(3, 7))*2
    #while gcd(abs(a), abs(b)) == 1:
        #a = maybeMakeNegative(random.randint(3, 7))
        #b = maybeMakeNegative(random.randint(3, 7))
    k = maybeMakeNegative(random.randint(3, 7))
    fa = float(a)
    fb = float(b)
    pointOfInterest = [fb/fa, k]
    if rootDegree == 2:
        if a > 0:
            xPlot = numpy.arange(pointOfInterest[0], pointOfInterest[0]+4, 0.05)
        else:
            xPlot = numpy.arange(pointOfInterest[0]-4, pointOfInterest[0], 0.05)
        equation = [coefficient * math.sqrt(xPlot[i] - fb) + k for i in range(len(xPlot)) ]
    else:
        xPlot = numpy.arange(pointOfInterest[0]-3, pointOfInterest[0]+3, 0.05)
        equation = [coefficient * cubeRootThis(xPlot[i] - fb) + k for i in range(len(xPlot)) ]
    figureName = "radicalGraphToEquation%s" %version
    sketchFunctionAndPoint(xPlot, equation, pointOfInterest, figureName)
    return [rootDegree, coefficient, pointOfInterest]

def displayEquation(rootDegree, coefficient, pointOfInterest):
    if rootDegree == 2:
        if pointOfInterest[0] < 0:
            if pointOfInterest[1] < 0:
                if coefficient < 0:
                    equation = "- \\sqrt{x + %d} - %d" %(-pointOfInterest[0], -pointOfInterest[1])
                else:
                    equation = "\\sqrt{x + %d} - %d" %(-pointOfInterest[0], -pointOfInterest[1])
            else:
                if coefficient < 0:
                    equation = "- \\sqrt{x + %d} + %s" %(-pointOfInterest[0], pointOfInterest[1])
                else:
                    equation = "\\sqrt{x + %d} + %d" %(-pointOfInterest[0], pointOfInterest[1])
        else:
            if pointOfInterest[1] < 0:
                if coefficient < 0:
                    equation = "- \\sqrt{x - %d} - %d" %(pointOfInterest[0], -pointOfInterest[1])
                else:
                    equation = "\\sqrt{x - %d} - %d" %(pointOfInterest[0], -pointOfInterest[1])
            else:
                if coefficient < 0:
                    equation = "- \\sqrt{x - %d} + %d" %(pointOfInterest[0], pointOfInterest[1])
                else:
                    equation = "\\sqrt{x - %d} + %d" %(pointOfInterest[0], pointOfInterest[1])
    else:
        if pointOfInterest[0] < 0:
            if pointOfInterest[1] < 0:
                if coefficient < 0:
                    equation = "- \\sqrt[3]{x + %d} - %s" %(-pointOfInterest[0], -pointOfInterest[1])
                else:
                    equation = "\\sqrt[3]{x + %d} - %d" %(-pointOfInterest[0], -pointOfInterest[1])
            else:
                if coefficient < 0:
                    equation = "- \\sqrt[3]{x + %d} + %s" %(-pointOfInterest[0], pointOfInterest[1])
                else:
                    equation = "\\sqrt[3]{x + %d} + %d" %(-pointOfInterest[0], pointOfInterest[1])
        else:
            if pointOfInterest[1] < 0:
                if coefficient < 0:
                    equation = "- \\sqrt[3]{x - %d} - %d" %(pointOfInterest[0], -pointOfInterest[1])
                else:
                    equation = "\\sqrt[3]{x - %d} - %d" %(pointOfInterest[0], -pointOfInterest[1])
            else:
                if coefficient < 0:
                    equation = "- \\sqrt[3]{x - %d} + %d" %(pointOfInterest[0], pointOfInterest[1])
                else:
                    equation = "\\sqrt[3]{x - %d} + %d" %(pointOfInterest[0], pointOfInterest[1])
    return equation

def createDistractors(rootDegree, coefficient, pointOfInterest):
    displayDistractor1 = displayEquation(rootDegree, -coefficient, [pointOfInterest[0], pointOfInterest[1]])
    distractor1 = [ displayDistractor1, "This corresponds to switching the coefficient and having the correct vertex with the root degree as $%d$." %rootDegree, 0]
    #
    displayDistractor2 = displayEquation(rootDegree, coefficient, [-pointOfInterest[0], pointOfInterest[1]] )
    distractor2 = [displayDistractor2, "This corresponds to the correct coefficient and switching the $x$-value of the vertex with the root degree as $%d$." %rootDegree, 0]
    #
    displayDistractor3 = displayEquation(rootDegree, -coefficient, [-pointOfInterest[0], pointOfInterest[1]])
    distractor3 = [displayDistractor3, "This corresponds to switching the coefficient AND switching the $x$-value of the vertex with the root degree as $%d$." %rootDegree, 0]
    return [distractor1, distractor2, distractor3]

##### END OF DEFINITIONS #####
goodGraphOrNot = random.randint(0, 1)
if goodGraphOrNot == 0:
    rootDegree, coefficient, pointOfInterest = createFunctionAndPointOfInterest()
    solution = [displayEquation(rootDegree, coefficient, pointOfInterest), "* This is the correct option.", 1]
    distractor1, distractor2, distractor3 = createDistractors(rootDegree, coefficient, pointOfInterest)
    displayProblem = "\\text{Graph of the function } f(x) = %s" %solution[0]
    displaySolution = solution[0]
    figureName = "radicalGraphToEquation"
    optionList = [solution, distractor1, distractor2, distractor3]
    random.shuffle(optionList)
    choices = ["f(x) = %s" %optionList[0][0], "f(x) = %s" %optionList[1][0], "f(x) = %s" %optionList[2][0], "f(x) = %s" %optionList[3][0], "\\text{None of the above}"]
    choiceComments = [optionList[0][1], optionList[1][1], optionList[2][1], optionList[3][1], "You likely though the graphs did not match the power of the radical."]
    answerIndex = 0
    letters = ["A", "B", "C", "D"]
    for checkLetter in letters:
        if optionList[answerIndex][2] == 1:
            answerLetter = letters[answerIndex]
            break
        answerIndex = answerIndex+1
else:
    rootDegree, coefficient, pointOfInterest = createFunctionAndPointOfInterest()
    if rootDegree == 2:
        newRootDegree = 3
    else:
        newRootDegree =2
    displaySolutionEquation = displayEquation(newRootDegree, coefficient, pointOfInterest)
    solution = [displaySolutionEquation, "This would be the correct option if the root degree was $%d$." %rootDegree, 0]
    distractor1, distractor2, distractor3 = createDistractors(newRootDegree, coefficient, pointOfInterest)
    displayProblem = "\\text{Graph of the function } f(x) = %s" %displayEquation(rootDegree, coefficient, pointOfInterest)
    displaySolution = "\\text{None of the above}"
    figureName = "radicalGraphToEquation" 
    optionList = [solution, distractor1, distractor2, distractor3]
    random.shuffle(optionList)
    choices = ["f(x) = %s" %optionList[0][0], "f(x) = %s" %optionList[1][0], "f(x) = %s" %optionList[2][0], "f(x) = %s" %optionList[3][0], "\\text{None of the above}"]
    choiceComments = [optionList[0][1], optionList[1][1], optionList[2][1], optionList[3][1], "* This is correct! The general shape of the graph is not correct for the radical power."]
    answerLetter = "E"

displayStem = "Choose the equation of the function graphed below."
generalComment = "General Comments: Remember that the general form of a radical equation is $ f(x) = a \\sqrt[b]{x - h} + k$, where $a$ is the leading coefficient (and in this case, we assume is either $1$ or $-1$), $b$ is the root degree (in this case, either $2$ or $3$), and $(h, k)$ is the vertex."

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
