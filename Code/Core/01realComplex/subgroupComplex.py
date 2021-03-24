import sys
import random
from math import gcd

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
def generateRationalFromSubgroupReal():
    numerator = random.randint(5, 25)
    denominator = random.randint(5, 25)
    while (gcd(numerator, denominator) > 1): # Checks to make sure we get a non-Whole, Rational number
        denominator = random.randint(5, 25)
    return [numerator**2, denominator**2]
def generateIrrationalFromSubgroupReal():
    discriminantbase = random.randint(9, 18)
    irrationalmaker = random.choice([5, 7, 11, 13]) #The number we will use to make sure we get an irrational number
    maskirrational = random.randint(5, 15) # Makes sure the product is not a perfect square
    while gcd(discriminantbase, irrationalmaker) > 1:
        irrationalmaker = random.randint(9, 18)
    numerator = discriminantbase * irrationalmaker * maskirrational
    denominator = maskirrational
    return [numerator, denominator]
def generateNonRealFromSubgroupReal():
    numerator = random.randint(5, 25)
    denominator = 0
    return [numerator, denominator]
def generateComplexFromSubgroupReal():
    discrim = random.randint(9, 18)
    irrationalmaker = random.choice([5, 7, 11, 13]) #The number we will use to make sure we get an irrational number
    maskirrational = random.randint(5, 15)
    while math.gcd(discrim, irrationalmaker) > 1:
        irrationalmaker = random.randint(9, 18)
    numerator = - discrim * irrationalmaker * maskirrational
    denominator = maskirrational
    return [numerator, denominator]
def generateRationalNumber():
    numerator = random.randint(2, 20)*(-1)**random.randint(0, 1)
    denominator = random.randint(2, 20)*(-1)**random.randint(0, 1)
    b = random.randint(2, 10)**2
    randomChoice=random.randint(0, 2)
    if randomChoice==0:
        displayProblem = '\\frac{%d}{%d}+\\sqrt{-%d}i' %(numerator, denominator, b)
    elif randomChoice==1:
        displayProblem = '\\frac{%d}{%d}+%di^2' %(numerator, denominator, b)
    else:
        numerator, denominator = generateRationalFromSubgroupReal()
        randomNeg = (-1)**random.randint(0, 1)
        if randomNeg == -1:
            displayProblem =  '-\\sqrt{\\frac{%d}{%d}} + %di^2' %(numerator, denominator, b)
        else:
            displayProblem =  '\\sqrt{\\frac{%d}{%d}} + %di^2' %(numerator, denominator, b)
    return displayProblem
def generateIrrationalNumber(): #Question Type 1 generates Irrational numbers of the form a + 0i
    discriminantbase = random.randint(9, 18) # Base of the number under the square root
    irrationalmaker = random.choice([5, 7, 11, 13]) #The number we will use to make sure we get an irrational number
    while gcd(discriminantbase, irrationalmaker) > 1: # Makes sure the product is not a perfect square
        irrationalmaker = random.randint(9, 18)
    numerator = discriminantbase * irrationalmaker
    denominator = random.randint(5, 20)
    b = random.randint(2, 10)
    randomChoice=random.randint(0, 2)
    if randomChoice == 0:
        displayProblem = '\\frac{\\sqrt{%d}}{%d}+\\sqrt{-%d}i' %(numerator, denominator, b)
    elif randomChoice == 1:
        displayProblem = '\\frac{\\sqrt{%d}}{%d}+%di^2' %(numerator, denominator, b)
    else:
        numerator, denominator = generateIrrationalFromSubgroupReal()
        randomNeg = (-1)**random.randint(0, 1)
        if randomNeg == -1:
            displayProblem =  '-\\sqrt{\\frac{%d}{%d}}+%di^2' %(numerator, denominator, b)
        else:
            displayProblem =  '\\sqrt{\\frac{%d}{%d}}+%di^2' %(numerator, denominator, b)
    return displayProblem
def generateNonRealComplexNumber(): #Question Type 2 generates Nonreal Complex numbers of the form a + bi
    numerator = random.randint(5, 25)*(-1)**random.randint(0, 1)
    denominator = random.randint(5, 25)
    while gcd(numerator, denominator) == denominator:
        denominator = random.randint(5, 25)
    discriminantbase = random.randint(9, 18) # Base of the number under the square root
    irrationalmaker = random.choice([5, 7, 11, 13]) #The number we will use to make sure we get an irrational number
    while gcd(discriminantbase, irrationalmaker) > 1: # Makes sure the product is not a perfect square
        irrationalmaker = random.randint(9, 18)
    inside = discriminantbase*irrationalmaker
    b = "\\sqrt{%d} i" %inside
    randomChoice=random.randint(0, 4)
    if randomChoice==0:
        displayProblem = '\\frac{%d}{%d}+%s' %(numerator, denominator, b)
    elif randomChoice==1:
        numerator, denominator = generateRationalFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{%d}}+%s' %(numerator, denominator, b)
    elif randomChoice==2:
        numerator, denominator = generateIrrationalFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{%d}}+%s' %(numerator, denominator, b)
    elif randomChoice==3:
        numerator, denominator = generateComplexFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{%d}}+\\sqrt{%d}' %(numerator, denominator, inside)
    else:
        numerator, denominator = generateComplexFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{%d}} i+\\sqrt{%d}i' %(numerator, denominator, inside)
    return displayProblem
