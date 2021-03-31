import sys
import random
import numpy

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

### DEFINITIONS ###
def generateCoefficients():    # Create an array of 6 distinct naturals, then make some integers
    coefficients = [0,0,0,0,0,0]
    OneSolutionCheck = 0
    while (OneSolutionCheck == 0):    # Makes sure there is exactly one solution
        coefficients = random.sample(range(2, 20), 6) # ensures all coefficients are distinct
        coefficients[0] = -coefficients[0] # to ensure a distractor for distribution of negative incorrectly
        coefficients[1] = maybeMakeNegative(coefficients[1])
        coefficients[2] = maybeMakeNegative(coefficients[2])
        coefficients[3] = -coefficients[3] # to ensure a distractor for distribution of negative incorrectly
        coefficients[4] = maybeMakeNegative(coefficients[4])
        coefficients[5] = maybeMakeNegative(coefficients[5])
        OneSolutionCheck = coefficients[0]*coefficients[2] - coefficients[3]*coefficients[4] # checks that the coefficient for resulting linear equation is nonzero
    return coefficients
def generateSolution(coefficients):
    a, b, c, d, e, f = coefficients
    eq1 = numpy.poly1d([a*b, a*c])
    eq2 = numpy.poly1d([d*e, d*f])
    basicLinearEquation = eq1 - eq2
    solution = basicLinearEquation.r
    if len(solution) == 0:
        solution=[0]
    return solution[0]
def generateDistractors(coefficients):
    a, b, c, d, e, f = coefficients
    distractor1 = generateSolution([a, b, -c, d, e, f])    # not distributing the negative in front of the first parentheses correctly
    distractor2 = generateSolution([a, b, c, d, e, -f])    # not distributing the negative in front of the second parentheses correctly
    distractor3 = generateSolution([-a, b, c, d, e, f])    # negative of the actual solution
    return [distractor1, distractor2, distractor3]
### VARIABLE DECLARATIONS ###
coefficients = generateCoefficients()
solution = generateSolution(coefficients)
distractor1, distractor2, distractor3 = generateDistractors(coefficients)
solutionList = [solution, distractor1, distractor2, distractor3]
### CREATE INTERVAL OPTIONS ###
intervalOptions = createIntervalOptions(solutionList, 3, 1)
### DEFINE ANSWER LIST AND DISPLAY SOLUTION ###
displaySolution = "x = %.3f" %solution
option1 = ["x \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1]), "* $x = %.3f$, which is the correct option." %solution, 1]
option2 = ["x \\in [%s, %s]" %(intervalOptions[1][0], intervalOptions[1][1]), "$x = %.3f$, which corresponds to not distributing the negative in front of the first parentheses correctly." %distractor1, 0]
option3 = ["x \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1]), "$x = %.3f$, which corresponds to not distributing the negative in front of the second parentheses correctly." %distractor2, 0]
option4 = ["x \\in [%s, %s]" %(intervalOptions[3][0], intervalOptions[3][1]), "$x = %.3f$, which corresponds to getting the negative of the actual solution." %distractor3, 0]
option5 = ["\\text{There are no real solutions.}", "Corresponds to students thinking a fraction means there is no solution to the equation.", 0]
answerList = [option1, option2, option3, option4]
random.shuffle(answerList)
answerList.append(option5)
### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)
### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
if response_type=="Multiple-Choice":
    displayStem = 'Solve the equation below. Then, choose the interval that contains the solution.'
else:
    displayStem = 'Solve the equation below.'
displayProblem = "%d(%s) = %d(%s)" %(coefficients[0], generatePolynomialDisplay([coefficients[1], coefficients[2]]), coefficients[3], generatePolynomialDisplay([coefficients[4], coefficients[5]]))
generalComment = "The most common mistake on this question is to not distribute the negative in front of the second fraction correctly. The best way to avoid this is putting the numerator in parentheses, which will help you remember to distribute the negative correctly."

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
