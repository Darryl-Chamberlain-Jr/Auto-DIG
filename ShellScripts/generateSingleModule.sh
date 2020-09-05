source /${DIR}/ShellScripts/./functionsForZenityScript.sh
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
title_of_assessment=$(zenity \
    --title="${titleOfProgram[@]}" \
    --entry \
    --text "Name your assessment:"
)
list_of_assessment_titles=( $title_of_assessment )
