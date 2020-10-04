# Create different types of questions
function listAllQuestions {
    ### List of all questions for each module
    module1questionList=( 'divideComplex' 'multiplyComplex' 'orderOfOperations' 'subgroupComplex' 'subgroupReal')
    module2questionList=( 'linearGraphToStandard' 'linearParOrPer' 'linearTwoPoints' 'solveIntegerLinear' 'solveRationalLinear' )
    module3questionList=( 'describeSet' 'solveCompoundAND' 'solveCompoundOR' 'solveIntegerInequality' 'solveRationalInequality')
    module4questionList=( 'factorLeadingOver1Composite' 'quadraticEquationToGraph' 'quadraticFormula' 'quadraticGraphToEquation' 'solveQuadraticFactorComposites')
    module5questionList=( 'domainRadical' 'radicalEquationToGraph' 'radicalGraphToEquation' 'solveRadicalLinear' 'solveRadicalQuadratic')
    module6questionList=( 'constructPolyComplex' 'constructPolyRationals' 'polyEndBehavior' 'polyGraphToFunction' 'polyZeroBehavior')
    module7questionList=( 'domainRational' 'rationalEquationToGraph' 'rationalGraphToEquation' 'solveRationalLinear' 'solveRationalQuadratic')
    module8questionList=( 'domainRangeExp' 'domainRangeLog' 'solveByConverting' 'solveByLogProperties' 'solveExpDifferentBases' )
    module9MquestionList=( 'domainLinearModel' 'constructLinearModelMixture' 'constructLinearModelCostsProfitsRevenue' 'constructLinearModelDistanceAndRate' 'identifyModelPopulation' )
    module10MquestionList=( 'constructDirectModel' 'constructIndirectModel' 'constructJointModel' 'identifyModelPopulation' 'identifyModelVariation')
    module11MquestionList=( 'constructBacteriaGrowth' 'constructHalfLifeModel' 'constructTemperatureModel' 'identifyModelGraph11' 'identifyModelPopulation')
    module12MquestionList=( 'constructModelMixed' 'identifyModelGraph12' 'solveModelExp' 'solveModelLinear' 'solveModelPower' )
    module9LquestionList=( 'determine1to1' 'domainAfterOperating' 'findInverseLogOrExp' 'findInversePolyOrRadical' 'functionComposition' )
    module10LquestionList=( 'factorUsingSynthetic2Integers' 'factorUsingSynthetic2Rationals' 'possibleRoots' 'syntheticDivision' 'syntheticDivisionMissingTerms' )
    module11LquestionList=( 'evaluateLimitAnalyticalEasy' 'evaluateLimitAnalyticalHard' 'evaluateLimitGraphically' 'interpretLimit' 'oneSidedLimits')
    module12LquestionList=( 'identifyGraphOfRationalFunction' 'identifyHAs' 'identifyHoles' 'identifyOAs' 'identifyVAs' )
}


function chooseQuestionStructure {
    # Defined just to describe the variables chooseQuestionStructure takes.
    moduleNumber=$1
    version=$2
    questionNumber=$3
    codeFolderName=$4
    codeName=$5
    fileNamePrefix=$6
    createBasicStructureQuestionList=( 'divideComplex' 'multiplyComplex' 'orderOfOperations' 'subgroupComplex' 'subgroupReal' 'linearParOrPer' 'linearTwoPoints' 'solveIntegerLinear' 'solveRationalLinear' 'describeSet' 'solveCompoundAND' 'solveCompoundOR' 'solveIntegerInequality' 'solveRationalInequality' 'factorLeadingOver1Composite' 'quadraticFormula' 'solveQuadraticFactorComposites' 'domainRadical' 'solveRadicalLinear' 'solveRadicalQuadratic' 'constructPolyComplex' 'constructPolyRationals' 'domainRational' 'solveRationalLinear' 'solveRationalQuadratic' 'domainRangeExp' 'domainRangeLog' 'solveByConverting' 'solveByLogProperties' 'solveExpDifferentBases' 'determine1to1' 'domainAfterOperating' 'findInverseLogOrExp' 'findInversePolyOrRadical' 'functionComposition' 'factorUsingSynthetic2Integers' 'factorUsingSynthetic2Rationals' 'possibleRoots' 'syntheticDivision' 'syntheticDivisionMissingTerms' 'evaluateLimitAnalyticalEasy' 'evaluateLimitAnalyticalHard' 'oneSidedLimits' 'identifyHAs' 'identifyHoles' 'identifyOAs' 'identifyVAs' )
    displayNoMathModeProblemQuestionList=( 'domainLinearModel' 'constructLinearModelMixture' 'constructLinearModelCostsProfitsRevenue' 'constructLinearModelDistanceAndRate' 'constructDirectModel' 'constructIndirectModel' 'constructJointModel' 'constructBacteriaGrowth' 'constructHalfLifeModel' 'constructTemperatureModel' 'constructModelMixed' 'solveModelExp' 'solveModelLinear' 'solveModelPower' 'interpretLimit' )
    displayNoMathModeProblem4OptionsQuestionList=( 'identifyModelVariation' )
    displayGraphProblemQuestionList=( 'linearGraphToStandard' 'quadraticGraphToEquation' 'radicalGraphToEquation' 'polyGraphToFunction' 'rationalGraphToEquation' 'identifyModelGraph11' 'identifyModelGraph12' 'evaluateLimitGraphically' 'identifyGraphOfRationalFunction' )
    displayTableProblemSpecialQuestionList=( 'identifyModelPopulation' )
    createMathProblemAnd4Graph1TextOptionsQuestionList=( 'quadraticEquationToGraph' 'radicalEquationToGraph' 'rationalEquationToGraph' )
    createMathProblemAnd4GraphOptionsQuestionList=( 'polyEndBehavior' 'polyZeroBehavior')
    if [[ " ${createBasicStructureQuestionList[@]} " =~ " ${codeName} " ]]; then
        createBasicStructure $1 $2 $3 $4 $5 $6
    elif [[ " ${displayNoMathModeProblemQuestionList[@]} " =~ " ${codeName} " ]]; then
        displayNoMathModeProblem $1 $2 $3 $4 $5 $6
    elif [[ " ${displayNoMathModeProblem4OptionsQuestionList[@]} " =~ " ${codeName} " ]]; then
        displayNoMathModeProblem4Options $1 $2 $3 $4 $5 $6
    elif [[ " ${displayGraphProblemQuestionList[@]} " =~ " ${codeName} " ]]; then
        displayGraphProblem $1 $2 $3 $4 $5 $6
    elif [[ " ${displayTableProblemSpecialQuestionList[@]} " =~ " ${codeName} " ]]; then
        displayTableProblemSpecial $1 $2 $3 $4 $5 $6
    elif [[ " ${createMathProblemAnd4Graph1TextOptionsQuestionList[@]} " =~ " ${codeName} " ]]; then
        createMathProblemAnd4Graph1TextOptions $1 $2 $3 $4 $5 $6
    elif [[ " ${createMathProblemAnd4GraphOptionsQuestionList[@]} " =~ " ${codeName} " ]]; then
        createMathProblemAnd4GraphOptions $1 $2 $3 $4 $5 $6
    else
        echo "Name of code was not found on question structure list."
        exit $ERRCODE
    fi
}

