typesOfModels = ["linear", "power", "logExp"]
chooseModel = random.choice(typesOfModels)
chooseQuestion = random.randint(1, 3)
if chooseModel == "linear":
    if chooseQuestion == 1:
        load("../Code/modelingTrack/modelingLinear/constructLinearModel1.sage")
    elif chooseQuestion == 2:
        load("../Code/modelingTrack/modelingLinear/constructLinearModel2.sage")
    else:
        load("../Code/modelingTrack/modelingLinear/constructLinearModel3.sage")
elif chooseModel == "power":
    if chooseQuestion == 1:
        load("../Code/modelingTrack/modelingPower/constructDirectModel.sage")
    elif chooseQuestion == 2:
        load("../Code/modelingTrack/modelingPower/constructIndirectModel.sage")
    else:
        load("../Code/modelingTrack/modelingPower/constructJointModel.sage")
else:
    if chooseQuestion == 1:
        load("../Code/modelingTrack/modelingLogExp/constructBacteriaGrowth.sage")
    elif chooseQuestion == 2:
        load("../Code/modelingTrack/modelingLogExp/constructHalfLifeModel.sage")
    else:
        load("../Code/modelingTrack/modelingLogExp/constructTemperatureModel.sage")
