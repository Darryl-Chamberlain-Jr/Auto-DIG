import shelve

### OPEN, ADD QUESTIONS TO LIST BY TOPIC, CLOSE
def addQuestionToListsByTopic(chooseQuestionList, codeName, objectiveNumber, shortObjDescription):
    ql = shelve.open('../Databases/questionLists.db')
    # masterQuestionMultiarray is an array of tuples: topicName, [codeName, objectiveNumber, shortObjDescription], [codeName, objectiveNumber, shortObjDescription], ...
    tempMasterList = ql['masterQuestionMultiarray']
    maxIndex=len(tempMasterList)
    countIndex=0
    while countIndex < maxIndex:
        if chooseQuestionList == tempMasterList[countIndex][0]:
            try:
                # Adds [codeName, objectiveNumber, shortObjDescription] to list of Qs by topic
                tempName = tempMasterList[countIndex]
                tempName.append([codeName, objectiveNumber, shortObjDescription])
                ql[str(tempMasterList[countIndex])] = tempName
                ql['masterQuestionMultiarray'] = tempMasterList
            finally:
                ql.close()
                break
        countIndex+=1
    if maxIndex == 0:
        return "The list of questions by topic is empty. Did you recently delete the database?"
    elif countIndex==maxIndex:
        return "Your topic does not appear in the master list of topics. Would you like to add this topic?"
    else:
        return "Your question '%s' has been successfully added to topic '%s'." %(codeName, chooseQuestionList)
    ql.close()
def addListByTopicToMasterArray(topicTitle):
    ql = shelve.open('../Databases/questionLists.db')
    try:
        tempMasterQuestionMultiarray = ql['masterQuestionMultiarray']
        tempMasterQuestionMultiarray.append([topicTitle])
        ql['masterQuestionMultiarray'] = tempMasterQuestionMultiarray
    except:
        ql['masterQuestionMultiarray'] = [ [topicTitle] ]
    finally:
        ql.close()
def addSpecialList(nameOfList, questionList):
    ql = shelve.open('../Databases/questionLists.db')
    try:
        tempNewList=ql[str(nameOfList)]
        for question in questionList:
            tempNewList.append(question)
        ql[str(nameOfList)]=tempNewList
    except:
        ql[str(nameOfList)]=questionList
    finally:
        ql.close()
