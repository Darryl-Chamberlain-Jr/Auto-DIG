titleOfProgram="Auto-DIG v.0.1"
DIR="home/dchamberlain31/git-repos/Auto-DIG"
###########################################
source ./questionCreationFunctions.sh
source ./fileManipulationFunctions.sh
source ./functionsForZenityAutoDIGshFile.sh
source ./generateExams.sh
generationOptions
typeOfGeneration=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=250 \
    --width=200 \
    --list \
    --text '<b> What do you want to do?</b>' \
    --column 'Generate...' \
    "$generationOption1" \
    "$generationOption2" \
    "$generationOption3" \
    "$generationOption4"
)
escape=$?
checkForEscape $escape
footnoteLeft=$(zenity \
    --title="${titleOfProgram[@]}" \
    --entry \
    --text 'What do you want to print on the bottom-right of the page?'
)
escape=$?
checkForEscape $escape
# Call as ${footnoteLeft[@]}
numberOfVersions=$(zenity \
    --title="${titleOfProgram[@]}" \
    --scale \
    --text="How many versions do you want to create?" \
    --value=3 \
    --min-value=1 \
    --max-value=26 \
    --step=1
)
escape=$?
checkForEscape $escape
defineVersionList
listAllQuestions
###
if [ "$typeOfGeneration" == "$generationOption1" ]; then # Creating a Progress Quiz
    chooseExamNumber=$(zenity \
        --title="${titleOfProgram[@]}" \
        --height=275 \
        --list \
        --text '<b>Which quiz do you want to create?</b>
        The quiz number will be printed at the top of each PDF.' \
        --column 'Quiz Number' \
        "1 - This creates Modules 1, 2, and 3." \
        "2 - This creates Modules 1, 2, 3, 4, 5, and 6." \
        "3 - This creates Modules 1-8, 9M, and 9L" \
        "4 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
        "5 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
        "6 - This creates Modules 1-8, 9M-12M, and 9L-12L"
    )
    escape=$?
    checkForEscape $escape
    examNumber=${chooseExamNumber:0:1}
    defineModuleList # Also defines the number of modules.
    examLongName="Progress\,Quiz\,${examNumber}"
elif [ "$typeOfGeneration" == "$generationOption2" ]; then # Creates a single module
    moduleOptions
    chooseModule=$(zenity \
        --title="${titleOfProgram[@]}" \
        --height=525 \
        --width=425 \
        --list \
        --text '<b>Which Module do you want to create?</b>' \
        --column 'Quiz Number' \
        "$moduleOption1" "$moduleOption2" "$moduleOption3" "$moduleOption4" "$moduleOption5" "$moduleOption6" "$moduleOption7" "$moduleOption8" "$moduleOption9M" "$moduleOption10M" "$moduleOption11M" "$moduleOption12M" "$moduleOption9L" "$moduleOption10L" "$moduleOption11L" "$moduleOption12L"
    )
    escape=$?
    checkForEscape $escape
    defineSingleModule ${chooseModule[@]}
    moduleList=( "${singleModule[@]}" )
    numberOfModules=1
    examLongName="Quiz on Module ${singleModule[@]}"
