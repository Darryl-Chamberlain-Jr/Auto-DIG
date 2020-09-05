import sys
import shelve

#DIR="home/dchamberlain31/git-repos/Auto-DIG"
DIR=sys.argv[1]
thisQuestion = sys.argv[2]
assessmentDB = sys.argv[3]
questionList = sys.argv[4]

# Retrieves metadata about question
ql = shelve.open(f"/{DIR}/Databases/questionMetadata.db")
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
newDB = shelve.open(f"/{DIR}/Databases/{assessmentDB}.db")
try:
    tempQuestionList = newDB[f"{questionList}"]
    tempQuestionList.append(this_question_dict)
    newDB[f"{questionList}"] = tempQuestionList
except:
    newDB[f"{questionList}"] = [ this_question_dict ]
finally:
    newDB.close()
