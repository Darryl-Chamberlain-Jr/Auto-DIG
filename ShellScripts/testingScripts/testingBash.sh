titleOfProgram="Auto-DIG v.0.1"
source .././functionsForZenityAutoDIGshFile.sh

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
echo ${flexibleQuestionList[@]}
questionList=(`echo ${flexibleQuestionList}`)
echo ${questionList[@]}
echo ${questionList[0]}

# This currently saves it all as a single string in an array. It needs to be parsed out...
