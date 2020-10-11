DIR="home/dchamberlain31/git-repos/Auto-DIG"
titleOfProgram="Auto-DIG v.0.2"
# cd to ShellScripts included to make python graphing work. Not sure why at this point.
cd /$DIR/ShellScripts/
###########################################
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
#eog --fullscreen /${DIR}/ImagesForApp/NewAutoDIGimage.png & espeak "Initiating diagnostic procedures" && pkill eog
eog --fullscreen /${DIR}/ImagesForApp/NewAutoDIGimage.png & sleep 1 && espeak "Welcome back doctor" & sleep 5 && espeak "Initiating diagnostic procedures" && pkill eog
eog --fullscreen /${DIR}/ImagesForApp/Auto-DIG_background.jpg </dev/null &>/dev/null &
sleep 3
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
    )
    checkForEscape $?
    footnote_right=$(zenity \
        --title="${titleOfProgram[@]}" \
        --entry \
        --text 'What do you want to print on the bottom-right of the page?'
    )
    escape=$?
    checkForEscape $escape
    db_name="$(( 1000 + RANDOM % 9000 ))-$(( 1000 + RANDOM % 9000 ))"
    footnote_left=$db_name
    #zenity \
    #    --title="${titleOfProgram[@]}" \
    #    --height=100 \
    #    --width=400 \
    #    --info \
    #    --text="You have been assigned ${db_name}. You'll need this to provide students specific feedback. Don't worry - it will be printed on each pdf."
    #escape=$?
    #checkForEscape $escape
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
    estimated_run_time=$( echo "scale=2;(5.5*$number_of_questions*$number_of_versions)/60" | bc )
    (
    # Clears old keys and pdfs
    rm -rf /${DIR}/Keys/*
    rm -rf /${DIR}/BuildExams/*
    # Estimated run time calculated as 5 seconds per question, with 1 error per 10 questions run.
    echo "#Estimated run time for ${number_of_questions} questions and ${number_of_versions} version: ${estimated_run_time} minutes"; sleep 3
    question_step=$( echo "scale=2;100/ ($number_of_questions*$number_of_versions)" | bc )
    counter=0
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
        # Shuffled and used in the same order for each version to make data analysis easier.
        question_list=( $(shuf -e "${question_list[@]}") )
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
            cp lettersAnswerKey${file_name}${version}.csv /$DIR/CompleteExam/"$exam_display_name"/Keys
            cp key${file_name}${version}.tex /$DIR/CompleteExam/"$exam_display_name"/TeXs
        done
        cd /$DIR/ShellScripts/
        for version in ${version_list[@]}
            full_db_name="$db_name-Ver$version"
            mv /$DIR/Databases/${full_db_name}.db /$DIR/CompleteExam/"$exam_display_name"/Databases
        cp -r /$DIR/Figures/. /$DIR/CompleteExam/"$exam_display_name"/Figures
    done
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
    # DO NOT USE AUTO-CLOSE! There is currently an echo somewhere with a value over 100, which is signaling zenity to close the process early while the process wants to continue, causing a broken pipe.
    checkForEscape $?
    EndTime=$( date +'%s' )
    currentDayTime=$( date +'%H:%M on %m/%d/%Y' )
    TotalRunTimeSeconds=$(( EndTime-StartTime ))
    RunTimeMinutes=$(( (EndTime-StartTime) / 60 ))
    RunTimeSecondsRemainder=$(( TotalRunTimeSeconds-(RunTimeMinutes*60) ))
    estimated_run_time_seconds_float=$( echo "scale=0;(60*$estimated_run_time)" | bc )
    estimated_run_time_seconds=${estimated_run_time_seconds_float%.*}
    #off_by_seconds=$( echo "scale=0;($estimate_run_time_seconds-$TotalRunTimeSeconds)" | bc )
    off_by_seconds=$(( estimated_run_time_seconds-TotalRunTimeSeconds ))
    zenity \
        --title="${titleOfProgram[@]}" \
        --height=100 \
        --width=400 \
        --info \
        --text="Auto-DIG has finished running at ${currentDayTime}. It took ${RunTimeMinutes} minutes and ${RunTimeSecondsRemainder} seconds. We estimated it would take ${estimated_run_time} minutes so our estimate was off by ${off_by_seconds} seconds."
done
pkill eog
