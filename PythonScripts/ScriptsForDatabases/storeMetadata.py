import shelve
import sys
#from originalQuestionMetadata import *
from copyQuestionMetadata import *
DIR=sys.argv[1]
database_name=sys.argv[2]

ql = shelve.open(f'/{DIR}/Databases/{database_name}.db')
try:
    tempMasterData = ql['masterMetadata']
    for new_dict in masterQuestionList:
        tempMasterData.append(new_dict)
    ql['masterMetadata'] = tempMasterData
except:
    ql['masterMetadata'] = masterQuestionList
finally:
    ql.close()
