# USE THIS IN saveQuestionListsToDatabase.py TO ADD ORIGINAL LIST TO DATABASE
counter=0
for topic in masterTopicList:
    addListByTopicToMasterArray(topic)
#    print("Added topic: %s" %topic)
    for i in range(counter, counter+5):
        addQuestionToListsByTopic(topic, masterQuestionList[i], masterObjNumList[i], masterDescriptionList[i])
    counter=counter+5
addSpecialList("MAC1105ExamQuestions", MAC1105ExamQuestions)
