source /${DIR}/ShellScripts/./functionsForZenityScript.sh

number_of_assessments=$(zenity \
    --title="${titleOfProgram[@]}" \
    --scale \
    --text="How many assessments do you want to create?" \
    --value=1 \
    --min-value=1 \
    --max-value=30 \
    --step=1
)
escape=$?
number_of_questions=0
checkForEscape $escape
for ((index=0;index<number_of_assessments;index++))
do
    # Zenity - NAME YOUR ASSESSMENT - exam_display_name
    exam_display_name=$(zenity \
        --title="${titleOfProgram[@]}" \
        --entry \
        --text 'What do you want to call this assessment?'
    )
    escape=$?
    checkForEscape $escape
    # Zenity - SHORT FILE NAME - file_name
    file_name=$(zenity \
        --title="${titleOfProgram[@]}" \
        --entry \
        --text 'Give a short, NO SPACES, name to your assessment.'
    )
    escape=$?
    checkForEscape $escape
    question_list_name="question_list_${index}"
    # Zenity - CHOOSE YOUR QUESTIONS - question_list_index
    defineAllQuestionsDynamically
    temp_question_list=$(
    for i in $(seq 0 $((  Length - 1 )) )
    do
        echo "FALSE"
        echo ${CodeNames[i]}
        echo ${ObjectiveNumber[i]}
        echo ${ShortDescription[i]}
        echo ${LongDescription[i]}
        echo ${Notes[i]}
        echo ${Author[i]}
        echo ${Date[i]}
    done | zenity \
    --title="Auto-DIG v.0.2" \
    --height=600 \
    --width=1000 \
    --list \
    --checklist \
    --separator=" " \
    --multiple \
    --text '<b> Which questions would you like to include?</b>' \
    --column 'Choose' --column 'File name' --column 'Obj. #' --column 'Short Description' --column 'Long Description' --column 'Notes' --column 'Author' --column 'Date'
    )
    checkForEscape $?
    eval "question_list_${index}=( ${temp_question_list[@]} )"
    # APPEND ASSESSMENT NAME TO list_of_assessment_titles
    list_of_assessment_titles=( "${list_of_assessment_titles[@]}" "${exam_display_name}" )
    # APPEND SHORT FILE NAME TO list_of_file_names
    list_of_file_names=( "${list_of_file_names[@]}" "$file_name" )
    number_of_questions=$(( number_of_questions + ${#temp_question_list[@]} ))
done
