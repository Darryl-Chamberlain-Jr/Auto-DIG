# This file contains all functions used to manipulate the files in some way.

function copyKeys {
    FileName=$1
    cp /${DIR}/Keys/*.pdf /${DIR}/CompleteExam/Keys/
    for version in A B C
    do
        cp /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv /${DIR}/CompleteExam/Keys/
        cp /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv /${DIR}/CompleteExam/Keys/
    done
}

function copyKeys {
    cp /${DIR}/Keys/*.pdf /${DIR}/CompleteExam/Keys/
    touch /${DIR}/CompleteExam/Keys/masterKeyALL.csv
    for version in A B C
    do
        cp /${DIR}/Keys/lettersMasterKey${version}.csv /${DIR}/CompleteExam/Keys/
        # cp /${DIR}/Keys/numbersMasterKey${version}.csv /${DIR}/CompleteExam/Keys/
    done
    # cat /${DIR}/CompleteExam/Keys/lettersMasterKeyA.csv /${DIR}/CompleteExam/Keys/lettersMasterKeyB.csv /${DIR}/CompleteExam/Keys/lettersMasterKeyC.csv > /${DIR}/CompleteExam/Keys/masterKeyALL.csv
}

function clearOldVersions {
    # Clears old keys and pdfs
    rm -rf /${DIR}/Keys/*
    rm -rf /${DIR}/buildExams/*
    rm -rf /${DIR}/CompleteExam/Keys/*
    rm -rf /${DIR}/CompleteExam/PDFs/*
    rm -rf /${DIR}/CompleteExam/LockedPDFs/*
    rm -rf /${DIR}/GenerationReport/*
}
