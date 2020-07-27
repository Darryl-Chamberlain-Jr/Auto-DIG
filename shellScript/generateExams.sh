#!/bin/bash
# This script generates exams.

### CHANGE THIS ONCE ###
DIR="home/archdoc/git-repos/AAG-College-Algebra"
currentDayTime=$( date +'%m_%d_%Y_%H_%M' )

############# DOES NOT NEED TO BE CHANGED #################
copyKeys() {
    FileName=$1
    cp /${DIR}/Keys/*.pdf /${DIR}/CompleteExam/Keys/
    for version in A B C
    do
        cp /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv /${DIR}/CompleteExam/Keys/
        cp /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv /${DIR}/CompleteExam/Keys/
    done
}

createAnswerKeyFile() {
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

finishAnswerKeyFile() {
    Version=$1
    FileName=$2
    /bin/cat >> /${DIR}/Keys/key${FileName}${Version}.tex << FINISH_HIM

\end{document}

FINISH_HIM
}

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


# This creates the end of each Module .tex file.
createExamEnding() {
  Version=$1
  FileName=$2
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\end{enumerate}

\end{document}

FINISH_HIM
}

# This lists each of the 40 current Progress Exam questions in order. These will be generated individually later.

# START OF MODULE 1 QUESTIONS

createQuestion1() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=1
problemNumber=$2
load("../Code/realComplex/subgroupReal.sage")
\end{sagesilent}
\litem{ \sage{displayStem}
\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate} }

FINISH_HIM
}

createQuestion2() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=1
problemNumber=$2
load("../Code/realComplex/orderOfOperations.sage")
\end{sagesilent}
\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate} }
FINISH_HIM
}

createQuestion3() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=1
problemNumber=$2
load("../Code/realComplex/subgroupComplex.sage")
\end{sagesilent}
\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate} }
FINISH_HIM
}

createQuestion4() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=1
problemNumber=$2
load("../Code/realComplex/multiplyComplex.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion5() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=1
problemNumber=$2
load("../Code/realComplex/divideComplex.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

# START OF MODULE 2 QUESTIONS

createQuestion6() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=2
problemNumber=$2
load("../Code/linear/linearTwoPoints.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion7() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=2
problemNumber=$2
load("../Code/linear/linearGraphToStandard.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\begin{center}
	 \includegraphics[width=.3\textwidth]{../Figures/linearGraphToStandard${Version}.png}
	 \end{center}

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion8() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=2
problemNumber=$2
load("../Code/linear/linearParOrPer.sage")
\end{sagesilent}

\litem{	\sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion9() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=2
problemNumber=$2
load("../Code/linear/solveIntegerLinear.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

  % \( \sage{displayProblem} \)
	\[ \sage{blocks[0]}(\sage{blocks[1]+blocks[2]*x}) = \sage{blocks[3]}(\sage{blocks[4]*x-blocks[5]}) \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion10() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=2
problemNumber=$2
load("../Code/linear/solveRationalLinear.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

# START OF MODULE 3

createQuestion11() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=3
problemNumber=$2
load("../Code/inequality/describeSet.sage")
\end{sagesilent}
\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion12() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=3
problemNumber=$2
load("../Code/inequality/solveIntegerInequality.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion13() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=3
problemNumber=$2
load("../Code/inequality/solveRationalInequality.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion14() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=3
problemNumber=$2
load("../Code/inequality/solveCompoundOR.sage")
\end{sagesilent}

\litem{ \sage{displayStem}
	\[ \sage{displayLeftFactor} \hspace*{4mm} \text{ or } \hspace*{4mm} \sage{displayRightFactor} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion15() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=3
problemNumber=$2
load("../Code/inequality/solveCompoundAND.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

# START OF MODULE 4

createQuestion16() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=4
problemNumber=$2
load("../Code/quadratic/quadraticGraphToEquation.sage")
\end{sagesilent}
% TYPE 1 - Graph to function

\litem{ \sage{displayStem}

	\begin{center} \includegraphics[scale=0.3]{../Figures/quadraticGraphToEquation${Version}.png} \end{center}

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion17() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=4
problemNumber=$2
load("../Code/quadratic/quadraticEquationToGraph.sage")
\end{sagesilent}

% TYPE 2 - Function to graph
\litem{ Graph the equation \( f(x)= \sage{functionToGraph}. \)
\begin{multicols}{2}
	\begin{enumerate}[label=\Alph*.]
		\item \includegraphics[width = 0.25\textwidth]{../Figures/quadraticEquationToGraphA${Version}.png}
		\item \includegraphics[width = 0.25\textwidth]{../Figures/quadraticEquationToGraphB${Version}.png}
		\item \includegraphics[width = 0.25\textwidth]{../Figures/quadraticEquationToGraphC${Version}.png}
		\item \includegraphics[width = 0.25\textwidth]{../Figures/quadraticEquationToGraphD${Version}.png}
		\item \\text{None of the above}
	\end{enumerate}
\end{multicols}
}
FINISH_HIM
}
createQuestion18() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=4
problemNumber=$2
load("../Code/quadratic/factorLeadingOver1Composite.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

  	\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}

}
FINISH_HIM
}

createQuestion19() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=4
problemNumber=$2
load("../Code/quadratic/solveQuadraticFactorComposites.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion20() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=4
problemNumber=$2
load("../Code/quadratic/quadraticFormula.sage")
\end{sagesilent}

\litem{ \sage{displayStem}
	\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}


# START OF MODULE 5

createQuestion21() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=5
problemNumber=$2
load("../Code/radical/domainRadical.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ \sage{displayProblem} \]
	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion22() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=5
problemNumber=$2
load("../Code/radical/radicalGraphToEquation.sage")
\end{sagesilent}

\litem{\sage{displayStem}
\begin{multicols}{2}
\begin{center}
\includegraphics[width=.3\textwidth]{../Figures/radicalGraphToEquation${Version}.png}
\end{center}

\columnbreak

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
    \item \( \\text{None of the above} \)
	\end{enumerate}
\end{multicols}
}
FINISH_HIM
}

createQuestion23() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=5
problemNumber=$2
load("../Code/radical/radicalEquationToGraph.sage")
\end{sagesilent}

\litem{\sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \begin{multicols}{2}
  		\item \begin{center}
  \includegraphics[width=.3\textwidth]{../Figures/radicalEquationToGraph${Version}A.png}
  \end{center}
  		\item \begin{center}
  \includegraphics[width=.3\textwidth]{../Figures/radicalEquationToGraph${Version}B.png}
  \end{center}
  \columnbreak
  		\item \begin{center}
  \includegraphics[width=.3\textwidth]{../Figures/radicalEquationToGraph${Version}C.png}
  \end{center}
  		\item \begin{center}
  \includegraphics[width=.3\textwidth]{../Figures/radicalEquationToGraph${Version}D.png}
  \end{center}
  \item None of the above.
  \end{multicols}
\end{enumerate}
}
FINISH_HIM
}

createQuestion24() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=5
problemNumber=$2
load("../Code/radical/solveRadicalLinear.sage")
\end{sagesilent}

\litem{\sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion25() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=5
problemNumber=$2
load("../Code/radical/solveRadicalQuadratic.sage")
\end{sagesilent}

\litem{\sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

# START OF MODULE 6

createQuestion26() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=6
problemNumber=$2
load("../Code/polynomial/polyGraphToFunction.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\begin{center}
	\includegraphics[width = 0.3\textwidth]{../Figures/polyGraphToFunction${Version}.png}
	\end{center}

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion27() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=6
problemNumber=$2
load("../Code/polynomial/polyEndBehavior.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ f(x) = \sage{displayPolynomial} \]

\begin{multicols}{4}
	\begin{enumerate}[label=\Alph*.]
		\item \begin{center} \includegraphics[width=.2\textwidth]{../Figures/endBehaviorNegativeOdd${version}} \end{center}
    \columnbreak
		\item \begin{center} \includegraphics[width=.2\textwidth]{../Figures/endBehaviorNegativeEven${version}}\end{center}
    \columnbreak
		\item \begin{center} \includegraphics[width=.2\textwidth]{../Figures/endBehaviorPositiveEven${version}}\end{center}
    \columnbreak
		\item \begin{center} \includegraphics[width=.2\textwidth]{../Figures/endBehaviorPositiveOdd${version}}\end{center}
	\end{enumerate}
\end{multicols}
}
FINISH_HIM
}

createQuestion28() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=6
problemNumber=$2
load("../Code/polynomial/polyZeroBehavior.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ f(x) = \sage{displayPolynomial} \]

\begin{multicols}{4}
	\begin{enumerate}[label=\Alph*.]
		\item \begin{center} \includegraphics[width=.2\textwidth]{../Figures/zeroBehaviorNegativeOdd${version}}\end{center}
    \columnbreak
		\item \begin{center} \includegraphics[width=.2\textwidth]{../Figures/zeroBehaviorNegativeEven${version}}\end{center}
    \columnbreak
		\item \begin{center} \includegraphics[width=.2\textwidth]{../Figures/zeroBehaviorPositiveEven${version}}\end{center}
    \columnbreak
		\item \begin{center} \includegraphics[width=.2\textwidth]{../Figures/zeroBehaviorPositiveOdd${version}}\end{center}
	\end{enumerate}
\end{multicols}
}
FINISH_HIM
}

createQuestion29() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=6
problemNumber=$2
load("../Code/polynomial/constructPolyRationals.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ \sage{displayZero1}, \sage{displayZero2}, \sage{displayZero3} \]

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion30() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=6
problemNumber=$2
load("../Code/polynomial/constructPolyComplex.sage")
\end{sagesilent}

\litem{	\sage{displayStem}

	\[ \sage{displayZero1} \text{ and } \sage{displayZero2} \]

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

# START OF MODULE 7

createQuestion31() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=7
problemNumber=$2
load("../Code/rational/domainRational.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion32() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=7
problemNumber=$2
load("../Code/rational/solveRationalLinear.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ \sage{leftSide} = \frac{\sage{factorNumerator3}}{\sage{factorDenominator3}}  \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion33() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=7
problemNumber=$2
load("../Code/rational/solveRationalQuadratic.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

	\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
    \item \( \sage{choices[0]} \)
    \item \( \sage{choices[1]} \)
    \item \( \sage{choices[2]} \)
    \item \( \sage{choices[3]} \)
    \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion34() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=7
problemNumber=$2
load("../Code/rational/rationalGraphToEquation.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\begin{multicols}{2}
\begin{center}
\includegraphics[width=.3\textwidth]{../Figures/rationalGraphToEquation${Version}.png}
\end{center}

\columnbreak

	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
    \item None of the above
	\end{enumerate}
\end{multicols}
}
FINISH_HIM
}

createQuestion35() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=7
problemNumber=$2
load("../Code/rational/rationalEquationToGraph.sage")
\end{sagesilent}

\litem{ \sage{displayStem}
\[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
\begin{multicols}{2}
		\item \begin{center}
\includegraphics[width=.3\textwidth]{../Figures/rationalEquationToGraph${Version}A.png}
\end{center}
		\item \begin{center}
\includegraphics[width=.3\textwidth]{../Figures/rationalEquationToGraph${Version}B.png}
\end{center}
\columnbreak
		\item \begin{center}
\includegraphics[width=.3\textwidth]{../Figures/rationalEquationToGraph${Version}C.png}
\end{center}
		\item \begin{center}
\includegraphics[width=.3\textwidth]{../Figures/rationalEquationToGraph${Version}D.png}
\end{center}
\item \\text{None of the above.}
\end{multicols}
	\end{enumerate}
}
FINISH_HIM
}

# START OF MODULE 8

createQuestion36() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=8
problemNumber=$2
load("../Code/logExp/domainRangeLog.sage")
\end{sagesilent}

% TYPE 1 - Describe the domain/range of Logarithmic functions.
\litem{ \sage{displayStem}
\[ \sage{displayProblem} \]
	\begin{enumerate}[label=\Alph*.]
		\item \( \sage{choices[0]} \)
		\item \( \sage{choices[1]} \)
		\item \( \sage{choices[2]} \)
		\item \( \sage{choices[3]} \)
		\item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion37() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=8
problemNumber=$2
load("../Code/logExp/domainRangeExp.sage")
\end{sagesilent}

% TYPE 2 - Describe the domain/range of Exponential functions.
\litem{ \sage{displayStem}
\[ \sage{displayProblem} \]
	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion38() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=8
problemNumber=$2
load("../Code/logExp/solveByConverting.sage")
\end{sagesilent}
\litem{ \sage{displayStem}
\[ \sage{displayProblem} \]
	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion39() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=8
problemNumber=$2
load("../Code/logExp/solveByLogProperties.sage")
\end{sagesilent}

\litem{ \sage{displayStem}
	\[ \sage{displayProblem} \]
	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion40() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=8
problemNumber = $2
load("../Code/logExp/solveExpDifferentBases.sage")
\end{sagesilent}

\litem{
\sage{displayStem}

\[ \sage{displayProblem} \]

\begin{enumerate}[label=\Alph*.]
\item \( \sage{choices[0]} \)
\item \( \sage{choices[1]} \)
\item \( \sage{choices[2]} \)
\item \( \sage{choices[3]} \)
\item \( \sage{choices[4]} \)
\end{enumerate} }

FINISH_HIM
}

createQuestion41() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/modelingTrack/modelingLinear/identifyModelPopulation.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\begin{tabular}{c|c|c|c|c|c|c|c|c|c}
\textbf{Year} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \tabularnewline
\hline
\textbf{Pop.} & \sage{populations[0]} & \sage{populations[1]} & \sage{populations[2]} & \sage{populations[3]} & \sage{populations[4]} & \sage{populations[5]} & \sage{populations[6]} & \sage{populations[7]} & \sage{populations[8]}
\end{tabular}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion42() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/modelingTrack/modelingLinear/domainLinear.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion43() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/modelingTrack/modelingLinear/constructLinearModel1.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion44() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/modelingTrack/modelingLinear/constructLinearModel2.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion45() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/modelingTrack/modelingLinear/constructLinearModel3.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion46() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/modelingTrack/modelingPower/identifyModelPopulation.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\begin{tabular}{c|c|c|c|c|c|c|c|c|c}
\textbf{Year} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \tabularnewline
\hline
\textbf{Pop.} & \sage{populations[0]} & \sage{populations[1]} & \sage{populations[2]} & \sage{populations[3]} & \sage{populations[4]} & \sage{populations[5]} & \sage{populations[6]} & \sage{populations[7]} & \sage{populations[8]}
\end{tabular}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion47() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/modelingTrack/modelingPower/identifyModelVariation.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion48() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/modelingTrack/modelingPower/constructDirectModel.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion49() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/modelingTrack/modelingPower/constructIndirectModel.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion50() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/modelingTrack/modelingPower/constructJointModel.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion51() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/modelingTrack/modelingLogExp/identifyModelPopulation.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\begin{tabular}{c|c|c|c|c|c|c|c|c|c}
\textbf{Year} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \tabularnewline
\hline
\textbf{Pop.} & \sage{populations[0]} & \sage{populations[1]} & \sage{populations[2]} & \sage{populations[3]} & \sage{populations[4]} & \sage{populations[5]} & \sage{populations[6]} & \sage{populations[7]} & \sage{populations[8]}
\end{tabular}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion52() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/modelingTrack/modelingLogExp/identifyModelGraph.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\begin{center}
\includegraphics[width = 0.3\textwidth]{../Figures/identifyModelGraphScatterplot${Version}.png}
\end{center}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion53() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/modelingTrack/modelingLogExp/constructBacteriaGrowth.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

  \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion54() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/modelingTrack/modelingLogExp/constructTemperatureModel.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion55() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/modelingTrack/modelingLogExp/constructHalfLifeModel.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion56() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/modelingTrack/solvingProblems/identifyModelGraph.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\begin{center}
\includegraphics[width = 0.3\textwidth]{../Figures/identifyModelGraphScatterplot${Version}.png}
\end{center}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion57() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/modelingTrack/solvingProblems/constructModelMixed.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion58() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/modelingTrack/solvingProblems/solveModelLinear.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion59() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/modelingTrack/solvingProblems/solveModelPower.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion60() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/modelingTrack/solvingProblems/solveModelExp.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion61() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/calculusTrack/operationsOnFunctions/domainAfterOperating.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion62() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/calculusTrack/operationsOnFunctions/functionComposition.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion63() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/calculusTrack/operationsOnFunctions/determine1to1.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion64() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/calculusTrack/operationsOnFunctions/findInversePolyOrRadical.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion65() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=9
problemNumber=$2
load("../Code/calculusTrack/operationsOnFunctions/findInverseLogOrExp.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion66() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/calculusTrack/syntheticDivision/syntheticDivision.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion67() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/calculusTrack/syntheticDivision/syntheticDivisionMissingTerms.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion68() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/calculusTrack/syntheticDivision/possibleRoots.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion69() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/calculusTrack/syntheticDivision/factorUsingSynthetic2Integers.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion70() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=10
problemNumber=$2
load("../Code/calculusTrack/syntheticDivision/factorUsingSynthetic2Rationals.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion71() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/calculusTrack/introToLimits/interpretLimit.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \sage{displayProblem}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion72() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/calculusTrack/introToLimits/oneSidedLimits.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion73() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/calculusTrack/introToLimits/evaluateLimitGraphically.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\begin{center}
 \includegraphics[width=.3\textwidth]{../Figures/evaluateLimitGraph1.png}
 \end{center}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion74() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/calculusTrack/introToLimits/evaluateLimitAnalyticalEasy.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion75() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=11
problemNumber=$2
load("../Code/calculusTrack/introToLimits/evaluateLimitAnalyticalHard.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion76() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/calculusTrack/graphingRationalFunctions/identifyHoles.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion77() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/calculusTrack/graphingRationalFunctions/identifyVAs.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion78() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/calculusTrack/graphingRationalFunctions/identifyHAs.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion79() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
load("../Code/calculusTrack/graphingRationalFunctions/identifyOAs.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

 \[ \sage{displayProblem} \]

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion80() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  TypeList=("A" "B" "C")
  TYPE=${TypeList[$(( $RANDOM %3 ))]}
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=12
problemNumber=$2
type= "${TYPE}"
load("../Code/calculusTrack/graphingRationalFunctions/identifyGraphOfRationalFunction.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\begin{center}
 \includegraphics[width=.5\textwidth]{../Figures/identifyRationalGraph${TYPE}.png}
\end{center}

	\begin{enumerate}[label=\Alph*.]
  \item \( \sage{choices[0]} \)
  \item \( \sage{choices[1]} \)
  \item \( \sage{choices[2]} \)
  \item \( \sage{choices[3]} \)
  \item \( \sage{choices[4]} \)
	\end{enumerate}
}
FINISH_HIM
}

createQuestion() {
  Version=$1
  ProblemNumber=$2
  ProblemCounter=$3
  FileName=$4
  if [ $ProblemNumber -eq 1 ]; then
    createQuestion1 $1 $3 $4
  elif [ $ProblemNumber -eq 2 ]; then
    createQuestion2 $1 $3 $4
  elif [ $ProblemNumber -eq 3 ]; then
    createQuestion3 $1 $3 $4
  elif [ $ProblemNumber -eq 4 ]; then
    createQuestion4 $1 $3 $4
  elif [ $ProblemNumber -eq 5 ]; then
    createQuestion5 $1 $3 $4
  elif [ $ProblemNumber -eq 6 ]; then
    createQuestion6 $1 $3 $4
  elif [ $ProblemNumber -eq 7 ]; then
    createQuestion7 $1 $3 $4
  elif [ $ProblemNumber -eq 8 ]; then
    createQuestion8 $1 $3 $4
  elif [ $ProblemNumber -eq 9 ]; then
    createQuestion9 $1 $3 $4
  elif [ $ProblemNumber -eq 10 ]; then
    createQuestion10 $1 $3 $4
  elif [ $ProblemNumber -eq 11 ]; then
    createQuestion11 $1 $3 $4
  elif [ $ProblemNumber -eq 12 ]; then
    createQuestion12 $1 $3 $4
  elif [ $ProblemNumber -eq 13 ]; then
    createQuestion13 $1 $3 $4
  elif [ $ProblemNumber -eq 14 ]; then
    createQuestion14 $1 $3 $4
  elif [ $ProblemNumber -eq 15 ]; then
    createQuestion15 $1 $3 $4
  elif [ $ProblemNumber -eq 16 ]; then
    createQuestion16 $1 $3 $4
  elif [ $ProblemNumber -eq 17 ]; then
    createQuestion17 $1 $3 $4
  elif [ $ProblemNumber -eq 18 ]; then
    createQuestion18 $1 $3 $4
  elif [ $ProblemNumber -eq 19 ]; then
    createQuestion19 $1 $3 $4
  elif [ $ProblemNumber -eq 20 ]; then
    createQuestion20 $1 $3 $4
  elif [ $ProblemNumber -eq 21 ]; then
    createQuestion21 $1 $3 $4
  elif [ $ProblemNumber -eq 22 ]; then
    createQuestion22 $1 $3 $4
  elif [ $ProblemNumber -eq 23 ]; then
    createQuestion23 $1 $3 $4
  elif [ $ProblemNumber -eq 24 ]; then
    createQuestion24 $1 $3 $4
  elif [ $ProblemNumber -eq 25 ]; then
    createQuestion25 $1 $3 $4
  elif [ $ProblemNumber -eq 26 ]; then
    createQuestion26 $1 $3 $4
  elif [ $ProblemNumber -eq 27 ]; then
    createQuestion27 $1 $3 $4
  elif [ $ProblemNumber -eq 28 ]; then
    createQuestion28 $1 $3 $4
  elif [ $ProblemNumber -eq 29 ]; then
    createQuestion29 $1 $3 $4
  elif [ $ProblemNumber -eq 30 ]; then
    createQuestion30 $1 $3 $4
  elif [ $ProblemNumber -eq 31 ]; then
    createQuestion31 $1 $3 $4
  elif [ $ProblemNumber -eq 32 ]; then
    createQuestion32 $1 $3 $4
  elif [ $ProblemNumber -eq 33 ]; then
    createQuestion33 $1 $3 $4
  elif [ $ProblemNumber -eq 34 ]; then
    createQuestion34 $1 $3 $4
  elif [ $ProblemNumber -eq 35 ]; then
    createQuestion35 $1 $3 $4
  elif [ $ProblemNumber -eq 36 ]; then
    createQuestion36 $1 $3 $4
  elif [ $ProblemNumber -eq 37 ]; then
    createQuestion37 $1 $3 $4
  elif [ $ProblemNumber -eq 38 ]; then
    createQuestion38 $1 $3 $4
  elif [ $ProblemNumber -eq 39 ]; then
    createQuestion39 $1 $3 $4
  elif [ $ProblemNumber -eq 40 ]; then
    createQuestion40 $1 $3 $4
  elif [ $ProblemNumber -eq 41 ]; then
    createQuestion41 $1 $3 $4
  elif [ $ProblemNumber -eq 42 ]; then
    createQuestion42 $1 $3 $4
  elif [ $ProblemNumber -eq 43 ]; then
    createQuestion43 $1 $3 $4
  elif [ $ProblemNumber -eq 44 ]; then
    createQuestion44 $1 $3 $4
  elif [ $ProblemNumber -eq 45 ]; then
    createQuestion45 $1 $3 $4
  elif [ $ProblemNumber -eq 46 ]; then
    createQuestion46 $1 $3 $4
  elif [ $ProblemNumber -eq 47 ]; then
    createQuestion47 $1 $3 $4
  elif [ $ProblemNumber -eq 48 ]; then
    createQuestion48 $1 $3 $4
  elif [ $ProblemNumber -eq 49 ]; then
    createQuestion49 $1 $3 $4
  elif [ $ProblemNumber -eq 50 ]; then
    createQuestion50 $1 $3 $4
  elif [ $ProblemNumber -eq 51 ]; then
    createQuestion51 $1 $3 $4
  elif [ $ProblemNumber -eq 52 ]; then
    createQuestion52 $1 $3 $4
  elif [ $ProblemNumber -eq 53 ]; then
    createQuestion53 $1 $3 $4
  elif [ $ProblemNumber -eq 54 ]; then
    createQuestion54 $1 $3 $4
  elif [ $ProblemNumber -eq 55 ]; then
    createQuestion55 $1 $3 $4
  elif [ $ProblemNumber -eq 56 ]; then
    createQuestion56 $1 $3 $4
  elif [ $ProblemNumber -eq 57 ]; then
    createQuestion57 $1 $3 $4
  elif [ $ProblemNumber -eq 58 ]; then
    createQuestion58 $1 $3 $4
  elif [ $ProblemNumber -eq 59 ]; then
    createQuestion59 $1 $3 $4
  elif [ $ProblemNumber -eq 60 ]; then
    createQuestion60 $1 $3 $4
  elif [ $ProblemNumber -eq 61 ]; then
    createQuestion61 $1 $3 $4
  elif [ $ProblemNumber -eq 62 ]; then
    createQuestion62 $1 $3 $4
  elif [ $ProblemNumber -eq 63 ]; then
    createQuestion63 $1 $3 $4
  elif [ $ProblemNumber -eq 64 ]; then
    createQuestion64 $1 $3 $4
  elif [ $ProblemNumber -eq 65 ]; then
    createQuestion65 $1 $3 $4
  elif [ $ProblemNumber -eq 66 ]; then
    createQuestion66 $1 $3 $4
  elif [ $ProblemNumber -eq 67 ]; then
    createQuestion67 $1 $3 $4
  elif [ $ProblemNumber -eq 68 ]; then
    createQuestion68 $1 $3 $4
  elif [ $ProblemNumber -eq 69 ]; then
    createQuestion69 $1 $3 $4
  elif [ $ProblemNumber -eq 70 ]; then
    createQuestion70 $1 $3 $4
  elif [ $ProblemNumber -eq 71 ]; then
    createQuestion71 $1 $3 $4
  elif [ $ProblemNumber -eq 72 ]; then
    createQuestion72 $1 $3 $4
  elif [ $ProblemNumber -eq 73 ]; then
    createQuestion73 $1 $3 $4
  elif [ $ProblemNumber -eq 74 ]; then
    createQuestion74 $1 $3 $4
  elif [ $ProblemNumber -eq 75 ]; then
    createQuestion75 $1 $3 $4
  elif [ $ProblemNumber -eq 76 ]; then
    createQuestion76 $1 $3 $4
  elif [ $ProblemNumber -eq 77 ]; then
    createQuestion77 $1 $3 $4
  elif [ $ProblemNumber -eq 78 ]; then
    createQuestion78 $1 $3 $4
  elif [ $ProblemNumber -eq 79 ]; then
    createQuestion79 $1 $3 $4
  elif [ $ProblemNumber -eq 80 ]; then
    createQuestion80 $1 $3 $4
  else
    echo "An invalid problem number was input. Please try again."
  fi
}

createFinalQuestion() {
  Version=$1
  ProblemNumber=$2
  FileName=$3
  /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\litem{
What version of the exam are you taking?

\begin{enumerate}[label=\Alph*.]
\item A
\item B
\item C
\end{enumerate} }

FINISH_HIM
}

# Function to check if item already exists in array
function checkArray
{
  for item in ${QuestionList[@]}
  do
    [[ "$item" == "$1" ]] && return 0 # Exists in QuestionList
  done
  return 1 # Not found
}

createModuleBodyTex() {
  MODULEVERSION=$1
  STARTENUMERATEAT=$2
  FILENAME=$3
  # Shuffle array
  # Contents of array src are shuffled randomly and result is stored in destination array
  # -------------------------------------------
  Q1=$((${STARTENUMERATEAT} + 1))
  Q2=$((${STARTENUMERATEAT} + 2))
  Q3=$((${STARTENUMERATEAT} + 3))
  Q4=$((${STARTENUMERATEAT} + 4))
  Q5=$((${STARTENUMERATEAT} + 5))
  IFS=$'\n'
  src=( ${Q1} ${Q2} ${Q3} ${Q4} ${Q5})
  QuestionList=()
  # Show original array
  echo "${src[@]}"
  # Main loop
  while [ "${#QuestionList[@]}" -ne "${#src[@]}" ]
  do
      rand=$[ $RANDOM % ${#src[@]} ]
      checkArray "${src[$rand]}" || QuestionList=(${QuestionList[@]} "${src[$rand]}")
  done
  echo "${QuestionList[@]}"
  QuestionCounter=$((${STARTENUMERATEAT} + 1))
  for question in ${QuestionList[@]}
  do
    createQuestion $1 $question $QuestionCounter $3
    QuestionCounter=$(($QuestionCounter + 1))
  done
}

createFinalExamHeading() {
  VERSION=$1
  SEMESTER=$2
  FileName=$3
  /bin/cat > /${DIR}/buildExams/${FileName}${VERSION}.tex << FINISH_HIM

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
\lhead{}
\chead{MAC 1105 Final Exam - Modules 1-8}
\rhead{}
\lfoot{${SEMESTER}}
\cfoot{}
\rfoot{Version ${VERSION}}

\begin{document}
\pagestyle{fancy}

\begin{sagesilent}
load("../Code/generalPurposeMethods.sage")
load("../Code/keyGeneration.sage")
keyFileName = "${FileName}"
version = "${VERSION}"
\end{sagesilent}
\vspace*{0.5mm}

\begin{enumerate}

FINISH_HIM
}

# This creates the end of each Module .tex file.
createFinalExamEnding() {
  VERSION=$1
  FileName=$2
  /bin/cat >> /${DIR}/buildExams/${FileName}${VERSION}.tex << FINISH_HIM

\end{enumerate}

\end{document}

FINISH_HIM
}

generateFinalExamAllVersions() {
    Password=$1
    Semester=$2
    FileName=$3
    RESULT=1
    # Shuffle array
    # Contents of array src are shuffled randomly and result is stored in destination array
    # -------------------------------------------
    IFS=$'\n'
    src=( 1 2 5 6 8 10 12 13 15 16 17 20 21 23 24 26 28 29 32 33 34 36 37 40)
    QuestionList=()
    # Show original array
    echo "${src[@]}"
    # Main loop
    while [ "${#QuestionList[@]}" -ne "${#src[@]}" ]
    do
        rand=$[ $RANDOM % ${#src[@]} ]
        checkArray "${src[$rand]}" || QuestionList=(${QuestionList[@]} "${src[$rand]}")
    done
    echo "${QuestionList[@]}"
    # Creating empty keys for all versions
    for version in A B C
    do
        cd /${DIR}/buildExams/
        createFinalExamHeading $version $2 $3
        problemCounter=1
        for i in "${QuestionList[@]}"
        do
            createQuestion $version $i $problemCounter $3
            problemCounter=$((problemCounter+1))
        done
        createFinalQuestion $version 25 $3
        createFinalExamEnding $version $3
        createAnswerKeyFile $version $2 $3 'FinalExam'
        touch /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
        touch /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
        RESULT=$?
        #This loops until the module runs without errors.
        while [ $RESULT != 0 ]
        do
            createFinalExamHeading $version $2 $3
            problemCounter=1
            for i in "${QuestionList[@]}"
            do
                createQuestion $version $i $problemCounter $3
                problemCounter=$((problemCounter+1))
            done
            createFinalQuestion $version 25 $3
            createFinalExamEnding $version $3
            createAnswerKeyFile $version $2 $3 'FinalExam'
            rm /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
            rm /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
            touch /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
            touch /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
            pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
            sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
            RESULT=$?
        done
        RESULT=1
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        finishAnswerKeyFile $version $3
        cd /${DIR}/Keys/
        pdflatex -file-line-error -halt-on-error /${DIR}/Keys/key${FileName}${version}.tex
        cat /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv >> /${DIR}/Keys/lettersMasterKey${version}.csv
        cat /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv >> /${DIR}/Keys/numbersMasterKey${version}.csv
    done
    #Copy/Pastes all completed PDFs to a new folder
    cp /${DIR}/buildExams/*.pdf /${DIR}/CompleteExam/PDFs
    cd /${DIR}/CompleteExam/PDFs
    for version in A B C
    do
        # Locks PDFs
        pdftk ${FileName}${version}.pdf output ../LockedPDFs/${FileName}${version}.pdf owner_pw SGS user_pw ${PASSWORD}
    done
}

generateModuleAllVersions() {
    MODULENUMBER=$1
    EXAMNUMBER=$2
    SEMESTER=$3
    STARTENUMERATEAT=$4
    LONGNAME=$5
    PASSWORD=$6
    FileName=$7
    RESULT=1
    FINALRESULT=1
    # Creating empty keys for all versions
    for version in A B C
    do
        cd /${DIR}/buildExams/
        createExamHeading $version $2 $3 $4 $5 $7
        createModuleBodyTex $version $4 $7
        createExamEnding $version $7
        createAnswerKeyFile $version $3 $7 $5
        touch /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
        touch /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
        RESULT=$?
        #This loops until the module runs without errors.
        while [ $RESULT != 0 ]; do
            createExamHeading $version $2 $3 $4 $5 $7
            createModuleBodyTex $version $4 $7
            createExamEnding $version $7
            createAnswerKeyFile $version $3 $7 $5
            rm /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
            rm /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
            touch /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv
            touch /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv
            sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
            RESULT=$?
        done
        RESULT=1
        FINALRESULT=1
        pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        FINALRESULT=$?
        # This was necessary to clear an error where the pdflatex thought there was an error because the sage had not updated yet.
        if [ $FINALRESULT != 0 ]; then
          rm /${DIR}/buildExams/${FileName}${version}.sagetex.sout
          sage /${DIR}/buildExams/${FileName}${version}.sagetex.sage
          pdflatex -file-line-error -halt-on-error /${DIR}/buildExams/${FileName}${version}.tex
        else
          echo "It worked the first time!"
        fi
        finishAnswerKeyFile $version $7
        cd /${DIR}/Keys/
        pdflatex -file-line-error -halt-on-error /${DIR}/Keys/key${FileName}${version}.tex
        cat /${DIR}/Keys/lettersAnswerKey${FileName}${version}.csv >> /${DIR}/Keys/lettersMasterKey${version}.csv
        cat /${DIR}/Keys/numbersAnswerKey${FileName}${version}.csv >> /${DIR}/Keys/numbersMasterKey${version}.csv
    done
    # Copy/Pastes all completed PDFs to a new folder
    cp /${DIR}/buildExams/*.pdf /${DIR}/CompleteExam/PDFs
    copyKeys $7
    cd /${DIR}/CompleteExam/PDFs
    for version in A B C
    do
        # Locks PDFs
        pdftk ${FileName}${version}.pdf output ../LockedPDFs/${FileName}${version}.pdf owner_pw SGS user_pw ${PASSWORD}
    done
    cd
}

copyKeys() {
    cp /${DIR}/Keys/*.pdf /${DIR}/CompleteExam/Keys/
    touch /${DIR}/CompleteExam/Keys/masterKeyALL.csv
    for version in A B C
    do
        cp /${DIR}/Keys/lettersMasterKey${version}.csv /${DIR}/CompleteExam/Keys/
        # cp /${DIR}/Keys/numbersMasterKey${version}.csv /${DIR}/CompleteExam/Keys/
    done
    # cat /${DIR}/CompleteExam/Keys/lettersMasterKeyA.csv /${DIR}/CompleteExam/Keys/lettersMasterKeyB.csv /${DIR}/CompleteExam/Keys/lettersMasterKeyC.csv > /${DIR}/CompleteExam/Keys/masterKeyALL.csv
}

clearOldVersions() {
    # Clears old keys and pdfs
    rm -rf /${DIR}/Keys/*
    rm -rf /${DIR}/buildExams/*
    rm -rf /${DIR}/CompleteExam/Keys/*
    rm -rf /${DIR}/CompleteExam/PDFs/*
    rm -rf /${DIR}/CompleteExam/LockedPDFs/*
}

clearOldVersions
setSemester=$1
setPassword=$2
setExamNumber=$3

if [ "$1" == "debug" ]; then
    if [ "$3" == 1 ]; then
        generateModuleAllVersions 1 $setExamNumber $setPassword 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" "debug" "Module1"
        copyKeys
        exit -1
    elif [ "$3" == 2 ]; then
        generateModuleAllVersions 2 $setExamNumber $setPassword 5 "Module\,2\,-\,Linear\,Functions" "debug" "Module2"
        copyKeys
        exit -1
    elif [ "$3" == 3 ]; then
        generateModuleAllVersions 3 $setExamNumber $setPassword 10 "Module\,3\,-\,Inequalities" "debug" "Module3"
        copyKeys
        exit -1
    elif [ "$3" == 4 ]; then
        generateModuleAllVersions 4 $setExamNumber $setPassword 15 "Module\,4\,-\,Quadratic\,Functions" "debug" "Module4"
        copyKeys
        exit -1
    elif [ "$3" == 5 ]; then
        generateModuleAllVersions 5 $setExamNumber $setPassword 20 "Module\,5\,-\,Radical\,Functions" "debug" "Module5"
        copyKeys
        exit -1
    elif [ "$3" == 6 ]; then
        generateModuleAllVersions 6 $setExamNumber $setPassword 25 "Module\,6\,-\,Polynomial\,Functions" "debug" "Module6"
        copyKeys
        exit -1
    elif [ "$3" == 7 ]; then
        generateModuleAllVersions 7 $setExamNumber $setPassword 30 "Module\,7\,-\,Rational\,Functions" "debug" "Module7"
        copyKeys
        exit -1
    elif [ "$3" == 8 ]; then
        generateModuleAllVersions 8 $setExamNumber $setPassword 35 "Module\,8\,-\,Logarithmic\,and\,Exponential\,Functions" "debug" "Module8"
        copyKeys
        exit -1
    elif [ "$3" == 9 ]; then
        generateModuleAllVersions "9M" $setExamNumber $setPassword 40 "Module\,9M\,-\,Modeling\,Linear\,Functions" "debug" "Module9M"
        copyKeys
        exit -1
    elif [ "$3" == 10 ]; then
        generateModuleAllVersions "10M" $setExamNumber $setPassword 45 "Module\,10M\,-\,Modeling\,with\,Power\,Functions" "debug" "Module10M"
        copyKeys
        exit -1
    elif [ "$3" == 11 ]; then
        generateModuleAllVersions "11M" $setExamNumber $setPassword 50 "Module\,11M\,-\,Modeling\,with\,Log\,and\,Exp\,Functions" "debug" "Module11M"
        copyKeys
        exit -1
    elif [ "$3" == 12 ]; then
        generateModuleAllVersions "12M" $setExamNumber $setPassword 55 "Module\,12M\,-\,Solving\,Word\,Problems" "debug" "Module12M"
        copyKeys
        exit -1
    elif [ "$3" == 13 ]; then
        generateModuleAllVersions "9L" $setExamNumber $setPassword 60 "Module\,9L\,-\,Operations\,on\,Functions" "debug" "Module9L"
        copyKeys
        exit -1
    elif [ "$3" == 14 ]; then
        generateModuleAllVersions "10L" $setExamNumber $setPassword 65 "Module\,10L\,-\,Synthetic\,Division" "debug" "Module10L"
        copyKeys
        exit -1
    elif [ "$2" == 15 ]; then
        generateModuleAllVersions "11L" $setExamNumber $setPassword 70 "Module\,11L\,-\,Introduction\,to\,Limits" "debug" "Module11L"
        copyKeys
        exit -1
    elif [ "$3" == 16 ]; then
        generateModuleAllVersions "12L" $setExamNumber $setPassword 75 "Module\,12L\,-\,Graphing\,Rational\,Functions" "debug" "Module12L"
        copyKeys
        exit -1
    else
        echo "You tried to run the debug mode but did not input a valid module number. Modeling modules are 9-12 and Limits modules are 13-16."
        exit -1
    fi
else
    while [ "$1" == "" ] || [ "$2" == "" ] || [ "$3" == "" ]; do
        echo -e "\nArguments for the exam are missing. The arguments are Semester, Password, and Exam Number. \n \nPlease put the semester in parentheses and make sure it has no spaces, such as 'Spring\,2020'. \nThe password should be a single word in parentheses, such as 'Password1'. \nThe exam number should be 1, 2, 3, 4, 5, 6, or 7 (final exam). The number of Modules generated is based on the exam number."
        echo -e "\n If you meant to debug, make the first argument 'debug', the second argument the Semester, and the third argument the single module you want to run. Modeling modules are 9-12 and Limits modules are 13-16."
        exit -1
    done

    if [ "$3" == 1 ]; then
        generateModuleAllVersions 1 $setExamNumber $setSemester 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" $setPassword "Module1"
        generateModuleAllVersions 2 $setExamNumber $setSemester 5 "Module\,2\,-\,Linear\,Functions" $setPassword "Module2"
        generateModuleAllVersions 3 $setExamNumber $setSemester 10 "Module\,3\,-\,Inequalities" $setPassword "Module3"
    elif [ "$3" == 2 ]; then
        generateModuleAllVersions 1 $setExamNumber $setSemester 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" $setPassword "Module1"
        generateModuleAllVersions 2 $setExamNumber $setSemester 5 "Module\,2\,-\,Linear\,Functions" $setPassword "Module2"
        generateModuleAllVersions 3 $setExamNumber $setSemester 10 "Module\,3\,-\,Inequalities" $setPassword "Module3"
        generateModuleAllVersions 4 $setExamNumber $setSemester 15 "Module\,4\,-\,Quadratic\,Functions" $setPassword "Module4"
        generateModuleAllVersions 5 $setExamNumber $setSemester 20 "Module\,5\,-\,Radical\,Functions" $setPassword "Module5"
        generateModuleAllVersions 6 $setExamNumber $setSemester 25 "Module\,6\,-\,Polynomial\,Functions" $setPassword "Module6"
    elif [ "$3" == 3 ]; then
        generateModuleAllVersions 1 $setExamNumber $setSemester 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" $setPassword "Module1"
        generateModuleAllVersions 2 $setExamNumber $setSemester 5 "Module\,2\,-\,Linear\,Functions" $setPassword "Module2"
        generateModuleAllVersions 3 $setExamNumber $setSemester 10 "Module\,3\,-\,Inequalities" $setPassword "Module3"
        generateModuleAllVersions 4 $setExamNumber $setSemester 15 "Module\,4\,-\,Quadratic\,Functions" $setPassword "Module4"
        generateModuleAllVersions 5 $setExamNumber $setSemester 20 "Module\,5\,-\,Radical\,Functions" $setPassword "Module5"
        generateModuleAllVersions 6 $setExamNumber $setSemester 25 "Module\,6\,-\,Polynomial\,Functions" $setPassword "Module6"
        generateModuleAllVersions 7 $setExamNumber $setSemester 30 "Module\,7\,-\,Rational\,Functions" $setPassword "Module7"
        generateModuleAllVersions 8 $setExamNumber $setSemester 35 "Module\,8\,-\,Logarithmic\,and\,Exponential\,Functions" $setPassword "Module8"
        generateModuleAllVersions "9M" $setExamNumber $setSemester 40 "Module\,9M\,-\,Modeling\,Linear\,Functions" $setPassword "Module9M"
        generateModuleAllVersions "9L" $setExamNumber $setSemester 60 "Module\,9L\,-\,Operations\,on\,Functions" $setPassword "Module9L"
    elif [ "$3" == 4 ] || [ "$3" == 5 ] || [ "$3" == 6 ]; then
        generateModuleAllVersions 1 $setExamNumber $setSemester 0 "Module\,1\,-\,Real\,and\,Complex\,Numbers" $setPassword "Module1"
        generateModuleAllVersions 2 $setExamNumber $setSemester 5 "Module\,2\,-\,Linear\,Functions" $setPassword "Module2"
        generateModuleAllVersions 3 $setExamNumber $setSemester 10 "Module\,3\,-\,Inequalities" $setPassword "Module3"
        generateModuleAllVersions 4 $setExamNumber $setSemester 15 "Module\,4\,-\,Quadratic\,Functions" $setPassword "Module4"
        generateModuleAllVersions 5 $setExamNumber $setSemester 20 "Module\,5\,-\,Radical\,Functions" $setPassword "Module5"
        generateModuleAllVersions 6 $setExamNumber $setSemester 25 "Module\,6\,-\,Polynomial\,Functions" $setPassword "Module6"
        generateModuleAllVersions 7 $setExamNumber $setSemester 30 "Module\,7\,-\,Rational\,Functions" $setPassword "Module7"
        generateModuleAllVersions 8 $setExamNumber $setSemester 35 "Module\,8\,-\,Logarithmic\,and\,Exponential\,Functions" $setPassword "Module8"
        generateModuleAllVersions "9M" $setExamNumber $setSemester 40 "Module\,9M\,-\,Modeling\,Linear\,Functions" $setPassword "Module9M"
        generateModuleAllVersions "10M" $setExamNumber $setSemester 45 "Module\,10M\,-\,Modeling\,with\,Power\,Functions" $setPassword "Module10M"
        generateModuleAllVersions "11M" $setExamNumber $setSemester 50 "Module\,11M\,-\,Modeling\,with\,Log\,and\,Exp\,Functions" $setPassword "Module11M"
        generateModuleAllVersions "12M" $setExamNumber $setSemester 55 "Module\,12M\,-\,Solving\,Word\,Problems" $setPassword "Module12M"
        generateModuleAllVersions "9L" $setExamNumber $setSemester 60 "Module\,9L\,-\,Operations\,on\,Functions" $setPassword "Module9L"
        generateModuleAllVersions "10L" $setExamNumber $setSemester 65 "Module\,10L\,-\,Synthetic\,Division" $setPassword "Module10L"
        generateModuleAllVersions "11L" $setExamNumber $setSemester 70 "Module\,11L\,-\,Introduction\,to\,Limits" $setPassword "Module11L"
        generateModuleAllVersions "12L" $setExamNumber $setSemester 75 "Module\,12L\,-\,Graphing\,Rational\,Functions" $setPassword "Module12L"
    else
        generateFinalExamAllVersions $setPassword $setSemester "FinalExam"
    fi
    copyKeys
fi
