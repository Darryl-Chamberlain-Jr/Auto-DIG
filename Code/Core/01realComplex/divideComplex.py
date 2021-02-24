import sys
import random

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
thisQuestion=sys.argv[5]
sys.path.insert(1, f"/{DIR}/PythonScripts")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
from storeQuestionData import *

### DEFINITIONS ###
def generateDistinctCoefficients():
    listIntegers = [i for i in range(1, 9)]
    constants = random.sample(listIntegers, 4)
    constants = [maybeMakeNegative(i) for i in constants]
    return constants

def round_set_of_floats(pairs_of_floats, round_to):
    return [[round(value[0], round_to), round(value[1], round_to)] for value in pairs_of_floats]

def generateDistractors(coefficients):
    a1, b1, a2, b2 = coefficients
    # Divide like terms
    distractor1 = [float(a1/a2), float(b1/b2)]
    # Multiply by non-conjugate and treat like conjugate in denominator
    quotientD2 = ( complex(a1, b1) * complex(a2, b2) ) / ( complex(a2, b2) * complex(a2, -b2) )
    distractor2 = [quotientD2.real, quotientD2.imag]
    # Multiply by conjugate, only divide first term
    numeratorD3 = complex(a1, b1) * complex(a2, -b2)
    denominatorD3 = complex(a2, b2) * complex(a2, -b2)
    realTermD3 = float(numeratorD3.real / denominatorD3.real)
    imagTermD3 = float(numeratorD3.imag)
    distractor3 = [realTermD3, imagTermD3]
    # Multiply by conjugate, only divide second term
    numeratorD4 = complex(a1, b1) * complex(a2, -b2)
    denominatorD4 = complex(a2, b2) * complex(a2, -b2)
    realTermD4 = float(numeratorD4.real)
    imagTermD4 = float(numeratorD4.imag / denominatorD4.real)
    distractor4 = [realTermD4, imagTermD4]
    return [distractor1, distractor2, distractor3, distractor4]
def displayComplexFloat(problem):
    a, b = problem
    if b < 0:
        if b == -1:
            display = "%.2f  - i" %a
        else:
            display = "%.2f  - %.2f i" %(a, -b)
    else:
        if b == 1:
            display = "%.2f + i" %a
        else:
            display = "%.2f  + %.2f i" %(a, b)
    return display
def generateProblemCoefficientsAndSolution():
    complex1 = complex(0,0)
    complex2 = complex(0,0)
    while complex1==complex2:
        initialCoefficients = generateDistinctCoefficients()
        a1, b1, a2, b2 = initialCoefficients
        a1 = 9 * a1
        b1 = 11 * b1
        complex1=complex(a1, b1)
        complex2=complex(a2, b2)
        coefficients=[a1, b1, a2, b2]
        quotient=complex1/complex2
        solution = [quotient.real, quotient.imag]
    return [coefficients, solution]

### VARIABLE DECLARATIONS ###
coefficients, solution = generateProblemCoefficientsAndSolution()
distractors = generateDistractors(coefficients)
# In the future, I need to do something to check if the distractors are far enough apart.

### CREATE INTERVAL OPTIONS ###
round_to=2
solutionList = round_set_of_floats([solution, distractors[0], distractors[1], distractors[2], distractors[3]], round_to)
intervalOptions = createIntervalOptions(solutionList, 1, 0.5)

### DEFINE ANSWERLIST AND DISPLAYSOLUTION ###
display_solution = displayComplexFloat([round(solution[0], 2), round(solution[1], 2)])
displayDistractor1 = displayComplexFloat([distractors[0][0], distractors[0][1]])
displayDistractor2 = displayComplexFloat([distractors[1][0], distractors[1][1]])
displayDistractor3 = displayComplexFloat([distractors[2][0], distractors[2][1]])
displayDistractor4 = displayComplexFloat([distractors[3][0], distractors[3][1]])

c0 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[0][0][0], intervalOptions[0][0][1], intervalOptions[0][1][0], intervalOptions[0][1][1])
c1 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[1][0][0], intervalOptions[1][0][1], intervalOptions[1][1][0], intervalOptions[1][1][1])
c2 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[2][0][0], intervalOptions[2][0][1], intervalOptions[2][1][0], intervalOptions[2][1][1])
c3 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[3][0][0], intervalOptions[3][0][1], intervalOptions[3][1][0], intervalOptions[3][1][1])
c4 = "a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[4][0][0], intervalOptions[4][0][1], intervalOptions[4][1][0], intervalOptions[4][1][1])

solutionInterval = [c0, "* $%s$, which is the correct option." %display_solution, 1]
distractor1Interval = [c1, " $%s$, which corresponds to just dividing the first term by the first term and the second by the second." %displayDistractor1, 0]
distractor2Interval = [c2, " $%s$, which corresponds to forgetting to multiply the conjugate by the numerator and not computing the conjugate correctly." %displayDistractor2, 0]
distractor3Interval = [c3, " $%s$, which corresponds to forgetting to multiply the conjugate by the numerator." %displayDistractor3, 0]
distractor4Interval = [c4, " $%s$, which corresponds to forgetting to multiply the conjugate by the numerator and using a plus instead of a minus in the denominator." %displayDistractor4, 0]
answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

### DEFINE STEM, PROBLEM, AND GENERAL COMMENT ###
display_stem = 'Simplify the expression below into the form $a+bi$. Then, choose the intervals that $a$ and $b$ belong to.'
display_problem = "\\frac{%s}{%s}" %(displayComplexFactor([coefficients[0], coefficients[1]]), displayComplexFactor([coefficients[2], coefficients[3]]))
general_comment = "Multiply the numerator and denominator by the *conjugate* of the denominator, then simplify. For example, if we have $2+3i$, the conjugate is $2-3i$."

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choice_comments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answer_letter_indicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answer_letter = identifyAnswerLetter(answer_letter_indicators)

# NEW!!!!!
display_stem_type="String"
display_problem_type="Math Mode"
display_options_type="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, display_stem_type, display_stem, display_problem_type, display_problem, display_options_type, choices, choice_comments, display_solution, answer_letter, general_comment)
