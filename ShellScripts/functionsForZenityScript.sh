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
function defineModuleList {
    if [ $examNumber -eq 1 ]; then
        moduleList=( 1 2 )
    elif [ $examNumber -eq 2 ]; then
        moduleList=( 1 2 3 4 )
    elif [ $examNumber -eq 3 ]; then
        moduleList=( 1 2 3 4 5 6)
    elif [ $examNumber -eq 4 ]; then
        moduleList=( 1 2 3 4 5 6 7 8)
    elif [ $examNumber -eq 5 ]; then
        moduleList=( 1 2 3 4 5 6 7 8 "9M" "10M" "9L" "10L")
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
        --height=100 \
        --width=200 \
        --text="You canceled the assessment generation early."
    pkill eog
    exit 0
    fi
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