elif [ "$typeOfGeneration" == "$generationOption3" ]; then # Creates a MAC 1105 Final Exam
    defineAllQuestionsForChecklist
    defineMAC1105FinalExamQuestionsList
    numberOfQuestionStructures=${#masterQuestionList[@]}
    flexibleQuestionList=$(for i in $(seq 0 $(( numberOfQuestionStructures-1 )) )
    do
        if [[ " ${MAC1105ExamQuestions[@]} " =~ " ${masterQuestionList[i]} " ]]; then
            echo "TRUE"
            echo ${masterQuestionList[i]}
            echo ${masterObjNumList[i]}
            echo "${masterDescriptionList[i]}"
        else
            echo "FALSE"
            echo ${masterQuestionList[i]}
            echo ${masterObjNumList[i]}
            echo "${masterDescriptionList[i]}"
        fi
    done | zenity \
        --title="${titleOfProgram[@]}" \
        --height=600 \
        --width=1000 \
        --list \
        --checklist \
        --separator=" " \
        --multiple \
        --text '<b> Which questions would you like to include?</b>' \
        --column 'Choose' --column 'File name' --column 'Obj. #' --column 'Description'
    )
    escape=$?
    checkForEscape $escape
    questionList=(`echo ${flexibleQuestionList}`)
    examLongName="Final Exam: Module 1-8"
    fileNamePrefix="FinalExam"
elif [ "$typeOfGeneration" == "$generationOption4" ]; then # Creates a flexible assessment
    defineAllQuestionsForChecklist
    numberOfQuestionStructures=${#masterQuestionList[@]}
    flexibleQuestionList=$(for i in $(seq 0 $(( numberOfQuestionStructures-1 )) )
    do
        echo "FALSE"
        echo ${masterQuestionList[i]}
        echo ${masterObjNumList[i]}
        echo "${masterDescriptionList[i]}"
    done | zenity \
        --title="${titleOfProgram[@]}" \
        --height=600 \
        --width=1000 \
        --list \
        --checklist \
        --separator=" " \
        --multiple \
        --text '<b> Which questions would you like to include?</b>' \
        --column 'Choose' --column 'File name' --column 'Obj. #' --column 'Description'
    )
    escape=$?
    checkForEscape $escape
    questionList=(`echo ${flexibleQuestionList}`)
    examLongName=$(zenity \
        --title="${titleOfProgram[@]}" \
        --entry \
        --text 'What do you want to call your assessment?'
    )
    escape=$?
    checkForEscape $escape
    fileNamePrefix=$(zenity \
        --title="${titleOfProgram[@]}" \
        --entry \
        --text 'Give a short, NO SPACES, name to your assessment.'
    )
    escape=$?
    checkForEscape $escape
fi
(
clearOldVersions
StartTime=$( date +'%s' )
# Step is the total number of modules * number of versions
if [ "$typeOfGeneration" == "$generationOption1" ] ; then
    step=$(( 100 / (numberOfModules*numberOfVersions) ))
else
    step=$(( 100 / numberOfVersions ))
fi
counter=0
while :
do
    if [ "$typeOfGeneration" == "$generationOption1" ] || [ "$typeOfGeneration" == "$generationOption2" ] ; then
        for module in ${moduleList[@]}
        do
            presetQuestionList $module # This defines the question list for the module
            fileNamePrefix="Module${module}"
            for version in ${versionList[@]}
            do
                echo "$counter" ; sleep 0
                generatePDFsAndKeys $fileNamePrefix "$examLongName" "$footnoteLeft" $version
                copyKeys $fileNamePrefix ${versionList[@]}
                counter=$(( counter+step ))
            done
        done
    else
        for version in ${versionList[@]}
        do
            echo "$counter" ; sleep 0
            echo "# Creating "$examLongName" Version $version. Progress: $counter%"
            generatePDFsAndKeys $fileNamePrefix "$examLongName" "$footnoteLeft" $version
            copyKeys $fileNamePrefix ${versionList[@]}
            counter=$(( counter+step ))
        done
    fi
    break
done
xdg-open /${DIR}/CompleteExam
EndTime=$( date +'%s' )
currentDayTime=$( date +'%H:%M on %m/%d/%Y' )
TotalRunTimeSeconds=$(( EndTime - StartTime ))
RunTimeMinutes=$(( (EndTime - StartTime) / 60 ))
RunTimeSecondsRemainder=$(( TotalRunTimeSeconds - (RunTimeMinutes * 60) ))
echo "100"
echo "# Auto-DIG has finished running at ${currentDayTime}. It took $RunTimeMinutes minutes and $RunTimeSecondsRemainder seconds. Not bad!"
) |
zenity --progress \
  --title="${titleOfProgram[@]}" \
  --text="Initializing parameters..." \
  --percentage=0 \
  --width=350 \
  --pulsate
