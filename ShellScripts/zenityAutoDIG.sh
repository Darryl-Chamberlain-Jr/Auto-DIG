DIR="home/pi/git-repos/Auto-DIG"
titleOfProgram="Auto-DIG v.0.3"
# Create a fresh questionMetadata.db
rm /$DIR/Databases/questionMetadata.db
python3 /$DIR/PythonScripts/ScriptsForDatabases/store_original_metadata.py $DIR
python3 /$DIR/PythonScripts/ScriptsForDatabases/store_copy_metadata.py $DIR
# cd to ShellScripts included to make python graphing work. Not sure why at this point.
cd /$DIR/ShellScripts/
###
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
while true
do
    # Allows user to choose what type of assessment they want to generate. Uses preset question lists to create assessments.
    typeOfGeneration=$(zenity \
        --title="${titleOfProgram[@]}" \
        --height=250 \
        --width=300 \
        --list \
        --text '<b> What do you want to do?</b>' \
        --column 'Generate...' \
        "One or more flexible assessments" \
        "MAC 1105 progress quiz" \
        "MAC 1105 single module" \
        "MAC 1105 final exam" \
        "Exit the program"
    )
    checkForEscape $?
    if [ "$typeOfGeneration" == "Exit the program" ]; then
        zenity --info --width=200 --title="${titleOfProgram[@]}" --text="Exiting now. Have a great day!"
        break
    fi
    footnote_right=$(zenity \
        --title="${titleOfProgram[@]}" \
        --entry \
        --text 'What do you want to print on the bottom-right of the page?'
    )
    escape=$?
    checkForEscape $escape
    db_name="$(( 1000 + RANDOM % 9000 ))-$(( 1000 + RANDOM % 9000 ))"
    footnote_left=$db_name
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
    if [ "$typeOfGeneration" == "MAC 1105 progress quiz" ]; then
        source /${DIR}/ShellScripts/Types_of_Generation/./generateProgressQuiz.sh
    elif [ "$typeOfGeneration" == "MAC 1105 single module" ]; then
        source /${DIR}/ShellScripts/Types_of_Generation/./generateSingleModule.sh
    elif [ "$typeOfGeneration" == "MAC 1105 final exam" ]; then
        source /${DIR}/ShellScripts/Types_of_Generation/./generateMAC1105FinalExam.sh
    elif [ "$typeOfGeneration" == "One or more flexible assessments" ]; then
        source /${DIR}/ShellScripts/Types_of_Generation/./generateFlexibleAssessment.sh
    fi
    StartTime=$( date +'%s' )
    # Estimated run time calculated as 5 seconds per question, with 1 error per 10 questions run.
    estimated_run_time=$( echo "scale=2;(5.5*$number_of_questions*$number_of_versions)/60" | bc )
    (
    # Clears old keys and pdfs
    rm -rf /${DIR}/Keys/*
    rm -rf /${DIR}/BuildExams/*
    echo "#Estimated run time for ${number_of_questions} questions and ${number_of_versions} version: ${estimated_run_time} minutes"; sleep 3
    question_step=$( echo "scale=2;100/ ($number_of_questions*$number_of_versions)" | bc )
    counter=0
    question_list_name_array=()
    code_name_array=()
    for ((index=0;index<number_of_assessments;index++))
    do
        exam_display_name=${list_of_assessment_titles[index]}
        completed_directory_root="/$DIR/CompleteExam/${exam_display_name}"
        if [ ! -d "$completed_directory_root" ]; then
            mkdir "$completed_directory_root"
            mkdir "$completed_directory_root"/PDFs
            mkdir "$completed_directory_root"/Keys
            mkdir "$completed_directory_root"/TeXs
            mkdir "$completed_directory_root"/Databases
            mkdir "$completed_directory_root"/Figures
        fi
        file_name=${list_of_file_names[index]}
        question_list_name="question_list_${index}"
        eval question_list=( \"\${question_list_${index}[@]}\" )
        # Creates array to associate each code_name with the correct question_list name for database recovery.
        for question in ${question_list[@]}
        do
            question_list_name_array=( ${question_list_name_array[@]} ${question_list_name} )
        done
        # Shuffled and used in the same order for each version to make data analysis easier.
        question_list=( $(shuf -e "${question_list[@]}") )
        # Creates master code_name array.
        code_name_array=( ${code_name_array[@]} ${question_list[@]} )
        for version in ${version_list[@]}
        do
            full_db_name="$db_name-Ver$version"
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Create Exam File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Create Key File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            for question in ${question_list[@]}
            do
                echo "$counter"
                echo "#Running '${question}' for Version ${version}."
                run_save_metadata="/$DIR/PythonScripts/ScriptsForDatabases/saveMetadataToNewDatabase.py"
                cd /$DIR/Code
                python3 $run_save_metadata "save" $DIR $question "$full_db_name" $question_list_name
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
                    python3 $question_py $DIR $full_db_name $question_list_name $version $question
                    return_error=$?
                    error_counter=$(( error_counter+1 ))
                done
                # Question data has now been saved with the metadata.
                python3 /$DIR/PythonScripts/ScriptsForPDFs/printQuestions.py "Print questions to exam" $DIR $file_name $full_db_name $question_list_name $question $version
                python3 /$DIR/PythonScripts/ScriptsForPDFs/printQuestions.py "Print questions to key" $DIR $file_name $full_db_name $question_list_name $question $version
                counter=$( echo "scale=2;$counter+$question_step" | bc )
                #counter=$(( counter+question_step ))
            done
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Finish Exam File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Finish Key File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            cd /$DIR/BuildExams/
            #pdflatex -file-line-error -halt-on-error ${file_name}${version}.tex
            while [[ ! -f ${file_name}${version}.pdf ]]
            do
                pdflatex -synctex=1 -interaction=nonstopmode ${file_name}${version}.tex
            done
            cp ${file_name}${version}.pdf /$DIR/CompleteExam/"$exam_display_name"/PDFs
            cp ${file_name}${version}.tex /$DIR/CompleteExam/"$exam_display_name"/TeXs
            cd /$DIR/Keys/
            while [[ ! -f key${file_name}${version}.pdf ]]
            do
                pdflatex -synctex=1 -interaction=nonstopmode key${file_name}${version}.tex
            done
            cp key${file_name}${version}.pdf /$DIR/CompleteExam/"$exam_display_name"/Keys
            #cp lettersAnswerKey${file_name}${version}.csv /$DIR/CompleteExam/"$exam_display_name"/Keys
            cp key${file_name}${version}.tex /$DIR/CompleteExam/"$exam_display_name"/TeXs
        done
    done
    # Create master key
    python3 /$DIR/PythonScripts/ScriptsForCSVs/create_grading_CSVs.py $DIR $db_name ${#version_list[@]} "${version_list[@]}" ${#code_name_array[@]} "${code_name_array[@]}" "${question_list_name_array[@]}"
    cp -r /$DIR/Keys/master_key_${db_name}.csv /$DIR/CompleteExam/"$exam_display_name"/Keys
    cd /$DIR/ShellScripts/
    for version in ${version_list[@]}
    do
        full_db_name="${db_name}-Ver${version}"
        mv /$DIR/Databases/${full_db_name}.db /$DIR/CompleteExam/"$exam_display_name"/Databases
    done
    cp -r /$DIR/Figures/. /$DIR/CompleteExam/"$exam_display_name"/Figures
    xdg-open /${DIR}/CompleteExam/"$exam_display_name"; sleep 3
    echo "100"
    echo "#Done! Click 'Ok' to see the time results."
    ) |
    zenity --progress \
      --title="${titleOfProgram[@]}" \
      --text="Initializing parameters..." \
      --percentage=0 \
      --width=350 \
    #  --auto-close
    # DO NOT USE AUTO-CLOSE! There is currently at least one echo somewhere with a value over 100, which is signaling zenity to close the process early while the process wants to continue, causing a broken pipe.
    checkForEscape $?
    EndTime=$( date +'%s' )
    currentDayTime=$( date +'%H:%M on %m/%d/%Y' )
    TotalRunTimeSeconds=$(( EndTime-StartTime ))
    RunTimeMinutes=$(( (EndTime-StartTime) / 60 ))
    RunTimeSecondsRemainder=$(( TotalRunTimeSeconds-(RunTimeMinutes*60) ))
    estimated_run_time_seconds_float=$( echo "scale=0;(60*$estimated_run_time)" | bc )
    estimated_run_time_seconds=${estimated_run_time_seconds_float%.*}
    estimated_run_time_minutes=$(( (estimated_run_time_seconds) / 60 ))
    estimated_run_time_seconds_remainder=$(( estimated_run_time_seconds - (estimated_run_time_minutes*60) ))
    off_by_seconds=$(( estimated_run_time_seconds-TotalRunTimeSeconds ))
    if [[  $off_by_seconds -lt 0 ]]; then
        off_by_seconds=$(( -1*off_by_seconds ))
        over_or_under="over"
    else
        over_or_under="under"
    fi
    off_by_seconds_minutes=$(( (off_by_seconds) / 60 ))
    off_by_seconds_remainder=$(( off_by_seconds - (off_by_seconds_minutes*60) ))
    if [[ $off_by_seconds_minutes -eq 0 ]]; then
        comparison_statement="${off_by_seconds_remainder} seconds"
    else
        comparison_statement="${off_by_seconds_minutes} minutes and ${off_by_seconds_remainder} seconds"
    fi
    zenity \
        --title="${titleOfProgram[@]}" \
        --height=100 \
        --width=400 \
        --info \
        --text="Auto-DIG has finished running at ${currentDayTime}. It took ${RunTimeMinutes} minutes and ${RunTimeSecondsRemainder} seconds. We estimated it would take ${estimated_run_time_minutes} minutes and ${estimated_run_time_seconds_remainder} so our estimate was ${over_or_under} by ${comparison_statement}."
done
pkill eog
