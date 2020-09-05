import shelve
import sys

database_name = sys.argv[1]

ql = shelve.open(f'../../Databases/{database_name}.db')

try:
    masterList = ql['masterMetadata']
    total=len(masterList)
    print(f"There are currently {total} questions loaded into the database.")
    for index in range(0, total):
        question_dict=masterList[index]
        for key in ["Code Name", "Folder", "Subfolder", "Topic", "Topic Number", "Objective Number", "Short Description", "Long Description", "Notes", "Author", "Date"]:
            key_data=question_dict.get(key)
            print(f"{key}: {key_data}")
        print()
    print()
except:
    print("\nMaster list is currently empty! Try adding a topic.")
finally:
    ql.close()
