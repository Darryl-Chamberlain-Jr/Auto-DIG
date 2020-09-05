typesOfModels = ["linear", "power", "logExp"]
chooseModel = random.choice(typesOfModels)
chooseQuestion = random.randint(1, 3)
if chooseModel == "linear":
    if chooseQuestion == 1:
        load("../Code/09modelingLinear/constructLinearModelDistanceAndRate.sage")
    elif chooseQuestion == 2:
        load("../Code/09modelingLinear/constructLinearModelCostsProfitsRevenue.sage")
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
