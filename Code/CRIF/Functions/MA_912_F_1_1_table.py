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
# This should list all definitions used. Be sure to check the commonly used functions file before creating a new one.
def generate_relation(parent):
    if (parent == "Linear"):
        m = maybeMakeNegative(random.randint(2, 7))
        b = maybeMakeNegative(random.randint(1, 9))
        linear_equation = numpy.poly1d([m, b])
        counter = maybeMakeNegative(random.randint(1, 4))
        relation = []
        for i in range(7):
            relation.append([counter, linear_equation(counter)])
            counter += 1
    elif (parent == "Quadratic"):
        a = maybeMakeNegative(random.randint(1, 5))
        quadratic_equation = numpy.poly1d([a, 0, 0])
        counter = maybeMakeNegative(random.randint(1, 4))
        relation = []
        for i in range(7):
            relation.append([counter, quadratic_equation(counter)])
            counter += 1
    elif (parent == "Absolute Value"):
        m = 1; b = 0; counter = 0
        while (counter > float(-b/m) ) or (counter == float(-b/m) ):
            m = maybeMakeNegative(random.randint(2, 7))
            b = maybeMakeNegative(random.randint(1, 9))
            counter = maybeMakeNegative(random.randint(1, 4))
        linear_equation = numpy.poly1d([m, b])
        relation = []
        for i in range(7):
            relation.append([counter, abs(linear_equation(counter))])
            counter += 1
    elif (parent == "Exponential base 2"):
        a = maybeMakeNegative(random.randint(1, 5))
        counter = random.randint(1, 4)
        relation = []
        for i in range(7):
            relation.append([counter, a*numpy.exp2(counter)])
            counter += 1
    elif (parent == "Linear irrational"):
        m = maybeMakeNegative(random.randint(2, 7))
        b = maybeMakeNegative(random.randint(1, 9))
        linear_equation = numpy.poly1d([m, b])
        counter = round(random.choice([2, 3, 5])**0.5, 2)*(-1)**(random.randint(0, 1))
        relation = []
        for i in range(7):
            relation.append([counter, linear_equation(counter)])
            counter += 1
    elif (parent == "Quadratic irrational"):
        a = maybeMakeNegative(random.randint(1, 5))
        quadratic_equation = numpy.poly1d([a, 0, 0])
        counter = round(random.choice([2, 3, 5])**0.5, 2)*(-1)**(random.randint(0, 1))
        relation = []
        for i in range(7):
            relation.append([counter, quadratic_equation(counter)])
            counter += 1
    elif (parent == "Square Root"):
        a = maybeMakeNegative(random.randint(1, 5))
        counter = round(random.choice([2, 3, 5])**0.5, 2)
        relation = []
        for i in range(7):
            relation.append([counter, round(a*(counter)**0.5, 2)])
            counter += 1
    elif (parent == "Cube Root"):
        a = maybeMakeNegative(random.randint(1, 5))
        counter = round(random.choice([2, 3, 5])**0.5, 2)
        relation = []
        for i in range(7):
            relation.append([counter, round(a*(counter)**(1./3.), 2)])
            counter += 1
    elif (parent == "Exponential base 1/2"):
        a = maybeMakeNegative(random.randint(1, 5))
        counter = round(random.choice([2, 3, 5])**0.5, 2)
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
function_parents_integers = ["Linear", "Quadratic", "Absolute Value", "Exponential base 2"]
function_parents_irrational = ["Linear irrational", "Square Root", "Cube Root", "Exponential base 1/2"]
# Ideas for later nonfunction_parents: "x^2+y^2=1", "y=sqrt(1-x^2)"
nonfunction_parents = ["x=y^2", "x=sqrt(y)", "x=|y|"]
# Describe all possible choices and choice comments.
c_linear=["Linear", "A linear function would have a constant rate of change. As $x$ increases by some value, the $y$ value would increase by a constant amount.", 0]
c_quadratic=["Quadratic", "A quadratic function would have a slowly increase rate of change. As $x$ increased, the $y$ value would increase by a slowly increasing amount.", 0]
c_absolute_value=["Absolute Value", "An absolute value function would have a constant rate of change that at some point would change signs.", 0]
c_exponential_base_2=["Exponential base 2", "An exponential function with base 2 would have a rate of change that increases extremely slowly at first, then extremely quickly.", 0]
c_sqrt=["Square Root", "A square root function would have a slowly decreasing rate of change. As $x$ increased, the $y$ value would increase at a slower and slower rate.", 0]
c_exponential_base_half=["Exponential base 1/2", "An exponential function with base 1/2 would have a rate of change that increases extremely quickly at first, then extremely slowly.", 0]
all_integer_choices=[c_linear, c_quadratic, c_absolute_value, c_exponential_base_2]
all_irrational_choices=[c_linear, c_sqrt, c_quadratic, c_exponential_base_half]
# Choose whether the table can be represented by a function, then determine whether that function will have integer vs irrational inputs.
relation_is_function = random.randint(0, 3) # Not a function appears 25% of time now.
function_values_irrational = random.randint(0, 1)
if relation_is_function == 0:
    relation_for_problem = random.choice(nonfunction_parents)
    relation = generate_relation(relation_for_problem)
    if function_values_irrational == 0:
        option_info=all_integer_choices
        random.shuffle(option_info)
    else:
        option_info=all_irrational_choices
        random.shuffle(option_info)
    choice_nonrelation=["Not a function", "The table does not describe a relation, therefore no function can be represented by the table.", 1]
    option_info.append(choice_nonrelation)
    displaySolution = "not a function"
else:
    if function_values_irrational == 0:
        option_info=all_integer_choices
        random.shuffle(option_info)
        option_info[0][2]=1
        displaySolution = option_info[0][0]
        random.shuffle(option_info)
        option_info.append(["Not a function", "For a relation to be a function, every $x$-value needs exactly one output. That means for a relation to NOT be a function, we would need one $x$-value that has two or more different outputs.", 0])
        relation=generate_relation(displaySolution)
    else:
        option_info=all_irrational_choices
        random.shuffle(option_info)
        option_info[0][2]=1
        displaySolution = option_info[0][0]
        if displaySolution == "Linear":
            relation_choice = "Linear irrational"
        elif displaySolution == "Quadratic":
            relation_choice = "Quadratic irrational"
        else:
            relation_choice = displaySolution
        random.shuffle(option_info)
        option_info.append(["Not a function", "For a relation to be a function, every $x$-value needs exactly one output. That means for a relation to NOT be a function, we would need one $x$-value that has two or more different outputs.", 0])
        relation=generate_relation(relation_choice)

# Note the stem does not change for multiple-choice vs free-response.
displayStem = "What function type \\textit{could} represent the table below?"
header_row = ["x", "y"]
displayProblem = [header_row, relation[0], relation[1], relation[2], relation[3], relation[4], relation[5], relation[6]]

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER
choices = [option_info[i][0] for i in range(5)]
choiceComments = [option_info[i][1] for i in range(5)]
identifier_list = [option_info[i][2] for i in range(5)]
answerLetter = identifyAnswerLetter(identifier_list)

### Define display variables ###
# Options are: "String", "Math Mode", "Graph", or "Table"
displayStemType="String"
displayProblemType="Table"
displayOptionsType="String"
generalComment="To identify a function that could represent the table, identify the rate of change."

### Writes important information to database. ###
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
