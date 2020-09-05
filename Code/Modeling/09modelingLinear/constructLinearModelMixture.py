# Mixture
lowPrice = round(random.uniform(2, 5), 2)
highPrice = round(random.uniform(lowPrice+1, lowPrice+3), 2)
midPrice = round((lowPrice+highPrice)/2, 2)
blendPrice = random.uniform(lowPrice+0.5, highPrice-0.5)

totalWeight = random.randint(7, 25)*10
typesOfBeans = ["high-quality", "low-quality"]
highOrLowQuality = typesOfBeans[random.randint(0,1)]

totalCostHigh = [highPrice-lowPrice, lowPrice*totalWeight]
totalCostLow = [lowPrice-highPrice, highPrice*totalWeight]

displayStem = "Using the situation below, construct a linear model that describes the cost of the coffee beans $C(h)$ in terms of the weight of the %s coffee beans $h$." %highOrLowQuality
displayProblem = "Veronica needs to prepare %d of blended coffee beans selling for \\$%.2f per pound. She has a high-quality bean that sells for \\$%.2f a pound and a low-quality bean that sells for \\$%.2f a pound." %(totalWeight, blendPrice, highPrice, lowPrice)

if highOrLowQuality == "high-quality":
    displaySolution = "C(h) = %.2f h + %.2f" %(totalCostHigh[0], totalCostHigh[1])
    option1 = ["C(h) = %.2f h + %.2f" %(totalCostHigh[0], totalCostHigh[1]), "* This is the correct option since the questions asked you to construct the cost model in terms of the weight of the high-quality bean.", 1]
    option2 = ["C(h) = %.2f h + %.2f" %(totalCostLow[0], totalCostLow[1]), "This would be correct if the question asked you to construct the cost model in terms of the weight of the low-quality bean.", 0]
    option3 = ["C(h) = %.2f h" %highPrice, "This models the cost of the high-quality bean only, not the blended beans.", 0]
    option4 = ["C(h) = %.2f h" %midPrice, "This assumes that exactly half of the high- and low- quality beans are mixed to create the blended coffee beans.", 0]
    option5 = ["\\text{None of the above.}", "If you chose this option, please talk to the coordinator to discuss why.", 0]
else:
    displaySolution = "C(h) = %.2f h + %.2f" %(totalCostLow[0], totalCostLow[1])
    option1 = ["C(h) = %.2f h + %.2f" %(totalCostLow[0], totalCostLow[1]), "* This is the correct option since the questions asked you to construct the cost model in terms of the weight of the low-quality bean.", 1]
    option2 = ["C(h) = %.2f h + %.2f" %(totalCostHigh[0], totalCostHigh[1]), "This would be correct if the question asked you to construct the cost model in terms of the weight of the high-quality bean.", 0]
    option3 = ["C(h) = %.2f h" %lowPrice, "This models the cost of the low-quality bean only, not the blended beans.", 0]
    option4 = ["C(h) = %.2f h" %midPrice, "This assumes that exactly half of the high- and low- quality beans are mixed to create the blended coffee beans.", 0]
    option5 = ["\\text{None of the above.}", "If you chose this option, please talk to the coordinator to discuss why.", 0]

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

generalComment = "\\textbf{General Comments:} This is exactly like the chemistry mixture question from the homework! If you are having trouble with this problem, be sure to review the video for building linear models."

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
