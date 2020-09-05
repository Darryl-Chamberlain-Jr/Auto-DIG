titleOfProgram="Auto-DIG v.0.2"
###########################################
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
eog --fullscreen /${DIR}/ImagesForApp/tempStartupImage.jpg & sleep 3 && pkill eog
# Allows user to choose what type of assessment they want to generate. Uses preset question lists to create assessments.
typeOfGeneration=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=250 \
    --width=200 \
    --list \
    --text '<b> What do you want to do?</b>' \
    --column 'Generate...' \
    "A Progress Quiz" \
    "A Single Module" \
    "A MAC 1105 Final Exam" \
    "A Flexible Assessment"
)
escape=$?
checkForEscape $escape
#
footnoteRight=$(zenity \
    --title="${titleOfProgram[@]}" \
    --entry \
    --text 'What do you want to print on the bottom-right of the page?'
)
escape=$?
checkForEscape $escape
db_name="$(( 1000 + RANDOM % 9000 ))-$(( 1000 + RANDOM % 9000 ))"
footnoteLeft=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=100 \
    --width=400 \
    --info \
    --text="You have been assigned ${db_name}. You'll need this to provide students specific feedback."
)
escape=$?
checkForEscape $escape
numberOfVersions=$(zenity \
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
    source /${DIR}/ShellScripts/./generateProgressQuiz.sh
elif [ "$typeOfGeneration" == "A Single Module" ]; then
    source /${DIR}/ShellScripts/./generateSingleModule.sh
elif [ "$typeOfGeneration" == "A MAC 1105 Final Exam" ]; then
    source /${DIR}/ShellScripts/./generateMAC1105FinalExam.sh
elif [ "$typeOfGeneration" == "A Flexible Assessment" ]; then
    source /${DIR}/ShellScripts/./generateFlexibleAssessment.sh
fi
(
#clearOldVersions
StartTime=$( date +'%s' )
# question_step is= 50 / (#_of_questions)*(#_of_versions)
# generation_step is the total number of PDFs being created= 50 / (2*(#_of_assessments)*(#_of_versions))
counter=0
while :
### NEW DO ### FOR GENERATING PYTHON QUESTIONS
# With a defined list of assessment titles and list of questions to print per title
    # list_of_assessment_titles=( first_title second_title third_title ... )
    # question_list_1 = ( first_question_code ... )
        # 1 is associated to first title
END=${#list_of_assessment_titles[@]}
do
    for ((index=0;index<=END;index++)); do
        title=${list_of_assessment_titles[index]}
        question_list_name="title_$index"
        question_list="${!question_list_name}"
        for version in ${versionList[@]}; do
            echo "$counter" ; sleep 0
            for question in ${question_list}; do
                echo "Running ${question} for version ${version}."
                full_db_name="$db_name-Ver$version"
                echo $full_db_name
                run_save_metadata="/$DIR/PythonScripts/ScriptsForDatabases/saveMetadataToNewDatabase.py"
                echo $DIR
                echo $question
                echo $full_db_name
                echo $question_list_name
                python3 $run_save_metadata $DIR $question $full_db_name $question_list_name
                return_error=1
                while [ return_error -ne 0 ]; do
                    run_return_key_value_from_db="/$DIR/PythonScripts/ScriptsForDatabases/return_key_value_from_db.py"
                    code_folder=$( python3 $run_return_key_value_from_db $DIR $full_db_name $question_list_name $question "Folder" )
                    code_subfolder=$( python3 $run_return_key_value_from_db $DIR $full_db_name $question_list_name $question "Subfolder" )
                    question_py="/$DIR/Code/$code_folder/$code_subfolder/$question.py"
                    python3 $question_py $DIR $full_db_name $question_list_name
                    return_error=$?
                counter=$(( counter+question_step ))
            done
            # Generate student LaTeX file for title version
            # Run LaTeX file
            # Generate key LaTeX file for title verison
            # Run LaTeX file
            # Create folder for Master Assessment in CompleteExam
            # Copy PDFs to correct folders in CompleteExam/MasterAssessmentName
        done
    done
done
### NEW DONE ###
### OLD DO ###
#do
#    if [ "$typeOfGeneration" == "A Progress Quiz" ] || [ "$typeOfGeneration" == "A Single Module" ] ; then
#        for module in ${moduleList[@]}
#        do
#            presetQuestionList $module # This defines the question list for the module
#            fileNamePrefix="Module${module}"
#            for version in ${versionList[@]}
#            do
#                echo "$counter" ; sleep 0
#                generatePDFsAndKeys $fileNamePrefix "$examLongName" "$footnoteRight" $version
#                copyKeys $fileNamePrefix $version
#                counter=$(( counter+step ))
#            done
#        done
#    else
#        for version in ${versionList[@]}
#        do
#            echo "$counter" ; sleep 0
#            echo "# Creating "$examLongName" Version $version. Progress: $counter%"
#            generatePDFsAndKeys $fileNamePrefix "$examLongName" "$footnoteRight" $version
#            copyKeys $fileNamePrefix $version
#            counter=$(( counter+step ))
#        done
#    fi
#    break
#done
### OLD DONE ###
xdg-open /${DIR}/CompleteExam
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
  --width=350 \
  --pulsate
