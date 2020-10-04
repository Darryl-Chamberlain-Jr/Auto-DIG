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
with open('test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Keys are the column titles
        print(row['name'])
############################

def random_option():
    options=["A", "B", "C", "D", "E"]
    return random.choice(options)

row_index=0
col_index
row=[]
for version in ['Version_A', 'Version_B', 'Version_C']:
    temp_new_row=[version]
    for i in range(1, 10):
        temp_new_row.append(random.choice(options))
    row.append(temp_new_row)

fieldnames = ['name', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': , 'Q1': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
