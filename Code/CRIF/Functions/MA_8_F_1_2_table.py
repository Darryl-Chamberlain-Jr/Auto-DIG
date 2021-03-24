### NECESSARY IMPORTS ###
import sys
import numpy
import random

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

### DEFINITIONS ###
# This should list all definitions used. Be sure to check the commonly used functions file before creating a new one.
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
    elif (parent == "absolute value"):
        m = 1; b = 0; counter = 0
        while (counter < float(-b/m) ):
            m = maybeMakeNegative(random.randint(2, 7))
            b = maybeMakeNegative(random.randint(1, 9))
            counter = maybeMakeNegative(random.randint(1, 4))
        linear_equation = numpy.poly1d([m, b])
        relation = []
        for i in range(7):
            relation.append([counter, abs(linear_equation(counter))])
            counter += 1
    elif (parent == "exponential base 2"):
        a = maybeMakeNegative(random.randint(1, 5))
        counter = random.randint(1, 4)
        relation = []
        for i in range(7):
            relation.append([counter, a*numpy.exp2(counter)])
            counter += 1
    elif (parent == "square root"):
        a = maybeMakeNegative(random.randint(1, 5))
        counter = random.randint(1, 4)
        relation = []
        for i in range(7):
            relation.append([counter, round(a*(counter)**0.5, 2)])
            counter += 1
    elif (parent == "cube root"):
        a = maybeMakeNegative(random.randint(1, 5))
        counter = random.randint(1, 4)
        relation = []
        for i in range(7):
            relation.append([counter, round(a*(counter)**(1./3.), 2)])
            counter += 1
    elif (parent == "exponential base 1/2"):
        a = maybeMakeNegative(random.randint(1, 5))
        counter = random.randint(1, 4)
        relation = []
        for i in range(7):
            relation.append([counter, round(a*(1/2)**(counter), 2)])
            counter += 1
    elif (parent == "x=y^2"):
        a = (-1)**random.randint(0,1)*random.randint(1, 5)
        counter = random.randint(1, 4)
        shift_index = random.randint(2, 4)
        relation = []
        for i in range(shift_index):
            relation.append([counter+i, -round(a*(counter+i)**0.5, 2)])
        relation.append([counter+shift_index, (-1)**random.randint(0,1)*round(a*(counter+i)**0.5, 2)])
        for i in range(6-shift_index):
            relation.append([counter-i+shift_index-1, round(a*(counter+i)**0.5, 2)])
    elif (parent == "x=sqrt(y)"):
        a = (-1)**random.randint(0,1)*random.randint(1, 5)
        counter = random.randint(1, 4)
        shift_index = random.randint(2, 4)
        relation = []
        for i in range(shift_index):
            relation.append([counter+i, -a*(counter+i)**2])
        relation.append([counter+shift_index, (-1)**random.randint(0,1)*a*(counter+i)**2])
        for i in range(6-shift_index):
            relation.append([counter-i+shift_index-1, a*(counter+i)**2])
    elif (parent == "x=|y|"):
        a = random.randint(1, 5)
        parity = random.randint(0,1)
        counter = random.randint(1, 4)
        shift_index = random.randint(2, 4)
        relation = []
        for i in range(shift_index):
            relation.append([counter+i, (-1)**(parity)*a*(counter+i)])
        relation.append([counter+shift_index, (-1)**random.randint(0,1)*a*(counter+i)])
        for i in range(6-shift_index):
            relation.append([counter-i+shift_index-1, (-1)**(parity+1)*a*(counter+i)])
    else:
        relation=["Inproper relation defined."]
    return relation

### VARIABLE DECLARATIONS ###
# Declare the necessary variables.
function_parents_integers = ["linear", "quadratic", "cubic", "absolute value", "exponential base 2"]
function_parents_irrational = ["linear irrational", "square root", "cube root", "exponential base 1/2"]
# Ideas for later nonfunction_parents: "x^2+y^2=1", "y=sqrt(1-x^2)"
nonfunction_parents = ["x=y^2", "x=sqrt(y)", "x=|y|"]
relation_is_function = random.randint(0, 1)
relation_is_linear = random.randint(0, 1)
if relation_is_function == 0:
    relation_for_problem = random.choice(nonfunction_parents)
    relation = generate_relation(relation_for_problem)
    displaySolution = "No"
    answerLetter = "B"
    yes_comment = "Notice how one $x$-value has two separate outputs? For a relation to be a function, every $x$-value needs exactly one output."
    no_comment = "* Correct! An $x$-value has two separate outputs and thus this relation is not a function, let alone a linear function."
elif relation_is_linear == 0:
    displaySolution = "No"
    answerLetter = "B"
    function_value_types = ["integer", "float"]
    function_choice = random.choice(function_value_types)
    if function_choice == "integer":
        relation_for_problem = random.choice(function_parents_integers)
        while relation_for_problem == "linear":
            relation_for_problem = random.choice(function_parents_integers)
    else:
        relation_for_problem = random.choice(function_parents_irrational)
        while relation_for_problem == "linear irrational":
            relation_for_problem = random.choice(function_parents_irrational)
    relation = generate_relation(relation_for_problem)
    yes_comment = "A linear function has a constant rate of growth. As $x$ increases/decreases, $y$ increases/decreases at the same rate. The table in this example does have a constant rate of change."
    no_comment = f"* Correct! The table in this example does not have a constant rate of change. This relation is a {function_choice} function."
else:
    displaySolution = "Yes"
    answerLetter = "A"
    function_value_types = ["integer", "float"]
    function_choice = random.choice(function_value_types)
    if function_choice == "integer":
        relation_for_problem = "linear"
    else:
        relation_for_problem = "linear irrational"
    relation = generate_relation(relation_for_problem)
    yes_comment = "* Correct! As $x$ increases/decreases, $y$ increases/decreases at the same rate."
    no_comment = "A linear function has a constant rate of growth. As $x$ increases/decreases, $y$ increases/decreases at the same rate."

displayStem = "Is the following relation a linear function?"
header_row = ["x", "y"]
displayProblem = [header_row, relation[0], relation[1], relation[2], relation[3], relation[4], relation[5], relation[6]]

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER
c0 = ["Yes", f"{yes_comment}"]
c1 = ["No", f"{no_comment}"]
choices = [c0[0], c1[0]]
choiceComments = [c0[1], c1[1]]

### Define display variables ###
# Options are: "String", "Math Mode", "Graph", or "Table"
displayStemType="String"
displayProblemType="Table"
displayOptionsType="String"
generalComment="For a relation to be a linear function, every $x$-value needs exactly one output AND there needs to be a constant rate of growth (as $x$ increases/decreases, $y$ increases/decreases at the same rate)."

### Writes important information to database. ###
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
