import csv
key_and_student_responses={}
# Read the CSV and pull out important info
with open('student_response_test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        field_names=[*row]
        number_of_columns = len(field_names)
        line_count = 1
        temp_dict={}
        for index in range(0, number_of_columns):
            dict_index=field_names[index]
            temp_dict[dict_index]=row[dict_index]
            line_count += 1
        if row["ID"] == "key":
            temp_key=f"version_{row['Version']}_key"
            key_and_student_responses[temp_key]=temp_dict
        else:
            temp_student_responses=f"{row['ID']}"
            key_and_student_responses[temp_student_responses]=temp_dict
number_of_keys=0
number_of_student_responses=0
for dict_item in [*key_and_student_responses]:
    #print(f"{key_and_student_responses[dict_item]}")
    temp_dict_for_counting=key_and_student_responses[dict_item]
    if temp_dict_for_counting["ID"]=="key":
        number_of_keys+=1
    else:
        number_of_student_responses+=1
print(f"Auto-DIG has loaded {number_of_keys} keys and {number_of_student_responses} student responses into a database!")
