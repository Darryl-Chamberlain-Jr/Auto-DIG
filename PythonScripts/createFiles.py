from pathlib import Path # To touch files within python
import sys

to_do = sys.argv[1]
file_name = sys.argv[2]
exam_display_name = sys.argv[3]
footnote_left = sys.argv[4]
footnote_right = sys.argv[5]
version = sys.argv[6]
DIR = sys.argv[7]

def createKeyFile(file_name, exam_name, footnote_left, footnote_right, version, DIR):
    Path('/' + str(DIR) + '/Keys/key' + str(file_name) + str(version)+ '.tex').touch()
    keyFile = open('/' + str(DIR) + '/Keys/key' + str(file_name) + str(version)+ '.tex', 'a')
    keyFile.write(r"""\documentclass{extbook}[14pt]
\usepackage{multicol, enumerate, enumitem, hyperref, color, soul, setspace, parskip, fancyhdr, amssymb, amsthm, amsmath, bbm, latexsym, units, mathtools}
\everymath{\displaystyle}
\usepackage[headsep=0.5cm,headheight=0cm, left=1 in,right= 1 in,top= 1 in,bottom= 1 in]{geometry}
\usepackage{dashrule}  %% Package to use the command below to create lines between items
\newcommand{\litem}[1]{\item #1

\rule{\textwidth}{0.4pt}}
\pagestyle{fancy}
\lhead{}
\chead{Answer Key for %s Version %s}
\rhead{}
\lfoot{%s}
\cfoot{}
\rfoot{%s}
\begin{document}
\textbf{This key should allow you to understand why you choose the option you did (beyond just getting a question right or wrong). \href{https://xronos.clas.ufl.edu/mac1105spring2020/courseDescriptionAndMisc/Exams/LearningFromResults}{More instructions on how to use this key can be found here}.}

\textbf{If you have a suggestion to make the keys better, \href{https://forms.gle/CZkbZmPbC9XALEE88}{please fill out the short survey here}.}

\textit{Note: This key is auto-generated and may contain issues and/or errors. The keys are reviewed after each exam to ensure grading is done accurately. If there are issues (like duplicate options), they are noted in the offline gradebook. The keys are a work-in-progress to give students as many resources to improve as possible.}

\rule{\textwidth}{0.4pt}

\begin{enumerate}""" %(exam_name, version, footnote_left, footnote_right)   )
    keyFile.close()
def createExamFile(file_name, exam_name, footnote_left, footnote_right, version, DIR):
    Path('/' + str(DIR) + '/BuildExams/' + str(file_name) + str(version)+ '.tex').touch()
    examFile = open('/' + str(DIR) + '/BuildExams/' + str(file_name) + str(version)+ '.tex', 'a')
    examFile.write(r"""\documentclass[14pt]{extbook}
\usepackage{multicol, enumerate, enumitem, hyperref, color, soul, setspace, parskip, fancyhdr} %%General Packages
\usepackage{amssymb, amsthm, amsmath, bbm, latexsym, units, mathtools} %%Math Packages
\everymath{\displaystyle} %%All math in Display Style
%% Packages with additional options
\usepackage[headsep=0.5cm,headheight=12pt, left=1 in,right= 1 in,top= 1 in,bottom= 1 in]{geometry}
\usepackage[usenames,dvipsnames]{xcolor}
\usepackage{dashrule}  %% Package to use the command below to create lines between items
\newcommand{\litem}[1]{\item#1\hspace*{-1cm}\rule{\textwidth}{0.4pt}}
\pagestyle{fancy}
\lhead{%s}
\chead{}
\rhead{Version %s}
\lfoot{%s}
\cfoot{}
\rfoot{%s}
\begin{document}

\begin{enumerate}
""" %(exam_name, version, footnote_left, footnote_right))
    examFile.close()
def finishKeyFile(file_name, version, DIR):
    keyFile = open('/' + str(DIR) + '/Keys/key' + str(file_name) + str(version)+ '.tex', 'a')
    keyFile.write(r"""\end{enumerate}

\end{document}""")
    keyFile.close()
def finishExamFile(file_name, version, DIR):
    examFile = open('/' + str(DIR) + '/BuildExams/' + str(file_name) + str(version)+ '.tex', 'a')
    examFile.write(r"""\end{enumerate}

\end{document}""")
    examFile.close()

if to_do == "Create Key File":
    createKeyFile(file_name, exam_display_name, footnote_left, footnote_right, version, DIR)
elif to_do == "Create Exam File":
    createExamFile(file_name, exam_display_name, footnote_left, footnote_right, version, DIR)
elif to_do == "Finish Key File":
    finishKeyFile(file_name, version, DIR)
elif to_do == "Finish Exam File":
    finishExamFile(file_name, version, DIR)
else:
    print("Check the command you submitted.")
    exit(1)
