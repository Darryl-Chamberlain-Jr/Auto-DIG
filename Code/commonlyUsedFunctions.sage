# Commonly used to find the GCF of two integers.
def greatestCommonDenominator(a, b):
    if(not (isinstance(a, int) and isinstance(b, int))):
        raise TypeError("One of the numbers you passed is not an integer.")
    while (not b == 0):
        temp = b
        b = a % b
        a = temp
    return abs(a)

# Takes the options available and the comments as they are assigned to each option before shuffle. *radicalEquationToGraph.sage* has a good example.
def commentsForGraphs(unshuffledOptionList, optionList, shuffledComments):
    if len(optionList) == 4:
        choiceComments =  ["", "", "", ""]
    else:
        choiceComments = ["", "", "", "", ""]
    k=0
    while k < len(optionList):
        i=0
        for letter in unshuffledOptionList:
            if letter == optionList[k]:
                choiceComments[k] = shuffledComments[i]
            i = i+1
        k=k+1
    return choiceComments

# Checks if the solution and distractors are "Distinct". If not, returns "Copies".
def checkUnique(values):
    # DARRYL COMMENT: Could this be rewritten to check that len(setInQuestion) == len(set(setInQuestion))?
    if len(values) == len(set(values)):
        return "Distinct"
    else:
        return "Copies"

# Generates the terms of a polynomial. Needed when polynomials are defined by set of coefficients. This removes terms with 0 coefficient and ensures signs are displayed correctly. Is not limited by number of coefficients.
def generateTerms(coefficients):
    i=0
    if len(coefficients) == 2:
        if coefficients[i] == 1:
            terms = ["x"]
        elif coefficients[i] == -1:
            terms = ["-x"]
        else:
            terms = ["%sx" %(coefficients[0])]
    elif len(coefficients) == 1:
        terms = ["%s" %coefficients[0]]
    else:
        if coefficients[i] == 1:
            terms = ["x^{%d}" %(len(coefficients)-1)]
        elif coefficients[i] == -1:
            terms = ["-x^{%d}" %(len(coefficients)-1)]
        else:
            terms = ["%sx^{%d}" %(coefficients[0], len(coefficients)-1)]
    i=i+1
    while i < len(coefficients):
        if coefficients[i] == 0:
            print("Skipping a zero term.")
        elif coefficients[i] < 0:
            if len(coefficients)-i-1 == 1:
                if coefficients[i] == -1:
                    terms.append("-x")
                else:
                    terms.append("-%s x" %(-coefficients[i]))
            elif len(coefficients)-i-1 == 0:
                terms.append("-%s" %(-coefficients[i]))
            else:
                if coefficients[i] == 1:
                    terms.append("-x^{%d}" %(len(coefficients)-i-1))
                else:
                    terms.append("-%s x^{%d}" %(-coefficients[i], len(coefficients)-i-1))
        else:
            if len(coefficients)-i-1 == 1:
                if coefficients[i] == 1:
                    terms.append("+x")
                else:
                    terms.append("+%s x" %(coefficients[i]))
            elif len(coefficients)-i-1 == 0:
                terms.append("+ %s" %(coefficients[i]))
            else:
                if coefficients[i] == 1:
                    terms.append("+ x^{%d}" %(len(coefficients)-i-1))
                else:
                    terms.append("+%s x^{%d}" %(coefficients[i], len(coefficients)-i-1))
        i=i+1
    return terms

# Used  to generate the display of polynomials for the .tex file. Works in tandem with the *generateTerms* function. Limited to 10 terms, though this can easily be expanded if needed.
def generatePolynomialDisplay(coefficients):
    terms = generateTerms(coefficients)
    if len(terms) == 10:
        polynomial = "%s %s %s %s %s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7], terms[8], terms[9])
    elif len(terms) == 9:
        polynomial = "%s %s %s %s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7], terms[8])
    elif len(terms) == 8:
        polynomial = "%s %s %s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7])
    elif len(terms) == 7:
        polynomial = "%s %s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6])
    elif len(terms) == 6:
        polynomial = "%s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5])
    elif len(terms) == 5:
        polynomial = "%s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4])
    elif len(terms) == 4:
        polynomial = "%s %s %s %s" %(terms[0], terms[1], terms[2], terms[3])
    elif len(terms) == 3:
        polynomial = "%s %s %s" %(terms[0], terms[1], terms[2])
    elif len(terms) == 2:
        polynomial = "%s %s" %(terms[0], terms[1])
    elif len(terms) == 1:
        polynomial = "%s" %(terms[0])
    else:
        polynomial = "Your polynomial has more than 10 terms."
    return polynomial

# Takes in a rational value and multiplies it by either 1 or -1.
def maybeMakeNegative(rational):
    maybeNegative = int((-1)**random.randint(0, 1))
    rational = maybeNegative * rational
    return rational
