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

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

thisQuestion="constructLinearModelCostsProfitsRevenueCopy"

# Costs, Profit, Revenue

savings = random.randint(5, 11)*1000
rent = random.randint(7, 12)*100
food = random.randint(4, 8)*10
misc = random.randint(4, 8)*8
edExpense = 2*random.randint(2, 5)*100
costs = rent + 4*food + 4*misc
badCosts = rent + food + misc
profits = edExpense + savings

costProfitOrRevenue = random.randint(0, 2)
correctOrNoneOfTheAbove = random.randint(0, 1)

if costProfitOrRevenue == 0:
    # COST
    displayStem = "For the information provided below, construct a linear model that describes her total costs, $C$, as a function of the number of months, $x$ she is at UF. "
    if correctOrNoneOfTheAbove == 0:
        displaySolution = "\\text{None of the above.}"
        option1 = ["C(x) = %d x" %profits, "This describes the student's income as if they received the savings and educational expense each month.", 0]
        option2 = ["C(x) = %d x" %badCosts, "This treats weekly expenses as monthly expenses rather than multiplying each weekly expense by 4.", 0]
        option3 = ["C(x) = %d" %profits, "This describes the student's income, not costs.", 0]
        option4 = ["C(x) = %d" %badCosts, "This treats weekly expenses as month expenses rather than multiplying each weekly expense by 4 AND does not account for these expenses per month.", 0]
        option5 = ["\\text{None of the above.}", "* This is the correct option as the model should be $C(x) = %d x$." %costs, 1]
    else:
        displaySolution = "C(x) = %d x" %costs
        option1 = ["C(x) = %d x" %costs, "* This is the correct option.", 1]
        option2 = ["C(x) = %d x" %badCosts, "This treats weekly expenses as monthly expenses rather than multiplying each weekly expense by 4.", 0]
        option3 = ["C(x) = %d" %costs, "This describes the costs as if they are one-time only and not monthly.", 0]
        option4 = ["C(x) = %d" %badCosts, "This treats weekly expenses as month expenses rather than multiplying each weekly expense by 4 AND does not account for these expenses per month.", 0]
        option5 = ["\\text{None of the above.}", "You may have chosen this as you thought you were modeling total income or total budget.", 0]
elif costProfitOrRevenue == 1:
    # INCOME
    displayStem = "For the information provided below, construct a linear model that describes her total income, $I$, as a function of the number of months, $x$ she is at UF."
    if correctOrNoneOfTheAbove == 0:
        displaySolution = "\\text{none of the above.}"
        option1 = ["I(x) = %d x" %costs, "This describes the monthly costs, not the monthly income.", 0]
        option2 = ["I(x) = %d x" %badCosts, "This treats weekly expenses as monthly expenses rather than multiplying each weekly expense by 4.", 0]
        option3 = ["I(x) = %d" %costs, "This describes the costs as if they are one-time only and not monthly.", 0]
        option4 = ["I(x) = %d" %badCosts, "This treats weekly expenses as month expenses rather than multiplying each weekly expense by 4 AND does not account for these expenses per month.", 0]
        option5 = ["\\text{None of the above.}", "* This is the correct option as the model should be $I(x) = %d$." %profits, 1]
    else:
        displaySolution = "I(x) = %d" %profits
        option1 = ["I(x) = %d" %profits, "* This is the correct option.", 1]
        option2 = ["I(x) = %d x + %d" %(edExpense, savings), "This treats the educational expense as something you get every month rather than a 1-time payment.", 0]
        option3 = ["I(x) = %d x + %d" %(savings, edExpense), "This treats the savings as something you get every month rather than a 1-time payment.", 0]
        option4 = ["I(x) = %d x" %profits, "This treats the educational expense and savings as something you get every month rather than a 1-time payment.", 0]
        option5 = ["\\text{None of the above.}", "You may have chosen this as you thought you were modeling total costs or total budget.", 0]
else:
    # BUDGET
    displayStem = "For the information provided below, construct a linear model that describes her total budget, $B$, as a function of the number of months, $x$ she is at UF."
    if correctOrNoneOfTheAbove == 0:
        displaySolution = "\\text{none of the above.}"
        option1 = ["B(x) = %d - %d x" %(badCosts, profits), "This treats weekly expenses as month expenses rather than multiplying each weekly expense.", 0]
        option2 = ["B(x) = %d - %d x" %(profits, costs), "", 0]
        option3 = ["B(x) = %d x + %d" %(edExpense, savings), "This treats the educational expense as something you get every month rather than a 1-time payment and is modeling Income, not Budget.", 0]
        option4 = ["B(x) = %d x + %d" %(savings, edExpense), "This treats the savings as something you get every month rather than a 1-time payment and is modeling Income, not Budget.", 0]
        option5 = ["\\text{None of the above.}", "* This is the correct option as the model should be $B(x) = %d - %d x$." %(costs, profits), 1]
    else:
        displaySolution = "B(x) = %d - %d x" %(costs, profits)
        option1 = ["B(x) = %d - %d x" %(costs, profits), "* This is the correct option.", 1]
        option2 = ["B(x) = %d - %d x" %(badCosts, profits), "This treats weekly expenses as month expenses rather than multiplying each weekly expense.", 0]
        option3 = ["B(x) = %d x" %(profits - costs), "This treats the educational expense and savings as something you get every month rather than a 1-time payment.", 0]
        option4 = ["B(x) = %d x" %(profits - badCosts), "This treats the educational expense and savings as something you get every month rather than a 1-time payment AND treats weekly expenses as month expenses rather than multiplying each weekly expense by 4.", 0]
        option5 = ["\\text{None of the above.}", "You may have chosen this if you thought you were modeling total costs or income.", 0]

displayProblem = "Aubrey is a college student going into her first year at UF. She will receive Bright Futures, which covers her tuition plus a \\$%d educational expense each year. Before college, Aubrey saved up \\$%d. She knows she will need to pay \\$%d in rent a month, \\$%d for food a week, and \\$%d in other weekly expenses." %(edExpense, savings, rent, food, misc)

generalComment = "This is a Costs, Profit, Revenue question! The most common issues here are: (1) not converting the weekly costs to monthly costs, (2) treating the one-time values like savings and educational expense as happening per month, and (3) not checking that your model is for cost, profit [income], or revenue [budget]."

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# THREE types of questions: Cost equation, Profit equation, Revenue Equation, None of the above for each type.

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="String"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
