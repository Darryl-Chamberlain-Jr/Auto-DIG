StartTime=$( date +'%s' )
TestingTime=$( date )
source ./func1.sh
happyBD Darryl Chamberlain

source ./func2.sh
notBD Darryl Chamberlain

EndTime=$( date +'%s' )

currentDayTime=$( date +'%H:%M on %m/%d/%Y' )
TimeToRunSeconds=$(( EndTime - StartTime ))
TimeToRunMinutes=$(( (EndTime - StartTime) / 60 ))
TimeToRunSecondsRemainder=$(( TimeToRunSeconds - (TimeToRunMinutes * 60) ))

dialog --title "Create Progress Quiz" --gauge "Creating versions of each Module..." 6 50 < <(
   totalNumberOfCopies=$(( 3*16 ))
   moduleVersionCounter=0
   while [ $moduleVersionCounter -le $totalNumberOfCopies ]; do
   PROGRESS=$(( 100*moduleVersionCounter/totalNumberOfCopies ))
cat <<EOF
XXX
$PROGRESS
Creating Module blank version blank...
XXX
EOF
   #"In the future I'll run the file here"
   source ./func1.sh
   happyBD Darryl Chamberlain
   moduleVersionCounter=$(( moduleVersionCounter + 1 ))
   done
cat <<EOF
XXX
Complete! Check the folders for PDFs and keys.
XXX
EOF
)

dialog --title "DONE" --infobox "Exits with info" 6 50 
