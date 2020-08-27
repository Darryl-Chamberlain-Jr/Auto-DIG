from sympy.abc import x
from sympy import *
import random
import matplotlib.pyplot as plt
import numpy

# SCATTERPLOT
def generate20randomPoints(type):
    arrayOfPoints=[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    leadingCoefficient=(-1)**random.randint(0, 1)
    if type=='linear':
        for i in range(30):
            value=random.randrange(-10, 10, 1)
            randomness=numpy.random.normal(0, 1, 1)
            arrayOfPoints[i] = (value, (leadingCoefficient*value)+randomness)
    elif type=='power':
        randomPower=random.randint(2, 5)
        for i in range(30):
            value=random.uniform(-10, 10)
            randomness=numpy.random.normal(0, 1, 1)
            arrayOfPoints[i] = (value/2, leadingCoefficient*(value/2)**randomPower+randomness)
    elif type=='log':
        for i in range(30):
            value=random.uniform(0.1, 10)
            randomness=numpy.random.normal(0, 1, 1)
            arrayOfPoints[i] = (value, leadingCoefficient*log(value)+randomness/10)
    elif type=='exp':
        for i in range(30):
            value=random.uniform(-10, 10)
            randomness=numpy.random.normal(0, 1, 1)
            arrayOfPoints[i] = (value, leadingCoefficient*exp(value)+randomness/10)
    else:
        arrayOfPoints=[(random.random(), random.random()) for _ in range(30)]
    return arrayOfPoints

type=['linear', 'power', 'log', 'exp', 'none']
questionType = type[random.randint(0,4)]
scatterplot=list_plot(generate20randomPoints(questionType), size=40, color='blue', fontsize=15)
scatterplot.save('../Figures/identifyModelGraph11' + str(version) + '.png')

option1 = ["\\text{Linear model}", "For this to be the correct option, we need to see a mostly straight line of points.", 0]
option2 = ["\\text{Non-linear Power model}", "For this to be the correct option, we need to see a polynomial or rational shape.", 0]
option3 = ["\\text{Logarithmic model}", "For this to be the correct option, we want a rapid change early, then an extremely slow change later.", 0]
option4 = ["\\text{Exponential model}", "For this to be the correct option, we want an extremely slow change early, then a rapid change later.", 0]
option5 = ["\\text{None of the above}", "For this to be the correct option, we want to see no pattern in the points.", 0]

if questionType == 'linear':
    option1[2] = 1
    displaySolution = option1[0]
elif questionType == 'power':
    option2[2] = 1
    displaySolution = option2[0]
elif questionType == 'log':
    option3[2] = 1
    displaySolution = option3[0]
elif questionType == 'exp':
    option4[2] = 1
    displaySolution = option4[0]
else:
    option5[2] = 1
    displaySolution = option5[0]

displayStem = "Determine the appropriate model for the graph of points below."
displayProblem = "identifyModelGraph11%s" %version

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]
generalComment = "\\textbf{General comments:} This question is testing if you can associate the models with their graphical representation. If you are having trouble, go back to the corresponding Core module to learn about the specific function you are having trouble recognizing."

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "Graph", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
