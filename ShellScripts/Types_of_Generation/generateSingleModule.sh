#DIR="home/pi/git-repos/Auto-DIG"
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
# NEED TO DEFINE
    # number_of_assessments
    # number_of_questions
    # exam_display_name
    # question_list_name
    # question_list
    # list_of_assessment_titles
    # list_of_file_names

function moduleOptions {
    moduleOption1="Module 1 - Real and Complex Numbers"
    moduleOption2="Module 2 - Linear Functions"
    moduleOption3="Module 3 - Linear Inequalities"
    moduleOption4="Module 4 - Quadratic Functions"
    moduleOption5="Module 5 - Radical Functions"
    moduleOption6="Module 6 - Polynomial Functions"
    moduleOption7="Module 7 - Rational Functions"
    moduleOption8="Module 8 - Logarithmic and Exponential Functions"
    moduleOption9M="Module 9M - Modeling w/ Linear Functions"
    moduleOption10M="Module 10M - Modeling w/ Power Functions"
    moduleOption11M="Module 11M - Modeling w/ Log and Exp Functions"
    moduleOption12M="Module 12M - Solving Real-World Word Problems"
    moduleOption9L="Module 9L - Operations on Functions"
    moduleOption10L="Module 10L - Synthetic Division"
    moduleOption11L="Module 11L - Introduction to Limits"
    moduleOption12L="Module 12L - Graphing Rational Functions"
}
function defineSingleModule {
    if [ "$chooseModule" == "$moduleOption1" ] || [ "$chooseModule" == "$moduleOption2" ] || [ "$chooseModule" == "$moduleOption3" ] || [ "$chooseModule" == "$moduleOption4" ] || [ "$chooseModule" == "$moduleOption5" ] || [ "$chooseModule" == "$moduleOption6" ] || [ "$chooseModule" == "$moduleOption7" ] || [ "$chooseModule" == "$moduleOption8" ]; then
        singleModule=${chooseModule:7:1}
    elif [ "$chooseModule" == "$moduleOption9L" ] || [ "$chooseModule" == "$moduleOption9M" ]; then
        singleModule=${chooseModule:7:2}
    else
        singleModule=${chooseModule:7:3}
    fi
}
number_of_assessments=1
number_of_questions=10
moduleOptions
chooseModule=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=525 \
    --width=425 \
    --list \
    --text '<b>Which Module do you want to create?</b>' \
    --column 'Quiz Number' \
    "$moduleOption1" "$moduleOption2" "$moduleOption3" "$moduleOption4" "$moduleOption5" "$moduleOption6" "$moduleOption7" "$moduleOption8" "$moduleOption9M" "$moduleOption10M" "$moduleOption11M" "$moduleOption12M" "$moduleOption9L" "$moduleOption10L" "$moduleOption11L" "$moduleOption12L"
)
escape=$?
checkForEscape $escape
defineSingleModule ${chooseModule[@]}
exam_display_name="Quiz on Module ${singleModule}"
file_name="Module${singleModule}"
question_list_name=$file_name
question_list_by_module
eval question_list_0=( \"\${module${singleModule}questionList[@]}\" )
list_of_assessment_titles=( $file_name )
list_of_file_names=( $file_name )
