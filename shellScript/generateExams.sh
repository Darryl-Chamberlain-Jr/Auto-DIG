# This script generates exams.

### CHANGE THIS ONCE ###
DIR="home/dchamberlain31/git-repos/AAG-College-Algebra"
###############################################
StartTime=$( date +'%s' )
function createQuestion {
  Version=$1
  QuestionStructure=$2 # As enumerated in the directoryOfQuestionStructures. This will need to be revised when we want to choose 5 questions from the collection in a module.
  ProblemNumber=$3
  FileName=$4
  source /${DIR}/shellScript/questionCreationFunctions.sh

  # MODULE 1: Questions 1-5
  if [ $QuestionStructure -eq 1 ]; then
    createBasicStructure $1 $3 $4 1 '01realComplex' 'divideComplex'
  elif [ $QuestionStructure -eq 2 ]; then
    createBasicStructure $1 $3 $4 1 '01realComplex' 'multiplyComplex'
  elif [ $QuestionStructure -eq 3 ]; then
    createBasicStructure $1 $3 $4 1 '01realComplex' 'orderOfOperations'
  elif [ $QuestionStructure -eq 4 ]; then
    createBasicStructure $1 $3 $4 1 '01realComplex' 'subgroupComplex'
  elif [ $QuestionStructure -eq 5 ]; then
    createBasicStructure $1 $3 $4 1 '01realComplex' 'subgroupReal'
  # MODULE 2: Questions 6-10
  elif [ $QuestionStructure -eq 6 ]; then
    displayGraphProblem $1 $3 $4 2 '02linear' 'linearGraphToStandard'
  elif [ $QuestionStructure -eq 7 ]; then
    createBasicStructure $1 $3 $4 2 '02linear' 'linearParOrPer'
  elif [ $QuestionStructure -eq 8 ]; then
    createBasicStructure $1 $3 $4 2 '02linear' 'linearTwoPoints'
  elif [ $QuestionStructure -eq 9 ]; then
    createBasicStructure $1 $3 $4 2 '02linear' 'solveIntegerLinear'
  elif [ $QuestionStructure -eq 10 ]; then
    createBasicStructure $1 $3 $4 2 '02linear' 'solveRationalLinear'
  # MODULE 3: Questions 11-15
  elif [ $QuestionStructure -eq 11 ]; then
    createBasicStructure $1 $3 $4 3 '03inequality' 'describeSet'
  elif [ $QuestionStructure -eq 12 ]; then
    createBasicStructure $1 $3 $4 3 '03inequality' 'solveCompoundAND'
  elif [ $QuestionStructure -eq 13 ]; then
    createBasicStructure $1 $3 $4 3 '03inequality' 'solveCompoundOR'
  elif [ $QuestionStructure -eq 14 ]; then
    createBasicStructure $1 $3 $4 3 '03inequality' 'solveIntegerInequality'
  elif [ $QuestionStructure -eq 15 ]; then
    createBasicStructure $1 $3 $4 3 '03inequality' 'solveRationalInequality'
  # MODULE 4: Questions 16-20
  elif [ $QuestionStructure -eq 16 ]; then
    createBasicStructure $1 $3 $4 4 '04quadratic' 'factorLeadingOver1Composite'
  elif [ $QuestionStructure -eq 17 ]; then
    createMathProblemAnd4Graph1TextOptions $1 $3 $4 4 '04quadratic' 'quadraticEquationToGraph'
  elif [ $QuestionStructure -eq 18 ]; then
    createBasicStructure $1 $3 $4 4 '04quadratic' 'quadraticFormula'
  elif [ $QuestionStructure -eq 19 ]; then
    displayGraphProblem $1 $3 $4 4 '04quadratic' 'quadraticGraphToEquation'
  elif [ $QuestionStructure -eq 20 ]; then
    createBasicStructure $1 $3 $4 4 '04quadratic' 'solveQuadraticFactorComposites'
  # MODULE 5: Questions 21-25
  elif [ $QuestionStructure -eq 21 ]; then
    createBasicStructure $1 $3 $4 5 '05radical' 'domainRadical'
  elif [ $QuestionStructure -eq 22 ]; then
    createMathProblemAnd4Graph1TextOptions $1 $3 $4 5 '05radical' 'radicalEquationToGraph'
  elif [ $QuestionStructure -eq 23 ]; then
    displayGraphProblem $1 $3 $4 5 '05radical' 'radicalGraphToEquation'
  elif [ $QuestionStructure -eq 24 ]; then
    createBasicStructure $1 $3 $4 5 '05radical' 'solveRadicalLinear'
  elif [ $QuestionStructure -eq 25 ]; then
    createBasicStructure $1 $3 $4 5 '05radical' 'solveRadicalQuadratic'
  # MODULE 6: Questions 26-30
  elif [ $QuestionStructure -eq 26 ]; then
    createBasicStructure $1 $3 $4 6 '06polynomial' 'constructPolyComplex'
  elif [ $QuestionStructure -eq 27 ]; then
    createBasicStructure $1 $3 $4 6 '06polynomial' 'constructPolyRationals'
  elif [ $QuestionStructure -eq 28 ]; then
    createMathProblemAnd4GraphOptions $1 $3 $4 6 '06polynomial' 'polyEndBehavior'
  elif [ $QuestionStructure -eq 29 ]; then
    displayGraphProblem $1 $3 $4 6 '06polynomial' 'polyGraphToFunction'
  elif [ $QuestionStructure -eq 30 ]; then
    createMathProblemAnd4GraphOptions $1 $3 $4 6 '06polynomial' 'polyZeroBehavior'
  # MODULE 7: Questions 31-35
  elif [ $QuestionStructure -eq 31 ]; then
    createBasicStructure $1 $3 $4 7 '07rational' 'domainRational'
  elif [ $QuestionStructure -eq 32 ]; then
    createMathProblemAnd4Graph1TextOptions $1 $3 $4 7 '07rational' 'rationalEquationToGraph'
  elif [ $QuestionStructure -eq 33 ]; then
    displayGraphProblem $1 $3 $4 7 '07rational' 'rationalGraphToEquation'
  elif [ $QuestionStructure -eq 34 ]; then
    createBasicStructure $1 $3 $4 7 '07rational' 'solveRationalLinear'
  elif [ $QuestionStructure -eq 35 ]; then
    createBasicStructure $1 $3 $4 7 '07rational' 'solveRationalQuadratic'
  # MODULE 8: Questions 36-40
  elif [ $QuestionStructure -eq 36 ]; then
    createBasicStructure $1 $3 $4 8 '08logExp' 'domainRangeExp'
  elif [ $QuestionStructure -eq 37 ]; then
    createBasicStructure $1 $3 $4 8 '08logExp' 'domainRangeLog'
  elif [ $QuestionStructure -eq 38 ]; then
    createBasicStructure $1 $3 $4 8 '08logExp' 'solveByConverting'
  elif [ $QuestionStructure -eq 39 ]; then
    createBasicStructure $1 $3 $4 8 '08logExp' 'solveByLogProperties'
  elif [ $QuestionStructure -eq 40 ]; then
    createBasicStructure $1 $3 $4 8 '08logExp' 'solveExpDifferentBases'
  # MODULE 9M: Questions 41-45
  elif [ $QuestionStructure -eq 41 ]; then
    displayNoMathModeProblem $1 $3 $4 "9M" '09modelingLinear' 'constructLinearModelDistanceAndRate'
  elif [ $QuestionStructure -eq 42 ]; then
    displayNoMathModeProblem $1 $3 $4 "9M" '09modelingLinear' 'constructLinearModelCostsProfitsRevenue'
  elif [ $QuestionStructure -eq 43 ]; then
    displayNoMathModeProblem $1 $3 $4 "9M" '09modelingLinear' 'constructLinearModelMixture'
  elif [ $QuestionStructure -eq 44 ]; then
    displayNoMathModeProblem $1 $3 $4 "9M" '09modelingLinear' 'domainLinearModel'
  elif [ $QuestionStructure -eq 45 ]; then
    displayTableProblemSpecial $1 $3 $4 "9M" '09modelingLinear' 'identifyModelPopulation'
  # MODULE 10M: Questions 46-50
  elif [ $QuestionStructure -eq 46 ]; then
    displayNoMathModeProblem $1 $3 $4 '10M' '10modelingPower' 'constructDirectModel'
  elif [ $QuestionStructure -eq 47 ]; then
    displayNoMathModeProblem $1 $3 $4 '10M' '10modelingPower' 'constructIndirectModel'
  elif [ $QuestionStructure -eq 48 ]; then
    displayNoMathModeProblem $1 $3 $4 '10M' '10modelingPower' 'constructJointModel'
  elif [ $QuestionStructure -eq 49 ]; then
    displayTableProblemSpecial $1 $3 $4 '10M' '10modelingPower' 'identifyModelPopulation'
  elif [ $QuestionStructure -eq 50 ]; then
    displayNoMathModeProblem4Options $1 $3 $4 '10M' '10modelingPower' 'identifyModelVariation'
  # MODULE 11M: Questions 51-55
  elif [ $QuestionStructure -eq 51 ]; then
    displayNoMathModeProblem $1 $3 $4 '11M' '11modelingLogExp' 'constructBacteriaGrowth'
  elif [ $QuestionStructure -eq 52 ]; then
    displayNoMathModeProblem $1 $3 $4 '11M' '11modelingLogExp' 'constructHalfLifeModel'
  elif [ $QuestionStructure -eq 53 ]; then
    displayNoMathModeProblem $1 $3 $4 '11M' '11modelingLogExp' 'constructTemperatureModel'
  elif [ $QuestionStructure -eq 54 ]; then
    displayGraphProblem $1 $3 $4 '11M' '11modelingLogExp' 'identifyModelGraph11'
  elif [ $QuestionStructure -eq 55 ]; then
    displayTableProblemSpecial $1 $3 $4 '11M' '11modelingLogExp' 'identifyModelPopulation'
  # MODULE 12M: Questions 56-60
  elif [ $QuestionStructure -eq 56 ]; then
    displayNoMathModeProblem  $1 $3 $4 '12M' '12solvingWordProblems' 'constructModelMixed'
  elif [ $QuestionStructure -eq 57 ]; then
    displayGraphProblem $1 $3 $4 '12M' '12solvingWordProblems' 'identifyModelGraph12'
  elif [ $QuestionStructure -eq 58 ]; then
    displayNoMathModeProblem  $1 $3 $4 '12M' '12solvingWordProblems' 'solveModelExp'
  elif [ $QuestionStructure -eq 59 ]; then
    displayNoMathModeProblem  $1 $3 $4 '12M' '12solvingWordProblems' 'solveModelLinear'
  elif [ $QuestionStructure -eq 60 ]; then
    displayNoMathModeProblem  $1 $3 $4 '12M' '12solvingWordProblems' 'solveModelPower'
  # MODULE 9L: Questions 61-65
  elif [ $QuestionStructure -eq 61 ]; then
    createBasicStructure $1 $3 $4 '9L' '13operationsOnFunctions' 'determine1to1'
  elif [ $QuestionStructure -eq 62 ]; then
    createBasicStructure $1 $3 $4 '9L' '13operationsOnFunctions' 'domainAfterOperating'
  elif [ $QuestionStructure -eq 63 ]; then
    createBasicStructure $1 $3 $4 '9L' '13operationsOnFunctions' 'findInverseLogOrExp'
  elif [ $QuestionStructure -eq 64 ]; then
    createBasicStructure $1 $3 $4 '9L' '13operationsOnFunctions' 'findInversePolyOrRadical'
  elif [ $QuestionStructure -eq 65 ]; then
    createBasicStructure $1 $3 $4 '9L' '13operationsOnFunctions' 'functionComposition'
  # MODULE 10L: Questions 66-70
  elif [ $QuestionStructure -eq 66 ]; then
    createBasicStructure $1 $3 $4 '10L' '14syntheticDivision' 'factorUsingSynthetic2Integers'
  elif [ $QuestionStructure -eq 67 ]; then
    createBasicStructure $1 $3 $4 '10L' '14syntheticDivision' 'factorUsingSynthetic2Rationals'
  elif [ $QuestionStructure -eq 68 ]; then
    createBasicStructure $1 $3 $4 '10L' '14syntheticDivision' 'possibleRoots'
  elif [ $QuestionStructure -eq 69 ]; then
    createBasicStructure $1 $3 $4 '10L' '14syntheticDivision' 'syntheticDivision'
  elif [ $QuestionStructure -eq 70 ]; then
    createBasicStructure $1 $3 $4 '10L' '14syntheticDivision' 'syntheticDivisionMissingTerms'
  # MODULE 11L: Questions 71-75
  elif [ $QuestionStructure -eq 71 ]; then
    createBasicStructure $1 $3 $4 '11L' '15introToLimits' 'evaluateLimitAnalyticalEasy'
  elif [ $QuestionStructure -eq 72 ]; then
    createBasicStructure $1 $3 $4 '11L' '15introToLimits' 'evaluateLimitAnalyticalHard'
  elif [ $QuestionStructure -eq 73 ]; then
    displayGraphProblem $1 $3 $4 '11L' '15introToLimits' 'evaluateLimitGraphically'
  elif [ $QuestionStructure -eq 74 ]; then
    displayNoMathModeProblem $1 $3 $4 '11L' '15introToLimits' 'interpretLimit'
  elif [ $QuestionStructure -eq 75 ]; then
    createBasicStructure $1 $3 $4 '11L' '15introToLimits' 'oneSidedLimits'
  # MODULE 12L: Questions 76-80
  elif [ $QuestionStructure -eq 76 ]; then
    displayGraphProblem $1 $3 $4 '12L' '16graphingRationalFunctions' 'identifyGraphOfRationalFunction'
  elif [ $QuestionStructure -eq 77 ]; then
    createBasicStructure $1 $3 $4 '12L' '16graphingRationalFunctions' 'identifyHAs'
  elif [ $QuestionStructure -eq 78 ]; then
    createBasicStructure $1 $3 $4 '12L' '16graphingRationalFunctions' 'identifyHoles'
  elif [ $QuestionStructure -eq 79 ]; then
    createBasicStructure $1 $3 $4 '12L' '16graphingRationalFunctions' 'identifyOAs'
  elif [ $QuestionStructure -eq 80 ]; then
    createBasicStructure $1 $3 $4 '12L' '16graphingRationalFunctions' 'identifyVAs'
  else
    echo "An invalid question structure was chosen. Please refer to the directoryOfQuestionStructures.txt to determine the number associated with each constructed question."
  fi
}

