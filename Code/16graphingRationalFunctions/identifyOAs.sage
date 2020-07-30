# Module 12 - Rational Functions
# Objective 3 - Horizontal and Oblique Asymptotes

# \\frac{(a0*x-b0)(a1*x-b1)(x-b3)}{(a0*x-b0)(a2*x-b2)}

def generateRationalFactor():
    a = random.randint(2, 4)
    b = maybeMakeNegative(random.randint(2, 5))
    while (gcd(abs(a), abs(b)) > 1):
        a = random.randint(2, 4)
        b = maybeMakeNegative(random.randint(2, 5))
    return [a, b]

def createNumAndDenom():
    a0, b0 = generateRationalFactor()
    a1, b1 = generateRationalFactor()
    a2, b2 = [1, maybeMakeNegative(random.randint(2, 5))]
    z0 = float(b0)/float(a0)
    z1 = float(b1)/float(a1)
    z2 = float(b2)/float(a2)
    while (z0 == z1) or (z0 == z2) or (z1 == z2):
        a0, b0 = generateRationalFactor()
        a1, b1 = generateRationalFactor()
        a2, b2 = [1, maybeMakeNegative(random.randint(2, 5))]
        z0 = float(b0)/float(a0)
        z1 = float(b1)/float(a1)
        z2 = float(b2)/float(a2)
    b3 = maybeMakeNegative(random.randint(1, 4))
    coeffNumA = a0*a1
    coeffNumB = -a0*b1 - a1*b0 - a0*a1*b3
    coeffNumC = b0*b1 + a0*b1*b3 + a1*b0*b3
    coeffNumD = -b0*b1*b3
    numerator = generatePolynomialDisplay([coeffNumA, coeffNumB, coeffNumC, coeffNumD])
    #(a0*x-b0)(a2*x-b2)
    coeffDenA = a0*a2
    coeffDenB = -a0*b2 - a2*b0
    coeffDenC = b0*b2
    denominator = generatePolynomialDisplay([coeffDenA, coeffDenB, coeffDenC])
    #
    falseHorizontalAsy = float(a1) / float(a2)
    hole = z0
    verticalAsy = z2
    obliqueAsyA = a1
    obliqueAsyB = -a1*b3 - b1 + b2*a1
    obliqueAsy = generatePolynomialDisplay([obliqueAsyA, obliqueAsyB])
    #
    return [numerator, denominator, obliqueAsy, verticalAsy, hole, falseHorizontalAsy]

def cleanRational(rational):
    return round(float(rational), 3)

numerator, denominator, obliqueAsy, verticalAsy, hole, falseHorizontalAsy = createNumAndDenom()

solution = ["\\text{Oblique Asymptote of } y = %s." %(obliqueAsy), "This is the correct answer.", 1]
distractorHorizontal = ["\\text{Horizontal Asymptote of } y = %s " %(cleanRational(falseHorizontalAsy)), "This corresponds to using rule for Horizontal Asymptote when degree of numerator and denominator match.", 0]
distractorVertical = ["\\text{Horizontal Asymptote at } y = %s" %(cleanRational(verticalAsy)), "This corresponds to considering where the denominator is equal to 0 as horizontal asymptote.", 0]
distractorObliqueAndHorizontal = ["\\text{Horizontal Asymptote of } y = %s \\text{ and Oblique Asymptote of } y = %s" %(cleanRational(falseHorizontalAsy), obliqueAsy), "This corresponds to believing there can be both a horizontal and oblique asymptote.", 0]
distractorObliqueAndVertical = ["\\text{Horizontal Asymptote of } y = %s \\text{ and Oblique Asymptote of } y = %s" %(cleanRational(verticalAsy), obliqueAsy), "This corresponds to believing there can be both a horizontal and oblique asymptote AND mixing up horizontal/vertical asymoptote.", 0]

displayStem = "Determine the horizontal and/or oblique asymptotes in the rational function below."
displayProblem = "\\frac{%s}{%s}" %(numerator, denominator)
displaySolution = "y = %s" %(obliqueAsy)
generalComment = "General Comments: We have a Horizontal Asymptote if the degree of the numerator is smaller than or equal to the degree of the denominator. We have an Oblique Asymptote if the degree of the numerator is larger than the degree of the denominator. We cannot have both!"

answerList = [solution, distractorHorizontal, distractorVertical, distractorObliqueAndHorizontal, distractorObliqueAndVertical]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
