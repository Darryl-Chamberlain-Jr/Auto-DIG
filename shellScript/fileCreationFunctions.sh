# This file contains all functions to create the initial .tex file for a module or key. 

function createAnswerKeyFile {
    Version=$1
    Semester=$2
    FileName=$3
    HeadingName=$4
    /bin/cat > /${DIR}/Keys/key${FileName}${Version}.tex << FINISH_HIM

\documentclass{article}[14pt]
\usepackage{multicol, enumerate, enumitem, hyperref, color, soul, setspace, parskip, fancyhdr, amssymb, amsthm, amsmath, bbm, latexsym, units, mathtools}
\everymath{\displaystyle}
\usepackage[headsep=0.5cm,headheight=0cm, left=1 in,right= 1 in,top= 1 in,bottom= 1 in]{geometry}
\pagestyle{fancy}
\lhead{}
\chead{Answer Key for ${HeadingName} Version ${Version}}
\rhead{}
\lfoot{${Semester}}
\cfoot{}
\rfoot{}
\begin{document}
\textbf{This key should allow you to understand why you choose the option you did (beyond just getting a question right or wrong). \href{https://xronos.clas.ufl.edu/mac1105spring2020/courseDescriptionAndMisc/Exams/LearningFromResults}{More instructions on how to use this key can be found here}.}

\textbf{If you have a suggestion to make the keys better, \href{https://forms.gle/CZkbZmPbC9XALEE88}{please fill out the short survey here}.}

\textit{Note: This key is auto-generated and may contain issues and/or errors. The keys are reviewed after each exam to ensure grading is done accurately. If there are issues (like duplicate options), they are noted in the offline gradebook. The keys are a work-in-progress to give students as many resources to improve as possible.}

\rule{\textwidth}{0.4pt}

FINISH_HIM
}

### Creates the Exam Heading for any Module.

createExamHeading() {
  MODULEVERSION=$1
  EXAMNUMBER=$2
  SEMESTER=$3
  STARTENUMERATEAT=$4
  LONGNAME=$5
  FileName=$6
  /bin/cat > /${DIR}/buildExams/${FileName}${MODULEVERSION}.tex << FINISH_HIM
\documentclass[14pt]{article}
%General Packages
\usepackage{multicol, enumerate, enumitem, hyperref, color, soul, setspace, parskip, fancyhdr}

%Math Packages
\usepackage{amssymb, amsthm, amsmath, bbm, latexsym, units, mathtools}

%All math in Display Style
\everymath{\displaystyle}

% Packages with additional options
%\usepackage[T1]{fontenc}
\usepackage[headsep=0.5cm,headheight=0cm, left=1 in,right= 1 in,top= 1 in,bottom= 1 in]{geometry}
\usepackage[usenames,dvipsnames]{xcolor}

% SageTeX
\usepackage{sagetex}

% Package to use the command below to create lines between items
\usepackage{dashrule}
\newcommand{\litem}[1]{\item#1\hspace*{-1cm}\rule{\textwidth}{0.4pt}}

\pagestyle{fancy}
\lhead{${LONGNAME}}
\chead{}
\rhead{Progress Exam ${EXAMNUMBER}}
\lfoot{${SEMESTER}}
\cfoot{}
\rfoot{Version ${MODULEVERSION}}

\begin{document}
\pagestyle{fancy}

\begin{sagesilent}
load("../Code/generalPurposeMethods.sage")
load("../Code/keyGeneration.sage")
keyFileName = "${FileName}"
version = "${MODULEVERSION}"
\end{sagesilent}

\begin{enumerate}
\setcounter{enumi}{${STARTENUMERATEAT}}

FINISH_HIM
}
