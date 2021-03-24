import random
import sys
import shelve

def print_question_to_exam(database_info, version, file_name, DIR):
    display_stem_type, display_stem, display_problem_type, display_problem, display_options_type, choices, choice_comments, solution, answer_letter, general_comment = database_info
    examFile = open('/' + str(DIR) + '/BuildExams/' + str(file_name) + '.tex', 'a')
    examFile.write(r"\litem{")
    examFile.write('\n')
    # display_stem_type: String, Math Mode, or Graph
    if display_stem_type=="String":
        examFile.write(display_stem)
    elif display_stem_type=="Math Mode":
        examFile.write("$%s$" %display_stem)
    elif display_stem_type=="Graph":
        examFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(code_name, version))
#    else:
#        print(f"You input {display_stem_type}, which was not a valid option.")
    # display_problem_type: String, Math Mode, Graph, or Table
    if display_problem_type=="String":
        examFile.write(r"""
\begin{center}
    \textit{ %s }
\end{center}
""" %display_problem)
    elif display_problem_type=="Math Mode":
        examFile.write(r"\[ %s \]" %display_problem)
    elif display_problem_type=="Graph":
        examFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(code_name, version))
    elif display_problem_type=="Table":
        # display_problem is now an array. Organize as [ row_1, row_2, row_3, ..., row_m ]
            # len(display_problem) is number of rows
            # len(display_problem[0]) is number of columns
        num_rows=len(display_problem)
        num_cols=len(display_problem[0])
        examFile.write('\n')
        examFile.write('\n')
        examFile.write('\\begin{tabular}{')
        for j in range(num_cols-1):
            examFile.write('c|')
        # Ends begin tabular and doesn't have a bar at the end.
        examFile.write('c}')
        examFile.write('\n')
        # Iterate through the rows and print and & between with a \tabularnewline at the end. Since last row doesn't need one it is done at the end after the loop finishes
        for i in range(num_rows-1):
            for j in range(num_cols-1):
                examFile.write(r"%s &" %display_problem[i][j])
            # Last item in row does not have an &
            examFile.write(r"%s" %display_problem[i][num_cols-1])
            examFile.write('\\tabularnewline \\hline')
            examFile.write('\n')
        for j in range(num_cols-1):
            examFile.write(r"%s &" %display_problem[num_rows-1][j])
        examFile.write(r"%s" %display_problem[num_rows-1][num_cols-1])
        examFile.write('\end{tabular}')
    # Begins enumerate for options
    examFile.write(r"\begin{enumerate}[label=\Alph*.]")
    examFile.write('\n')
    # display_options_type: String, Math Mode, or Graph
    if display_options_type=="String":
        for i in range(len(choices)):
            examFile.write(r"\item %s" %choices[i])
            examFile.write('\n')
    elif display_options_type=="Math Mode":
        for i in range(len(choices)):
            examFile.write(r"\item \( %s \)" %choices[i])
            examFile.write('\n')
    elif display_options_type=="Graph":
        examFile.write(r"\begin{multicols}{2}")
        for i in range(len(choices)):
            options=["A", "B", "C", "D", "E", "F", "G", "H"]
            examFile.write(r"\item \includegraphics[width = 0.3\textwidth]{../Figures/%s%s%s.png}" %(code_name, options[i], version))
        examFile.write(r"\end{multicols}")
        examFile.write(r"\item None of the above.")
    examFile.write('\n')
    examFile.write(r"\end{enumerate} }") # The close bracket ends the litem initiated in the first examFile.write
    # Ends enumerate for options
    examFile.write('\n')
    examFile.close()
