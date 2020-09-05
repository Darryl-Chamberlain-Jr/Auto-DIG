function notBD {
    firstName=$1
    lastName=$2
    printf "%s %s is a liar! It's not his birthday. \n" "${firstName}" "${lastName}"
}
