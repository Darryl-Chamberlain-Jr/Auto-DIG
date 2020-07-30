items = [['\\text{Whole}', 0, "These are the counting numbers with 0 (0, 1, 2, 3, ...)"], ['\\text{Integer}', 1, "These are the negative and positive counting numbers (..., -3, -2, -1, 0, 1, 2, 3, ...)"], ['\\text{Rational}', 2, "These are numbers that can be written as fraction of Integers (e.g., -2/3)"], ['\\text{Irrational}', 3, "These cannot be written as a fraction of Integers."], ['\\text{Not a Real number}', 4, "These are Nonreal Complex numbers OR things that are not numbers (dividing by 0)."]]
random.shuffle(items)
chooseSomething = random.randint(0, 4)
questionTypePrint = items[chooseSomething][0]
questionTypeGeneration = items[chooseSomething][1]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if items[answerIndex][0] == questionTypePrint:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

#Question Type 1 generates Whole numbers
if questionTypeGeneration==0:
    denominatorbase = random.randint(5, 25)
    numeratorbase = denominatorbase * random.randint(5, 25)
    denominator = denominatorbase * denominatorbase
    numerator = numeratorbase * numeratorbase
    displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
    simplifiedNumber = numeratorbase
#Question Type 2 generates Integers
elif questionTypeGeneration==1:
    denominatorbase = random.randint(5, 25)
    # Makes sure we return a natural number
    numeratorbase = denominatorbase * random.randint(5, 25)
    # Makes perfect squares
    denominator = denominatorbase * denominatorbase
    numerator = numeratorbase * numeratorbase
    displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
    simplifiedNumber = -numeratorbase
#Question Type 3 generates Rational numbers
elif questionTypeGeneration==2:
    numerator = random.randint(5, 25)
    denominator = random.randint(5, 25)
    # Checks to make sure we get a non-Whole, Rational number
    while (gcd(numerator, denominator) > 1):
        denominator = random.randint(5, 25)
    randomNeg = (-1)**random.randint(0, 1)
    if randomNeg == -1:
        displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator**2, denominator**2)
        simplifiedNumber = '-\\frac{%d}{%d}' %(numerator, denominator)
    else:
        displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator**2, denominator**2)
        simplifiedNumber = '\\frac{%d}{%d}' %(numerator, denominator)
#Question Type 4 generates Irrational numbers
elif questionTypeGeneration==3:
	# Base of the number under the square root
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
    randomNeg = (-1)**random.randint(0, 1)
    if randomNeg == -1:
        displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
        simplifiedNumber = '-\\sqrt{%d}' %(discriminantbase*irrationalmaker)
    else:
        displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
        simplifiedNumber = '\\sqrt{%d}' %(discriminantbase*irrationalmaker)
#Question Type 5 generates Non-Real numbers (divding by zero or complex)
elif questionTypeGeneration==4:
    chooseZeroOrComplex = random.randint(0, 1)
    if chooseZeroOrComplex == 0:
        # Not a number
        numerator = random.randint(5, 25)
        denominator = 0
        randomNeg = (-1)**random.randint(0, 1)
        if randomNeg == -1:
            displayProblem =  '-\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
        else:
            displayProblem =  '\\sqrt{\\frac{%d}{%d}}' %(numerator, denominator)
        simplifiedNumber = displayProblem
    else:
        # Complex number
        discrim = random.randint(9, 18)
        irrationalmaker = 5
        maskirrational = random.randint(5, 15)
        while gcd(discrim, irrationalmaker) > 1:
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
else:
    print("Something bad happened!")

#displayNumber = randomnegative * sqrt(numerator/denominator)
# This randomizes the answer items
displayStem = 'Choose the \\textbf{smallest} set of Real numbers that the number below belongs to.'
if questionTypeGeneration == 4:
    displaySolution = "\\text{Not a Real Number}"
else:
    displaySolution = "\\text{%s}" %questionTypePrint

# No comments per choice
choices = [items[0][0], items[1][0], items[2][0], items[3][0], items[4][0]]
choiceComments = [items[0][2], items[1][2], items[2][2], items[3][2], items[4][2]]
generalComment = "General Comments: First, you \\textbf{NEED} to simplify the expression. This question simplifies to $%s$. \n \n Be sure you look at the simplified fraction and not just the decimal expansion. Numbers such as 13, 17, and 19 provide \\textbf{long but repeating/terminating decimal expansions!} \n \n The only ways to *not* be a Real number are: dividing by 0 or taking the square root of a negative number. Irrational numbers are more than just square root of 3: adding or subtracting values from square root of 3 is also irrational." %simplifiedNumber

writeToKey(keyFileName, version, problemNumber, displayStem, "MathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
