number_of_versions=$(zenity \
    --title="${titleOfProgram[@]}" \
    --scale \
    --text="How many versions do you want to create?" \
    --value=3 \
    --min-value=1 \
    --max-value=26 \
    --step=1
)

function defineVersionList {
    fullVersionList=( "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")
    version_counter=0
    version_list=()
    while [ $version_counter -lt $number_of_versions ]
    do
        version_list=( "${version_list[@]}" "${fullVersionList[$version_counter]}" )
        version_counter=$(( version_counter+1 ))
    done
}

defineVersionList
echo ${version_list[@]}
