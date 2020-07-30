# TYPES - Autogenerate a Rational, Irrational, Nonreal Complex, Pure Imaginary, or Non-Complex number

def generateRationalFromSubgroupReal():
    numerator = random.randint(5, 25)
    denominator = random.randint(5, 25)
    # Checks to make sure we get a non-Whole, Rational number
    while (gcd(numerator, denominator) > 1):
        denominator = random.randint(5, 25)
    return [numerator**2, denominator**2]

def generateIrrationalFromSubgroupReal():
    discriminantbase = random.randint(9, 18)
    # The number we will use to make sure we get an irrational number
    irrationalmaker = 5
    # Masks that the fraction is not a perfect square
    maskirrational = random.randint(5, 15)
    # Makes sure the product is not a perfect square
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
    irrationalmaker = 5
    maskirrational = random.randint(5, 15)
    while gcd(discrim, irrationalmaker) > 1:
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

#Question Type 1 generates Irrational numbers of the form a + 0i
def generateIrrationalNumber():
    # Base of the number under the square root
    discriminantbase = random.randint(9, 18)
    # The number we will use to make sure we get an irrational number
    irrationalmaker = 5
    # Makes sure the product is not a perfect square
    while gcd(discriminantbase, irrationalmaker) > 1:
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

#Question Type 2 generates Nonreal Complex numbers of the form a + bi
def generateNonRealComplexNumber():
    numerator = random.randint(5, 25)*(-1)**random.randint(0, 1)
    denominator = random.randint(5, 25)
    while gcd(numerator, denominator) == denominator:
        denominator = random.randint(5, 25)
    # Base of the number under the square root
    discriminantbase = random.randint(9, 18)
    # The number we will use to make sure we get an irrational number
    irrationalmaker = 5
    # Makes sure the product is not a perfect square
    while gcd(discriminantbase, irrationalmaker) > 1:
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

#Question Type 3 generates Pure Imaginary numbers of the form 0 + bi
def generatePureImaginaryNumber():
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

#Question Type 4 generates Non-Complex numbers (dividing by 0)
def generateNonNumber():
    numerator = random.randint(5, 25)*(-1)**random.randint(0, 1)
    denominator = random.randint(5, 25)
    while gcd(numerator, denominator) == denominator:
        denominator = random.randint(5, 25)
    # Base of the number under the square root
    discriminantbase = random.randint(9, 18)
    # The number we will use to make sure we get an irrational number
    irrationalmaker = 5
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

############
items = [["\\text{Rational}", 0, "These are numbers that can be written as fraction of Integers (e.g., -2/3 + 5)"], ["\\text{Irrational}", 1, "These cannot be written as a fraction of Integers. Remember: $\\pi$ is not an Integer!"], ["\\text{Nonreal Complex}", 2, "This is a Complex number $(a+bi)$ that is not Real (has $i$ as part of the number)."], ["\\text{Pure Imaginary}", 3, "This is a Complex number $(a+bi)$ that \\textbf{only} has an imaginary part like $2i$."], ["\\text{Not a Complex Number}", 4, "This is not a number. The only non-Complex number we know is dividing by 0 as this is not a number!"]]
random.shuffle(items)
chooseSomething = random.randint(0, 4)
displaySolution = items[chooseSomething][0]
questionTypeGeneration = items[chooseSomething][1]

#Question Type 0 generates Rational numbers of the form a + 0i
if questionTypeGeneration == 0:
    displayProblem = generateRationalNumber()
elif questionTypeGeneration == 1:
    displayProblem = generateIrrationalNumber()
elif questionTypeGeneration == 2:
    displayProblem = generateNonRealComplexNumber()
elif questionTypeGeneration == 3:
    displayProblem = generatePureImaginaryNumber()
else:
    displayProblem = generateNonNumber()

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if items[answerIndex][0] == displaySolution:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

choices = [items[0][0], items[1][0], items[2][0], items[3][0], items[4][0]]
choiceComments = [items[0][2], items[1][2], items[2][2], items[3][2], items[4][2]]

displayStem = 'Choose the \\textbf{smallest} set of Complex numbers that the number below belongs to.'
generalComment = "General Comments: Be sure to simplify $i^2 = -1$. This may remove the imaginary portion for your number. If you are having trouble, you may want to look at the \\textit{Subgroups of the Real Numbers} section."

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
