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

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

thisQuestion="constructModelMixed.py"

typesOfModels = ["linear", "power", "logExp"]
chooseModel = random.choice(typesOfModels)
chooseQuestion = random.randint(1, 3)
if chooseModel == "linear":
    if chooseQuestion == 1:
        from constructLinearModelDistanceAndRate import *
        #load("../Code/09modelingLinear/constructLinearModelDistanceAndRate.sage")
    elif chooseQuestion == 2:
        from constructLinearModelCostsProfitsRevenue import *
        #load("../Code/09modelingLinear/constructLinearModelCostsProfitsRevenue.sage")
    else:
        load("../Code/09modelingLinear/constructLinearModelMixture.sage")
elif chooseModel == "power":
    if chooseQuestion == 1:
        load("../Code/10modelingPower/constructDirectModel.sage")
    elif chooseQuestion == 2:
        load("../Code/10modelingPower/constructIndirectModel.sage")
    else:
        load("../Code/10modelingPower/constructJointModel.sage")
else:
    if chooseQuestion == 1:
        load("../Code/11modelingLogExp/constructBacteriaGrowth.sage")
    elif chooseQuestion == 2:
        load("../Code/11modelingLogExp/constructHalfLifeModel.sage")
    else:
        load("../Code/11modelingLogExp/constructTemperatureModel.sage")
