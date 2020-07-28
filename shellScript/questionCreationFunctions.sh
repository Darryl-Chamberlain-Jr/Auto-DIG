# Create different types of questions

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
