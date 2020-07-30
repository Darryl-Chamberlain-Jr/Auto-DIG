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
There was an error when running the sage file on Module $2 Version $3. This will be improved in the future to print the error that occurred. For now, review the Terminal. \n \n

FINISH_HIM
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
    TimeToRunSeconds=$(( EndTime - StartTime ))
    TimeToRunMinutes=$(( (EndTime - StartTime) / 60 ))
    TimeToRunSecondsRemainder=$(( TimeToRunSeconds - (TimeToRunMinutes * 60) ))
    cat >> /${DIR}/GenerationReport/ProgressExam${ExamNumber}Report.txt << FINISH_HIM
The exam is done running at ${currentDayTime}.

It took $TimeToRunSeconds seconds to run, which is $TimeToRunMinutes minutes and $TimeToRunSecondsRemainder seconds.

FINISH_HIM
}
