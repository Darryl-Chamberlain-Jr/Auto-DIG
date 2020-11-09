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

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
thisQuestion=sys.argv[5]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

### DEFINITIONS ###
def generateWhole():
    denominatorbase = random.randint(5, 25)
    numeratorbase = denominatorbase * random.randint(5, 25)
    denominator = denominatorbase * denominatorbase
    numerator = numeratorbase * numeratorbase
    displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
    simplifiedNumber = numeratorbase
    return [displayProblem, simplifiedNumber]
def generateInteger():
    denominatorbase = random.randint(5, 25)
    numeratorbase = denominatorbase * random.randint(5, 25) # Makes sure we return a natural number
    denominator = denominatorbase * denominatorbase # Makes perfect squares
    numerator = numeratorbase * numeratorbase
    displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
    simplifiedNumber = -numeratorbase
    return [displayProblem, simplifiedNumber]
def generateRational():
    numerator = random.randint(5, 25)
    denominator = random.randint(5, 25)
    while (math.gcd(numerator, denominator) > 1): # Checks to make sure we get a non-Whole, Rational number
        denominator = random.randint(5, 25)
    randomNeg = (-1)**random.randint(0, 1)
    if randomNeg == -1:
        displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator**2, denominator**2)
        simplifiedNumber = '-\\frac{%d}{%d}' %(numerator, denominator)
    else:
        displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator**2, denominator**2)
        simplifiedNumber = '\\frac{%d}{%d}' %(numerator, denominator)
    return [displayProblem, simplifiedNumber]
def generateIrrational():
    discriminantbase = random.randint(9, 18) #Base of the number under the square root
    irrationalmaker = random.choice([5, 7, 11, 13]) #The number we will use to make sure we get an irrational number
    maskirrational = random.randint(5, 15) # Masks that the fraction is not a perfect square
    while math.gcd(discriminantbase, irrationalmaker) > 1: # Makes sure the product is not a perfect square
        irrationalmaker = random.randint(9, 18)
    numerator = discriminantbase * irrationalmaker * maskirrational
    denominator = maskirrational
    randomNeg = maybeMakeNegative(1)
    if randomNeg == -1:
        displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
        simplifiedNumber = '-\\sqrt{%d}' %(discriminantbase*irrationalmaker)
    else:
        displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
        simplifiedNumber = '\\sqrt{%d}' %(discriminantbase*irrationalmaker)
    return [displayProblem, simplifiedNumber]
def generateNonReal():
    chooseDivideByZeroOrComplex = random.randint(0, 1)
    if chooseDivideByZeroOrComplex == 0:
        # Divides by zero
        numerator = random.randint(5, 25)
        denominator = 0
        randomNeg = maybeMakeNegative(1)
        if randomNeg == -1:
            displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
        else:
            displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
        simplifiedNumber = displayProblem
    else:
        # Complex number
        discrim = random.randint(9, 18)
        irrationalmaker = random.choice([5, 7, 11, 13])
        maskirrational = random.randint(5, 15)
        while math.gcd(discrim, irrationalmaker) > 1:
            irrationalmaker = random.randint(9, 18)
        numerator = - discrim * irrationalmaker * maskirrational
        denominator = maskirrational
        randomNeg = (-1)**random.randint(0, 1)
        if randomNeg == -1:
            displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
            simplifiedNumber = '-\\sqrt{%d} i' %(discrim * irrationalmaker)
        else:
            displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
            simplifiedNumber = '\\sqrt{%d} i' %(discrim * irrationalmaker)
    return [displayProblem, simplifiedNumber]

### VARIABLE DECLARATIONS ###
types = ["Whole", "Integer", "Rational", "Irrational", "Nonreal"]
questionType = random.choice(types)

### DEFINE ANSWERLIST AND DISPLAYSOLUTION ###
option0 = ['\\text{Whole}', "These are the counting numbers with 0 (0, 1, 2, 3, ...)", 0]
option1 = ['\\text{Integer}', "These are the negative and positive counting numbers (..., -3, -2, -1, 0, 1, 2, 3, ...)", 0]
option2 = ['\\text{Rational}', "These are numbers that can be written as fraction of Integers (e.g., -2/3)", 0]
option3 = ['\\text{Irrational}', "These cannot be written as a fraction of Integers.", 0]
option4 = ['\\text{Not a Real number}', "These are Nonreal Complex numbers \\textbf{OR} things that are not numbers (e.g., dividing by 0).", 0]

if questionType == "Whole":
    displayProblem, simplifiedNumber = generateWhole()
    displaySolution = option0[0]
    option0[1]="* This is the correct option!"
    option0[2]=1
elif questionType == "Integer":
    displayProblem, simplifiedNumber = generateInteger()
    displaySolution = option1[0]
    option1[1]="* This is the correct option!"
    option1[2]=1
elif questionType == "Rational":
    displayProblem, simplifiedNumber = generateRational()
    displaySolution = option2[0]
    option2[1]="* This is the correct option!"
    option2[2]=1
elif questionType == "Irrational":
    displayProblem, simplifiedNumber = generateIrrational()
    displaySolution = option3[0]
    option3[1]="* This is the correct option!"
    option3[2]=1
else:
    displayProblem, simplifiedNumber = generateNonReal()
    displaySolution = option4[0]
    option4[1]="* This is the correct option!"
    option4[2]=1

answerList = [option0, option1, option2, option3, option4]
random.shuffle(answerList)

### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
displayStem = 'Choose the \\textbf{smallest} set of Real numbers that the number below belongs to.'
# displayProblem was defined previously
generalComment = "First, you \\textbf{NEED} to simplify the expression. This question simplifies to $%s$. \n \n Be sure you look at the simplified fraction and not just the decimal expansion. Numbers such as 13, 17, and 19 provide \\textbf{long but repeating/terminating decimal expansions!} \n \n The only ways to *not* be a Real number are: dividing by 0 or taking the square root of a negative number. \n \n Irrational numbers are more than just square root of 3: adding or subtracting values from square root of 3 is also irrational." %simplifiedNumber

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
