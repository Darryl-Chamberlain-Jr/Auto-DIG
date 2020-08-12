option1="A Progress Quiz"
option2="A single Module"
option3="A single version of a Module"
option4="A Final Exam"
typeOfGeneration=$(zenity --height=200 --width=350 --list --radiolist --text '<b> style="background-color:powderblue; What do you want to do?</b> </body>' --column 'Select...' --column 'Generate...' FALSE "$option1" FALSE "$option2" FALSE "$option3" FALSE "$option4")
semester=$(zenity --entry --text "Enter the semester" --width=300)
examNumber=$(zenity --height=200 --width=350 --list --radiolist --text '<b>Which quiz do you want to create?</b>' --column 'Select...' --column 'Quiz Number' FALSE 1 FALSE 2 FALSE 3 FALSE 4 FALSE 5 FALSE 6)
if [ $examNumber -eq 1 ]; then
    numberOfModules=3
    moduleList=( 1 2 3 )
elif [ $examNumber -eq 2 ]; then
    numberOfModules=6
    moduleList=( 1 2 3 4 5 6 )
elif [ $examNumber -eq 3 ]; then
    numberOfModules=10
    moduleList=( 1 2 3 4 5 6 7 8 "9M" "9L")
else
    numberOfModule=16
    moduleList=( 1 2 3 4 5 6 7 8 "9M" "10M" "11M" "12M" "9L" "10L" "11L" "12L")
fi
numberOfVersions=$(zenity --entry --text "How many versions do you want to create?" --width=300)
fullVersionList=( "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")
versionCounter=0
versionList=()
while [ "$versionCounter" -lt "$numberOfVersions" ]
do
    versionList=( "${versionList[@]}" "${fullVersionList[$versionCounter]}" )
    versionCounter=$(( versionCounter+1 ))
done
(
source /${DIR}/shellScript/fileManipulationFunctions.sh
clearOldVersions
StartTime=$( date +'%s' )
# Step is the total number of modules * number of versions
step=$(( 100/ (numberOfModules*numberOfVersions) ))
counter=0
while :
do
    for module in ${moduleList[@]}
    do
        for version in ${versionList[@]}
        do
            echo "$counter" ; sleep 1
            echo "# Creating Module $module Version $version."
            source /${DIR}/shellScript/generateExams.sh
            generateModule $module $examNumber $semester $version
            counter=$(( counter+step ))
        done
    done
    break
done
copyKeys
EndTime=$( date +'%s' )
currentDayTime=$( date +'%H:%M on %m/%d/%Y' )
TotalRunTimeSeconds=$(( EndTime - StartTime ))
RunTimeMinutes=$(( (EndTime - StartTime) / 60 ))
RunTimeSecondsRemainder=$(( TotalRunTimeSeconds - (RunTimeMinutes * 60) ))
echo "100"
echo "# Auto-DIG has finished running at ${currentDayTime}. It took $RunTimeMinutes minutes and $RunTimeSecondsRemainder seconds. Not bad!"
) |
zenity --progress \
  --title="Creating a Progress Quiz" \
  --text="Initializing parameters..." \
  --percentage=0 \
  --width=350
