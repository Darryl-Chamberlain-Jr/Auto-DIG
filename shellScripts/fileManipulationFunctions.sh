# This file contains all functions used to manipulate the files in some way.

function copyKeys {
    FileName=$1
    version=$2
    cp /${DIR}/Keys/key${FileName}${version}.pdf /${DIR}/CompleteExam/Keys/
    cp /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv /${DIR}/CompleteExam/Keys/
}

function clearOldVersions {
    # Clears old keys and pdfs
    rm -rf /${DIR}/Keys/*
    rm -rf /${DIR}/buildExams/*
    rm -rf /${DIR}/CompleteExam/Keys/*
    rm -rf /${DIR}/CompleteExam/PDFs/*
    rm -rf /${DIR}/CompleteExam/LockedPDFs/*
}
