# Manually define directory to root of git repo
DIR="home/dchamberlain31/git-repos/Auto-DIG"

# cd to ShellScripts included to make python graphing work. Not sure why at this point.
cd /$DIR/ShellScripts/
# Defines a randomly generated 8-digit database name. Used to save all question data for exam generation and future retrieval. Printed with the pdfs in the bottom-left corner.
db_name="$(( 1000 + RANDOM % 9000 ))-$(( 1000 + RANDOM % 9000 ))"
footnote_left=$db_name
# Statically defined variables. These were previously dynamically defined with Zenity.
footnote_right="Minimal test"
number_of_versions=3
version_list=( "A" "B" "C" )
number_of_assessments=1
number_of_questions=2
exam_display_name="Testing Minimal Auto-DIG"
file_name="min"
question_list=( "divideComplex" "quadraticEquationToGraph" )
question_list_name="question_list_0"
###
# BEGINING OLD ZENITY PIPE #
# Clears old keys and pdfs
rm -rf /${DIR}/Keys/*
rm -rf /${DIR}/BuildExams/*
completed_directory_root="/$DIR/CompleteExam/${exam_display_name}"
if [ ! -d "$completed_directory_root" ]; then
    mkdir "$completed_directory_root"
    mkdir "$completed_directory_root"/PDFs
    mkdir "$completed_directory_root"/Keys
    mkdir "$completed_directory_root"/TeXs
    mkdir "$completed_directory_root"/Databases
    mkdir "$completed_directory_root"/Figures
fi
# Suffles question list
question_list=( $(shuf -e "${question_list[@]}") )
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
            if [ $question == "divideComplex" ]; then
                code_folder="Core"
                code_subfolder="01realComplex"
            else
                code_folder="Core"
                code_subfolder="04quadratic"
            fi
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

# ENDS old zenity pipe to create assessments.
