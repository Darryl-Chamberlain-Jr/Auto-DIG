k, distractork, badk, badDistractork = 0, 0, 0, 0
duplicate = True

while duplicate == True:
    initialTemp = random.randint(10, 20)*10
    bathTemp = random.randint(10, 20)
    finalTemp = initialTemp - random.randint(40, 70)
    timePassed = random.randint(10, 40)
    A = initialTemp - bathTemp
    distractorA = initialTemp
    k = math.log( float(finalTemp - bathTemp) / float(A) ) / float( timePassed*math.log(math.exp(1)) )
    distractork = math.log( float(finalTemp - bathTemp) / float(distractorA) ) / float( timePassed*math.log(math.exp(1)) )
    badk = -math.log(finalTemp - bathTemp) / float( timePassed*math.log(math.exp(1)*A) )
    badDistractork = -math.log(finalTemp - bathTemp) / float( timePassed*math.log(math.exp(1)*distractorA) )
    ### Checks list of values for duplicates
    checkList = [round(k, 5), round(distractork, 5), round(badk, 5), round(badDistractork, 5)]
    if len(checkList) == len(set(checkList)):
        duplicate = False
    else:
        duplicate = True
###
displayStem = "The temperature of an object, $T$, in a different surrounding temperature $T_s$ will behave according to the formula $T(t) = Ae^{kt} + T_s$, where $t$ is minutes, $A$ is a constant, and k is a constant. Use this formula and the situation below to construct a model that describes the uranium's temperature, $T$, based on the amount of time t (in minutes) that have passed. Choose the correct constant $k$ from the options below."
displayProblem = "\\begin{center} \\textit{Uranium is taken out of the reactor with a temperature of $%d^{\\circ}$ C and is placed into a $%d^{\\circ}$ C bath to cool. After %d minutes, the uranium has cooled to $%d^{\\circ}$ C.} \\end{center}" %(initialTemp, bathTemp, timePassed, finalTemp)

listedOrNot = random.randint(0, 1)
if listedOrNot == 0:
    option1 = ["k = %.5f" %(badk), "This uses $A$ correctly and solves for $k$ incorrectly.", 0]
    option2 = ["k = %.5f" %(distractork), "This uses $A$ as the initial temperature and solves for $k$ incorrectly.", 0]
    option3 = ["k = %.5f" %(badDistractork), "This uses $A$ as the initial temperature and solves for $k$ incorrectly.", 0]
    option4 = ["k = %.5f" %(distractork), "This uses $A$ as the initial temperature and solves for $k$ correctly.", 0]
    option5 = ["\\text{None of the above}", "* This is the correct answer as $k = %.5f$." %(k), 1]
    displaySolution = option5[0]
else:
    option1 = ["k = %.5f" %(k), "* This is the correct option.", 1]
    option2 = ["k = %.5f" %(badk), "This uses $A$ correctly but solves for $k$ incorrectly.", 0]
    option3 = ["k = %.5f" %(distractork), "This uses $A$ as the initial temperature and solves for $k$ incorrectly.", 0]
    option4 = ["k = %.5f" %(badDistractork), "This uses $A$ as the initial temperature and solves for $k$ correctly.", 0]
    option5 = ["\\text{None of the above}", "If you chose this, please contact the coordinator to discuss why you believe none of the other answers are correct.", 0]
    displaySolution = option1[0]

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "\\textbf{General comments:} The initial temperature is when $t = 0$. Unlike power models, that means $A$ is not the initial temperature!"

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "NoMathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
