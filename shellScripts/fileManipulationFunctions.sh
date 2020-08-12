# This file contains all functions used to manipulate the files in some way.

function copyKeys {
    FileName=$1
    versionList=$2
    cp /${DIR}/Keys/*.pdf /${DIR}/CompleteExam/Keys/
    for version in $versionList
    do
        cp /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv /${DIR}/CompleteExam/Keys/
    done
}

function clearOldVersions {
    # Clears old keys and pdfs
    rm -rf /${DIR}/Keys/*
    rm -rf /${DIR}/buildExams/*
    rm -rf /${DIR}/CompleteExam/Keys/*
    rm -rf /${DIR}/CompleteExam/PDFs/*
    rm -rf /${DIR}/CompleteExam/LockedPDFs/*
}
