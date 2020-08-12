function generationOptions {
    generationOption1="A Progress Quiz"
    generationOption2="A Single Module"
    generationOption3="A MAC 1105 Final Exam"
    generationOption4="A Flexible Assessment"
}
function defineVersionList {
    fullVersionList=( "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")
    versionCounter=0
    versionList=()
    while [ "$versionCounter" -lt "$numberOfVersions" ]
    do
        versionList=( "${versionList[@]}" "${fullVersionList[$versionCounter]}" )
        versionCounter=$(( versionCounter+1 ))
    done
}
function defineModuleList {
    if [ $examNumber -eq 1 ]; then
        moduleList=( 1 2 3 )
    elif [ $examNumber -eq 2 ]; then
        moduleList=( 1 2 3 4 5 6 )
    elif [ $examNumber -eq 3 ]; then
        moduleList=( 1 2 3 4 5 6 7 8 "9M" "9L")
    else
        moduleList=( 1 2 3 4 5 6 7 8 "9M" "10M" "11M" "12M" "9L" "10L" "11L" "12L")
    numberOfModules=${#moduleList[@]}
    fi
}
function moduleOptions {
    moduleOption1="Module 1 - Real and Complex Numbers"
    moduleOption2="Module 2 - Linear Functions"
    moduleOption3="Module 3 - Linear Inequalities"
    moduleOption4="Module 4 - Quadratic Functions"
    moduleOption5="Module 5 - Radical Functions"
    moduleOption6="Module 6 - Polynomial Functions"
    moduleOption7="Module 7 - Rational Functions"
    moduleOption8="Module 8 - Logarithmic and Exponential Functions"
    moduleOption9M="Module 9M - Modeling w/ Linear Functions"
    moduleOption10M="Module 10M - Modeling w/ Power Functions"
    moduleOption11M="Module 11M - Modeling w/ Log and Exp Functions"
    moduleOption12M="Module 12M - Solving Real-World Word Problems"
    moduleOption9L="Module 9L - Operations on Functions"
    moduleOption10L="Module 10L - Synthetic Division"
    moduleOption11L="Module 11L - Introduction to Limits"
    moduleOption12L="Module 12L - Graphing Rational Functions"
}
function defineSingleModule {
    if [ "$chooseModule" == "$moduleOption1" ] || [ "$chooseModule" == "$moduleOption2" ] || [ "$chooseModule" == "$moduleOption3" ] || [ "$chooseModule" == "$moduleOption4" ] || [ "$chooseModule" == "$moduleOption5" ] || [ "$chooseModule" == "$moduleOption6" ] || [ "$chooseModule" == "$moduleOption7" ] || [ "$chooseModule" == "$moduleOption8" ]; then
        singleModule=${chooseModule:7:1}
    elif [ "$chooseModule" == "$moduleOption9L" ] || [ "$chooseModule" == "$moduleOption9M" ]; then
        singleModule=${chooseModule:7:2}
    else
        singleModule=${chooseModule:7:3}
    fi
}
function presetQuestionList {
    singleModule=$1
    listAllQuestions
    if [ "$singleModule" == "1" ]; then
        questionList=${module1questionList[@]}
    elif [ "$singleModule" == "2" ]; then
        questionList=${module2questionList[@]}
    elif [ "$singleModule" == "3" ]; then
        questionList=${module3questionList[@]}
    elif [ "$singleModule" == "4" ]; then
        questionList=${module4questionList[@]}
    elif [ "$singleModule" == "5" ]; then
        questionList=${module5questionList[@]}
    elif [ "$singleModule" == "6" ]; then
        questionList=${module6questionList[@]}
    elif [ "$singleModule" == "7" ]; then
        questionList=${module7questionList[@]}
    elif [ "$singleModule" == "8" ]; then
        questionList=${module8questionList[@]}
    elif [ "$singleModule" == "9M" ]; then
        questionList=${module9MquestionList[@]}
    elif [ "$singleModule" == "10M" ]; then
        questionList=${module10MquestionList[@]}
    elif [ "$singleModule" == "11M" ]; then
        questionList=${module11MquestionList[@]}
    elif [ "$singleModule" == "12M" ]; then
        questionList=${module12MquestionList[@]}
    elif [ "$singleModule" == "9L" ]; then
        questionList=${module9LquestionList[@]}
    elif [ "$singleModule" == "10L" ]; then
        questionList=${module10LquestionList[@]}
    elif [ "$singleModule" == "11L" ]; then
        questionList=${module11LquestionList[@]}
    elif [ "$singleModule" == "12L" ]; then
        questionList=${module12LquestionList[@]}
    else
        echo "Something went wrong when defining the question list."
    fi
}
function checkForEscape {
    escape=$1
    if [ $escape -eq 1 ]; then
    zenity \
        --error \
        --text="You canceled the assessment generation early."
    exit 0
    fi
}
function defineAllQuestionsForChecklist {
    masterQuestionList=(
    # Module 1
    'divideComplex' \
    'multiplyComplex' \
    'orderOfOperations' \
    'subgroupComplex' \
    'subgroupReal' \
    # Module 2
    'linearGraphToStandard' \
    'linearParOrPer' \
    'linearTwoPoints' \
    'solveIntegerLinear' \
    'solveRationalLinear' \
    # Module 3
    'describeSet' \
    'solveCompoundAND' \
    'solveCompoundOR' \
    'solveIntegerInequality' \
    'solveRationalInequality' \
    # Module 4
    'factorLeadingOver1Composite' \
    'quadraticEquationToGraph' \
    'quadraticFormula' \
    'quadraticGraphToEquation' \
    'solveQuadraticFactorComposites' \
    # Module 5
    'domainRadical' \
    'radicalEquationToGraph' \
    'radicalGraphToEquation' \
    'solveRadicalLinear' \
    'solveRadicalQuadratic' \
    # Module 6
    'constructPolyComplex' \
    'constructPolyRationals' \
    'polyEndBehavior' \
    'polyGraphToFunction' \
    'polyZeroBehavior' \
    # Module 7
    'domainRational' \
    'rationalEquationToGraph' \
    'rationalGraphToEquation' \
    'solveRationalLinear' \
    'solveRationalQuadratic' \
    # Module 8
    'domainRangeExp' \
    'domainRangeLog' \
    'solveByConverting' \
    'solveByLogProperties' \
    'solveExpDifferentBases' \
    # Module 9M
    'domainLinearModel' \
    'constructLinearModelMixture' \
    'constructLinearModelCostsProfitsRevenue' \
    'constructLinearModelDistanceAndRate' \
    'identifyModelPopulation' \
    # Module 10M
    'constructDirectModel' \
    'constructIndirectModel' \
    'constructJointModel' \
    'identifyModelPopulation' \
    'identifyModelVariation' \
    # Module 11M
    'constructBacteriaGrowth' \
    'constructHalfLifeModel' \
    'constructTemperatureModel' \
    'identifyModelGraph11' \
    'identifyModelPopulation' \
    # Module 12M
    'constructModelMixed' \
    'identifyModelGraph12' \
    'solveModelExp' \
    'solveModelLinear' \
    'solveModelPower' \
    # Module 9L
    'determine1to1' \
    'domainAfterOperating' \
    'findInverseLogOrExp' \
    'findInversePolyOrRadical' \
    'functionComposition' \
    # Module 10L
    'factorUsingSynthetic2Integers' \
    'factorUsingSynthetic2Rationals' \
    'possibleRoots' \
    'syntheticDivision' \
    'syntheticDivisionMissingTerms' \
    # Module 11L
    'evaluateLimitAnalyticalEasy' \
    'evaluateLimitAnalyticalHard' \
    'evaluateLimitGraphically' \
    'interpretLimit' \
    'oneSidedLimits' \
    # Module 12L
    'identifyGraphOfRationalFunction' \
    'identifyHAs' \
    'identifyHoles' \
    'identifyOAs' \
    'identifyVAs' \
    )
    masterObjNumList=(
    # Module 1
    '01.4' \
    '01.4' \
    '01.3' \
    '01.2' \
    '01.1' \
    # Module 2
    '02.3' \
    '02.3' \
    '02.1' \
    '02.4' \
    '02.4' \
    # Module 3
    '03.1' \
    '03.3' \
    '03.3' \
    '03.3' \
    '03.3' \
    # Module 4
    '04.3' \
    '04.2' \
    '04.4' \
    '04.3' \
    '04.4' \
    # Module 5
    '05.1' \
    '05.2' \
    '05.2' \
    '05.3' \
    '05.3' \
    # Module 6
    '06.4' \
    '06.4' \
    '06.1' \
    '06.3' \
    '06.2'
    # Module 7
    '07.1' \
    '07.2' \
    '07.2' \
    '07.3' \
    '07.3' \
    # Module 8
    '08.1' \
    '08.1' \
    '08.2' \
    '08.3' \
    '08.4' \
    # Module 9M
    '09M.2' \
    '09M.3' \
    '09M.3' \
    '09M.3' \
    '09M.1' \
    # Module 10M
    '10M.2' \
    '10M.3' \
    '10M.4' \
    '10M.1' \
    '10M.1' \
    # Module 11M
    '11M.3' \
    '11M.2' \
    '11M.3' \
    '11M.1' \
    '11M.1' \
    # Module 12M
    '12M.2' \
    '12M.1' \
    '12M.3' \
    '12M.3' \
    '12M.3' \
    # Module 9L
    '09L.3' \
    '09L.1' \
    '09L.4' \
    '09L.4' \
    '09L.2' \
    # Module 10L
    '10L.3' \
    '10L.3' \
    '10L.2' \
    '10L.1' \
    '10L.1' \
    # Module 11L
    '11L.3' \
    '11L.3' \
    '11L.3' \
    '11L.1' \
    '11L.2' \
    # Module 12L
    '12L.5' \
    '12L.3' \
    '12L.1' \
    '12L.4' \
    '12L.2' \
    )
    masterDescriptionList=(
    # Module 1
    "Divide two complex numbers." \
    "Multiply two complex numbers." \
    "Simplify the expression using the order of operations." \
    "Identify the smallest subgroup an unsimplified number belongs to." \
    "Identify the smallest subgroup an unsimplified number belongs to." \
    # Module 2
    "Convert from graph to standard form." \
    "Use a point and a description of another line to construct a line." \
    "Use two points to construct a line." \
    "Solve a linear function with integer coefficients." \
    "Solve a linear function with rational coefficients." \
    # Module 3
    "Translate a description of numbers to interval notation." \
    "Solve an 'or'-inequality." \
    "Solve an 'and'-type inequality." \
    "Solve a linear inequality with integer coefficients." \
    "Solve a linear inequality with rational coefficients." \
    # Module 4
    "Factor a quadratic with leading coefficients greater than 1." \
    "Use a quadratic equation to identify its graph. " \
    "Solve a quadratic equation using the Quadratic Formula." \
    "Use a quadratic graph to construct its equation." \
    "Solve a quadratic equation that can be factored." \
    # Module 5
    "Determine the domain of a radical function." \
    "Use the equation of a radical function to identify its graph." \
    "Use the graph of a radical function to construct its equation." \
    "Solve a radical equation that leads to a linear equation." \
    "Solve a radical equation that leads to a quadratic equation." \
    # Module 6
    "Construct the lowest-degree polynomial given at least one complex root." \
    "Construct the lowest-degree polynomial given at least one rational root." \
    "Identify the end behavior of the polynomial." \
    "Use a graph of a polynomial to identify its equation." \
    "Identify the zero behavior of a particular root for a polynomial." \
    # Module 7
    "Identify the domain of a rational function." \
    "Use a rational equation to identify its graph." \
    "Use a graph of a rational function to identify its equation." \
    "Solve a rational equation that leads to a linear equation." \
    "Solve a rational equation that leads to a quadratic equation." \
    # Module 8
    "Identify the domain or range of an exponential function." \
    "Identify the domain or range of a logarithmic function." \
    "Solve a logarithmic equation by converting to exponential form." \
    "Solve a logarithmic equation by using log properties." \
    "Solve an exponential equation with different bases." \
    # Module 9M
    "Determine the domain of the linear model." \
    "Construct a linear model for a mixture-type real-world problem." \
    "Construct a linear model for a costs-profits-revenue real-world problem." \
    "Construct a linear model for a distance-rate-time real-world problem." \
    "Identify whether the population can be modeled by a linear equation." \
    # Module 10M
    "Construct a direct model for the real-world problem." \
    "Construct an indirect model for the real-world problem." \
    "Construct a joint model for the real-world problem." \
    "Identify whether the population can be modeled by a power equation." \
    "Identify whether the word description can be modeled by a power equation." \
    # Module 11M
    "Construct a model for a bacteria growth real-world problem." \
    "Construct a model for a half-life real-world problem." \
    "Given an exponential model for temperature, determine all coefficients." \
    "Identify the type of model best used for the graph provided." \
    "Identify the type of model best used for the table provided." \
    # Module 12M
    "Construct the linear, power, logarithmic, or exponential model needed for the situation." \
    "Identify the type of model best used for the graph provided." \
    "Solve the real-world problem using an exponential model." \
    "Solve the real-world problem using a linear model." \
    "Solve the real-world problem using a power model." \
    # Module 9L
    "Determine whether the equation is 1-1." \
    "Determine the domain after operating on two functions." \
    "Evaluate the inverse of a logarithmic or exponential function at a point." \
    "Evaluate the inverse of a polynomial or radical function at a point." \
    "Evaluate the composition of two functions at a point." \
    # Module 10L
    "Factor the polynomial using synthetic division with integer roots." \
    "Factor the polynomial using synthetic division with rational roots." \
    "Determine the possible (rational or integer) roots of the polynomial." \
    "Synthetically divide the polynomial without missing terms." \
    "Synthetically divide the polynomial with missing terms." \
    # Module 11L
    "Evaluate the limit analytically, where the limit is a real number." \
    "Evaluate the limit analytically, where the limit may not be defined on one side." \
    "Evaluate the limit graphically." \
    "Use the interpretation of the limit to choose the corresponding limit notation." \
    "Evaluate the one-sided limit analytically or graphically." \
    # Module 12L
    "Identify the graph of a rational function in general form using asymptotes and/or roots." \
    "Identify the horizontal asymptotes of a rational function, if any exist." \
    "Identify the holes of a rational function, if any exist." \
    "Identify the oblique asymptotes of a rational function, if any exist." \
    "Identify the vertical asymptotes of a rational function, if any exist." \
    )
}
function defineMAC1105FinalExamQuestionsList {
    MAC1105ExamQuestions=( \
    # M1
    'subgroupReal' 'divideComplex' 'orderOfOperations' \
    # M2
    'linearTwoPoints' 'linearParOrPer' 'solveRationalLinear' \
    # M3
    'solveIntegerInequality' 'solveRationalInequality' 'solveCompoundAND' \
    # M4
    'quadraticEquationToGraph' 'quadraticGraphToEquation' 'quadraticFormula' \
    # M5
    'domainRadical' 'radicalEquationToGraph' 'solveRadicalLinear' \
    # M6
    'polyGraphToFunction' 'polyZeroBehavior' 'constructPolyRationals' \
    # M7
    'solveRationalQuadratic' 'rationalGraphToEquation' 'solveRationalLinear' \
    # M8
    'domainRangeExp' 'domainRangeLog' 'solveExpDifferentBases' \
    )
}
