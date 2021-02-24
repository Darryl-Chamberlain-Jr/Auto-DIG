import sys
import shelve

DIR=sys.argv[1]
thisQuestion = sys.argv[2]
assessmentDB = sys.argv[3]
questionList = sys.argv[4]
OS_type=sys.argv[5]

if "linux-gnu" in OS_type:
    ql = shelve.open(f'/{DIR}/Databases/questionMetadata')
else: 
    ql = shelve.open(f'/{DIR}/Databases/questionMetadata.db')
try:
    masterList = ql['masterMetadata']
    total=len(masterList)
    for index in range(0, total):
        question_dict=masterList[index]
        if question_dict.get("Code Name") == thisQuestion:
            this_question_dict = question_dict
            break
except:
    print("\n Question did not appear in the master list. I can't run the code if it does not appear in the master list...")
finally:
    ql.close()

# Now we can open a new database and save the info there.
if "linux-gnu" in OS_type:
    newDB = shelve.open(f'/{DIR}/Databases/{assessmentDB}')
else: 
    newDB = shelve.open(f'/{DIR}/Databases/{assessmentDB}.db')
list_of_keys=list(newDB.keys())
# Checks if there are no lists
try:
    tempQuestionList = newDB[f"{questionList}"]
    tempQuestionList.append(this_question_dict)
    newDB[f"{questionList}"] = tempQuestionList
except:
    newDB[f"{questionList}"] = [ this_question_dict ]
finally:
    newDB.close()
