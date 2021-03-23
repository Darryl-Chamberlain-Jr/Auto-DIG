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

def generateDisplayAndZeros():
    # This can be improved in the future with numpy.poly1d as it provides quotient and remainder with poly division.
    #Goal: (a0*x+b0)*(a1*x+b1)*(x-za)(x-zb)
    a0 = random.randint(2, 5)
    b0 = maybeMakeNegative(random.randint(2, 5))
    a1 = random.randint(2, 5)
    b1 = maybeMakeNegative(random.randint(2, 5))
    za = maybeMakeNegative(random.randint(2, 5))
    zb = maybeMakeNegative(random.randint(2, 5))
    while (gcd(a0, b0)>1 or gcd(a1, b1)>1) or (a0 == a1 and b0 == b1) or (za == zb):
        a0 = random.randint(2, 5)
        b0 = maybeMakeNegative(random.randint(2, 5))
        a1 = random.randint(2, 5)
        b1 = maybeMakeNegative(random.randint(2, 5))
        za = maybeMakeNegative(random.randint(2, 5))
        zb = maybeMakeNegative(random.randint(2, 5))
    #intermediatePolynomial = (a0*a1)*x**3 + (-a0*a1*za + a0*b1 + a1*b0)*x**2+ (-a0*b1*za - a1*b0*za + b0*b1)*x + (-b0*b1*za)
    c3 = a0*a1
    c2 = -a0*a1*za + a0*b1 + a1*b0
    c1 = -a0*b1*za - a1*b0*za + b0*b1
    c0 = -b0*b1*za
    # intermediatePolynomial = interCo1*x**3 + interCo2*x**2 + interCo3*x + interCo4
    f4 = c3
    f3 = c2 - c3*zb
    f2 = c1 - c2*zb
    f1 = c0 - c1*zb
    f0 = -c0*zb
    finalPoly = generatePolynomialDisplay([f4, f3, f2, f1, f0])
    z1 = round(float(-b0/a0), 3)
    z2 = round(float(-b1/a1), 3)
    z3 = za
    z4 = zb
    #zeros = [float(-b0/a0), float(-b1/a1), za, zb]
    zeros = descendingOrder(z1, z2, z3, z4)
    coefficients = [a0, b0, a1, b1, za, zb]

    return [finalPoly, zeros, coefficients]

def descendingOrder(z1, z2, z3, z4):
    # First we put z1, z2 and z3 in order, then fit z4 in.
    if (z1 <= z2 and z1 <=z3):
        #Then z1 is the smallest
        if (z2 <= z3):
            zeros = [z1, z2, z3]
        else:
            zeros = [z1, z3, z2]
    # z1 is not the smallest
    elif (z2<=z3):
        if(z1<=z3):
            zeros = [z2, z1, z3]
        else:
            zeros = [z2, z3, z1]
    else:
        if(z1<=z2):
            zeros = [z3, z1, z2]
        else:
            zeros = [z3, z2, z1]

    if (z4<= zeros[0] and z4 <= zeros[1] and z4 <= zeros[2]):
        listOfZeros = [z4, zeros[0], zeros[1], zeros[2]]
    elif (z4 <= zeros[1] and z4 <= zeros[2]):
        listOfZeros = [zeros[0], z4, zeros[1], zeros[2]]
    elif (z4 <= zeros[2]):
        listOfZeros = [zeros[0], zeros[1], z4, zeros[2]]
    else:
        listOfZeros = [zeros[0], zeros[1], zeros[2], z4]

    return listOfZeros

