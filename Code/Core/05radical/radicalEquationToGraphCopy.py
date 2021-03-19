import sys
import numpy
import random
import matplotlib.pyplot as plt

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
    plt.plot(graphX, graphY, linewidth = 5)
    plt.plot( [ pointOfInterest[0] ], [ pointOfInterest[1] ], 'bs')
    SMALL_SIZE = 24
    MEDIUM_SIZE = 28
    BIGGER_SIZE = 32
    plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(figureName) + str(optionLetter) + str(version) + '.png', bbox_inches='tight')
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
    sketchFunctionAndPoint(rootDegree, coefficient, pointOfInterest, figureName, optionList[0])
    # THIS IS NOT AN ERROR. There is a bug that scales down the text of the graph for the first image created on this question. Running the function creation twice fixes the issue.

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
figureName = thisQuestion
optionList = ["A", "B", "C", "D"]
unshuffledOptionList = optionList
shuffledComments = [ "* This is the correct option.", "Corresponds to switching the coefficient and having the correct vertex.", "Corresponds to the correct coefficient and switching the $x$-value of the vertex.", "Corresponds to switching the coefficient AND switching the $x$-value of the vertex." ]
random.shuffle(optionList)
choices = [ "%s%s%s" %(figureName, optionList[0], version), "%s%s%s" %(figureName, optionList[1], version), "%s%s%s" %(figureName, optionList[2], version), "%s%s%s" %(figureName, optionList[3], version)]
choiceComments = commentsForGraphs(unshuffledOptionList, optionList, shuffledComments)
rootDegree, coefficient, pointOfInterest = createFunctionAndPointOfInterest()

displaySolution = "radicalEquationToGraph%s%s" %(optionList[0], version)
solution, distractor1, distractor2, distractor3 = createGraphs(rootDegree, coefficient, pointOfInterest, optionList, figureName)

displayStem = "Choose the graph of the equation below."
displayProblem = "f(x) = %s" %solution[0]
generalComment = "Remember that the general form of a radical equation is $ f(x) = a \\sqrt[b]{x - h} + k $, where $a$ is the leading coefficient (and in this case, we assume is either 1 or -1), $b$ is the root degree (in this case, either 2 or 3), and $(h, k)$ is the vertex."
answerLetter = optionList[0]

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Graph"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
