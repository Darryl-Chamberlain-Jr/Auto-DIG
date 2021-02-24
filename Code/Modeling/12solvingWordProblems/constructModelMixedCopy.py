import sys
from sympy import *
import numpy
import random
import math
from decimal import Decimal
import decimal
import traceback
import cmath
import matplotlib.pyplot as plt
from sympy.abc import x, y
from sympy.solvers import solve

import subprocess

DIR=sys.argv[1]
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
    OS_type=sys.argv[7]
else:
    database_name="empty"
    question_list="empty"
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

typesOfModels = ["linear", "power", "logExp"]
chooseModel = random.choice(typesOfModels)
chooseQuestion = random.randint(1, 3)
if chooseModel == "linear":
    if chooseQuestion == 1:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/09modelingLinear/constructLinearModelDistanceAndRate.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
    elif chooseQuestion == 2:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/09modelingLinear/constructLinearModelCostsProfitsRevenue.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
    else:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/09modelingLinear/constructLinearModelMixture.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
elif chooseModel == "power":
    if chooseQuestion == 1:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/10modelingPower/constructDirectModel.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
    elif chooseQuestion == 2:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/10modelingPower/constructIndirectModel.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
    else:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/10modelingPower/constructJointModel.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
else:
    if chooseQuestion == 1:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/11modelingLogExp/constructBacteriaGrowth.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
    elif chooseQuestion == 2:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/11modelingLogExp/constructHalfLifeModel.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
    else:
        subprocess.call(['python3', f"{debug}", f"/{DIR}/Code/Modeling/11modelingLogExp/constructTemperatureModel.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}", f"{thisQuestion}"])