def print_question_to_key(database_info, version, code_name, file_name, DIR):
    display_stem_type, display_stem, display_problem_type, display_problem, display_options_type, choices, choice_comments, solution, answer_letter, general_comment = database_info
    keyFile = open('../Keys/key' + str(file_name) + '.tex', 'a')
    keyFile.write(r"\litem{")
    keyFile.write('\n')
    # display_stem_type: String, Math Mode, or Graph
    if display_stem_type=="String":
        keyFile.write(display_stem)
    elif display_stem_type=="Math Mode":
        keyFile.write("$%s$" %display_stem)
    elif display_stem_type=="Graph":
        keyFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(code_name, version))
    keyFile.write('\n')
    # display_problem_type: String, Math Mode, Graph, or Table
    if display_problem_type=="String":
        keyFile.write(r"""
\begin{center}
    \textit{ %s }
\end{center}
""" %display_problem)
    elif display_problem_type=="Math Mode":
        keyFile.write(r"\[ %s \]" %display_problem)
    elif display_problem_type=="Graph":
        keyFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(code_name, version))
        keyFile.write('\n\n')
    elif display_problem_type=="Table":
        # display_problem is now an array. Organize as [ row_1, row_2, row_3, ..., row_m ]
            # len(display_problem) is number of rows
            # len(display_problem[0]) is number of columns
        num_rows=len(display_problem)
        num_cols=len(display_problem[0])
        keyFile.write('\n')
        keyFile.write('\n')
        keyFile.write('\\begin{tabular}{')
        for j in range(num_cols-1):
            keyFile.write('c|')
        # Ends begin tabular and doesn't have a bar at the end.
        keyFile.write('c}')
        keyFile.write('\n')
        # Iterate through the rows and print and & between with a \tabularnewline at the end. Since last row doesn't need one it is done at the end after the loop finishes
        for i in range(num_rows-1):
            for j in range(num_cols-1):
                keyFile.write(r"%s &" %display_problem[i][j])
            # Last item in row does not have an &
            keyFile.write(r"%s" %display_problem[i][num_cols-1])
            keyFile.write('\\tabularnewline \\hline')
            keyFile.write('\n')
        for j in range(num_cols-1):
            keyFile.write(r"%s &" %display_problem[num_rows-1][j])
        keyFile.write(r"%s" %display_problem[num_rows-1][num_cols-1])
        keyFile.write('\end{tabular}')
    if display_options_type=="String":
        keyFile.write("The solution is %s, which is option %s." %(solution, answer_letter))
        keyFile.write('\n')
        keyFile.write('\n')
        keyFile.write(r"\begin{enumerate}[label=\Alph*.]")
        keyFile.write('\n')
        for i in range(len(choices)):
            keyFile.write(r"\item %s" %choices[i])
            keyFile.write('\n')
            keyFile.write('\n')
            keyFile.write(choice_comments[i])
            keyFile.write('\n')
        keyFile.write(r"\end{enumerate}")
        keyFile.write('\n')
        keyFile.write('\n')
    elif display_options_type=="Math Mode":
        keyFile.write("The solution is \( %s \), which is option %s." %(solution, answer_letter))
        keyFile.write(r"\begin{enumerate}[label=\Alph*.]")
        keyFile.write('\n')
        for i in range(len(choices)):
            keyFile.write(r"\item \( %s \)" %choices[i])
            keyFile.write('\n')
            keyFile.write('\n')
            keyFile.write(choice_comments[i])
            keyFile.write('\n')
        keyFile.write(r"\end{enumerate}")
        keyFile.write('\n')
    elif display_options_type=="Graph":
        keyFile.write(r"""The solution is the graph below, which is option %s.
\begin{center}
    \includegraphics[width=0.3\textwidth]{../Figures/%s%s%s.png}
\end{center}""" %(answer_letter, code_name, answer_letter, version) )
        keyFile.write(r"\begin{enumerate}[label=\Alph*.]")
        keyFile.write('\n')
        keyFile.write(r"\begin{multicols}{2}")
        keyFile.write('\n')
        for i in range(len(choices)):
            options=["A", "B", "C", "D", "E", "F", "G", "H"]
            keyFile.write(r"\item \includegraphics[width = 0.3\textwidth]{../Figures/%s%s%s.png}" %(code_name, options[i], version))
            keyFile.write('\n')
        keyFile.write(r"\end{multicols}")
        keyFile.write(r"\item None of the above.")
        keyFile.write(r"\end{enumerate}")
    keyFile.write('\n')
    keyFile.write(r"\textbf{General Comment:} %s" %general_comment)
    keyFile.write('\n')
    keyFile.write(r"}") # The close bracket ends the litem initiated in the first keyFile.write
    keyFile.write('\n')
    keyFile.close()
    # Adds letter to masterAnswerKeyFile
    lettersAnswerKey = open('../Keys/lettersAnswerKey' + str(file_name) + str(version) + '.csv', 'a')
    lettersAnswerKey.write("%s," %answer_letter)
    lettersAnswerKey.close()
