function defineVersionList {
    fullVersionList=( "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")
    version_counter=0
    version_list=()
    while [ $version_counter -lt $number_of_versions ]
    do
        version_list=( "${version_list[@]}" "${fullVersionList[$version_counter]}" )
        version_counter=$(( version_counter+1 ))
    done
}
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
    module9MquestionList=( 'domainLinearModel' 'constructLinearModelMixture' 'constructLinearModelCostsProfitsRevenue' 'constructLinearModelDistanceAndRate' 'identifyModelPopulation' 'domainLinearModelCopy' 'constructLinearModelMixtureCopy' 'constructLinearModelCostsProfitsRevenueCopy' 'constructLinearModelDistanceAndRateCopy' 'identifyModelPopulationCopy' )
    module10MquestionList=( 'constructDirectModel' 'constructIndirectModel' 'constructJointModel' 'identifyModelPopulation' 'identifyModelVariation' 'constructDirectModelCopy' 'constructIndirectModelCopy' 'constructJointModelCopy' 'identifyModelPopulationCopy' 'identifyModelVariationCopy' )
    module11MquestionList=( 'constructBacteriaGrowth' 'constructHalfLifeModel' 'constructTemperatureModel' 'identifyModelGraph11' 'identifyModelPopulation' 'constructBacteriaGrowthCopy' 'constructHalfLifeModelCopy' 'constructTemperatureModelCopy' 'identifyModelGraph11Copy' 'identifyModelPopulationCopy' )
    module12MquestionList=( 'constructModelMixed' 'identifyModelGraph12' 'solveModelExp' 'solveModelLinear' 'solveModelPower' 'constructModelMixedCopy' 'identifyModelGraph12Copy' 'solveModelExpCopy' 'solveModelLinearCopy' 'solveModelPowerCopy' )
    module9LquestionList=( 'determine1to1' 'domainAfterOperating' 'findInverseLogOrExp' 'findInversePolyOrRadical' 'functionComposition' 'determine1to1Copy' 'domainAfterOperatingvCopy' 'findInverseLogOrExpCopy' 'findInversePolyOrRadicalCopy' 'functionCompositionCopy' )
    module10LquestionList=( 'factorUsingSynthetic2Integers' 'factorUsingSynthetic2Rationals' 'possibleRoots' 'syntheticDivision' 'syntheticDivisionMissingTerms' 'factorUsingSynthetic2IntegersCopy' 'factorUsingSynthetic2RationalsCopy' 'possibleRootsCopy' 'syntheticDivisionCopy' 'syntheticDivisionMissingTermsCopy' )
    module11LquestionList=( 'evaluateLimitAnalyticalEasy' 'evaluateLimitAnalyticalHard' 'evaluateLimitGraphically' 'interpretLimit' 'oneSidedLimits' 'evaluateLimitAnalyticalEasyCopy' 'evaluateLimitAnalyticalHardCopy' 'evaluateLimitGraphicallyCopy' 'interpretLimitCopy' 'oneSidedLimitsCopy' )
    module12LquestionList=( 'identifyGraphOfRationalFunction' 'identifyHAs' 'identifyHoles' 'identifyOAs' 'identifyVAs' 'identifyGraphOfRationalFunctionCopy' 'identifyHAsCopy' 'identifyHolesCopy' 'identifyOAsCopy' 'identifyVAsCopy' )
}
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
function defineAllQuestionsDynamically {
    OIFS=$IFS;
    IFS=";";
    Length=$(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Length" $DIR)
    CodeNames=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Code Name" $DIR))
    Folder=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Folder" $DIR))
    Subfolder=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Subfolder" $DIR))
    TopicNumber=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Topic Number" $DIR))
    ObjectiveNumber=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Objective Number" $DIR))
    Topic=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Topic" $DIR))
    ShortDescription=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Short Description" $DIR))
    LongDescription=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Long Description" $DIR))
    Notes=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Notes" $DIR))
    Author=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Author" $DIR))
    Date=($(python3 /${DIR}/PythonScripts/ScriptsForDatabases/return_all_values_of_key.py "Date" $DIR))
    IFS=$OIFS
}
