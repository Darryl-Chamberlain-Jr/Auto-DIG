import shelve
import sys

DIR = sys.argv[1]
database_name = sys.argv[2]
questionList = sys.argv[3]

ql = shelve.open(f'/{DIR}/Databases/{database_name}.db')

try:
    masterList = ql[f'{questionList}']
    total=len(masterList)
    print(f"There are currently {total} questions loaded into the database for {questionList}.")
    for index in range(0, total):
        question_dict=masterList[index]
        for key in ["Code Name", "Folder", "Subfolder", "Topic", "Topic Number", "Objective Number", "Short Description", "Long Description", "Notes", "Author", "Date", "Display Step Type", "Display Stem", "Display Problem Type", "Display Problem", "Display Options Type", "Choices", "Choice Comments", "Solution", "Answer Letter", "General Comment"]:
            key_data=question_dict.get(key)
            print(f"{key}: {key_data}")
        print()
    print()
except:
    print(f"\n {questionList} is currently empty! Try adding a topic.")
finally:
    ql.close()
