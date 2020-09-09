source /${DIR}/ShellScripts/./functionsForZenityScript.sh
chooseExamNumber=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=275 \
    --list \
    --text '<b>Which quiz do you want to create?</b>
    The quiz number will be printed at the top of each PDF.' \
    --column 'Quiz Number' \
    "1 - This creates Modules 1 and 2." \
    "2 - This creates Modules 1, 2, 3 and 4." \
    "3 - This creates Modules 1-6." \
    "4 - This creates Modules 1-8." \
    "5 - This creates Modules 1-8, 9M-10M, and 9L-10L" \
    "6 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "7 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "8 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "9 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
    "10 - This creates Modules 1-8, 9M-12M, and 9L-12L" \
)
escape=$?
checkForEscape $escape
examNumber=${chooseExamNumber:0:2}
defineModuleList # Also defines the number of modules.
examLongName="Progress Quiz ${examNumber}"
