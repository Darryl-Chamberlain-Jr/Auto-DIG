DIR="home/dchamberlain31/git-repos/Auto-DIG"
function defineAllQuestionsDynamically {
    Length=$(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "length")
    CodeNames=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Code Name"))
    Folder=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Folder"))
    Subfolder=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Subfolder"))
    TopicNumber=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Topic Number"))
    ObjectiveNumber=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Objective Number"))
    OIFS=$IFS;
    IFS=";";
    Topic=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Topic"))
    ShortDescription=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Short Description"))
    LongDescription=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Long Description"))
    Notes=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Notes"))
    Author=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Author"))
    Date=($(python3 /${DIR}/PythonScripts/originalQuestionMetadata.py "Date"))
    IFS=$OIFS
}
defineAllQuestionsDynamically
(
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
