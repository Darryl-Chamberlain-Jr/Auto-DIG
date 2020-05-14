def createCoefficients():
    listNaturals=list(range(1, 21))
    # Array of 6 distinct integers
    constants = random.sample(listNaturals, 6)
    counter=0
    while counter < len(constants):
        constants[counter] = float(constants[counter])
        counter=counter+1
    return constants

def generateStructure0():
    c1, c2, c3, c4, c5, c6 = createCoefficients()
    solution = float((c1 - ((c2/c3) * c4)) - (c5 * c6 ))
    distractor1 = float(c1 - (c2 / (c3 * c4) ) - (c5 * c6))
    distractor2 =  float(c1 - (c2 / (c3 * c4)) - c5 * -1.0 * c6)
    distractor3 =  float(((c1 - ((c2/c3) * c4)) - c5) * c6)
    solutionList = [solution, distractor1, distractor2, distractor3]
    while checkUnique(solutionList)=="Copies":
        c1, c2, c3, c4, c5, c6 = createCoefficients()
        solution = float((c1 - ((c2/c3) * c4)) - (c5 * c6))
        distractor1 =  float(c1 - (c2 / (c3 * c4)) - (c5 * c6))
        distractor2 = float(c1 - (c2 / (c3 * c4)) + c5  * c6)
        distractor3 = float(((c1 - ((c2/c3) * c4)) - c5) * c6)
        #distractor4 = float((c1 + ((c2/c3) *  c4) - c5) * c6)
        solutionList = [solution, distractor1, distractor2, distractor3]
    displayProblem = '%d - %d \\div %d * %d - (%d * %d)' %(c1, c2, c3, c4, c5, c6)
    displaySolution = round(solution, 3)
    intervalOptions = createIntervalOptions(solutionList, 5, 1)
    solutionInterval = [intervalOptions[0], "* %.3f, which is the correct option." %solution, 1]
    distractor1Interval = [intervalOptions[1], " %.3f, which corresponds to an Order of Operations error: not reading left-to-right for multiplication/division." %round(distractor1, 3), 0]
    distractor2Interval = [intervalOptions[2], " %.3f, which corresponds to not distributing addition and subtraction correctly." %round(distractor2, 3), 0]
    distractor3Interval = [intervalOptions[3], " %.3f, which corresponds to not distributing a negative correctly." %round(distractor3, 3), 0]
    distractor4Interval = ["\\text{None of the above}", " You may have gotten this by making an unanticipated error. If you got a value that is not any of the others, please let the coordinator know so they can help you figure out what happened.", 0]
    answerListTemp = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
    random.shuffle(answerListTemp)
    answerList = [answerListTemp[0], answerListTemp[1], answerListTemp[2], answerListTemp[3], distractor4Interval]
    return [answerList, displayProblem, displaySolution]

def generateStructure1():
    c1, c2, c3, c4, c5, c6 = createCoefficients()
    solution = float( c1 - c2**2 + (c3/c4) * (c5/c6) )
    distractor1 = float( c1 + c2**2 + (c3/c4) * (c5/c6) )
    distractor2 =  float( c1 - c2**2 + (c3 / (c4*c5))/c6 )
    distractor3 =  float( c1 + c2**2 + (c3 / (c4*c5))/c6 )
    solutionList = [solution, distractor1, distractor2, distractor3]
    while checkUnique(solutionList)=="Copies":
        c1, c2, c3, c4, c5, c6 = createCoefficients()
        solution = float( c1 - c2**2 + (c3/c4) * (c5/c6) )
        distractor1 = float( c1 + c2**2 + (c3/c4) * (c5/c6) )
        distractor2 =  float( c1 - c2**2 + (c3 / (c4*c5))/c6 )
        distractor3 =  float( c1 + c2**2 + (c3 / (c4*c5))/c6 )
        solutionList = [solution, distractor1, distractor2, distractor3]
    displayProblem = '%d - %d^2 + %d \\div %d * %d \\div %d' %(c1, c2, c3, c4, c5, c6)
    displaySolution = round(solution, 3)
    intervalOptions = createIntervalOptions(solutionList, 5, 1)
    solutionInterval = [intervalOptions[0], "* %f, this is the correct option" %round(solution, 3),  1]
    distractor1Interval = [intervalOptions[1], " %f, which corresponds to an Order of Operations error: multiplying by negative before squaring. For example: $(-3)^2 \\neq -3^2$" %round(distractor1, 3), 0]
    distractor2Interval = [intervalOptions[2], " %f, which corresponds to an Order of Operations error: not reading left-to-right for multiplication/division." %round(distractor2, 3), 0]
    distractor3Interval = [intervalOptions[3], " %f, which corresponds to two Order of Operations errors." %round(distractor3, 3), 0]
    distractor4Interval = ["\\text{None of the above}", " You may have gotten this by making an unanticipated error. If you got a value that is not any of the others, please let the coordinator know so they can help you figure out what happened.", 0]
    answerListTemp = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
    random.shuffle(answerListTemp)
    answerList = [answerListTemp[0], answerListTemp[1], answerListTemp[2], answerListTemp[3], distractor4Interval]
    return [answerList, displayProblem, displaySolution]

chooseStructureType = random.randint(0, 1)
if chooseStructureType == 0:
    answerList, displayProblem, displaySolution = generateStructure0()
else:
    answerList, displayProblem, displaySolution = generateStructure1()

displayStem = 'Simplify the expression below and choose the interval the simplification is contained within.'
generalComment = "General Comments: While you may remember (or were taught) PEMDAS is done in order, it is actually done as P/E/MD/AS. When we are at MD or AS, we read left to right."

c0 = "[%s, %s]" %(answerList[0][0][0], answerList[0][0][1])
c1 = "[%s, %s]" %(answerList[1][0][0], answerList[1][0][1])
c2 = "[%s, %s]" %(answerList[2][0][0], answerList[2][0][1])
c3 = "[%s, %s]" %(answerList[3][0][0], answerList[3][0][1])
c4 = "%s" %(answerList[4][0])
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
