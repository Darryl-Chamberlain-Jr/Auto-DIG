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
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
thisQuestion=sys.argv[5]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

typesOfModels = ["linear", "power", "logExp"]
#chooseModel = random.choice(typesOfModels)
#chooseQuestion = random.randint(1, 3)
chooseModel="linear"
chooseQuestion=1
if chooseModel == "linear":
    #sys.path.insert(1, f"/{DIR}/Code/Modeling/09modelingLinear")
    if chooseQuestion == 1:
        #from constructLinearModelDistanceAndRate import *
        #subprocess.Popen(f"/{DIR}/Code/Modeling/09modelingLinear/constructLinearModelDistanceAndRate.py" f"{DIR}" f"{database_name}" f"{question_list}" f"{version}", shell=True)
        subprocess.call(['python3', f"/{DIR}/Code/Modeling/09modelingLinear/constructLinearModelDistanceAndRate.py", f"{DIR}", f"{database_name}", f"{question_list}", f"{version}"])
    elif chooseQuestion == 2:
        from constructLinearModelCostsProfitsRevenue import *
    else:
        from constructLinearModelMixture import *
elif chooseModel == "power":
    sys.path.insert(1, f"/{DIR}/Code/Modeling/10modelingPower")
    if chooseQuestion == 1:
        from constructDirectModel import *
    elif chooseQuestion == 2:
        from constructIndirectModel import *
    else:
        from constructJointModel import *
else:
    sys.path.insert(1, f"/{DIR}/Code/Modeling/11modelingLogExp")
    if chooseQuestion == 1:
        from constructBacteriaGrowth import *
    elif chooseQuestion == 2:
        from constructHalfLifeModel import *
    else:
        from constructTemperatureModel import *
