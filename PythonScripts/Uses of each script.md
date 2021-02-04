Initial setup of metadata database:
    originalQuestionMetadata.py -- stores metadata for small set of questions to use for testing
    store_original_metadata.py -- saves dicts in originalQuestionMetadata.py to a master database
    run python3 store_original_metadata.py $DIR
    DIR="home/dchamberlain31/git-repos/Auto-DIG"

Used by Individual Question Structure Codes:
    commonlyUsedFunctions.py -- functions that I generalized and use often, such as displaying a polynomial nicely.
    intervalMaskingMethod.py -- functions to generate intervals based on arrays.

Used by zenityAutoDIG.sh:
    create_grading_CSVs.py -- After code is run, creates csv key based on database info.
    createFiles.py -- Used to initially create and complete .tex files for exam and keys.
    printQuestions.py -- Takes saved database info on a question and prints it in .tex files.
    return_all_values_of_key.py -- Used for zenity to dynamically list questions to the user.
    return_key_value_from_db.py -- Used to pull the folder, subfolder, and other info per question so questions can be dynamically run.
    saveMetadataToNewDatabase.py -- Uses a subseteq array of questions to copy over their information from the master metadate database.
    storeQuestionData.py -- Stores question info into database after the question structure is ran.
