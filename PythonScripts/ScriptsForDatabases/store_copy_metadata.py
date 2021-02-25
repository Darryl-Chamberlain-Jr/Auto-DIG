import shelve
import sys

DIR=sys.argv[1]
OS_type=sys.argv[2]
from copyQuestionMetadata import *

if "linux-gnu" == OS_type:
    ql = shelve.open(f'/{DIR}/Databases/questionMetadata.db')
else:
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
