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

echo $StartTime

echo $TestingTime

echo $EndTime

echo $TimeToRunMinutes

echo $TimeToRunSecondsRemainder
