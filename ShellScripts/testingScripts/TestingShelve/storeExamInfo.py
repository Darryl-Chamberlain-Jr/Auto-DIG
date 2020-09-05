import shelve

#questionCodeName - Name of the code. This will be iterated when checking how individual students did.
#objectiveNumber - Check that this matches the shell code variable
#objectiveShortName - Check that this matches the shell code variable
#displayStem
#displayProblem
#displayComment
#choices
#choiceComments
#specificFeedbackComments - This is new and will need to be added to each code for the new automated feedback feature.
#answerLetterIndicators
#answerLetter
#version
#problemNumber

### USE THESE NEXT VARIABLES TO BETTER PRINT .TEX FILES ###
#howToDisplayStem
#howToDisplayProblem
#howToDisplayOptions

# 

s = shelve.open('text1.db')
try:
    tempStem = s['displayStem']
    tempStem.append(displayStem)
    s['displayStem'] = tempStem
except:
    s['displayStem'] = [displayStem]
try:
    tempProblem = s['displayProblem']
    tempProblem.append(displayProblem)
    s['displayProblem'] = tempProblem
except:
    s['displayProblem'] = [displayProblem]
try:
    tempSolution = s['displaySolution']
    tempSolution.append(displaySolution)
    s['displaySolution'] = tempSolution
except:
    s['displaySolution'] = [displaySolution]
finally:
    s.close()
