### NECESSARY IMPORTS ###
import sys
from sympy import *
import numpy
import random
import math
from decimal import Decimal
import decimal
import traceback
import cmath
import matplotlib.pyplot as plt
from sympy.abc import x, y
from sympy.solvers import solve

### System variables ###
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

### Define as name of the file. This will be used for any images generated. ###
#thisQuestion="MA_8_F_1_1"

### DEFINITIONS ###
# This should list all definitions used. Be sure to check the commonly used functions file before creating a new one.
def generate_sqrt_value(value, a, h, k):
    return a*numpy.sqrt(value-h)+k

def generate_relation(parent):
    if (parent == "linear"):
        m = maybeMakeNegative(random.randint(2, 7))
        b = maybeMakeNegative(random.randint(1, 9))
        linear_equation = numpy.poly1d([m, b])
        counter = maybeMakeNegative(random.randint(1, 4))
        relation = []
        for i in range(7):
            relation.append([counter, linear_equation(counter)])
            counter += 1
    elif (parent == "quadratic"):
        a = maybeMakeNegative(random.randint(1, 5))
        quadratic_equation = numpy.poly1d([a, 0, 0])
        counter = maybeMakeNegative(random.randint(1, 4))
        relation = []
        for i in range(7):
            relation.append([counter, quadratic_equation(counter)])
            counter += 1
    elif (parent == "cubic"):
        a = maybeMakeNegative(random.randint(1, 5))
        cubic_equation = numpy.poly1d([a, 0, 0, 0])
        counter = maybeMakeNegative(random.randint(1, 4))
        relation = []
        for i in range(7):
            relation.append([counter, cubic_equation(counter)])
            counter += 1
    elif (parent == "square root"):
        a = maybeMakeNegative(random.randint(1, 5))
        h = maybeMakeNegative(random.randint(1, 5))
        k = maybeMakeNegative(random.randint(1, 5))
        # Uses this as the base, then does (x-sqrt_equation)**
        sqrt_equation = numpy.poly1d([-h])
        counter = maybeMakeNegative(random.randint(1, 4))
        relation = []
        for i in range(7):
            relation.append([counter, sqrt_equation(counter)])
            counter += 1

### VARIABLE DECLARATIONS ###
# Declare the necessary variables.
function_switch_variable = ["function", "nonfunction"]
function_parents = ["linear", "quadratic", "cubic", "square root", "cube root", "absolute value", "exponential base 2" "exponential base 1/2"]
nonfunction_parents = ["x=y^2", "x=sqrt(y)", "x=|y|", "x^2+y^2=1", "y=sqrt(1-x^2)"]

# Graph and mapping diagram will be completed at a later time
representation_options = ["ordered pair", "table", "graph", "mapping diagram"]

### CREATE INTERVAL OPTIONS
# Use the General Method Function 'createIntervalOptions(setOfValues, intervalRange, precision)'.
    # *setOfValues* is the set of values you are trying to disguise in intervals. This can be a set of sets!
    # setOfValues = [set1, set2, set3, set4]
        # Be sure all sets are of equal length. This is necessary when checking that values are not contained in other intervals.
    # *intervalRange* is the approximate size of the interval masking the values. This should be small when values are close to each other and larger when values are further away. In the future, this may be automatically determined using a min distance between values.
    # *precision* is an optional input. If specified, it is used to fine-tune the endpoint of the intervals used to mask values. Should only be included when values are extremely close together.

### USE INTERVAL OPTIONS OUTPUT TO CREATE ANSWERLIST
# answerList should be created as a list of sets, where each set is [choice, comment, answerLetterIndicator].
    # *choice* is exactly the way the option should be displayed. This should include math mode or display of intervals.
    # *comment* is the related comment that should be displayed on the key. It should include the exact answer (if the value is being disguised in an interval) and start with a * if it is the solution.
    # *answerLetterIndicator* is 1 for the correct option and 0 otherwise. This is used to note the correct letter for the question.
    # answerList = [solutionSet, distractor1Set, distractor2Set, distractor3Set, distractor4Set]

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER
    # choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]
    # choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
    # answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
    # answerLetter = identifyAnswerLetter(answerLetterIndicators)

### Define display variables ###
# Options are: "String", "Math Mode", or "Graph"
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"

### Writes important information to database. ###
if debug=="save":
    writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
