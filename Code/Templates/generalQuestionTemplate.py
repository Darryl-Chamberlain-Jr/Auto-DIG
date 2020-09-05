# Name of Module
# Name of Content Objective

### DEFINITIONS ###
# This should list all definitions used. Be sure to check the commonly used functions file before creating a new one.

### VARIABLE DECLARATIONS ###
# Declare the necessary variables.

### CREATE INTERVAL OPTIONS
# Use the General Method Function 'createIntervalOptions(setOfValues, intervalRange, precision)'.
    # *setOfValues* is the set of values you are trying to disguise in intervals. This can be a set of sets!
    # setOfValues = [set1, set2, set3, set4]
        # Be sure all sets are of equal length. This is necessary when checking that values are not contained in other intervals.
    # *intervalRange* is the approximate size of the interval masking the values. This should be small when values are close to each other and larger when values are further away. In the future, this may be automatically determined using a min distance between values.
    # *precision* is an optional input. If specified, it is used to fine-tune the endpoint of the intervals used to mask values. Should only be included when values are extremely close together.

### USE INTERVAL OPTIONS OUTPUT TO CREATE ANSWERLIST
# answerList should be created as a list of sets, where each set is [choice, comment, answerLetterIndicator].
    # *choice* is exactly the way the option should be displayed. This should include math mode or display of intervals.
    # *comment* is the related comment that should be displayed on the key. It should include the exact answer (if the value is being disguised in an interval) and start with a * if it is the solution.
    # *answerLetterIndicator* is 1 for the correct option and 0 otherwise. This is used to note the correct letter for the question.
    # answerList = [solutionSet, distractor1Set, distractor2Set, distractor3Set, distractor4Set]

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER
    # choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]
    # choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
    # answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
    # answerLetter = identifyAnswerLetter(answerLetterIndicators)

### WRITE TO KEY
    # writeToKey(keyFileName, version, problemNumber, displayStem, problemModeType, displayProblem, solutionModeType, displaySolution, answerLetter, choices, choiceComments, generalComment)
    # *keyFileName*, *version*, *problemNumber* are all defined in .tex file, not at this level. All should be included verbatim.
    # *displayStem* should describe any instructions for the problem. This is a string variable and should be defined just before the writeToKey declaration.
    # *problemModeType* is how to display the problem of the question. Checks for one of three cases:
        # "MathMode" puts the problem in '\[ \]' to format the equation or function on a separate line.
        # "NoMathMode" does not put the problem in '\[ \]'. This is useful for when the problem is largely text such as in a word problem.
        # "Graph" uses the problem as the name of the graph and centers it on the page.
    # *displayProblem* displays the question's problem. This is a string variable and should be defined just before the writeToKey declaration.
    # *solutionModeType* is how to display the solution in the key. Checks for one of two cases:
        # "MathMode" prints "The solution is $ %s $" where %s is the solution as a string. It also lists the options in math modes and comments as text.
        # "Graphs" prints the solution graph and all options as graphs. If there are 5 graph options, it prints all 5 graph options. If there are 4 graph options, it prints the 4 and a "None of the above." option as E.
    # *displaySolution* is the solution to be displayed. In math mode this should be an equation or value while in graph mode it should be the name of the solution image. It should be defined when the solutionSet is defined.
    # *answerLetter*, *choices*, and *choiceComments* were explicitly defined previously and should be included verbatim.
    # *generalComment* is for any general comments that are not specific to the common misconceptions or errors a student would make. It should be defined just before writeToKey and start as "\\textbf{General Comments:} " for consistency.


#############################
# SHORT VERSION #
#############################
# Name of Module
# Name of Content Objective

### DEFINITIONS ###

### VARIABLE DECLARATIONS ###

### CREATE INTERVAL OPTIONS ###
# createIntervalOptions(setOfValues, intervalRange, precision)

### DEFINE ANSWERLIST AND DISPLAYSOLUTION ###
# option = [choice, comment, answerLetterIndicator]
# displaySolution =

### DEFINE STEM, PROBLEM, GENERAL COMMENT ###
# displayStem =
# displayProblem =
# generalComment = 

### DEFINE CHOICES, CHOICE COMMENTS, AND ANSWER LETTER ###
    # choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], answerList[4][0]
    # choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]
    # answerLetterIndicators = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]
    # answerLetter = identifyAnswerLetter(answerLetterIndicators)

### WRITE TO KEY ###
# writeToKey(keyFileName, version, problemNumber, displayStem, problemModeType, displayProblem, solutionModeType, displaySolution, answerLetter, choices, choiceComments, generalComment)
