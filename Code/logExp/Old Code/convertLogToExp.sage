# OBJECTIVE 2 - Covert between logarithmic and exponential forms.

# Type 1 - Logarithmic to Exponential

# Base form: \log_{\sage{base}}x = \sage{exponent}
load("../Code/generalPurposeMethods.sage")
def generatePair():
    base = random.randint(4, 10)
    exponent = maybeMakeNegative(random.randint(2, 3))
    power0 = base**exponent
    power1 = exponent**base
    while (base == exponent or power0==power1):
        base = random.randint(4, 10)
        exponent = maybeMakeNegative(random.randint(2, 3))
        power0 = base**exponent
        power1 = exponent**base
    return [base, exponent]

def generateSolution(pair):
    base, exponent = pair
    solution = base**exponent
    return solution

def distractorSolutionReverse(pair):
    base, exponent = pair
    solution = exponent**base
    return solution

def distractorSolutionDivideByBase(pair):
    base, exponent = pair
    solution = exponent/base
    return solution

def distractorSolutionDivideByExponent(pair):
    base, exponent = pair
    solution = base/exponent
    return solution

def generateSolutionInterval(solution, intervalRange):
    interval = createInterval(solution, intervalRange)
    return interval

def intervalToString(interval):
    return ['x \\in [%s,%s]' %(interval[0], interval[1])]

# \log_{\sage{base}}x = \sage{exponent}
intervalRange = 5
pair = generatePair()
solution = generateSolution(pair)

distractor1 = distractorSolutionReverse(pair)
distractor2 = distractorSolutionDivideByBase(pair)
distractor3 = distractorSolutionDivideByExponent(pair)

solutionList = [solution, distractor1, distractor2, distractor3]
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = intervalToString(intervalOptions[0])
distractor1Interval = intervalToString(intervalOptions[1])
distractor2Interval = intervalToString(intervalOptions[2])
distractor3Interval = intervalToString(intervalOptions[3])
#distractor4Interval = ['\\text{There is no solution to the equation.}']

solutionInterval.append('* This is the correct solution.')
distractor1Interval.append(' Distractor: This corresponds to reversing the exponent and base.')
distractor2Interval.append(' Distractor: This corresponds to dividing the exponent by the base.')
distractor3Interval.append(' Distractor: This corresponds to dividing the base by the exponent.')
#distractor4Interval.append(' This corresponds to students believing they cannot solve the logarithmic equation.')

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)
answerList.append(['\\text{There is no solution to the equation.}', "This corresponds to students believing they cannot solve the logarithmic equation."] )

c0 = answerList[0][0]
c1 = answerList[1][0]
c2 = answerList[2][0]
c3 = answerList[3][0]
c4 = answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1],  answerList[3][1], answerList[4][1]]

displayStem = 'Convert the logarithmic function below to an exponential function in order to solve for $x$. Then, choose the interval $x$ belongs to (if it exists).'
displayProblem = '\\log_{%d}(x) = %d' %(pair[0], pair[1])
displaySolution = "x = %f" %solution
generalComments = "General Comments: Just be sure to convert correctly and you will get the solution."

writeQuestionToFile(moduleNumber, version, problemNumber, displayStem, displayProblem)
writeSolutionAndOptionsToFile(moduleNumber, version, displaySolution, choices, choiceComments)
writeCommentsToFile(moduleNumber, version, generalComments)

print "I finished Module 8, Objective 2, Type 1, Master"
