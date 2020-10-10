import csv
import random
# Adds letter to masterAnswerKeyFile
#lettersAnswerKey = open('../Keys/lettersAnswerKey' + str(file_name) + str(version) + '.csv', 'a')
#lettersAnswerKey.write("%s," %answer_letter)
#lettersAnswerKey.close()

# Goals
#-----------------------
#-----------------------
# Two documents: Data Analysis csv and Student Grading csv
#   Data Analysis csv
#       Print original question list at top row
#       Print answers according to question type
#   Student Grading csv
#       Print randomize answers for each version

# Testing
#with open('test.csv', newline='') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
        # Keys are the column titles
#        print(row['name'])

############################

def random_option():
    options=["A", "B", "C", "D", "E"]
    return random.choice(options)
def version_dict(version):
    dict={
    'Version': version,
    'Q1': random_option(),
    'Q2': random_option(),
    'Q3': random_option(),
    'Q4': random_option(),
    'Q5': random_option(),
    'Q6': random_option(),
    'Q7': random_option(),
    'Q8': random_option(),
    'Q9': random_option(),
    'Q10': random_option()
    }
    return dict

version_A=version_dict('A')
version_B=version_dict('B')
version_C=version_dict('C')

with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['Version', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(version_A)
    writer.writerow(version_B)
    writer.writerow(version_C)

# IDEA - Read all values in a row. Apppend a new value at the end of the row.
# First row: fieldnames as written above
# Second row: name of code file
# Third row: correct answer letter
# Fourth row: minor error answer letter
# Fifth, Sixth, Seventh row: major error answer

#row_index=3
#col_index=0
#row=[]
#for version in ['Version_A', 'Version_B', 'Version_C']:
#    temp_new_row=[version]
#    for i in range(1, 10):
#        temp_new_row.append(random.choice(options))
#    row.append(temp_new_row)
