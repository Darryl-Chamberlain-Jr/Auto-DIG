# Module 5 - Radical Equations
    # Objective 1 - Identify the domain on which a radical function is not defined.
    # Objective 2 - Identify the graph of a radical function.
        # Two types of questions:
            # Graph to equation
            # Equation to graph
    # Objective 3 - Solve radical equations that lead to linear equations.
    # Objective 4 - Solve radical equations that lead to quadratic equations.

import numpy
import math
import random
import matplotlib.pyplot as plt

def cubeRootThis(value):
    if value > 0:
        return (value)**(1./3.)
    else:
        return -(-value)**(1./3.)

def sketchFunctionAndPoint(rootDegree, coefficient, pointOfInterest, figureName, optionLetter):
    if rootDegree == 2:
        graphX = numpy.arange(pointOfInterest[0], pointOfInterest[0]+4, 0.05)
        graphY = [coefficient * math.sqrt(graphX[i] - pointOfInterest[0]) + pointOfInterest[1] for i in range(len(graphX)) ]
    else:
        graphX = numpy.arange(pointOfInterest[0]-3, pointOfInterest[0]+3, 0.05)
        graphY = [coefficient * cubeRootThis(graphX[i] - pointOfInterest[0]) + pointOfInterest[1] for i in range(len(graphX)) ]

    plt.figure(1)
    plt.subplot(111)
    plt.plot(graphX, graphY, linewidth = 5)

    plt.subplot(111)
    plt.plot( [ pointOfInterest[0] ], [ pointOfInterest[1] ], 'bs')

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
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('../Figures/' + str(figureName) + str(optionLetter) + '.png', bbox_inches='tight')
    plt.close()

def createFunctionAndPointOfInterest():
    rootDegree = random.randint(2, 3)
    coefficient = maybeMakeNegative(1)
    b = maybeMakeNegative(random.randint(3, 7))*2
    k = maybeMakeNegative(random.randint(3, 7))
    fb = float(b)
    pointOfInterest = [fb, k]
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
                    equation = "- \\sqrt{x + %d} + %d" %(-pointOfInterest[0], pointOfInterest[1])
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
                    equation = "- \\sqrt[3]{x + %d} - %d" %(-pointOfInterest[0], -pointOfInterest[1])
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

def createGraphs(rootDegree, coefficient, pointOfInterest, optionList, figureName):
    # Solution
    solution = [displayEquation(rootDegree, coefficient, pointOfInterest), "This is the correct option."]
    sketchFunctionAndPoint(rootDegree, coefficient, pointOfInterest, figureName, optionList[0])
    # -coefficient, [pointOfInterest[0], pointOfInterest[1]]
    distractor1 = [displayEquation(rootDegree, -coefficient, pointOfInterest), "Corresponds to switching the coefficient and having the correct vertex."]
    sketchFunctionAndPoint(rootDegree, -coefficient, pointOfInterest, figureName, optionList[1])

    # coefficient, (-pointOfInterest[0], pointOfInterest[1])
    distractor2 = [displayEquation(rootDegree, coefficient, [-pointOfInterest[0], pointOfInterest[1]]), "Corresponds to the correct coefficient and switching the $x$-value of the vertex."]
    sketchFunctionAndPoint(rootDegree, coefficient, [-pointOfInterest[0], pointOfInterest[1]], figureName, optionList[2])

    # -coefficient, (-pointOfInterest[0], pointOfInterest[1])
    distractor3 = [displayEquation(rootDegree, -coefficient, [-pointOfInterest[0], pointOfInterest[1]]), "Corresponds to switching the coefficient AND switching the $x$-value of the vertex."]
    sketchFunctionAndPoint(rootDegree, -coefficient, [-pointOfInterest[0], pointOfInterest[1]], figureName, optionList[3])

    return [solution, distractor1, distractor2, distractor3]

##### END OF DEFINITIONS #####
figureName = "radicalEquationToGraph%s" %version
optionList = ["A", "B", "C", "D"]
random.shuffle(optionList)
choices = [ "%sA" %figureName, "%sB" %figureName, "%sC" %figureName, "%sD" %figureName]
#choices = [ "%s%s" %(figureName, optionList[0]), "%s%s" %(figureName, optionList[1]), "%s%s" %(figureName, optionList[2]), "%s%s" %(figureName, optionList[3])]
rootDegree, coefficient, pointOfInterest = createFunctionAndPointOfInterest()

displaySolution = "radicalEquationToGraph%s%s" %(version, optionList[0])
shuffledCommentList = ["* This is the correct option.", "Corresponds to switching the coefficient and having the correct vertex.", "Corresponds to the correct coefficient and switching the $x$-value of the vertex.", "Corresponds to switching the coefficient AND switching the $x$-value of the vertex."]

choiceComments = ["", "", "", ""]
solution, distractor1, distractor2, distractor3 = createGraphs(rootDegree, coefficient, pointOfInterest, optionList, figureName)

displayStem = "Choose the graph of the equation below."
displayProblem = "f(x) = %s" %solution[0]
generalComment = "General Comments: Remember that the general form of a radical equation is $ f(x) = a \\sqrt[b]{x - h} + k $, where $a$ is the leading coefficient (and in this case, we assume is either 1 or -1), $b$ is the root degree (in this case, either 2 or 3), and $(h, k)$ is the vertex."
answerLetter = optionList[0]

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "Graphs", displaySolution, answerLetter, choices, choiceComments, generalComment)
