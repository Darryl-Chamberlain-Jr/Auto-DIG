import shelve
import sys

DIR=sys.argv[1]
from originalQuestionMetadata import *

ql = shelve.open(f'/{DIR}/Databases/questionMetadata')
try:
    tempMasterData = ql['masterMetadata']
    for new_dict in masterQuestionList:
        tempMasterData.append(new_dict)
    ql['masterMetadata'] = tempMasterData
except:
    ql['masterMetadata'] = masterQuestionList
finally:
    ql.close()
