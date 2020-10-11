import random
import sys
import shelve
import numpy
import csv

#fieldnames need to be 'Version' then all question code names
list_of_dicts=[]
temp_dict={}
version_list=['A', 'B', 'C']
array1=['divideComplex', 'multiplyComplex', 'orderOfOperations']
array2=['linearGraphToStandard', 'linearParOrPer', 'solveLinearRational']
#array3=['describeSet', 'solveCompoundOR', 'solveCompoundAND']

master_array = [ array1, array2 ]
question_list_names = ['question_list_0', 'question_list_1']
list_index=0
field_names= ['Version']
for array in master_array:
    field_names = numpy.concatenate((field_names, array))
DIR="home/dchamberlain31/git-repos/Auto-DIG"
database_name='3114-1073'

for array in master_array:
    for version in version_list:
        ql = shelve.open(f'/{DIR}/Databases/{database_name}-Ver{version}.db')
        temp_dict={'Version': version}
        for code_name in array:
            master_list = ql[question_list_names[list_index]]
            total=len(master_list)
            for index in range(0, total):
                question_dict=master_list[index]
                if question_dict.get("Code Name") == code_name:
                    temp_dict[code_name]=question_dict.get("Answer Letter")
                    break
        list_of_dicts.append(temp_dict)
        ql.close()
    list_index += 1

# Merge dicts with same version
version_A={}
version_B={}
version_C={}
version_D={}
version_E={}
version_F={}
version_G={}
version_H={}
version_I={}
version_J={}
version_K={}
version_L={}
version_M={}
version_N={}
version_O={}
version_P={}
version_Q={}
version_R={}
version_S={}
version_T={}
version_U={}
version_V={}
version_W={}
version_X={}
version_Y={}
version_Z={}
for dict in list_of_dicts:
    if dict.get('Version')=="A":
        version_A.update(dict)
    elif dict.get('Version')=="B":
        version_B.update(dict)
    elif dict.get('Version')=="C":
        version_C.update(dict)
    elif dict.get('Version')=="D":
        version_D.update(dict)
    elif dict.get('Version')=="E":
        version_E.update(dict)
    elif dict.get('Version')=="B":
        version_B.update(dict)
    elif dict.get('Version')=="C":
        version_C.update(dict)
    elif dict.get('Version')=="D":
        version_D.update(dict)
    elif dict.get('Version')=="E":
        version_E.update(dict)
    elif dict.get('Version')=="F":
        version_F.update(dict)
    elif dict.get('Version')=="G":
        version_G.update(dict)
    elif dict.get('Version')=="H":
        version_H.update(dict)
    elif dict.get('Version')=="I":
        version_I.update(dict)
    elif dict.get('Version')=="J":
        version_J.update(dict)
    elif dict.get('Version')=="K":
        version_K.update(dict)
    elif dict.get('Version')=="L":
        version_L.update(dict)
    elif dict.get('Version')=="M":
        version_M.update(dict)
    elif dict.get('Version')=="N":
        version_N.update(dict)
    elif dict.get('Version')=="O":
        version_O.update(dict)
    elif dict.get('Version')=="P":
        version_P.update(dict)
    elif dict.get('Version')=="Q":
        version_Q.update(dict)
    elif dict.get('Version')=="R":
        version_R.update(dict)
    elif dict.get('Version')=="S":
        version_S.update(dict)
    elif dict.get('Version')=="T":
        version_T.update(dict)
    elif dict.get('Version')=="U":
        version_U.update(dict)
    elif dict.get('Version')=="V":
        version_V.update(dict)
    elif dict.get('Version')=="W":
        version_W.update(dict)
    elif dict.get('Version')=="X":
        version_X.update(dict)
    elif dict.get('Version')=="Y":
        version_Y.update(dict)
    elif dict.get('Version')=="Z":
        version_Z.update(dict)
with open('new_test.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for dict in [version_A, version_B, version_C, version_D, version_E, version_F, version_G, version_H, version_I, version_J, version_K, version_L, version_M, version_N, version_O, version_P, version_Q, version_R, version_S, version_T, version_U, version_V, version_W, version_X, version_Y, version_Z]:
        writer.writerow(dict)
