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

# Write into CSV
with open('test.csv', 'w', newline='') as csv_file:
    fieldnames = ['Version', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(version_A)
    writer.writerow(version_B)
    writer.writerow(version_C)

# Read the files that are in the CSV
with open('test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'The field names are {", ".join(row)}')
            line_count += 1
        print(f'Ver {row["Version"]}: Q1 is {row["Q1"]}, Q2 is {row["Q2"]}, Q3 is {row["Q3"]}, Q4 is {row["Q4"]}')
        line_count += 1
