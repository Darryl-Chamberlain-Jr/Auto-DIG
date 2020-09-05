import shelve

def writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, solution, answerLetter, generalComment):
    qdb=shelve.open(f"/{DIR}/Databases/{database_name}.db")
    temp_question_list=qdb[f"{question_list}"]
    total=len(temp_question_list)
    for index in range(0, total):
        question_dict=temp_question_list[index]
        if question_dict.get("Code Name") == thisQuestion:
            question_keys = {
                "Display Step Type": displayStemType,
                "Display Stem": displayStem,
                "Display Problem Type": displayProblemType,
                "Display Problem": displayProblem,
                "Display Options Type": displayOptionsType,
                "Choices": choices,
                "Choice Comments": choiceComments,
                "Solution": solution,
                "Answer Letter": answerLetter,
                "General Comment": generalComment
            }
            question_dict.update(question_keys)
            temp_question_list[index]=question_dict
            break
    qdb[f"{question_list}"]=temp_question_list
    print("I finished storing the questions.")
    qdb.close()
