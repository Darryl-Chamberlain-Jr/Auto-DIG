# Module 12 - Rational Functions
# Objective 2 - Vertical Asymptotes and Holes

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
    a2, b2 = generateRationalFactor()
    z0 = float(b0)/float(a0)
    z1 = float(b1)/float(a1)
    z2 = float(b2)/float(a2)
    while (z0 == z1) or (z0 == z2) or (z1 == z2):
        a0, b0 = generateRationalFactor()
        a1, b1 = generateRationalFactor()
        a2, b2 = generateRationalFactor()
        z0 = float(b0)/float(a0)
        z1 = float(b1)/float(a1)
        z2 = float(b2)/float(a2)
    b3 = maybeMakeNegative(random.randint(1, 4))
    coeffNumA = a0*a1
    coeffNumB = -a0*b1 - a1*b0 - a0*a1*b3
    coeffNumC = b0*b1 + a0*b1*b3 + a1*b0*b3
    coeffNumD = -b0*b1*b3
    if coeffNumB < 0:
        if coeffNumC < 0:
            if coeffNumD < 0:
                numerator = "%s x^3 - %s x^2 - %s x - %s" %(coeffNumA, -coeffNumB, -coeffNumC, -coeffNumD)
            else:
                numerator = "%s x^3 - %s x^2 - %s x + %s" %(coeffNumA, -coeffNumB, -coeffNumC, coeffNumD)
        else:
            if coeffNumD < 0:
                numerator = "%s x^3 - %s x^2 + %s x - %s" %(coeffNumA, -coeffNumB, coeffNumC, -coeffNumD)
            else:
                numerator = "%s x^3 - %s x^2 + %s x + %s" %(coeffNumA, -coeffNumB, coeffNumC, coeffNumD)
    else:
        if coeffNumC < 0:
            if coeffNumD < 0:
                numerator = "%s x^3 + %s x^2 - %s x - %s" %(coeffNumA, coeffNumB, -coeffNumC, -coeffNumD)
            else:
                numerator = "%s x^3 + %s x^2 - %s x + %s" %(coeffNumA, coeffNumB, -coeffNumC, coeffNumD)
        else:
            if coeffNumD < 0:
                numerator = "%s x^3 + %s x^2 + %s x - %s" %(coeffNumA, coeffNumB, coeffNumC, -coeffNumD)
            else:
                numerator = "%s x^3 + %s x^2 + %s x + %s" %(coeffNumA, coeffNumB, coeffNumC, coeffNumD)
    #(a0*x-b0)(a2*x-b2)
    coeffDenA = a0*a2
    coeffDenB = -a0*b2 - a2*b0
    coeffDenC = b0*b2
    if coeffDenB < 0:
        if coeffDenC < 0:
            denominator = "%s x^2 - %s x - %s" %(coeffDenA, -coeffDenB, -coeffDenC)
        else:
            denominator = "%s x^2 - %s x + %s" %(coeffDenA, -coeffDenB, coeffDenC)
    else:
        if coeffDenC < 0:
            denominator = "%s x^2 + %s x - %s" %(coeffDenA, coeffDenB, -coeffDenC)
        else:
            denominator = "%s x^2 + %s x + %s" %(coeffDenA, coeffDenB, coeffDenC)
    #
    horizontalAsy = float(a1) / float(a2)
    hole = z0
    verticalAsy = z2
    fakeVert = z1
    return [numerator, denominator, verticalAsy, hole, horizontalAsy, fakeVert]

def cleanRational(rational):
    return round(float(rational), 3)

numerator, denominator, verticalAsy, hole, horizontalAsy, fakeVert = createNumAndDenom()

solution = ["\\text{Vertical Asymptote of } x = %s \\text{ and hole at } x = %s" %(cleanRational(verticalAsy), cleanRational(hole)), "This is the correct answer."]
distractorAllVertical = ["\\text{Vertical Asymptotes of } x = %s \\text{ and } x = %s \\text{ with no holes.}" %(cleanRational(verticalAsy), cleanRational(hole)), "This corresponds to not factoring out the hole."]
distractorAllHoles = ["\\text{Holes at } x = %s \\text{ and } x = %s \\text{ with no vertical asymptotes.}" %(cleanRational(verticalAsy), cleanRational(hole)), "This corresponds to considering where the denominator is equal to 0 as holes."]
distractorHor = ["\\text{Vertical Asymptote of } x = %s \\text{ and hole at } x = %s" %(cleanRational(horizontalAsy), cleanRational(hole)), "This corresponds to mixing vertical and horizontal asymptotes."]
distractorAllNumerator = ["\\text{Vertical Asymptotes of } x = %s \\text{ and } x = %s \\text{ with a hole at } x = %s" %(cleanRational(verticalAsy), cleanRational(fakeVert), cleanRational(hole)), "This corresponds to setting the numerator equal to 0."]

displayStem = "Determine the vertical asymptotes and holes in the rational function below."
displayProblem = "\\frac{%s}{%s}" %(numerator, denominator)
displaySolution = solution[0]
generalComments = "General Comments: Remember to factor the numerator and denominator. Any factors that cancel are holes in the function. The zeros left in the denominator are the vertical asymptotes."

answerList = [solution, distractorAllVertical, distractorAllHoles, distractorHor, distractorAllNumerator]
random.shuffle(answerList)

c0 = answerList[0][0]
c1 = answerList[1][0]
c2 = answerList[2][0]
c3 = answerList[3][0]
c4 = answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

writeQuestionToFile(moduleNumber, version, problemNumber, displayStem, displayProblem)
writeSolutionAndOptionsToFile(moduleNumber, version, displaySolution, choices, choiceComments)
writeCommentsToFile(moduleNumber, version, generalComments)

print "I have completed Module 12 Objective 2, Master"
