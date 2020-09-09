import shelve

def writeToDatabase(DIR, database_name, question_list, this_question, display_stem_type, display_stem, display_problem_type, display_problem, display_options_type, choices, choice_comments, solution, answer_letter, general_comment):
    qdb=shelve.open(f"/{DIR}/Databases/{database_name}.db")
    temp_question_list=qdb[f"{question_list}"]
    total=len(temp_question_list)
    for index in range(0, total):
        question_dict=temp_question_list[index]
        if question_dict.get("Code Name") == this_question:
            question_keys = {
                "Display Stem Type": display_stem_type,
                "Display Stem": display_stem,
                "Display Problem Type": display_problem_type,
                "Display Problem": display_problem,
                "Display Options Type": display_options_type,
                "Choices": choices,
                "Choice Comments": choice_comments,
                "Solution": solution,
                "Answer Letter": answer_letter,
                "General Comment": general_comment
            }
            question_dict.update(question_keys)
            temp_question_list[index]=question_dict
            break
    qdb[f"{question_list}"]=temp_question_list
    print("I finished storing the questions.")
    qdb.close()