def generatePureImaginaryNumber(): #Question Type 3 generates Pure Imaginary numbers of the form 0 + bi
    denominator = random.randint(2, 20)*(-1)**random.randint(0, 1)
    b = int(random.randint(2, 10))
    randomChoice=random.randint(0, 3)
    if randomChoice==0:
        displayProblem = '\\frac{0}{%d \\pi}+\\sqrt{%s}i' %(denominator, b)
    elif randomChoice==1:
        numerator, denominator = generateRationalFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{0}{%d}}+\\sqrt{%s}i' %(denominator, b)
    elif randomChoice==2:
        numerator, denominator = generateIrrationalFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{0}{%d}}+\\sqrt{%s}i' %(denominator, b)
    else:
        numerator, denominator = generateComplexFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{%d}}+\\sqrt{0}i' %(numerator, denominator)
    return displayProblem
def generateNonNumber(): #Question Type 4 generates Non-Complex numbers (dividing by 0)
    numerator = random.randint(5, 25)*(-1)**random.randint(0, 1)
    denominator = random.randint(5, 25)
    while gcd(numerator, denominator) == denominator:
        denominator = random.randint(5, 25)
    # Base of the number under the square root
    discriminantbase = random.randint(9, 18)
    # The number we will use to make sure we get an irrational number
    irrationalmaker = random.choice([5, 7, 11, 13]) #The number we will use to make sure we get an irrational number
    # Makes sure the product is not a perfect square
    while gcd(discriminantbase, irrationalmaker) > 1:
        irrationalmaker = random.randint(9, 18)
    inside = discriminantbase*irrationalmaker
    b = "\\sqrt{%d} i" %inside
    randomChoice=random.randint(0, 4)
    if randomChoice==0:
        displayProblem = '\\frac{%d}{0}+%s' %(numerator, b)
    elif randomChoice==1:
        numerator, denominator = generateRationalFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{0}}+%s' %(numerator, b)
    elif randomChoice==2:
        numerator, denominator = generateIrrationalFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{0}}+%s' %(numerator, b)
    elif randomChoice==3:
        numerator, denominator = generateComplexFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{0}}+\\sqrt{%d}' %(numerator, inside)
    else:
        numerator, denominator = generateComplexFromSubgroupReal()
        displayProblem = '\\sqrt{\\frac{%d}{0}} i+\\sqrt{%d}i' %(numerator, inside)
    return displayProblem
### VARIABLE DECLARATIONS ###
types = ["Rational", "Irrational", "NonrealComplex", "PureImaginary", "NotComplex"]
questionType = random.choice(types)

### DEFINE ANSWERLIST AND DISPLAYSOLUTION ###
option0 = ['\\text{Rational}', "These are numbers that can be written as fraction of Integers (e.g., -2/3 + 5)", 0]
option1 = ['\\text{Irrational}', "These cannot be written as a fraction of Integers. Remember: $\\pi$ is not an Integer!", 0]
option2 = ['\\text{Nonreal Complex}', "This is a Complex number $(a+bi)$ that is not Real (has $i$ as part of the number).", 0]
option3 = ['\\text{Pure Imaginary}', "This is a Complex number $(a+bi)$ that \\textbf{only} has an imaginary part like $2i$.", 0]
option4 = ['\\text{Not a Complex Number}', "This is not a number. The only non-Complex number we know is dividing by 0 as this is not a number!", 0]

if questionType == "Rational":
    displayProblem = generateRationalNumber()
    displaySolution = option0[0]
    option0[1]="* This is the correct option!"
    option0[2]=1
elif questionType == "Irrational":
    displayProblem = generateIrrationalNumber()
    displaySolution = option1[0]
    option1[1]="* This is the correct option!"
    option1[2]=1
elif questionType == "NonrealComplex":
    displayProblem = generateNonRealComplexNumber()
    displaySolution = option2[0]
    option2[1]="* This is the correct option!"
    option2[2]=1
elif questionType == "PureImaginary":
    displayProblem = generatePureImaginaryNumber()
    displaySolution = option3[0]
    option3[1]="* This is the correct option!"
    option3[2]=1
else:
    displayProblem = generateNonNumber()
    displaySolution = option4[0]
    option4[1]="* This is the correct option!"
    option4[2]=1

answerList = [option0, option1, option2, option3, option4]
random.shuffle(answerList)

### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
displayStem = 'Choose the \\textbf{smallest} set of Complex numbers that the number below belongs to.'
# displayProblem was defined previously
generalComment = "Be sure to simplify $i^2 = -1$. This may remove the imaginary portion for your number. If you are having trouble, you may want to look at the \\textit{Subgroups of the Real Numbers} section."

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
