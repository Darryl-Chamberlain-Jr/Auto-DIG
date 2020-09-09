source /${DIR}/ShellScripts/./functionsForZenityScript.sh
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
defineAllQuestionsDynamically
flexibleQuestionList=$(
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
escape=$?
checkForEscape $escape
question_list=(`echo ${flexibleQuestionList}`)
exam_display_name=$(zenity \
    --title="${titleOfProgram[@]}" \
    --entry \
    --text 'What do you want to call your assessment?'
)
escape=$?
checkForEscape $escape
file_name=$(zenity \
    --title="${titleOfProgram[@]}" \
    --entry \
    --text 'Give a short, NO SPACES, name to your assessment.'
)
escape=$?
checkForEscape $escape
list_of_assessment_titles=( $file_name )
