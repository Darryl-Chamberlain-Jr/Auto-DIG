import shelve
import sys

database_name = sys.argv[1]
question_list = sys.argv[2]
OS_type=sys.argv[3]

if "linux-gnu" in OS_type:
    ql = shelve.open(f'../../Databases/{database_name}')
else: 
    ql = shelve.open(f'../../Databases/{database_name}.db')

try:
    print(list(ql.keys()))
    master_list = ql[question_list]
    total=len(master_list)
    print(f"There are currently {total} questions loaded into the database.")
    for index in range(0, total):
        question_dict=master_list[index]
        for key in ["Code Name", "Folder", "Subfolder", "Topic", "Topic Number", "Objective Number", "Short Description", "Long Description", "Notes", "Author", "Date"]:
            key_data=question_dict.get(key)
            print(f"{key}: {key_data}")
        print()
    print()
except:
    print("\nMaster list is currently empty! Try adding a topic.")
finally:
    ql.close()
