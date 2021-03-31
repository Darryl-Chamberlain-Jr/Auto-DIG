import sys
import random

DIR=sys.argv[1]
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
    OS_type=sys.argv[7]
    response_type=sys.argv[8]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

### DEFINITIONS ###
def createCoefficients():
    listNaturals=list(range(1, 21))
    constants = random.sample(listNaturals, 6)
    return constants
def generateStructure0():
    c1, c2, c3, c4, c5, c6 = createCoefficients()
    solution = float((c1 - ( float(c2/c3) * c4 ) ) - ( c5 * c6 ))
    distractor1 = float(c1 - float(c2 / (c3 * c4) ) - (c5 * c6))
    distractor2 =  float(c1 - float(c2 / (c3 * c4)) + c5 * c6)
    distractor3 =  float(((c1 - (float(c2/c3) * c4)) - c5) * c6)
    solutionList = [solution, distractor1, distractor2, distractor3]
    while checkUnique(solutionList)=="Copies":
        c1, c2, c3, c4, c5, c6 = createCoefficients()
        solution = float((c1 - (float(c2/c3) * c4)) - (c5 * c6))
        distractor1 = float(c1 - float(c2 / (c3 * c4) ) - (c5 * c6))
        distractor2 =  float(c1 - float(c2 / (c3 * c4)) + c5 * c6)
        distractor3 =  float(((c1 - (float(c2/c3) * c4)) - c5) * c6)
        solutionList = [solution, distractor1, distractor2, distractor3]
    displayProblem = '%d - %d \\div %d * %d - (%d * %d)' %(c1, c2, c3, c4, c5, c6)
    comment0 = "* %.3f, which is the correct option." %solution
    comment1 = " %.3f, which corresponds to an Order of Operations error: not reading left-to-right for multiplication/division." %distractor1
    comment2 = " %.3f, which corresponds to not distributing addition and subtraction correctly." %distractor2
    comment3 = " %.3f, which corresponds to not distributing a negative correctly." %distractor3
    comment4 = " You may have gotten this by making an unanticipated error. If you got a value that is not any of the others, please let the coordinator know so they can help you figure out what happened."
    comments = [comment0, comment1, comment2, comment3, comment4]
    return [solutionList, displayProblem, comments]
def generateStructure1():
    c1, c2, c3, c4, c5, c6 = createCoefficients()
    solution = float( c1 - c2**2 + float(c3/c4) * float(c5/c6) )
    distractor1 = float( c1 + c2**2 + float(c3/c4) * float(c5/c6) )
    distractor2 =  float( c1 - c2**2 + float(c3 / float(c4*c5))/c6 )
    distractor3 =  float( c1 + c2**2 + float(c3 / float(c4*c5))/c6 )
    solutionList = [solution, distractor1, distractor2, distractor3]
    while checkUnique(solutionList)=="Copies":
        c1, c2, c3, c4, c5, c6 = createCoefficients()
        solution = float( c1 - c2**2 + float(c3/c4) * float(c5/c6) )
        distractor1 = float( c1 + c2**2 + float(c3/c4) * float(c5/c6) )
        distractor2 =  float( c1 - c2**2 + float(c3 / float(c4*c5))/c6 )
        distractor3 =  float( c1 + c2**2 + float(c3 / float(c4*c5))/c6 )
        solutionList = [solution, distractor1, distractor2, distractor3]
    displayProblem = '%d - %d^2 + %d \\div %d * %d \\div %d' %(c1, c2, c3, c4, c5, c6)
    comment0 = "* %.3f, this is the correct option" %solution
    comment1 = " %.3f, which corresponds to an Order of Operations error: multiplying by negative before squaring. For example: $(-3)^2 \\neq -3^2$" %distractor1
    comment2 = " %.3f, which corresponds to an Order of Operations error: not reading left-to-right for multiplication/division." %distractor2
    comment3 = " %.3f, which corresponds to two Order of Operations errors." %distractor3
    comment4 = " You may have gotten this by making an unanticipated error. If you got a value that is not any of the others, please let the coordinator know so they can help you figure out what happened."
    comments = [comment0, comment1, comment2, comment3, comment4]
    return [solutionList, displayProblem, comments]
### VARIABLE DECLARATIONS ###
chooseStructureType = random.randint(0, 1)
if chooseStructureType == 0:
    solutionList, displayProblem, comments = generateStructure0()
else:
    solutionList, displayProblem, comments = generateStructure1()

### CREATE INTERVAL OPTIONS ###
intervalOptions = createIntervalOptions(solutionList, 5, 1)

### DEFINE ANSWERLIST AND DISPLAYSOLUTION ###
displaySolution = "%.3f" %solutionList[0]
c0 = "[%s, %s]" %(intervalOptions[0][0], intervalOptions[0][1])
c1 = "[%s, %s]" %(intervalOptions[1][0], intervalOptions[1][1])
c2 = "[%s, %s]" %(intervalOptions[2][0], intervalOptions[2][1])
c3 = "[%s, %s]" %(intervalOptions[3][0], intervalOptions[3][1])
c4 = "\\text{None of the above}"

solutionInterval = [c0, comments[0], 1]
distractor1Interval = [c1, comments[1], 0]
distractor2Interval = [c2, comments[2], 0]
distractor3Interval = [c3, comments[3], 0]
distractor4Interval = [c4, comments[4], 0]
answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)
answerList.append(distractor4Interval)

### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
if response_type=="Multiple-Choice":
    displayStem = 'Simplify the expression below and choose the interval the simplification is contained within.'
else:
    displayStem = 'Simplify the expression below.'
# displayProblem was already defined
generalComment = "While you may remember (or were taught) PEMDAS is done in order, it is actually done as P/E/MD/AS. When we are at MD or AS, we read left to right."

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
answerLetter = identifyAnswerLetter(answerLetterIndicators)

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
