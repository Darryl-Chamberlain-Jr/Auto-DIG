# function checkForEscape determines whether the user canceled rather than answered a prompt or canceled while the exam was generating.
function checkForEscape {
    escape=$1
    if [ $escape -eq 1 ]; then
    zenity \
        --error \
        --height=100 \
        --width=200 \
        --text="You canceled the assessment generation early."
    pkill eog
    exit 0
    fi
}

# function question_list_by_module lists usable code question structure by module. Generating a MAC 1105 single module or Progress Quiz [from ${typeOfGeneration} in zenityAutoDIG.sh] uses these arrays.
function question_list_by_module {
    ### List of all questions for each module
    module1questionList=( "divideComplex" "multiplyComplex" "orderOfOperations" "subgroupComplex" "subgroupReal" "divideComplexCopy" "multiplyComplexCopy" "orderOfOperationsCopy" "subgroupComplexCopy" "subgroupRealCopy" )
    module2questionList=( "linearGraphToStandard" "linearParOrPer" "linearTwoPoints" "solveIntegerLinear" "solveLinearRational" "linearGraphToStandardCopy" "linearParOrPerCopy" "linearTwoPointsCopy" "solveIntegerLinearCopy" "solveLinearRationalCopy" )
    module3questionList=( 'describeSet' 'solveCompoundAND' 'solveCompoundOR' 'solveIntegerInequality' 'solveRationalInequality' 'describeSetCopy' 'solveCompoundAND_copy' 'solveCompoundOR_copy' 'solveIntegerInequalityCopy' 'solveRationalInequalityCopy')
    module4questionList=( 'factorLeadingOver1Composite' 'quadraticEquationToGraph' 'quadraticFormula' 'quadraticGraphToEquation' 'solveQuadraticFactorComposites' 'factorLeadingOver1CompositeCopy' 'quadraticEquationToGraphCopy' 'quadraticFormulaCopy' 'quadraticGraphToEquationCopy' 'solveQuadraticFactorCompositesCopy' )
    module5questionList=( 'domainRadical' 'radicalEquationToGraph' 'radicalGraphToEquation' 'solveRadicalLinear' 'solveRadicalQuadratic' 'domainRadicalCopy' 'radicalEquationToGraphCopy' 'radicalGraphToEquationCopy' 'solveRadicalLinearCopy' 'solveRadicalQuadraticCopy' )
    module6questionList=( 'constructPolyComplex' 'constructPolyRationals' 'polyEndBehavior' 'polyGraphToFunction' 'polyZeroBehavior' 'constructPolyComplexCopy' 'constructPolyRationalsCopy' 'polyEndBehaviorCopy' 'polyGraphToFunctionCopy' 'polyZeroBehaviorCopy')
    module7questionList=( 'domainRational' 'rationalEquationToGraph' 'rationalGraphToEquation' 'solveRationalLinear' 'solveRationalQuadratic' 'domainRationalCopy' 'rationalEquationToGraphCopy' 'rationalGraphToEquationCopy' 'solveRationalLinearCopy' 'solveRationalQuadraticCopy' )
    module8questionList=( 'domainRangeExp' 'domainRangeLog' 'solveByConverting' 'solveByLogProperties' 'solveExpDifferentBases' 'domainRangeExpCopy' 'domainRangeLogCopy' 'solveByConvertingCopy' 'solveByLogPropertiesCopy' 'solveExpDifferentBasesCopy' )
    # START EDITING HERE
    module9MquestionList=( 'domainLinearModel' 'constructLinearModelMixture' 'constructLinearModelCostsProfitsRevenue' 'constructLinearModelDistanceAndRate' 'identifyModelPopulationLinear' 'domainLinearModelCopy' 'constructLinearModelMixtureCopy' 'constructLinearModelCostsProfitsRevenueCopy' 'constructLinearModelDistanceAndRateCopy' 'identifyModelPopulationLinearCopy' )
    module10MquestionList=( 'constructDirectModel' 'constructIndirectModel' 'constructJointModel' 'identifyModelPopulationPower' 'identifyModelVariation' 'constructDirectModelCopy' 'constructIndirectModelCopy' 'constructJointModelCopy' 'identifyModelPopulationPowerCopy' 'identifyModelVariationCopy' )
    module11MquestionList=( 'constructBacteriaGrowth' 'constructHalfLifeModel' 'constructTemperatureModel' 'identifyModelGraph11' 'identifyModelPopulationLogExp' 'constructBacteriaGrowthCopy' 'constructHalfLifeModelCopy' 'constructTemperatureModelCopy' 'identifyModelGraph11Copy' 'identifyModelPopulationLogExpCopy' )
    module12MquestionList=( 'constructModelMixed' 'identifyModelGraph12' 'solveModelExp' 'solveModelLinear' 'solveModelPower' 'constructModelMixedCopy' 'identifyModelGraph12Copy' 'solveModelExpCopy' 'solveModelLinearCopy' 'solveModelPowerCopy' )
    module9LquestionList=( 'determine1to1' 'domainAfterOperating' 'findInverseLogOrExp' 'findInversePolyOrRadical' 'functionComposition' 'determine1to1Copy' 'domainAfterOperatingCopy' 'findInverseLogOrExpCopy' 'findInversePolyOrRadicalCopy' 'functionCompositionCopy' )
    module10LquestionList=( 'factorUsingSynthetic2Integers' 'factorUsingSynthetic2Rationals' 'possibleRoots' 'syntheticDivision' 'syntheticDivisionMissingTerms' 'factorUsingSynthetic2IntegersCopy' 'factorUsingSynthetic2RationalsCopy' 'possibleRootsCopy' 'syntheticDivisionCopy' 'syntheticDivisionMissingTermsCopy' )
    module11LquestionList=( 'evaluateLimitAnalyticalEasy' 'evaluateLimitAnalyticalHard' 'evaluateLimitGraphically' 'interpretLimit' 'oneSidedLimits' 'evaluateLimitAnalyticalEasyCopy' 'evaluateLimitAnalyticalHardCopy' 'evaluateLimitGraphicallyCopy' 'interpretLimitCopy' 'oneSidedLimitsCopy' )
    module12LquestionList=( 'identifyGraphOfRationalFunction' 'identifyHAs' 'identifyHoles' 'identifyOAs' 'identifyVAs' 'identifyGraphOfRationalFunctionCopy' 'identifyHAsCopy' 'identifyHolesCopy' 'identifyOAsCopy' 'identifyVAsCopy' )
}

# Used when creating a flexible assessment. Converts master database info to be displayed for the user using zenity.
function defineAllQuestionsDynamically {
    OIFS=$IFS;
    IFS=";";
    Length=$(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Length" $DIR $OSTYPE)
    CodeNames=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Code Name" $DIR $OSTYPE))
    Folder=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Folder" $DIR $OSTYPE))
    Subfolder=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Subfolder" $DIR $OSTYPE))
    TopicNumber=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Topic Number" $DIR $OSTYPE))
    ObjectiveNumber=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Objective Number" $DIR $OSTYPE))
    Topic=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Topic" $DIR $OSTYPE))
    ShortDescription=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Short Description" $DIR $OSTYPE))
    LongDescription=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Long Description" $DIR $OSTYPE))
    Notes=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Notes" $DIR $OSTYPE))
    Author=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Author" $DIR $OSTYPE))
    Date=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Date" $DIR $OSTYPE))
    IFS=$OIFS
}
