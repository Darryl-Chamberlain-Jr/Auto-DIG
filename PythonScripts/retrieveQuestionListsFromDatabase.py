import shelve

ql = shelve.open('../Databases/questionLists.db')
try:
    masterList = ql['masterQuestionMultiarray']
    index=len(masterList)
    print("\n\nCurrent master list by topic:")
    for i in range(0,  index):
        print("Topic %d: %s" %(i+1, masterList[i][0]) )
        if len(masterList[i]) == 1:
            print("    This topic does not have any questions! Try adding a question.")
        else:
            for j in range(1, len(masterList[i])):
                print("    %s" %masterList[i][j])
        print()
except:
    print("\nMaster list is currently empty! Try adding a topic.")
finally:
    ql.close()

# masterList[i][j] is a tuple: [codeName, objNumb, shortObjDescription]
