DIR="home/dchamberlain31/git-repos/Auto-DIG"
titleOfProgram="Auto-DIG v.0.2"
###########################################
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
footnote_right="Fall 2020"
db_name="$(( 1000 + RANDOM % 9000 ))-$(( 1000 + RANDOM % 9000 ))"
#db_name="1269-8776"
footnote_left=$db_name
number_of_versions=3
version_list=( "A" "B" "C" )
question_list_0=( "divideComplex" "multiplyComplex" "orderOfOperations" "subgroupComplex" "subgroupReal" "divideComplexCopy" "multiplyComplexCopy" "orderOfOperationsCopy" "subgroupComplexCopy" "subgroupRealCopy" )
question_list_1=( "linearGraphToStandard" "linearParOrPer" "linearTwoPoints" "solveIntegerLinear" "solveLinearRational" "linearGraphToStandardCopy" "linearParOrPerCopy" "linearTwoPointsCopy" "solveIntegerLinearCopy" "solveLinearRationalCopy" )
list_of_assessment_titles=( "Progress Quiz 2" "Progress Quiz 2" )
number_of_assessments=${#list_of_assessment_titles[@]}
list_of_file_names=( "Module1" "Module2" )
number_of_questions=20
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
        echo "#This is the question list name: ${question_list_name}"; sleep 3
        eval question_list=( \"\${question_list_${index}[@]}\" )
        echo "#This is the question list: ${question_list[@]}"; sleep 3
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
