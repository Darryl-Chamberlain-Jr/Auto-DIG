function createReportFile {
    ExamNumber=$1
    touch /${DIR}/GenerationReport/ProgressExam${ExamNumber}Report.txt
    cat >> /${DIR}/GenerationReport/ProgressExam${ExamNumber}Report.txt << FINISH_HIM
This starts the report on Progress Exam $1.

FINISH_HIM
}

function reportOnSageError {
    ExamNumber=$1
    ModuleNumber=$2
    Version=$3
    cat >> /${DIR}/GenerationReport/ProgressExam${ExamNumber}Report.txt << FINISH_HIM

There was an error when running the sage file on Module $2 Version $3. This will be improved in the future to print the error that occurred. For now, review the Terminal.

FINISH_HIM
}

function reportOnModuleRunTime {
    ModuleNumber=$1
    ExamNumber=$2
    ModuleRunTimeStart=$3
    ModuleRunTimeEnd=$4
    Version=$5
    TotalRunTimeSeconds=$(( ModuleRunTimeEnd - ModuleRunTimeStart ))
    RunTimeMinutes=$(( (ModuleRunTimeEnd - ModuleRunTimeStart) / 60 ))
    RunTimeSecondsRemainder=$(( TotalRunTimeSeconds - (RunTimeMinutes * 60) ))
    if [ $RunTimeMinutes == 0 ]
    then
        cat >> /${DIR}/GenerationReport/ProgressExam${ExamNumber}Report.txt << FINISH_HIM
Module $1 Version $5 took $RunTimeSecondsRemainder seconds to run.
FINISH_HIM
    else
        cat >> /${DIR}/GenerationReport/ProgressExam${ExamNumber}Report.txt << FINISH_HIM
Module $1 Version $5 took $RunTimeMinutes minutes and $RunTimeSecondsRemainder seconds to run.
FINISH_HIM
    fi
}

function reportOnPDFlatexError {
    ExamNumber=$1
    ModuleNumber=$2
    Version=$3
    cat >> /${DIR}/GenerationReport/ProgressExam${ExamNumber}Report.txt << FINISH_HIM

There was an error when running the tex file on Module $2 Version $3. This will be improved in the future to print the error that occurred. For now, review the Terminal.

FINISH_HIM
}

function finishReport {
    ExamNumber=$1
    StartTime=$2
    EndTime=$3
    currentDayTime=$( date +'%H:%M on %m/%d/%Y' )
    TotalRunTimeSeconds=$(( EndTime - StartTime ))
    RunTimeMinutes=$(( (EndTime - StartTime) / 60 ))
    RunTimeSecondsRemainder=$(( TotalRunTimeSeconds - (RunTimeMinutes * 60) ))
    cat >> /${DIR}/GenerationReport/ProgressExam${ExamNumber}Report.txt << FINISH_HIM

The exam finished running at ${currentDayTime}. It took $RunTimeMinutes minutes and $RunTimeSecondsRemainder seconds.

FINISH_HIM
}
