import shelve
import sys
from originalQuestionMetadata import *
DIR=sys.argv[1]

ql = shelve.open(f'/{DIR}/Databases/questionMetadata.db')
try:
    tempMasterData = ql['masterMetadata']
    for new_dict in masterQuestionList:
        tempMasterData.append(new_dict)
    ql['masterMetadata'] = tempMasterData
except:
    ql['masterMetadata'] = masterQuestionList
finally:
    ql.close()
