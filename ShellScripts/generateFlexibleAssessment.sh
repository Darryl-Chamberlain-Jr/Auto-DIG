source /${DIR}/ShellScripts/./functionsForZenityScript.sh
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
