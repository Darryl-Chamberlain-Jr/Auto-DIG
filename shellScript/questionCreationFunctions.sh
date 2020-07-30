# Create different types of questions

function createBasicStructure {
    Version=$1
    ProblemNumber=$2
    FileName=$3
    ModuleNumber=$4
    CodeFolderName=$5
    CodeName=$6
    /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM
\begin{sagesilent}
moduleNumber=$4
problemNumber=$2
load("../Code/${CodeFolderName}/${CodeName}.sage")
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

function displayNoMathModeProblem {
    Version=$1
    ProblemNumber=$2
    FileName=$3
    ModuleNumber=$4
    CodeFolderName=$5
    CodeName=$6
    /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=$4
problemNumber=$2
load("../Code/${CodeFolderName}/${CodeName}.sage")
\end{sagesilent}

  \litem{ \sage{displayStem}

   \begin{center}
      \textit{ \sage{displayProblem} }
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

function displayGraphProblem {
    Version=$1
    ProblemNumber=$2
    FileName=$3
    ModuleNumber=$4
    CodeFolderName=$5
    CodeName=$6
    /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

  \begin{sagesilent}
  moduleNumber=$4
  problemNumber=$2
  load("../Code/${CodeFolderName}/${CodeName}.sage")
  \end{sagesilent}

  \litem{ \sage{displayStem}

   \begin{center}
       \includegraphics[width=0.3\textwidth]{../Figures/${CodeName}${Version}.png}
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

function displayTableProblemSpecial {
    Version=$1
    ProblemNumber=$2
    FileName=$3
    ModuleNumber=$4
    CodeFolderName=$5
    CodeName=$6
    /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

  \begin{sagesilent}
  moduleNumber=$4
  problemNumber=$2
  load("../Code/${CodeFolderName}/${CodeName}.sage")
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
    \item \( \sage{choices[4]} \)
  	\end{enumerate}
  }
FINISH_HIM
}

function createMathProblemAnd4Graph1TextOptions {
    Version=$1
    ProblemNumber=$2
    FileName=$3
    ModuleNumber=$4
    CodeFolderName=$5
    CodeName=$6
    /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=$4
problemNumber=$2
load("../Code/${CodeFolderName}/${CodeName}.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

\begin{enumerate}[label=\Alph*.]
    \begin{multicols}{2}
	      \item \includegraphics[width = 0.3\textwidth]{../Figures/${CodeName}A${Version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${CodeName}B${Version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${CodeName}C${Version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${CodeName}D${Version}.png}
    \end{multicols}
        \item \\text{None of the above.}
\end{enumerate}
}
FINISH_HIM
}

function createMathProblemAnd4GraphOptions {
    Version=$1
    ProblemNumber=$2
    FileName=$3
    ModuleNumber=$4
    CodeFolderName=$5
    CodeName=$6
    /bin/cat >> /${DIR}/buildExams/${FileName}${Version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber=$4
problemNumber=$2
load("../Code/${CodeFolderName}/${CodeName}.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

\begin{enumerate}[label=\Alph*.]
    \begin{multicols}{2}
	      \item \includegraphics[width = 0.3\textwidth]{../Figures/${CodeName}A${Version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${CodeName}B${Version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${CodeName}C${Version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${CodeName}D${Version}.png}
    \end{multicols}
        \item \\text{None of the above.}
\end{enumerate}
}
FINISH_HIM
}
