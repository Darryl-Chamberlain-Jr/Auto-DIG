source /${DIR}/shellScripts/./fileManipulationFunctions.sh
source /${DIR}/shellScripts/./questionCreationFunctions.sh
source /${DIR}/shellScripts/./fileCreationFunctions.sh
function defineModuleLongName {
    moduleNumber=$1
    if [ "$moduleNumber" -eq "1" ]; then
        moduleLongName="Module 1 - Real and Complex Numbers"
    elif [ "$moduleNumber" -eq "2" ]; then
        moduleLongName="Module 2 - Linear Functions"
    elif [ "$moduleNumber" -eq "3" ]; then
        moduleLongName="Module 3 - Linear Inequalities"
    elif [ "$moduleNumber" -eq "4" ]; then
        moduleLongName="Module 4 - Quadratic Functions"
    elif [ "$moduleNumber" -eq "5" ]; then
        moduleLongName="Module 5 - Radical Functions"
    elif [ "$moduleNumber" -eq "6" ]; then
        moduleLongName="Module 6 - Polynomial Functions"
    elif [ "$moduleNumber" -eq "7" ]; then
        moduleLongName="Module 7 - Rational Functions"
    elif [ "$moduleNumber" -eq "8" ]; then
        moduleLongName="Module 8 - Log and Exp Functions"
    elif [ "$moduleNumber" -eq "9M" ]; then
        moduleLongName="Module 9M - Modeling w/ Linear Functions"
    elif [ "$moduleNumber" -eq "10M" ]; then
        moduleLongName="Module 10M - Modeling w/ Power Functions"
    elif [ "$moduleNumber" -eq "11M" ]; then
        moduleLongName="Module 11M - Modeling w/ Log and Exp Functions"
    elif [ "$moduleNumber" -eq "12M" ]; then
        moduleLongName="Module 12M - Solving Real-World Word Problems"
    elif [ "$moduleNumber" -eq "9L" ]; then
        moduleLongName="Module 9L - Operations on Functions"
    elif [ "$moduleNumber" -eq "10L" ]; then
        moduleLongName="Module 10L - Synthetic Division"
    elif [ "$moduleNumber" -eq "11L" ]; then
        moduleLongName="Module 11L - Introduction to Limits"
    elif [ "$moduleNumber" -eq "12L" ]; then
        moduleLongName="Module 12L - Graphing Rational Functions"
    else
        echo "There isn't a Module $moduleNumber. Be sure to put in either 1-8, 9M-12M, or 9L-12L."
        exit $ERRCODE
    fi
}
function determineCodeFolderName {
    codeName=$1
    # Takes in a specific question. Defines the codeFolderName based on that specific question. Used for the *createQuestions* function.
    # List of all questions is stored in *questionCreationFunctions.sh*
    if [[ " ${module1questionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='01realComplex'
        moduleNumber="1"
    elif [[ " ${module2questionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='02linear'
        moduleNumber="2"
    elif [[ " ${module3questionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='03inequality'
        moduleNumber="3"
    elif [[ " ${module4questionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='04quadratic'
        moduleNumber="4"
    elif [[ " ${module5questionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='05radical'
        moduleNumber="5"
    elif [[ " ${module6questionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='06polynomial'
        moduleNumber="6"
    elif [[ " ${module7questionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='07rational'
        moduleNumber="7"
    elif [[ " ${module8questionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='08logExp'
        moduleNumber="8"
    elif [[ " ${module9MquestionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='09modelingLinear'
        moduleNumber="9M"
    elif [[ " ${module10MquestionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='10modelingPower'
        moduleNumber="10M"
    elif [[ " ${module11MquestionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='11modelingLogExp'
        moduleNumber="11M"
    elif [[ " ${module12MquestionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='12solvingWordProblems'
        moduleNumber="12M"
    elif [[ " ${module9LquestionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='13operationsOnFunctions'
        moduleNumber="9L"
    elif [[ " ${module10LquestionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='14syntheticDivision'
        moduleNumber="10L"
    elif [[ " ${module11LquestionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='15introToLimits'
        moduleNumber="11L"
    elif [[ " ${module12LquestionList[@]} " =~ " ${codeName} " ]]; then
        codeFolderName='16graphingRationalFunctions'
        moduleNumber="12L"
    fi
}
function createQuestions {
    version=$1
    questionNumber=1
    shuffledQuestionList=( $(shuf -e "${questionList[@]}") )
    for question in ${shuffledQuestionList[@]}; do ### Creates questions 1 by 1.
        determineCodeFolderName $question # Defines moduleNumber and codeFolderName
        chooseQuestionStructure $moduleNumber $version $questionNumber $codeFolderName $question $fileNamePrefix
        questionNumber=$((questionNumber+1))
    done
}
function generatePDFsAndKeys {
    fileNamePrefix=$1
    examLongName=$2
    footnoteLeft=$3
    version=$4
    # These are dummy .csv files that will be deleted later. This ensures the while loop runs correctly every time.
    touch /${DIR}/Keys/lettersAnswerKey${fileNamePrefix}${version}.csv
    touch /${DIR}/Keys/numbersAnswerKey${fileNamePrefix}${version}.csv
    SAGEresult=1
    PDFresult=1
    #This loops until the files run without error
    while [ $SAGEresult -ne 0 ] || [ $PDFresult -ne 0 ]; do
        cd /${DIR}/buildExams/
        createExamFile $fileNamePrefix "$examLongName" "$footnoteLeft" $version
        createQuestions $version ${questionList[@]}
        finishExamFile $fileNamePrefix $version
        createAnswerKeyFile $fileNamePrefix "$examLongName" "$footnoteLeft" $version
        rm /${DIR}/Keys/lettersAnswerKey${fileNamePrefix}${version}.csv
        rm /${DIR}/Keys/numbersAnswerKey${fileNamePrefix}${version}.csv
        touch /${DIR}/Keys/lettersAnswerKey${fileNamePrefix}${version}.csv
        touch /${DIR}/Keys/numbersAnswerKey${fileNamePrefix}${version}.csv
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${fileNamePrefix}${version}.tex
        sage /${DIR}/buildExams/${fileNamePrefix}${version}.sagetex.sage
        SAGEresult=$?
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${fileNamePrefix}${version}.tex
        PDFresult=$?
    done
    finishAnswerKeyFile $fileNamePrefix $version
    cd /${DIR}/Keys/
    pdflatex -file-line-error -halt-on-error /${DIR}/Keys/key${fileNamePrefix}${version}.tex
    cat /${DIR}/Keys/lettersAnswerKey${fileNamePrefix}${version}.csv >> /${DIR}/Keys/lettersMasterKey${version}.csv
    cp /${DIR}/buildExams/*.pdf /${DIR}/CompleteExam/PDFs
    cd /${DIR}/
}
