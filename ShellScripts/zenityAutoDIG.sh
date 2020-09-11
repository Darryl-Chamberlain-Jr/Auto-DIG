DIR="home/dchamberlain31/git-repos/Auto-DIG"
titleOfProgram="Auto-DIG v.0.2"
###########################################
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
eog --fullscreen /${DIR}/ImagesForApp/NewAutoDIGimage.png & sleep 1 && espeak "Welcome back doctor" & sleep 3 && espeak "Initiating diagnostic procedures" && pkill eog
eog --fullscreen /${DIR}/ImagesForApp/Auto-DIG_background.jpg </dev/null &>/dev/null &
sleep 3
# Allows user to choose what type of assessment they want to generate. Uses preset question lists to create assessments.
typeOfGeneration=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=250 \
    --width=300 \
    --list \
    --text '<b> What do you want to do?</b>' \
    --column 'Generate...' \
    "One or more flexible assessments" \
    "A Progress Quiz" \
    "A Single Module" \
    "A MAC 1105 Final Exam" \
)
checkForEscape $?
#
footnote_right=$(zenity \
    --title="${titleOfProgram[@]}" \
    --entry \
    --text 'What do you want to print on the bottom-right of the page? I normally print the semester.'
)
escape=$?
checkForEscape $escape
db_name="$(( 1000 + RANDOM % 9000 ))-$(( 1000 + RANDOM % 9000 ))"
footnote_left=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=100 \
    --width=400 \
    --info \
    --text="You have been assigned ${db_name}. You'll need this to provide students specific feedback. Don't worry - it will be printed on each pdf."
)
escape=$?
checkForEscape $escape
number_of_versions=$(zenity \
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
###
if [ "$typeOfGeneration" == "A Progress Quiz" ]; then
    source /${DIR}/ShellScripts/Types_of_Generation/./generateProgressQuiz.sh
elif [ "$typeOfGeneration" == "A Single Module" ]; then
    source /${DIR}/ShellScripts/Types_of_Generation/./generateSingleModule.sh
elif [ "$typeOfGeneration" == "A MAC 1105 Final Exam" ]; then
    source /${DIR}/ShellScripts/Types_of_Generation/./generateMAC1105FinalExam.sh
elif [ "$typeOfGeneration" == "One or more flexible assessments" ]; then
    # Zenity - HOW MANY ASSESSMENTS?
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
        ### THIS IS UNTESTED
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
        eval "question_list_${index}=( ${temp_question_list[@]} )"
        escape=$?
        zenity --question --text="Is this a complete list? ${question_list_0[@]}"
        checkForEscape $escape
        # APPEND ASSESSMENT NAME TO list_of_assessment_titles
        list_of_assessment_titles=( "${list_of_assessment_titles[@]}" "${exam_display_name}" )
        # APPEND SHORT FILE NAME TO list_of_file_names
        list_of_file_names=( "${list_of_file_names[@]}" "$file_name" )
        number_of_questions=$(( number_of_questions + ${#question_list_name[@]} ))
    done
fi
(
# Clears old keys and pdfs
rm -rf /${DIR}/Keys/*
rm -rf /${DIR}/BuildExams/*
StartTime=$( date +'%s' )
question_step=$(( 100 / (number_of_questions*number_of_versions) ))
counter=0
while true
do
    for ((index=0;index<number_of_assessments;index++))
    do
        exam_display_name=${list_of_assessment_titles[index]}
        completed_directory_root="/$DIR/CompleteExam/${exam_display_name}"
        if [ ! -d "$completed_directory_root" ]
        then
            mkdir "$completed_directory_root"
            mkdir "$completed_directory_root"/PDFs
            mkdir "$completed_directory_root"/Keys
            mkdir "$completed_directory_root"/TeXs
            mkdir "$completed_directory_root"/Databases
        fi
        file_name=${list_of_file_names[index]}
        question_list_name="question_list_${index}"
        eval question_list=( \"\${question_list_${index}[@]}\" )
        for version in ${version_list[@]}
        do
            full_db_name="$db_name-Ver$version"
            echo "$counter" ; sleep 0
            counter=$(( counter+question_step ))
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Create Exam File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Create Key File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            for question in ${question_list[@]}
            do
                echo "$counter" ; sleep 0
                echo "#Running ${question} for version ${version}."
                run_save_metadata="/$DIR/PythonScripts/ScriptsForDatabases/saveMetadataToNewDatabase.py"
                python3 $run_save_metadata $DIR $question "$full_db_name" $question_list_name
                return_error=1
                error_counter=0
                while [ $return_error -ne 0 ]
                do
                    if [ $error_counter -ne 0 ]; then
                        echo "#An error occured while running ${question} for version ${version}. Don't worry - we will continue to try again. Attempt: ${error_counter}"
                    fi
                    run_return_key_value_from_db="/$DIR/PythonScripts/ScriptsForDatabases/return_key_value_from_db.py"
                    code_folder=$( python3 $run_return_key_value_from_db $DIR $full_db_name $question_list_name $question "Folder" )
                    code_subfolder=$( python3 $run_return_key_value_from_db $DIR $full_db_name $question_list_name $question "Subfolder" )
                    question_py="/$DIR/Code/$code_folder/$code_subfolder/$question.py"
                    python3 $question_py $DIR $full_db_name $question_list_name $version
                    # Question data has now been saved with the metadata.
                    return_error=$?
                    error_counter=$(( error_counter+1 ))
                python3 /$DIR/PythonScripts/ScriptsForPDFs/printQuestions.py "Print questions to exam" $DIR $file_name $full_db_name $question_list_name $question $version
                python3 /$DIR/PythonScripts/ScriptsForPDFs/printQuestions.py "Print questions to key" $DIR $file_name $full_db_name $question_list_name $question $version
                counter=$(( counter+question_step ))
                done
            done
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Finish Exam File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Finish Key File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            cd /$DIR/BuildExams/
            pdflatex -file-line-error -halt-on-error ${file_name}${version}.tex
            cp ${file_name}${version}.pdf /$DIR/CompleteExam/"$exam_display_name"/PDFs
            cp ${file_name}${version}.tex /$DIR/CompleteExam/"$exam_display_name"/TeXs
            cd /$DIR/Keys/
            pdflatex -file-line-error -halt-on-error key${file_name}${version}.tex
            cp key${file_name}${version}.pdf /$DIR/CompleteExam/"$exam_display_name"/Keys
            cp key${file_name}${version}.tex /$DIR/CompleteExam/"$exam_display_name"/TeXs
            cd /$DIR/ShellScripts/
            cp /$DIR/Databases/${full_db_name} /$DIR/CompleteExam/"$exam_display_name"/Databases
        done
    done
    break
done
xdg-open /${DIR}/CompleteExam/"$exam_display_name"
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
  --width=350
checkForEscape $?
pkill eog
