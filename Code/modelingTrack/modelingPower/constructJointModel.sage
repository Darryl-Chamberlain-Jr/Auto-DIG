displayStem = "For the scenario below, use the model for the volume of a cylinder as $V = \\pi r^2 h$ to find the coefficient for the model of the new volume."

increasesOrDecreasesRadius = random.choice(["increase", "decrease"])
increasesOrDecreasesHeight = random.choice(["increase", "decrease"])
radiusPercentChange = random.randint(10, 20)
heightPercentChange = random.randint(10, 20)
while radiusPercentChange == heightPercentChange:
    radiusPercentChange = random.randint(10, 20)
    heightPercentChange = random.randint(10, 20)
if increasesOrDecreasesRadius == "increases":
    newRadius = 100+radiusPercentChange
    radiusSign = 1
else:
    newRadius = 100-radiusPercentChange
    radiusSign = -1
if increasesOrDecreasesHeight == "increases":
    newHeight = 100+heightPercentChange
    heightSign = 1
else:
    newHeight = 100-heightPercentChange
    heightSign = -1

constant = float( pi * (newRadius/100.0)**2 * (newHeight/100.0)  )
withoutPi = float((newRadius/100.0)**2 * newHeight/100.0)
justChange = float( pi * (radiusPercentChange/100.0)**2 * (heightPercentChange/100.0)  )
justChangeWithoutPi = float( (radiusPercentChange/100.0)**2 * (heightPercentChange/100.0)  )
combinePercentages = float(pi * (radiusPercentChange*radiusSign + heightPercentChange*heightSign) )

displayProblem = "\\begin{center} \\textit{Pepsi wants to increase the volume of soda in their cans. They've decided to %s the radius by %d percent and %s the height by %d percent. They want to model the new volume based on the radius and height of the original cans.} \\end{center}" %(increasesOrDecreasesRadius, radiusPercentChange, increasesOrDecreasesHeight, heightPercentChange)

option1 = ["k = %.5f" %constant, "* This is the correct option and corresponds to the model: $V = \\pi (%.2f r)^2 (%.2f h)$." %(float(newRadius/100), float(newHeight/100)), 1]
option2 = ["k = %.5f" %withoutPi, "This corresponds to the model: $V = (%.2f r)^2 (%.2f h)$." %(float(newRadius/100), float(newHeight/100)), 0]
option3 = ["k = %.5f" %justChange, "This corresponds to the model: $V = \\pi (%.2f r)^2 (%.2f h)$." %(float(radiusPercentChange/100), float(heightPercentChange/100)), 0]
option4 = ["k = %.5f" %justChangeWithoutPi, "This corresponds to the model: $V = (%.2f r)^2 (%.2f h)$." %(float(radiusPercentChange/100), float(heightPercentChange/100)), 0]
option5 = ["\\text{None of the above.}", "If you chose this, please talk with the coordinator to discuss why you believe none of the options are correct.", 0]

displaySolution = option1[0]
generalComment = "\\textbf{General comments:} When calculating the new dimensions, you need to add/subtract from 100\\%. For example, a 10\\% increase in height would result in 110\\% of the original height: $1.1h_{old} = h_{new}$."
################################################

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "NoMathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
