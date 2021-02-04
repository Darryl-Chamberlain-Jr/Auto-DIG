DIR="home/dchamberlain31/git-repos/Auto-DIG"
titleOfProgram="Auto-DIG v.0.3"
# cd to ShellScripts included to make python graphing work. Not sure why at this point.
cd /$DIR/ShellScripts/

### BEGIN DEFINING ALL FUNCTIONS ###
# function checkForEscape determines whether the user canceled rather than answered a prompt or canceled while the exam was generating.
function checkForEscape {
    escape=$1
    if [ $escape -eq 1 ]; then
    zenity \
        --error \
        --height=100 \
        --width=200 \
        --text="You canceled the assessment generation early."
    pkill eog
    exit 0
    fi
}
# Used when creating a flexible assessment. Converts master database info to be displayed for the user using zenity.
function defineAllQuestionsDynamically {
    OIFS=$IFS;
    IFS=";";
    Length=$(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Length" $DIR)
    CodeNames=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Code Name" $DIR))
    Folder=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Folder" $DIR))
    Subfolder=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Subfolder" $DIR))
    TopicNumber=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Topic Number" $DIR))
    ObjectiveNumber=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Objective Number" $DIR))
    Topic=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Topic" $DIR))
    ShortDescription=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Short Description" $DIR))
    LongDescription=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Long Description" $DIR))
    Notes=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Notes" $DIR))
    Author=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Author" $DIR))
    Date=($(python3 /${DIR}/PythonScripts/return_all_values_of_key.py "Date" $DIR))
    IFS=$OIFS
}
### END DEFINING ALL FUNCTIONS ###

# Keeps program running until the user exists.
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
        "Exit the program"
    )
    checkForEscape $?
    # Allows user to end program.
    if [ "$typeOfGeneration" == "Exit the program" ]; then
        zenity --info --width=200 --title="${titleOfProgram[@]}" --text="Exiting now. Have a great day!"
        break
    fi
    # Currently used to denote the semester the exam is taking place in. Flexible to print anything the user wants in the bottom-right of the page. Can take spaces.
    footnote_right=$(zenity \
        --title="${titleOfProgram[@]}" \
        --entry \
        --text 'What do you want to print on the bottom-right of the page?'
    )
    checkForEscape $?
    # Defines a randomly generated 8-digit database name. Used to save all question data for exam generation and future retrieval. Printed with the pdfs in the bottom-left corner.
    db_name="$(( 1000 + RANDOM % 9000 ))-$(( 1000 + RANDOM % 9000 ))"
    footnote_left=$db_name
    # Asks user how many versions they would like to create. Currently defaults to 3 with a slider between 1 and 26.
    number_of_versions=$(zenity \
        --title="${titleOfProgram[@]}" \
        --scale \
        --text="How many versions do you want to create?" \
        --value=3 \
        --min-value=1 \
        --max-value=26 \
        --step=1
    )
    checkForEscape $?
    # Converts ${number_of_versions} to an array of version letters.
    fullVersionList=( "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")
    version_counter=0
    version_list=()
    while [ $version_counter -lt $number_of_versions ]
    do
        version_list=( "${version_list[@]}" "${fullVersionList[$version_counter]}" )
        version_counter=$(( version_counter+1 ))
    done
    # Takes user input to either generate a preset assessment or prompts the user toward creating an assessment of their creation.
    number_of_assessments=$(zenity \
        --title="${titleOfProgram[@]}" \
        --scale \
        --text="How many assessments do you want to create?" \
        --value=1 \
        --min-value=1 \
        --max-value=30 \
        --step=1
    )
    checkForEscape $?
    number_of_questions=0
    for ((index=0;index<number_of_assessments;index++))
    do
        # Zenity - NAME YOUR ASSESSMENT - exam_display_name
        exam_display_name=$(zenity \
            --title="${titleOfProgram[@]}" \
            --entry \
            --text 'What do you want to call this assessment?'
        )
        checkForEscape $?
        # Zenity - SHORT FILE NAME - file_name
        file_name=$(zenity \
            --title="${titleOfProgram[@]}" \
            --entry \
            --text 'Give a short, NO SPACES, name to your assessment.'
        )
        checkForEscape $?
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
    # BEGINS zenity pipe to create assessments.
    (
    # Clears old keys and pdfs
    rm -rf /${DIR}/Keys/*
    rm -rf /${DIR}/BuildExams/*
    # ${question_step} defines the step used in the progress bar display. Increases step after each question data is saved in the database.
    question_step=$( echo "scale=2;100/ ($number_of_questions*$number_of_versions)" | bc )
    # ${counter} to track progress bar. Starts at 0 and increases by question_step.
    counter=0
    # Initizaling arrays to be used later.
    question_list_name_array=()
    code_name_array=()
    # ${number_of_assessments} is defined in the specific .sh based on what type of assessment the user chooses. If assessments are supposed to have different names [like creating numerous 10-questions per module], each has a separate name.
    for ((index=0;index<number_of_assessments;index++))
    do
        # ${exam_display_name} is used in naming a single or collection of assessments. Currently used to create the folder all files are placed in as well. ${completed_directory_root} creates this directory or points to this folder (if it was created in a previous step of this for loop).
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
        # ${file_name} of the single pdf
        file_name=${list_of_file_names[index]}
        # ${question_list_${index}} is defined in previous .sh files based on what type of assessment the user chooses. Defined dynamically using ${module${number}questionList} that are defined statically in functionsForZenityScript.sh.
        question_list_name="question_list_${index}"
        # Defines question_list elements dynamically based on ${question_list_${index}}.
        eval question_list=( \"\${question_list_${index}[@]}\" )
        # Creates array to associate each code_name with the correct question_list name for database recovery.
        for question in ${question_list[@]}
        do
            question_list_name_array=( ${question_list_name_array[@]} ${question_list_name} )
        done
        # Shuffled and used in the same order for each version to make data analysis easier.
        question_list=( $(shuf -e "${question_list[@]}") )
        # Creates master code_name array. Used later to create for loop to generate and save each question to the database.
        code_name_array=( ${code_name_array[@]} ${question_list[@]} )
        # For loop to create and save questions per version. Each version has its own database.
        for version in ${version_list[@]}
        do
            # Name for the database based on the version of the exam. This can later be collapsed into a single database but was easier to separate for now.
            full_db_name="$db_name-Ver$version"
            # Python script to create .tex file portions depending on the phrase declaration.
            python3 /$DIR/PythonScripts/createFiles.py "Create Exam File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            python3 /$DIR/PythonScripts/createFiles.py "Create Key File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            # for loop to create and save question data.
            for question in ${question_list[@]}
            do
                # Both echos are to show the user the current progress and announce the specific question/version that is being generated.
                echo "$counter"
                echo "#Running '${question}' for Version ${version}."
                # Defines name of python script to be called later. Saves all metadata for question to the new database ${full_db_name}.
                run_save_metadata="/$DIR/PythonScripts/saveMetadataToNewDatabase.py"
                # Unclear why this is needed. Will need to investigate. saveMetadataToNewDatabase.py uses absolute calls.
                cd /$DIR/Code
                python3 $run_save_metadata $DIR $question "$full_db_name" $question_list_name
                # Defines two variables for the next while loop. ${return_error} is set to 1 as no errors. Defined in while loop as error return after running python script for a question. ${error_counter} announces to the user how many times the code has needed to rerun.
                return_error=1
                error_counter=0
                # While loop that runs python script for a specific question until it runs without error. Notifies the user each time an error occurs and how many times it has attempted to run the python script.
                while [ $return_error -ne 0 ]
                do
                    if [ $error_counter -ne 0 ]; then
                        echo "#An error occured while running ${question} for version ${version}. Don't worry - we will continue to try again. Attempt: ${error_counter}"
                    fi
                    # This python script is used to dynamically define the corresponding folder and subfolder the code is housed in based on a question's metadata.
                    run_return_key_value_from_db="/$DIR/PythonScripts/return_key_value_from_db.py"
                    code_folder=$( python3 $run_return_key_value_from_db $DIR $full_db_name $question_list_name $question "Folder" )
                    code_subfolder=$( python3 $run_return_key_value_from_db $DIR $full_db_name $question_list_name $question "Subfolder" )
                    # Easier-to-read script name.
                    question_py="/$DIR/Code/$code_folder/$code_subfolder/$question.py"
                    # Actual python script to generate and save question information to the corresponding database.
                    python3 $question_py $DIR $full_db_name $question_list_name $version $question
                    return_error=$?
                    error_counter=$(( error_counter+1 ))
                done # Question data has now been saved with the metadata.

                # Python script to import question data saved in the database into a latex file.
                python3 /$DIR/PythonScripts/printQuestions.py "Print questions to exam" $DIR $file_name $full_db_name $question_list_name $question $version
                python3 /$DIR/PythonScripts/printQuestions.py "Print questions to key" $DIR $file_name $full_db_name $question_list_name $question $version
                # Increments the ${counter} by ${question_step} to display progress to user.
                counter=$( echo "scale=2;$counter+$question_step" | bc )
            done

            # Python script to cap latex files.
            python3 /$DIR/PythonScripts/createFiles.py "Finish Exam File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            python3 /$DIR/PythonScripts/createFiles.py "Finish Key File" $file_name "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR

            # Points to where latex files will be built. This keeps aux latex files separate from .tex and .pdfs associated to the assessment.
            cd /$DIR/BuildExams/

            # While the pdf is not built, run pdflatex. Unclear whether this is needed anymore, but was useful in forcing files that would not compile on the first try but would a subsequent time.
            while [[ ! -f ${file_name}${version}.pdf ]]
            do
                pdflatex -synctex=1 -interaction=nonstopmode ${file_name}${version}.tex
            done

            # Copies pdf and latex files into folders for the user.
            cp ${file_name}${version}.pdf /$DIR/CompleteExam/"$exam_display_name"/PDFs
            cp ${file_name}${version}.tex /$DIR/CompleteExam/"$exam_display_name"/TeXs

            # While the pdf of the key is not built, run pdflatex. Again unclear if this is needed anymore.
            cd /$DIR/Keys/
            while [[ ! -f key${file_name}${version}.pdf ]]
            do
                pdflatex -synctex=1 -interaction=nonstopmode key${file_name}${version}.tex
            done

            # Copies pdfs and latex files into folders for the user.
            cp key${file_name}${version}.pdf /$DIR/CompleteExam/"$exam_display_name"/Keys
            cp key${file_name}${version}.tex /$DIR/CompleteExam/"$exam_display_name"/TeXs
        done
    done
    # Creates master key which includes ALL answers for ALL versions. Order of question structures was kept static earlier to ensure question structures for each version correspond by number.
    python3 /$DIR/PythonScripts/create_grading_CSVs.py $DIR $db_name ${#version_list[@]} "${version_list[@]}" ${#code_name_array[@]} "${code_name_array[@]}" "${question_list_name_array[@]}"
    # Copies master key to the keys folder for the user.
    cp -r /$DIR/Keys/master_key_${db_name}.csv /$DIR/CompleteExam/"$exam_display_name"/Keys

    # Returns to pointing to the ShellScripts folder. Unclear why this is necessary when all calls are by absolute directory.
    cd /$DIR/ShellScripts/

    # Moves all databases to a folder for the user.
    for version in ${version_list[@]}
    do
        full_db_name="${db_name}-Ver${version}"
        mv /$DIR/Databases/${full_db_name}.db /$DIR/CompleteExam/"$exam_display_name"/Databases
    done

    # Indescriminately copies all figures currently in the figure folder. This is overkill and could be refined in the future.
    cp -r /$DIR/Figures/. /$DIR/CompleteExam/"$exam_display_name"/Figures

    # Final declaration to user that exam has been completed.
    xdg-open /${DIR}/CompleteExam/"$exam_display_name"; sleep 1
    echo "100"
    echo "#Done! Click 'Ok' to see the time results."
    ) |
    # ENDS zenity pipe to create assessments.
    zenity --progress \
      --title="${titleOfProgram[@]}" \
      --text="Initializing parameters..." \
      --percentage=0 \
      --width=350 \
    #  --auto-close
    # DO NOT USE AUTO-CLOSE! There is currently at least one echo somewhere with a value over 100, which is signaling zenity to close the process early while the process wants to continue, causing a broken pipe.
    checkForEscape $?
    # Alerts user to the amount of time that passed and how that compares with estimates.
    zenity \
        --title="${titleOfProgram[@]}" \
        --height=100 \
        --width=400 \
        --info \
        --text="Auto-DIG has finished running."
done