def generateDistractors(coefficients):
    a0, b0, a1, b1, z0, z1 = coefficients
    a0f = float(a0)
    a1f = float(a1)
    b0f = float(b0)
    b1f = float(b1)
    # Distractor 1: Corresponds to negatives of all zeros.
    distractor1 = descendingOrder(float(b0f/a0f), float(b1f/a1f), -z0, -z1)
    # Distractor 2: Corresponds to inversing rational roots.
    distractor2 = descendingOrder(float(-a0f/b0f), float(-a1f/b1f), z0, z1)
    # Distractor 3: Corresponds to negatives of all zeros AND inversing rational roots.
    distractor3 = descendingOrder(float(a0f/b0f), float(a1f/b1f), -z0, -z1)
    # Distractor 4: Corresponds to moving factors from one rational to another.
    distractor4 = descendingOrder(b0, float(b1f/(a1f*a0f)), -z0, -z1)
    distractors = [distractor1, distractor2, distractor3, distractor4]
    return distractors

intervalRange = 3
precision = 1

displayPolynomial, zeros, coefficients = generateDisplayAndZeros()
solution = zeros
distractors = generateDistractors(coefficients)

solutionList = [solution, distractors[0], distractors[1], distractors[2], distractors[3]]
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = intervalOptions[0]
distractor1Interval = intervalOptions[1]
distractor2Interval = intervalOptions[2]
distractor3Interval = intervalOptions[3]
distractor4Interval = intervalOptions[4]

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

solutionInterval.append("* This is the solution!")
distractor1Interval.append(" Distractor 1: Corresponds to negatives of all zeros.")
distractor2Interval.append(" Distractor 2: Corresponds to inversing rational roots.")
distractor3Interval.append(" Distractor 3: Corresponds to negatives of all zeros AND inversing rational roots.")
distractor4Interval.append(" Distractor 4: Corresponds to moving factors from one rational to another.")

solutionInterval.append(1)
distractor1Interval.append(0)
distractor2Interval.append(0)
distractor3Interval.append(0)
distractor4Interval.append(0)

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

if(coefficients[4]<0):
    displayStem = "Factor the polynomial below completely, knowing that $x+%d$ is a factor. Then, choose the intervals the zeros of the polynomial belong to, where $z_1 \\leq z_2 \\leq z_3 \\leq z_4$. \\textit{To make the problem easier, all zeros are between -5 and 5.}" %(-coefficients[4])
else:
    displayStem = "Factor the polynomial below completely, knowing that $x-%d$ is a factor. Then, choose the intervals the zeros of the polynomial belong to, where $z_1 \\leq z_2 \\leq z_3 \\leq z_4$. \\textit{To make the problem easier, all zeros are between -5 and 5.}" %coefficients[4]

displayProblem = "f(x) = %s" %displayPolynomial
displaySolution = solution
generalComment = "Remember to try the middle-most integers first as these normally are the zeros. Also, once you get it to a quadratic, you can use your other factoring techniques to finish factoring."

c0 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], z_3 \\in [%s, %s], \\text{   and   } z_4 \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1], answerList[0][1][0], answerList[0][1][1], answerList[0][2][0], answerList[0][2][1], answerList[0][3][0], answerList[0][3][1])
c1 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], z_3 \\in [%s, %s], \\text{   and   } z_4 \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1], answerList[1][1][0], answerList[1][1][1], answerList[1][2][0], answerList[1][2][1], answerList[1][3][0], answerList[1][3][1])
c2 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], z_3 \\in [%s, %s], \\text{   and   } z_4 \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1], answerList[2][1][0], answerList[2][1][1], answerList[2][2][0], answerList[2][2][1], answerList[2][3][0], answerList[2][3][1])
c3 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], z_3 \\in [%s, %s], \\text{   and   } z_4 \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1], answerList[3][1][0], answerList[3][1][1], answerList[3][2][0], answerList[3][2][1], answerList[3][3][0], answerList[3][3][1])
c4 = "z_1 \\in [%s, %s], \\text{   }  z_2 \\in [%s, %s], z_3 \\in [%s, %s], \\text{   and   } z_4 \\in [%s, %s]" %(answerList[4][0][0], answerList[4][0][1], answerList[4][1][0], answerList[4][1][1], answerList[4][2][0], answerList[4][2][1], answerList[4][3][0], answerList[4][3][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][4], answerList[1][4], answerList[2][4], answerList[3][4], answerList[4][4]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][5] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
