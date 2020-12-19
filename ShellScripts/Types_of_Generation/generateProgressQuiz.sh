DIR="home/dchamberlain31/git-repos/Auto-DIG"
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
# NEED TO DEFINE
    # number_of_assessments
    # number_of_questions
    # exam_display_name
    # question_list_${index}
    # list_of_assessment_titles
    # list_of_file_names

## Determine Progress Quiz number
choose_quiz_number=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=400 \
    --list \
    --text '<b>Which quiz do you want to create?</b>
    The quiz number will be printed at the top of each PDF.' \
    --column 'Quiz Number' \
    "1 - This creates Modules 1-2." \
    "2 - This creates Modules 1-4." \
    "3 - This creates Modules 1-6" \
    "Makeup 1 - This creates Modules 1-8." \
    "4 - This creates Modules 1-8, 9M-10M, and 9L-10L" \
    "5 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "6 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "Makeup 2 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "7 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "8 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "9 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "Makeup 3 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "10 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
)
escape=$?
checkForEscape $escape
if [ "$choose_quiz_number" == "10 - This creates Modules 1-8, 9M-12M, and 9L-12L" ]; then
    quiz_number=10
elif [ "$choose_quiz_number" == "Makeup 1 - This creates Modules 1-8." ]; then
    quiz_number=11
elif [ "$choose_quiz_number" == "Makeup 2 - This creates Modules 1-8, 9M-12M, and 9L-12L" ]; then
    quiz_number=12
elif [ "$choose_quiz_number" == "Makeup 3 - This creates Modules 1-8, 9M-12M, and 9L-12L" ]; then
    quiz_number=13
else
    quiz_number=$(( ${choose_quiz_number:0:1} ))
fi
if [ $quiz_number -lt 11 ]; then
    exam_display_name="Progress Quiz ${quiz_number}"
else
    makeup_number=$(( $quiz_number-10 ))
    exam_display_name="Makeup Progress Quiz ${makeup_number}"
fi
question_list_by_module
if [ $quiz_number -eq 1 ]; then
    module_names=( "1" "2" )
    number_of_assessments=${#module_names[@]}
    number_of_questions=$(( 10 * ${#module_names[@]} ))
    list_of_assessment_titles=( "${exam_display_name}" "${exam_display_name}" )
    list_of_file_names=( "Module1" "Module2")
elif [ $quiz_number -eq 2 ]; then
    module_names=( "1" "2" "3" "4" )
    number_of_assessments=${#module_names[@]}
    number_of_questions=$(( 10 * ${#module_names[@]} ))
    list_of_assessment_titles=( "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}")
    list_of_file_names=( "Module1" "Module2" "Module3" "Module4")
elif [ $quiz_number -eq 3 ]; then
    module_names=( "1" "2" "3" "4" "5" "6")
    number_of_assessments=${#module_names[@]}
    number_of_questions=$(( 10 * ${#module_names[@]} ))
    list_of_assessment_titles=( "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}")
    list_of_file_names=( "Module1" "Module2" "Module3" "Module4" "Module5" "Module6")
elif [ $quiz_number -eq 11 ]; then
    module_names=( "1" "2" "3" "4" "5" "6" "7" "8")
    number_of_assessments=${#module_names[@]}
    number_of_questions=$(( 10 * ${#module_names[@]} ))
    list_of_assessment_titles=( "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}")
    list_of_file_names=( "Module1" "Module2" "Module3" "Module4" "Module5" "Module6" "Module7" "Module8")
elif [ $quiz_number -eq 4 ]; then
    module_names=( "1" "2" "3" "4" "5" "6" "7" "8" "9M" "10M" "9L" "10L")
    number_of_assessments=${#module_names[@]}
    number_of_questions=$(( 10 * ${#module_names[@]} ))
    list_of_assessment_titles=( "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}")
    list_of_file_names=( "Module1" "Module2" "Module3" "Module4" "Module5" "Module6" "Module7" "Module8" "Module9M" "Module10M" "Module9L" "Module10L")
else
    module_names=( "1" "2" "3" "4" "5" "6" "7" "8" "9M" "10M" "11M" "12M" "9L" "10L" "11L" "12L")
    number_of_assessments=${#module_names[@]}
    number_of_questions=$(( 10 * ${#module_names[@]} ))
    list_of_assessment_titles=( "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}" "${exam_display_name}")
    list_of_file_names=( "Module1" "Module2" "Module3" "Module4" "Module5" "Module6" "Module7" "Module8" "Module9M" "Module10M" "Module11M" "Module12M" "Module9L" "Module10L" "Module11L" "Module12L")
fi
#####
# Defines the question_list_index needed for the modules.
index=0
for module in ${module_names[@]}
do
    eval "question_list_${index}=( \"\${module${module}questionList[@]}\" )"
    index=$(( index+1 ))
done
