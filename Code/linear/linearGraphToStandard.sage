import numpy
from sympy.abc import x, y
from sympy import Symbol
import matplotlib.pyplot as plt

##### IMPORTANT #####
# If we just use, Sage assumes it is the Sage function (and so we have to be careful what types of values we feed it.)
# To just use the Python gcd, we import math and use math.gcd

# OBJECTIVE 1 - Constructing linear functions from points and slope
# We can make a few types of this:
    # Type 1 - Two points (zero/non-zero slope)
    # Type 2 - Another line and a point
    # Type 3 - Go from graph to equation (either slope-int or standard)
    # Future Type - Ask for Standard Form A, B, C.

# Type 3 - Graph to Standard Form
# For now, we make sure the y-intercept is an integer.
def simplifySolution(A, B, C):
    A = int(A)
    B = int(B)
    C = int(C)
    if(A < 0):
        A = -A
        B = -B
        C = -C
    aBGCD = gcd(A, B)
    bCGCD = gcd(B, C)
    mixedGCD = gcd(aBGCD, bCGCD)
    while(mixedGCD > 1):
        A = int(A/mixedGCD)
        B = int(B/mixedGCD)
        C = int(C/mixedGCD)
        aBGCD = gcd(A, B)
        bCGCD = gcd(B, C)
        mixedGCD = gcd(aBGCD, bCGCD)
    return [A, B, C]

def generateProblemAndSolution(numeratorMax, interceptMax):
    numeratorSlope = maybeMakeNegative(random.randint(2, numeratorMax))
    denominatorSlope = random.randint(2, numeratorMax)

    # Makes sure slope is rational
    while gcd(numeratorSlope, denominatorSlope) > 1:
        numeratorSlope = maybeMakeNegative(random.randint(2, numeratorMax))
        denominatorSlope = random.randint(2, numeratorMax)

    slopeGraph = float(numeratorSlope)/float(denominatorSlope)
    yInt = random.randint(-interceptMax, interceptMax)

    point2 = [denominatorSlope, slopeGraph*denominatorSlope + yInt]
    point3 = [-denominatorSlope, -slopeGraph*denominatorSlope + yInt]

    # Converts to Stadard Form
    if slopeGraph > 0:
        aOfGraph = -numeratorSlope
        bOfGraph = denominatorSlope
        cOfGraph = denominatorSlope*yInt
    else:
        aOfGraph = numeratorSlope
        bOfGraph = -denominatorSlope
        cOfGraph = -denominatorSlope*yInt
    return [simplifySolution(aOfGraph, bOfGraph, cOfGraph), [slopeGraph, yInt], point2, point3]

def distractorNegativeA(solution):
    # (-aOfGraph, -bOfGraph, -cOfGraph)
        # Student didn't make sure A is positive
    A, B, C = solution
    return [-A, -B, -C]
def distractorRemoveFractions(slopeInt):
    # (-slopeGraph, 1, yInt)
        # Student didn't remove rational coefficients
    slope, yInt = slopeInt
    return[-slope, 1, yInt]
def distractorOppositeSlope(solution):
    A, B, C = solution
    return [-B, A, (A*C)/B]
    # (- denominatorSlope, numeratorSlope*pointGraph[1], numeratorSlope*yIntBad)
        # Used opposite slope. Recalculate yInt for the opposite slope.
def distractorOppositeSlopeRemoveFractions(solution):
    A, B, C = solution
    return [-B/A, 1, (A*C)/B]

def generateSolutionInterval(solution, intervalRange):
    intervalList = [[]]*len(solution)
    for i in range(0, len(solution)):
        intervalList[i] = createInterval(solution[i], intervalRange)
    return intervalList

def displayStandardForm(coefficients):
    A, B, C = coefficients
    if B < 0:
        standardForm = "%sx - %sy = %s" %(A, -B, C)
    else:
        standardForm = "%sx + %sy = %s" %(A, B, C)
    return standardForm

# Ideas for Distractors
    # (-denominatorSlope/numeratorSlope, 1, yIntBad)
        # Student didn't remove rational coefficients

