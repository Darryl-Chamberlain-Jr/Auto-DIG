import sys
import shelve

generalForm = {
    "Code Name": "",
    "Folder": "", # Core, Limits, or Modeling
    "Subfolder": "",
    "Topic": "",
    "Topic Number": "",
    "Objective Number": "", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "",
    "Long Description": "",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Export question info to bash env
gimme=sys.argv[1]
DIR=sys.argv[2]

ql = shelve.open(f'/{DIR}/Databases/questionMetadata.db')
try:
    masterList = ql['masterMetadata']
    if gimme=="Length":
        print(len(masterList))
    elif gimme in generalForm.keys():
        for question in masterList:
            print(f"{question.get(gimme)};")
    else:
        print("I didn't give you anything.")
except:
    print("Error when printing all key values.")
    exit(1)
finally:
    ql.close()
