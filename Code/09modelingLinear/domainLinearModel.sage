# Sort by Restricted Domain

### NATURAL ###
natural0 = "\\begin{center} \\textit{Hannah plans to pay off a no-interest loan from her parents. Her loan balance is \\$1,000. She plans to pay \\$35 at the end of every week until her balance is \\$0. How many weeks will it be until she has paid off her loan?} \\end{center}"
naturals = [natural0]

### INTEGERS ###
integers0 = "\\begin{center} \\textit{Fred is a store manager at Publix. The store normally orders two pallets of water bottles a week and sells 1000 bottles per day. However, a hurricane is coming and Fred expects water bottle sales to increase tenfold for three days, then decrease by half of normal sales for four days. How many more pallets of water bottles should Fred order the week before the hurricane?} \\end{center}"
integers = [integers0]

### RATIONALS ###
rationals0 = "\\begin{center} \\textit{Veronica needs to prepare 170 lbs of blended coffee beans to sell for \\$4.71 per pound. She has a high-quality bean that sells for \\$6.00 a pound and a low-quality been that sells for \\$3.25 a pound.} \\end{center}"
rationals = [rationals0]

### PROPER SUBSET OF REALS ###
properSubReal0 = "\\begin{center} \\textit{Chemists commonly create a solution by mixing two products of differing concentrations together. A 10\\% and 30\\% solution can make an acid solution of some value between these, such as a 24\\% acid solution. The chemist wants to make differing solution percentages of 7 liters each.} \\end{center}"
properSubReal1 = "\\begin{center} \\textit{Two UFPD are patrolling the campus on foot. To cover more ground, they split up and begin walking in different directions. Office A is walking at 3 mph while Office B is walking at 5 mph.} \\end{center}"
properSubReal2 = "\\begin{center} \\textit{The rate at which a cricket chirps is a linear function of temperature. At 59 degrees F they make 76 chirps per minute and at 65 degrees F they make 100 chirps per minute.} \\end{center}"
properSubReals = [properSubReal0, properSubReal1, properSubReal2]

### NO RESTRICTED DOMAIN ####
noRestriction0 = "\\begin{center} \\textit{Bridges on highways often have expansion joints, which are small gaps in the roadway between one bridge section and the next. The gaps are put there so the bridge will have room to expand when the weather gets hot. Assume the gap width varies constantly with the temperature. Suppose a bridge has a gap of 1.3 cm when the temperature is 22 degrees C and that the gap narrows to 0.9 cm when the temperature warms to 30 degrees C.} \\end{center}"
noRestrictions = [noRestriction0]

typesToChooseFrom = ["natural", "integer", "rational", "properSubReal", "noRestriction"]
problemType = typesToChooseFrom[random.randint(0, len(typesToChooseFrom)-1)]
displayStem = "What is the \\textbf{best} way to describe the domain of the scenario below?"
naturalAnswer = 0
integerAnswer = 0
rationalAnswer = 0
properSubAnswer = 0
noRestrictionsAnswer = 0

if problemType == "natural":
    displayProblem = naturals[random.randint(0, len(naturals)-1)]
    naturalAnswer = 1
elif problemType == "integer":
    displayProblem = integers[random.randint(0, len(integers)-1)]
    integerAnswer = 1
elif problemType == "rational":
    displayProblem = rationals[random.randint(0, len(rationals)-1)]
    rationalAnswer = 1
elif problemType == "properSubReal":
    displayProblem = properSubReals[random.randint(0, len(properSubReals)-1)]
    properSubAnswer = 1
else:
    displayProblem = noRestrictions[random.randint(0, len(noRestrictions)-1)]
    noRestrictionsAnswer = 1

c0 = ["\\text{Subset of the Natural numbers}", "Recall that the Naturals are the counting numbers: 1, 2, 3, ...", naturalAnswer]
c1 = ["\\text{Subset of the Integers}", "Recall that the Integers are the positive and negative counting numbers: ..., -3, -2, -1, 0, 1, 2, 3, ... ", integerAnswer]
c2 = ["\\text{Subset of the Rational numbers}", "Recall that the Rationals are fractions with Integers in the numerator and denominator.", rationalAnswer]
c3 = ["\\text{Proper subset of the Real numbers}", "This means we have a domain of the Real numbers but need to throw out values based on the context.", properSubAnswer]
c4 = ["\\text{There is no restricted domain in this scenario}", "This means we have a domain of the Real numbers and we don't need to remove any values even in the real-world context.", noRestrictionsAnswer]

choiceAndCommentList = [c0, c1, c2, c3, c4]
random.shuffle(choiceAndCommentList)

choices = [0, 0, 0, 0, 0]
choiceComments = [0, 0, 0, 0, 0]
generalComment = "\\textbf{General Comments:} We often have to remove values in the domain when working with real-world models."

for k in range(0, 5):
    choices[k] = choiceAndCommentList[k][0]
    choiceComments[k] = choiceAndCommentList[k][1]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if choiceAndCommentList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        displaySolution = choiceAndCommentList[answerIndex][0]
        break
    answerIndex = answerIndex+1

### moduleNumber, version, problemNumber are defined in the tex file ###
writeToKey(keyFileName, version, problemNumber, displayStem, "NoMathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
