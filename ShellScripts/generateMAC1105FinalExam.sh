source /${DIR}/ShellScripts/./functionsForZenityScript.sh
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