function createBasicStructure {
    moduleNumber=$1
    version=$2
    questionNumber=$3
    codeFolderName=$4
    codeName=$5
    fileNamePrefix=$6
    /bin/cat >> /${DIR}/buildExams/${fileNamePrefix}${version}.tex << FINISH_HIM
\begin{sagesilent}
moduleNumber="${moduleNumber}"
problemNumber=$3
load("../Code/${codeFolderName}/${codeName}.sage")
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
    moduleNumber=$1
    version=$2
    questionNumber=$3
    codeFolderName=$4
    codeName=$5
    fileNamePrefix=$6
    /bin/cat >> /${DIR}/buildExams/${fileNamePrefix}${version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber="${moduleNumber}"
problemNumber=$3
load("../Code/${codeFolderName}/${codeName}.sage")
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
function displayNoMathModeProblem4Options {
    moduleNumber=$1
    version=$2
    questionNumber=$3
    codeFolderName=$4
    codeName=$5
    fileNamePrefix=$6
    /bin/cat >> /${DIR}/buildExams/${fileNamePrefix}${version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber="${moduleNumber}"
problemNumber=$3
load("../Code/${codeFolderName}/${codeName}.sage")
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
  	\end{enumerate}
  }
FINISH_HIM
}
function displayGraphProblem {
    moduleNumber=$1
    version=$2
    questionNumber=$3
    codeFolderName=$4
    codeName=$5
    fileNamePrefix=$6
    /bin/cat >> /${DIR}/buildExams/${fileNamePrefix}${version}.tex << FINISH_HIM

  \begin{sagesilent}
  moduleNumber="${moduleNumber}"
  problemNumber=$3
  load("../Code/${codeFolderName}/${codeName}.sage")
  \end{sagesilent}

  \litem{ \sage{displayStem}

   \begin{center}
       \includegraphics[width=0.5\textwidth]{../Figures/${codeName}${version}.png}
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
    moduleNumber=$1
    version=$2
    questionNumber=$3
    codeFolderName=$4
    codeName=$5
    fileNamePrefix=$6
    /bin/cat >> /${DIR}/buildExams/${fileNamePrefix}${Version}.tex << FINISH_HIM

  \begin{sagesilent}
  moduleNumber="${moduleNumber}"
  problemNumber=$3
  load("../Code/${codeFolderName}/${codeName}.sage")
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
    moduleNumber=$1
    version=$2
    questionNumber=$3
    codeFolderName=$4
    codeName=$5
    fileNamePrefix=$6
    /bin/cat >> /${DIR}/buildExams/${fileNamePrefix}${version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber="${moduleNumber}"
problemNumber=$3
load("../Code/${codeFolderName}/${codeName}.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

\begin{enumerate}[label=\Alph*.]
    \begin{multicols}{2}
	      \item \includegraphics[width = 0.3\textwidth]{../Figures/${codeName}A${version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${codeName}B${version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${codeName}C${version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${codeName}D${version}.png}
    \end{multicols}
        \item \\text{None of the above.}
\end{enumerate}
}
FINISH_HIM
}
function createMathProblemAnd4GraphOptions {
    moduleNumber=$1
    version=$2
    questionNumber=$3
    codeFolderName=$4
    codeName=$5
    fileNamePrefix=$6
    /bin/cat >> /${DIR}/buildExams/${fileNamePrefix}${version}.tex << FINISH_HIM

\begin{sagesilent}
moduleNumber="${moduleNumber}"
problemNumber=$3
load("../Code/${codeFolderName}/${codeName}.sage")
\end{sagesilent}

\litem{ \sage{displayStem}

\[ \sage{displayProblem} \]

\begin{enumerate}[label=\Alph*.]
    \begin{multicols}{2}
	      \item \includegraphics[width = 0.3\textwidth]{../Figures/${codeName}A${version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${codeName}B${version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${codeName}C${version}.png}
		    \item \includegraphics[width = 0.3\textwidth]{../Figures/${codeName}D${version}.png}
    \end{multicols}
        \item \\text{None of the above.}
\end{enumerate}
}
FINISH_HIM
}