#
#########################
def plotGraph(slopeGraph, yInt, point2, point3):
    graphX = numpy.arange(-5.0, 5.0, 0.01)
    graphY = slopeGraph*graphX + yInt
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
    plt.plot(graphX, graphY, linewidth = 5, color = '#02325f')
    #
    #plt.subplot(111)
    #plt.plot([0], [yInt], 'bo')
    #
    plt.subplot(111)
    plt.plot([point2[0]], [point2[1]], 'bo', markersize=20)
    #
    plt.subplot(111)
    plt.plot([point3[0]], [point3[1]], 'bo', markersize=20)
    #
    if slopeGraph > 0:
        #plt.text(0, yInt, "[0, %s]" %yInt, fontsize=28, horizontalalignment='right')
        plt.text(point2[0], point2[1], "[%d, %d]" %(point2[0], point2[1]), fontsize=28, horizontalalignment='right')
        plt.text(point3[0], point3[1], "[%d, %d]" %(point3[0], point3[1]), fontsize=28, horizontalalignment='right')
    else:
        #plt.text(0, yInt, "[0, %s]" %yInt, fontsize=28)
        plt.text(point2[0], point2[1], "[%d, %d]" %(point2[0], point2[1]), fontsize=28)
        plt.text(point3[0], point3[1], "[%d, %d]" %(point3[0], point3[1]), fontsize=28)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('../Figures/linearGraphToStandard' + str(version) + '.png', bbox_inches='tight')
    plt.close()
    return

intervalRange = 5
numeratorMax = 5
interceptMax = 5
solution, slopeInt, point2, point3 = generateProblemAndSolution(numeratorMax, interceptMax)
plotGraph(slopeInt[0], slopeInt[1], point2, point3)

#solutionInterval = generateSolutionInterval(listToFloats(solution), intervalRange)
distractor1 = distractorNegativeA(solution)
distractor2 = simplifySolution(distractorRemoveFractions(slopeInt)[0], distractorRemoveFractions(slopeInt)[1], distractorRemoveFractions(slopeInt)[2])
distractor3 = simplifySolution(distractorOppositeSlope(solution)[0], distractorOppositeSlope(solution)[1], distractorOppositeSlope(solution)[2])
distractor4 = simplifySolution(distractorOppositeSlopeRemoveFractions(solution)[0], distractorOppositeSlopeRemoveFractions(solution)[1], distractorOppositeSlopeRemoveFractions(solution)[2])

solutionList = [solution, distractor1, distractor2, distractor3, distractor4]
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = intervalOptions[0]
distractor1Interval = intervalOptions[1]
distractor2Interval = intervalOptions[2]
distractor3Interval = intervalOptions[3]
distractor4Interval = intervalOptions[4]

solutionInterval.append("* $%s$, which is the correct option." %displayStandardForm(solution))
distractor1Interval.append(" $%s$, which corresponds to not making $A$ positive (by multiplying the equation by $-1$)." %displayStandardForm(distractor1))
distractor2Interval.append(" $%s$, which corresponds to not removing rational values." %displayStandardForm(distractor2))
distractor3Interval.append(" $%s$, which corresponds to using the opposite slope of the graph, but did everything else correctly." %displayStandardForm(distractor3))
distractor4Interval.append(" $%s$, which corresponds to using the opposite slope of the graph and not removing rational values." %displayStandardForm(distractor4))

solutionInterval.append(1)
distractor1Interval.append(0)
distractor2Interval.append(0)
distractor3Interval.append(0)
distractor4Interval.append(0)

slopeGraph, yInt = slopeInt
graphToEquation = slopeGraph * x + yInt

###########################

displayStem = 'Write the equation of the line in the graph below in Standard form $Ax+By=C$. Then, choose the intervals that contain $A, B, \\text{ and } C$.'

displaySlope = round(slopeGraph, 3)
if yInt < 0:
    equationToDisplay = "%s x - %s" %(displaySlope, -yInt)
else:
    equationToDisplay = "%s x + %s" %(displaySlope, yInt)
displayProblem = "\\text{Equation that was graphed:} f(x)= %s" %equationToDisplay

if solution[1] < 0:
    solutionFunction = "%s x - %s y" %(Integer(solution[0]), -Integer(solution[1]))
else:
    solutionFunction = "%s x + %s y" %(Integer(solution[0]), Integer(solution[1]))

displaySolution = "%s = %s" %(solutionFunction, Integer(solution[2]))

generalComment = "General Comments: Standard form is supposed to have $A > 0$ and all fractions removed."

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

c0 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1], answerList[0][1][0], answerList[0][1][1], answerList[0][2][0], answerList[0][2][1])
c1 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1], answerList[1][1][0], answerList[1][1][1], answerList[1][2][0], answerList[1][2][1])
c2 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1], answerList[2][1][0], answerList[2][1][1], answerList[2][2][0], answerList[2][2][1])
c3 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1], answerList[3][1][0], answerList[3][1][1], answerList[3][2][0], answerList[3][2][1])
c4 = "A \\in [%s, %s], \\hspace{3mm} B \\in [%s, %s], \\text{ and } \\hspace{3mm} C \\in [%s, %s]" %(answerList[4][0][0], answerList[4][0][1], answerList[4][1][0], answerList[4][1][1], answerList[4][2][0], answerList[4][2][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][3], answerList[1][3], answerList[2][3], answerList[3][3], answerList[4][3]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][4] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
