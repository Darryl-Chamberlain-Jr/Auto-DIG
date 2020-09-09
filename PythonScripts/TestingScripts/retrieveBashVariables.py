import sys

# Export question info to bash env
gimme=sys.argv[1]
# Variables for Shell Script
if gimme in generalForm.keys():
    for question in masterQuestionList:
        print(f"{question.get(gimme)};")
elif gimme=="Length":
    print(len(masterQuestionList))
else:
    print("I didn't give you anything.")


# In the Shell Script:
#function defineAllQuestionsDynamically {
#    Length=$(python3 originalQuestionMetadata.py "length")
#    CodeNames=($(python3 originalQuestionMetadata.py "Code Name"))
#    Folder=($(python3 originalQuestionMetadata.py "Folder"))
#    Subfolder=($(python3 originalQuestionMetadata.py "Subfolder"))
#    Topic=($(python3 originalQuestionMetadata.py "Topic"))
#    TopicNumber=($(python3 originalQuestionMetadata.py "Topic Number"))
#    ObjectiveNumber=($(python3 originalQuestionMetadata.py "Objective Number"))
#    ShortDescription=($(python3 originalQuestionMetadata.py "Short Description"))
#    LongDescription=($(python3 originalQuestionMetadata.py "Long Description"))
#    Notes=($(python3 originalQuestionMetadata.py "Notes"))
#    Author=($(python3 originalQuestionMetadata.py "Author"))
#    Year=($(python3 originalQuestionMetadata.py "Year"))
#}