# Function to check if item already exists in array
function checkArray {
  for item in ${QuestionList[@]}
  do
    [[ "$item" == "$1" ]] && return 0 # Exists in QuestionList
  done
  return 1 # Not found
}

function createModuleBodyTex {
  MODULEVERSION=$1
  STARTENUMERATEAT=$2
  FILENAME=$3
  # Shuffle array
  # Contents of array src are shuffled randomly and result is stored in destination array
  # -------------------------------------------
  Q1=$((${STARTENUMERATEAT} + 1))
  Q2=$((${STARTENUMERATEAT} + 2))
  Q3=$((${STARTENUMERATEAT} + 3))
  Q4=$((${STARTENUMERATEAT} + 4))
  Q5=$((${STARTENUMERATEAT} + 5))
  IFS=$'\n'
  src=( ${Q1} ${Q2} ${Q3} ${Q4} ${Q5})
  QuestionList=()
  # Main loop
  while [ "${#QuestionList[@]}" -ne "${#src[@]}" ]
  do
      rand=$[ $RANDOM % ${#src[@]} ]
      checkArray "${src[$rand]}" || QuestionList=(${QuestionList[@]} "${src[$rand]}")
  done
  QuestionCounter=$((${STARTENUMERATEAT} + 1))
  for question in ${QuestionList[@]}
  do
    createQuestion $1 $question $QuestionCounter $3
    QuestionCounter=$(($QuestionCounter + 1))
  done
}

function generateFinalExamAllVersions {
    Password=$1
    Semester=$2
    FileName=$3
    RESULT=1
    # Shuffle array
    # Contents of array src are shuffled randomly and result is stored in destination array
    # -------------------------------------------
    IFS=$'\n'
    src=( 1 2 5 6 8 10 12 13 15 16 17 20 21 23 24 26 28 29 32 33 34 36 37 40)
    QuestionList=()
    # Main loop
    while [ "${#QuestionList[@]}" -ne "${#src[@]}" ]
    do
        rand=$[ $RANDOM % ${#src[@]} ]
        checkArray "${src[$rand]}" || QuestionList=(${QuestionList[@]} "${src[$rand]}")
    done
    # Creating empty keys for all versions
    for version in A B C
    do
        cd /${DIR}/buildExams/
        source /${DIR}/shellScript/fileCreationFunctions.sh
        createFinalExamHeading $version $2 $3
        problemCounter=1
        for i in "${QuestionList[@]}"
        do
            createQuestion $version $i $problemCounter $3
            problemCounter=$((problemCounter+1))
        done
        createFinalExamEnding $version $3
        createAnswerKeyFile $version $2 $3 'FinalExam'
        touch /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
        touch /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
        RESULT=$?
        #This loops until the module runs without errors.
        while [ $RESULT != 0 ]
        do
            createFinalExamHeading $version $2 $3
            problemCounter=1
            for i in "${QuestionList[@]}"
            do
                createQuestion $version $i $problemCounter $3
                problemCounter=$((problemCounter+1))
            done
            createFinalExamEnding $version $3
            createAnswerKeyFile $version $2 $3 'FinalExam'
            rm /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
            rm /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
            touch /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
            touch /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
            pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
            sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
            RESULT=$?
        done
        RESULT=1
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        finishAnswerKeyFile $version $3
        cd /${DIR}/Keys/
        pdflatex -file-line-error -halt-on-error /${DIR}/Keys/key${FileName}${version}.tex
        cat /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv >> /${DIR}/Keys/lettersMasterKey${version}.csv
        cat /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv >> /${DIR}/Keys/numbersMasterKey${version}.csv
    done
    #Copy/Pastes all completed PDFs to a new folder
    cp /${DIR}/buildExams/*.pdf /${DIR}/CompleteExam/PDFs
    cd /${DIR}/CompleteExam/PDFs
    for version in A B C
    do
        # Locks PDFs
        pdftk ${FileName}${version}.pdf output ../LockedPDFs/${FileName}${version}.pdf owner_pw SGS user_pw ${PASSWORD}
    done
}

function generateModuleAllVersions {
    MODULENUMBER=$1
    EXAMNUMBER=$2
    SEMESTER=$3
    STARTENUMERATEAT=$4
    LONGNAME=$5
    PASSWORD=$6
    FileName=$7
    RESULT=1
    FINALRESULT=1
    source /${DIR}/shellScript/fileCreationFunctions.sh
    source /${DIR}/shellScript/reportFunctions.sh
    # Creating empty keys for all versions
    for version in A B C
    do
        ModuleRunTimeStart=$( date +'%s' )
        cd /${DIR}/buildExams/
        createExamHeading $version $2 $3 $4 $5 $7
        createModuleBodyTex $version $4 $7
        createExamEnding $version $7
        createAnswerKeyFile $version $3 $7 $5
        touch /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
        touch /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
        SAGEresult=$?
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        PDFresult=$?
        #This loops until the module runs without errors.
        while [ $SAGEresult != 0 ] || [ $PDFresult != 0 ]; do
            if $SAGEresult != 0; then
                reportOnSageError $2 $1 $version
            else:
                reportOnPDFlatexError $2 $1 $version
            fi
            createExamHeading $version $2 $3 $4 $5 $7
            createModuleBodyTex $version $4 $7
            createExamEnding $version $7
            createAnswerKeyFile $version $3 $7 $5
            rm /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
            rm /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
            touch /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
            touch /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
            pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
            sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
            SAGEresult=$?
            pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
            PDFresult=$?
        done
        finishAnswerKeyFile $version $7
        cd /${DIR}/Keys/
        pdflatex -file-line-error -halt-on-error /${DIR}/Keys/key${FileName}${version}.tex
        cat /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv >> /${DIR}/Keys/lettersMasterKey${version}.csv
        cat /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv >> /${DIR}/Keys/numbersMasterKey${version}.csv
        ModuleRunTimeEnd=$( date +'%s' )
        reportOnModuleRunTime $1 $2 $ModuleRunTimeStart $ModuleRunTimeEnd $version
    done
    # Copy/Pastes all completed PDFs to a new folder
    cp /${DIR}/buildExams/*.pdf /${DIR}/CompleteExam/PDFs
    source /${DIR}/shellScript/fileManipulationFunctions.sh
    copyKeys $7
    cd /${DIR}/CompleteExam/PDFs
    for version in A B C
    do
        # Locks PDFs
        pdftk ${FileName}${version}.pdf output ../LockedPDFs/${FileName}${version}.pdf owner_pw SGS user_pw ${PASSWORD}
    done
    cd
}

source /${DIR}/shellScript/fileManipulationFunctions.sh
source /${DIR}/shellScript/reportFunctions.sh
clearOldVersions
setSemester=$1
setPassword=$2
setExamNumber=$3
setModuleNumber=$4

createReportFile $3

if [ "$1" == "debug" ]; then
    if [ "$4" == 1 ]; then
        generateModuleAllVersions "1" $setExamNumber $setPassword 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" "debug" "Module1"
    elif [ "$4" == 2 ]; then
        generateModuleAllVersions "2" $setExamNumber $setPassword 5 "Module\,2\,-\,Linear\,Functions" "debug" "Module2"
    elif [ "$4" == 3 ]; then
        generateModuleAllVersions "3" $setExamNumber $setPassword 10 "Module\,3\,-\,Inequalities" "debug" "Module3"
    elif [ "$4" == 4 ]; then
        generateModuleAllVersions "4" $setExamNumber $setPassword 15 "Module\,4\,-\,Quadratic\,Functions" "debug" "Module4"
    elif [ "$4" == 5 ]; then
        generateModuleAllVersions "5" $setExamNumber $setPassword 20 "Module\,5\,-\,Radical\,Functions" "debug" "Module5"
    elif [ "$4" == 6 ]; then
        generateModuleAllVersions "6" $setExamNumber $setPassword 25 "Module\,6\,-\,Polynomial\,Functions" "debug" "Module6"
    elif [ "$4" == 7 ]; then
        generateModuleAllVersions "7" $setExamNumber $setPassword 30 "Module\,7\,-\,Rational\,Functions" "debug" "Module7"
    elif [ "$4" == 8 ]; then
        generateModuleAllVersions "8" $setExamNumber $setPassword 35 "Module\,8\,-\,Logarithmic\,and\,Exponential\,Functions" "debug" "Module8"
    elif [ "$4" == 9 ]; then
        generateModuleAllVersions "9M" $setExamNumber $setPassword 40 "Module\,9M\,-\,Modeling\,Linear\,Functions" "debug" "Module9M"
    elif [ "$4" == 10 ]; then
        generateModuleAllVersions "10M" $setExamNumber $setPassword 45 "Module\,10M\,-\,Modeling\,with\,Power\,Functions" "debug" "Module10M"
    elif [ "$4" == 11 ]; then
        generateModuleAllVersions "11M" $setExamNumber $setPassword 50 "Module\,11M\,-\,Modeling\,with\,Log\,and\,Exp\,Functions" "debug" "Module11M"
    elif [ "$4" == 12 ]; then
        generateModuleAllVersions "12M" $setExamNumber $setPassword 55 "Module\,12M\,-\,Solving\,Word\,Problems" "debug" "Module12M"
    elif [ "$4" == 13 ]; then
        generateModuleAllVersions "9L" $setExamNumber $setPassword 60 "Module\,9L\,-\,Operations\,on\,Functions" "debug" "Module9L"
    elif [ "$4" == 14 ]; then
        generateModuleAllVersions "10L" $setExamNumber $setPassword 65 "Module\,10L\,-\,Synthetic\,Division" "debug" "Module10L"
    elif [ "$4" == 15 ]; then
        generateModuleAllVersions "11L" $setExamNumber $setPassword 70 "Module\,11L\,-\,Introduction\,to\,Limits" "debug" "Module11L"
    elif [ "$4" == 16 ]; then
        generateModuleAllVersions "12L" $setExamNumber $setPassword 75 "Module\,12L\,-\,Graphing\,Rational\,Functions" "debug" "Module12L"
    else
        echo "You tried to run the debug mode but did not input a valid module number. Modeling modules are 9-12 and Limits modules are 13-16."
    fi
else
    while [ "$1" == "" ] || [ "$2" == "" ] || [ "$3" == "" ]; do
        echo -e "\nArguments for the exam are missing. The arguments are Semester, Password, and Exam Number. \n \nPlease put the semester in parentheses and make sure it has no spaces, such as 'Spring\,2020'. \nThe password should be a single word in parentheses, such as 'Password1'. \nThe exam number should be 1, 2, 3, 4, 5, 6, or 7 (final exam). The number of Modules generated is based on the exam number."
        echo -e "\n If you meant to debug, make the first argument 'debug', the second argument the Semester, the third argument the exam number, and the fourth argument the single module you want to run. Modeling modules are 9-12 and Limits modules are 13-16."
        exit -1
    done

    if [ "$3" == 1 ]; then
        generateModuleAllVersions "1" $setExamNumber $setSemester 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" $setPassword "Module1"
        generateModuleAllVersions "2" $setExamNumber $setSemester 5 "Module\,2\,-\,Linear\,Functions" $setPassword "Module2"
        generateModuleAllVersions "3" $setExamNumber $setSemester 10 "Module\,3\,-\,Inequalities" $setPassword "Module3"
    elif [ "$3" == 2 ]; then
        generateModuleAllVersions "1" $setExamNumber $setSemester 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" $setPassword "Module1"
        generateModuleAllVersions "2" $setExamNumber $setSemester 5 "Module\,2\,-\,Linear\,Functions" $setPassword "Module2"
        generateModuleAllVersions "3" $setExamNumber $setSemester 10 "Module\,3\,-\,Inequalities" $setPassword "Module3"
        generateModuleAllVersions "4" $setExamNumber $setSemester 15 "Module\,4\,-\,Quadratic\,Functions" $setPassword "Module4"
        generateModuleAllVersions "5" $setExamNumber $setSemester 20 "Module\,5\,-\,Radical\,Functions" $setPassword "Module5"
        generateModuleAllVersions "6" $setExamNumber $setSemester 25 "Module\,6\,-\,Polynomial\,Functions" $setPassword "Module6"
    elif [ "$3" == 3 ]; then
        generateModuleAllVersions "1" $setExamNumber $setSemester 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" $setPassword "Module1"
        generateModuleAllVersions "2" $setExamNumber $setSemester 5 "Module\,2\,-\,Linear\,Functions" $setPassword "Module2"
        generateModuleAllVersions "3" $setExamNumber $setSemester 10 "Module\,3\,-\,Inequalities" $setPassword "Module3"
        generateModuleAllVersions "4" $setExamNumber $setSemester 15 "Module\,4\,-\,Quadratic\,Functions" $setPassword "Module4"
        generateModuleAllVersions "5" $setExamNumber $setSemester 20 "Module\,5\,-\,Radical\,Functions" $setPassword "Module5"
        generateModuleAllVersions "6" $setExamNumber $setSemester 25 "Module\,6\,-\,Polynomial\,Functions" $setPassword "Module6"
        generateModuleAllVersions "7" $setExamNumber $setSemester 30 "Module\,7\,-\,Rational\,Functions" $setPassword "Module7"
        generateModuleAllVersions "8" $setExamNumber $setSemester 35 "Module\,8\,-\,Logarithmic\,and\,Exponential\,Functions" $setPassword "Module8"
        generateModuleAllVersions "9M" $setExamNumber $setSemester 40 "Module\,9M\,-\,Modeling\,Linear\,Functions" $setPassword "Module9M"
        generateModuleAllVersions "9L" $setExamNumber $setSemester 60 "Module\,9L\,-\,Operations\,on\,Functions" $setPassword "Module9L"
    elif [ "$3" == 4 ] || [ "$3" == 5 ] || [ "$3" == 6 ]; then
        generateModuleAllVersions "1" $setExamNumber $setSemester 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" $setPassword "Module1"
        generateModuleAllVersions "2" $setExamNumber $setSemester 5 "Module\,2\,-\,Linear\,Functions" $setPassword "Module2"
        generateModuleAllVersions "3" $setExamNumber $setSemester 10 "Module\,3\,-\,Inequalities" $setPassword "Module3"
        generateModuleAllVersions "4" $setExamNumber $setSemester 15 "Module\,4\,-\,Quadratic\,Functions" $setPassword "Module4"
        generateModuleAllVersions "5" $setExamNumber $setSemester 20 "Module\,5\,-\,Radical\,Functions" $setPassword "Module5"
        generateModuleAllVersions "6" $setExamNumber $setSemester 25 "Module\,6\,-\,Polynomial\,Functions" $setPassword "Module6"
        generateModuleAllVersions "7" $setExamNumber $setSemester 30 "Module\,7\,-\,Rational\,Functions" $setPassword "Module7"
        generateModuleAllVersions "8" $setExamNumber $setSemester 35 "Module\,8\,-\,Logarithmic\,and\,Exponential\,Functions" $setPassword "Module8"
        generateModuleAllVersions "9M" $setExamNumber $setSemester 40 "Module\,9M\,-\,Modeling\,Linear\,Functions" $setPassword "Module9M"
        generateModuleAllVersions "10M" $setExamNumber $setSemester 45 "Module\,10M\,-\,Modeling\,with\,Power\,Functions" $setPassword "Module10M"
        generateModuleAllVersions "11M" $setExamNumber $setSemester 50 "Module\,11M\,-\,Modeling\,with\,Log\,and\,Exp\,Functions" $setPassword "Module11M"
        generateModuleAllVersions "12M" $setExamNumber $setSemester 55 "Module\,12M\,-\,Solving\,Word\,Problems" $setPassword "Module12M"
        generateModuleAllVersions "9L" $setExamNumber $setSemester 60 "Module\,9L\,-\,Operations\,on\,Functions" $setPassword "Module9L"
        generateModuleAllVersions "10L" $setExamNumber $setSemester 65 "Module\,10L\,-\,Synthetic\,Division" $setPassword "Module10L"
        generateModuleAllVersions "11L" $setExamNumber $setSemester 70 "Module\,11L\,-\,Introduction\,to\,Limits" $setPassword "Module11L"
        generateModuleAllVersions "12L" $setExamNumber $setSemester 75 "Module\,12L\,-\,Graphing\,Rational\,Functions" $setPassword "Module12L"
    else
        generateFinalExamAllVersions $setPassword $setSemester "FinalExam"
    fi
    copyKeys
fi
EndTime=$( date +'%s' )
finishReport $3 $StartTime $EndTime
