from pathlib import Path # To touch files within python

def createKeyFile(fileNamePrefix, examLongName, footnoteLeft, version, rootDirectory):
    Path('/' + str(rootDirectory) + '/Keys/key' + str(fileNamePrefix) + str(version)+ '.tex').touch()
    keyFile = open('/' + str(rootDirectory) + '/Keys/key' + str(fileNamePrefix) + str(version)+ '.tex', 'a')
    keyFile.write(r"""\documentclass{extbook}[14pt]
\usepackage{multicol, enumerate, enumitem, hyperref, color, soul, setspace, parskip, fancyhdr, amssymb, amsthm, amsmath, bbm, latexsym, units, mathtools}
\everymath{\displaystyle}
\usepackage[headsep=0.5cm,headheight=0cm, left=1 in,right= 1 in,top= 1 in,bottom= 1 in]{geometry}
\usepackage{dashrule}  %% Package to use the command below to create lines between items
\newcommand{\litem}[1]{\item#1\hspace*{-1cm}\rule{\textwidth}{0.4pt}}
\pagestyle{fancy}
\lhead{}
\chead{Answer Key for %s Version %s}
\rhead{}
\lfoot{%s}
\cfoot{}
\rfoot{}
\begin{document}
\textbf{This key should allow you to understand why you choose the option you did (beyond just getting a question right or wrong). \href{https://xronos.clas.ufl.edu/mac1105spring2020/courseDescriptionAndMisc/Exams/LearningFromResults}{More instructions on how to use this key can be found here}.}

\textbf{If you have a suggestion to make the keys better, \href{https://forms.gle/CZkbZmPbC9XALEE88}{please fill out the short survey here}.}

\textit{Note: This key is auto-generated and may contain issues and/or errors. The keys are reviewed after each exam to ensure grading is done accurately. If there are issues (like duplicate options), they are noted in the offline gradebook. The keys are a work-in-progress to give students as many resources to improve as possible.}

\rule{\textwidth}{0.4pt}

\begin{enumerate}""" %(examLongName, version, footnoteLeft)   )
    keyFile.close()
def createExamFile(fileNamePrefix, examLongName, footnoteLeft, version, rootDirectory):
    Path('/' + str(rootDirectory) + '/buildExams/' + str(fileNamePrefix) + str(version)+ '.tex').touch()
    examFile = open('/' + str(rootDirectory) + '/buildExams/' + str(fileNamePrefix) + str(version)+ '.tex', 'a')
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
\lhead{}
\chead{%s}
\rhead{}
\lfoot{%s}
\cfoot{}
\rfoot{Version %s}
\begin{document}

\begin{sagesilent}
load("../PythonScripts/pythonImports.py")
load("../PythonScripts/intervalMaskingMethod.sage")
load("../PythonScripts/keyGeneration.sage")
load("../PythonScripts/commonlyUsedFunctions.sage")
keyFileName = "%s"
version = "%s"
\end{sagesilent}

\begin{enumerate}
""" %(examLongName, footnoteLeft, version, fileNamePrefix, version))
    examFile.close()
def finishKeyFile(fileNamePrefix, version, rootDirectory):
    keyFile = open('/' + str(rootDirectory) + '/Keys/key' + str(fileNamePrefix) + str(version)+ '.tex', 'a')
    keyFile.write(r"""\end{enumerate}

\end{document}""")
    keyFile.close()
def finishExamFile(fileNamePrefix, version, rootDirectory):
    examFile = open('/' + str(rootDirectory) + '/buildExams/' + str(fileNamePrefix) + str(version)+ '.tex', 'a')
    examFile.write(r"""\end{enumerate}

\end{document}""")
    examFile.close()

# USED FOR TESTING FUNCTIONS - DELETE WHEN DONE
fileNamePrefix="Test"
examLongName="Testing creation of a file"
footnoteLeft="Dead"
version="A"
rootDirectory="home/dchamberlain31/git-repos/Auto-DIG"
createKeyFile(fileNamePrefix, examLongName, footnoteLeft, version, rootDirectory)
createExamFile(fileNamePrefix, examLongName, footnoteLeft, version, rootDirectory)
finishKeyFile(fileNamePrefix, version, rootDirectory)
finishExamFile(fileNamePrefix, version, rootDirectory)
