# Module 12 - Rational Functions
# Objective 1 - Domain of Rational Functions

import random

def generateRationalFunction():
    a1 = random.randint(3, 6)
    b1 = maybeMakeNegative(random.randint(3, 6))
    a2 = random.randint(3, 6)
    b2 = maybeMakeNegative(random.randint(3, 6))
    excludeFromDomain1 = min(float(-b1)/float(a1), float(-b2)/float(a2))
    excludeFromDomain2 = max(float(-b1)/float(a1), float(-b2)/float(a2))
    while (excludeFromDomain1 == excludeFromDomain2):
        a1 = random.randint(3, 6)
        b1 = maybeMakeNegative(random.randint(3, 6))
        a2 = random.randint(3, 6)
        b2 = maybeMakeNegative(random.randint(3, 6))
        excludeFromDomain1 = min(float(-b1)/float(a1), float(-b2)/float(a2))
        excludeFromDomain2 = max(float(-b1)/float(a1), float(-b2)/float(a2))
    # (a1*x+b1)(a2*x+b2) = (a1*a2)*x**2 + (a1*b2 + a2*b1)*x + (b1*b2)
    function = generatePolynomialDisplay([a1*a2, a1*b2+a2*b1, b1*b2])
    distractor1 = min(-a1*b1, -a2*b2)
    distractor2 = max(-a1*b1, -a2*b2)
    return [function, excludeFromDomain1, excludeFromDomain2, distractor1, distractor2]

quadraticDenominator, exclude1, exclude2, distractor1, distractor2 = generateRationalFunction()
numerator = random.randint(3, 6)
intervalRange = 3
precision = 1

listOfValues = [exclude1, exclude2, distractor1, distractor2]
intervalOptions = createIntervalOptions(listOfValues, intervalRange, precision)

solution = ["\\text{All Real numbers except } x = a \\text{ and } x = b, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1], intervalOptions[1][0], intervalOptions[1][1]), "All Real numbers except $x = %.3f$ and $x = %.3f$, which is the correct option." %(exclude1, exclude2), 1]
distractorExclude2 = ["\\text{All Real numbers except } x = a \\text{ and } x = b, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1], intervalOptions[3][0], intervalOptions[3][1]), "All Real numbers except $x = %.3f$ and $x = %.3f$, which corresponds to not factoring the denominator correctly." %(distractor1, distractor2), 0]
distractorExclude1Wrong = ["\\text{All Real numbers except } x = a, \\text{ where } a \\in [%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1]), "All Real numbers except $x = %.3f$, which corresponds to removing only 1 value from the denominator." %exclude1, 0]
distractorExclude1Right = ["\\text{All Real numbers except } x = a, \\text{ where } a \\in [%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1]), "All Real numbers except $x = %.3f$, which corresponds to removing a distractor value from the denominator." %distractor1, 0]
distractorAll = ["\\text{All Real numbers.}", "This corresponds to thinking the denominator has complex roots or that rational functions have a domain of all Real numbers.", 0]

displayStem = "Determine the domain of the function below."
displayProblem = "f(x) = \\frac{%s}{%s}" %(numerator, quadraticDenominator)
displaySolution = "\\text{All Real numbers except } x = %.3f \\text{ and } x = %.3f." %(exclude1, exclude2)
generalComment = "General Comments: The new domain is the intersection of the previous domains."

answerList = [solution, distractorExclude2, distractorExclude1Wrong, distractorExclude1Right, distractorAll]
random.shuffle(answerList)

c0 = answerList[0][0]
c1 = answerList[1][0]
c2 = answerList[2][0]
c3 = answerList[3][0]
c4 = answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
