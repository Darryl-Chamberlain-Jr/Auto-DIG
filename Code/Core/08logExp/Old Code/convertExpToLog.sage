# OBJECTIVE 2 - Covert between logarithmic and exponential forms.
import random
load("../Code/generalPurposeMethods.sage")
# Type 1 - Logarithmic to Exponential

# Base form: \sage{base}^x = \frac{1}{\sage{denominator}}
# 1 / (b**a) = b**x
# x = -a

def generatePair():
    base = random.randint(4, 7)
    exponent = random.randint(2, 3)
    while (base == exponent):
        base = random.randint(4, 7)
        exponent = random.randint(2, 3)
    return [base, exponent]

def generateSolution(pair):
    base, exponent = pair
    solution = -exponent
    return solution

def distractorSolutionReverse(pair):
    base, exponent = pair
    solution = -base
    return solution

def distractorSolutionPositiveExponent(pair):
    base, exponent = pair
    solution = exponent
    return solution

def distractorSolutionPositiveBase(pair):
    base, exponent = pair
    solution = base
    return solution

def generateSolutionInterval(solution, intervalRange):
    interval = createInterval(solution, intervalRange)
    return interval

def intervalToString(interval):
    return ['x \in [%s,%s]' %(interval[0], interval[1])]

# \sage{base}^x = \frac{1}{\sage{denominator}}
intervalRange = 2
pair = generatePair()
base = pair[0]
denominator = pair[0]**pair[1]
solution = generateSolution(pair)
solutionInterval = intervalToString(generateSolutionInterval(float(solution), intervalRange))

distractor1 = distractorSolutionReverse(pair)
distractor2 = distractorSolutionPositiveExponent(pair)
distractor3 = distractorSolutionPositiveBase(pair)
#distractor4

solutionList = [solution, distractor1, distractor2, distractor3]
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = intervalToString(intervalOptions[0])
distractor1Interval = intervalToString(intervalOptions[1])
distractor2Interval = intervalToString(intervalOptions[2])
distractor3Interval = intervalToString(intervalOptions[3])
#distractor4Interval = ['\\text{There is no solution to the equation.}']

solutionInterval.append('* This is the real solution')
distractor1Interval.append(' Distractor 1: Corresponds to mixing the base and exponent when converting.')
distractor2Interval.append(' Distractor 2: Corresponds to leaving off the negative of the exponent answer.')
distractor3Interval.append(' Distractor 3: Corresponds to mixing the base and exponent when converting AND making the result positive.')
#distractor4Interval.append(' This is a distractor')
answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)
answerList.append('There is no solution to the equation.')

c0 = answerList[0][0]
c1 = answerList[1][0]
c2 = answerList[2][0]
c3 = answerList[3][0]
c4 = "\\text{There is no solution to the equation.}"
choices = [c0, c1, c2, c3, c4]
choiceComments =  [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], "This corresponds to believing the exponential functional cannot be solved."]

displayStem = 'Convert the exponential function below to a logarithmic function in order to solve for $x$. Then, choose the interval $x$ belongs to (if it exists).'
displayProblem = '%d^x = \\frac{1}{%d}' %(base, denominator)
displaySolution = "x = %d" %solution
generalComments = "General Comments: The most common issue on this question is to not convert correctly."

writeQuestionToFile(moduleNumber, version, problemNumber, displayStem, displayProblem)
writeSolutionAndOptionsToFile(moduleNumber, version, displaySolution, choices, choiceComments)
writeCommentsToFile(moduleNumber, version, generalComments)

print "I finished Module 8, Objective 2, Type 2, Master"