def print_question_to_feedback(database_info, student_answer_letter, version, code_name, file_name, DIR):
    display_stem_type, display_stem, display_problem_type, display_problem, display_options_type, choices, choice_comments, solution, answer_letter, general_comment = database_info
    feedbackFile = open('../Feedback/feedback' + str(file_name) + '.tex', 'a')
    feedbackFile.write(r"\litem{")
    # display_stem_type: String, Math Mode, or Graph
    if display_stem_type=="String":
        feedbackFile.write(display_stem)
    elif display_stem_type=="Math Mode":
        feedbackFile.write("$%s$" %display_stem)
    elif display_stem_type=="Graph":
        feedbackFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(code_name, version))
    # display_problem_type: String, Math Mode, Graph, or Table
    if display_problem_type=="String":
        feedbackFile.write(r"""
\begin{center}
    \textit{ %s }
\end{center}
""" %display_problem)
    elif display_problem_type=="Math Mode":
        feedbackFile.write(r"\[ %s \]" %display_problem)
    elif display_problem_type=="Graph":
        feedbackFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(code_name, version))
    elif display_problem_type=="Table":
        # display_problem is now an array. Organize as [ row_1, row_2, row_3, ..., row_m ]
            # len(display_problem) is number of rows
            # len(display_problem[0]) is number of columns
        num_rows=len(display_problem)
        num_cols=len(display_problem[0])
        feedbackFile.write('\n')
        feedbackFile.write('\n')
        feedbackFile.write('\\begin{tabular}{')
        for j in range(num_cols-1):
            feedbackFile.write('c|')
        # Ends begin tabular and doesn't have a bar at the end.
        feedbackFile.write('c}')
        feedbackFile.write('\n')
        # Iterate through the rows and print and & between with a \tabularnewline at the end. Since last row doesn't need one it is done at the end after the loop finishes
        for i in range(num_rows-1):
            for j in range(num_cols-1):
                feedbackFile.write(r"%s &" %display_problem[i][j])
            # Last item in row does not have an &
            feedbackFile.write(r"%s" %display_problem[i][num_cols-1])
            feedbackFile.write('\\tabularnewline \\hline')
            feedbackFile.write('\n')
        for j in range(num_cols-1):
            feedbackFile.write(r"%s &" %display_problem[num_rows-1][j])
        feedbackFile.write(r"%s" %display_problem[num_rows-1][num_cols-1])
        feedbackFile.write('\end{tabular}')
    # displayCorrectSolution
        # display_options_type: String, Math Mode, or Graph
        if display_options_type=="String":
            feedbackFile.write("The solution is %s, which is option %s." %(solution, answer_letter))
        elif display_options_type=="Math Mode":
            feedbackFile.write("The solution is \( %s \), which is option %s." %(solution, answer_letter))
        elif display_options_type=="Graph":
            feedbackFile.write(r"\begin{multicols}{2}")
            feedbackFile.write(r"""The solution is the graph below, which is option %s.
    \\begin{center}
        \\includegraphics[width=0.3\\textwidth]{../Figures/%s%s%s.png}
    \\end{center}""" %(answer_letter, code_name, answer_letter, version) )
    # displayStudentSolution
    if student_answer_letter == answer_letter:
        superlative=["Excellent", "Magnificent", "Wonderful", "Marvelous", "Brilliant", "Outstanding", "Great job", "Fantastic job", "Awesome", "Exceptional", "Well done"]
        feedbackFile.write("You chose option %s. %s! That is the correct answer." %(student_answer_letter, random.choice(superlative))) # Student correct!
    else:
        feedbackFile.write("You chose option %s. Unfortunately, that is not the correct answer." %student_answer_letter)
        options=["A", "B", "C", "D", "E", "F", "G", "H"]
        for letter in options:
            index=0
            if student_answer_letter == letter and answer_letter != letter:
                 feedbackFile.write(choiceSpecificComments[index])
                 break
            index+=1 # Student incorrect. Prints feedback to improve.
    feedbackFile.close()

to_do = sys.argv[1]
DIR = sys.argv[2]
file_name = sys.argv[3]
database_name = sys.argv[4]
question_list = sys.argv[5]
code_name = sys.argv[6]
version = sys.argv[7]
OS_type = sys.argv[8]
single_or_combined = sys.argv[9]

if "linux-gnu" == OS_type:
    ql=shelve.open(f"/{DIR}/Databases/{database_name}.db")
else:
    ql=shelve.open(f"/{DIR}/Databases/{database_name}")

if single_or_combined == "single":
    full_file_name = f"{file_name}{version}"
else:
    full_file_name = f"{file_name}ALL"

try:
    master_list = ql[f'{question_list}']
    total=len(master_list)
    for index in range(0, total):
        question_dict=master_list[index]
        if question_dict.get("Code Name") == code_name:
            # print the variables necessary
            display_stem_type=question_dict.get("Display Stem Type")
            display_stem=question_dict.get("Display Stem")
            display_problem_type=question_dict.get("Display Problem Type")
            display_problem=question_dict.get("Display Problem")
            display_options_type=question_dict.get("Display Options Type")
            choices=question_dict.get("Choices")
            choice_comments=question_dict.get("Choice Comments")
            solution=question_dict.get("Solution")
            answer_letter=question_dict.get("Answer Letter")
            general_comment=question_dict.get("General Comment")
            database_info = [display_stem_type, display_stem, display_problem_type, display_problem, display_options_type, choices, choice_comments, solution, answer_letter, general_comment]
            ql.close()
            if to_do == "Print questions to exam":
                print_question_to_exam(database_info, version, full_file_name, DIR)
            elif to_do == "Print questions to key":
                print_question_to_key(database_info, version, code_name, full_file_name, DIR)
            elif to_do == "Print questions to feedback":
                print_question_to_feedback(database_info, student_answer_letter, version, code_name, full_file_name, DIR)
            else:
                print("Error occured when trying print questions to tex files.")
                exit(1)
            break
except:
    print(f"{code_name} has not been loaded into database {database_name}.db.")
    exit(1)
finally:
    print(f"The question list {question_list} has been printed into {full_file_name}.tex.")
