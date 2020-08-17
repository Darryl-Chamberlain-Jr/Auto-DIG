import random
### printQuestionToExam requires these values from database ###
    # displayStemType [options: String, Math Mode, or Graph]
    # displayStem
    # displayProblemType [options: String, Math Mode, Graph, or Table]
        # For Table type: populations array with 9 entries
    # displayProblem
    # displayOptionsType [options: String, Math Mode, Graph]
    # choices

### printQuestionToKey requires these values from database ###
    # displayStemType [options: String, Math Mode, or Graph]
    # displayStem
    # displayProblemType [options: String, Math Mode, Graph, or Table]
        # For Table type: populations array with 9 entries
    # displayProblem
    # displayOptionsType [options: String, Math Mode, Graph]
    # choices
    # choiceComments
    # solution
    # answerLetter
    # generalComment

### printQuestionToFeedback requires these values from database ###
    # displayStemType [options: String, Math Mode, or Graph]
    # displayStem
    # displayProblemType [options: String, Math Mode, Graph, or Table]
        # For Table type: populations array with 9 entries
    # displayProblem
    # displayOptionsType [options: String, Math Mode, Graph]
    # choiceComments
    # choiceSpecificComments
    # solution
    # answerLetter
    # studentAnswerLetter

def printQuestionToExam(moduleNumber, version, questionNumber, codeFolderName, codeName, fileNamePrefix, rootDirectory):
    examFile = open('/' + str(rootDirectory) + '/buildExams/' + str(fileNamePrefix) + str(version)+ '.tex', 'a')
    examFile.write(r"""
\begin{sagesilent}
moduleNumber="%s"
problemNumber=%s
load("../Code/%s/%s.sage")
\end{sagesilent}

\litem{
""" %(moduleNumber, questionNumber, codeFolderName, codeName) )
    # displayStemType: String, Math Mode, or Graph
    if displayStemType=="String":
        examFile.write(displayStem)
    elif displayStemType=="Math Mode":
        examFile.write("$%s$" %displayStem)
    elif displayStemType=="Graph":
        examFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(codeName, version))
    # displayProblemType: String, Math Mode, Graph, or Table
    if displayProblemType=="String":
        examFile.write(r"""
\begin{center}
    \textit{ %s }
\end{center}
""" %displayProblem)
    elif displayProblemType=="Math Mode":
        examFile.write(r"\[ %s \]" %displayProblem)
    elif displayProblemType=="Graph":
        examFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(codeName, version))
    elif displayProblemType=="Table":
        examFile.write(r"""
\begin{tabular}{c|c|c|c|c|c|c|c|c|c}
\textbf{Year} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \tabularnewline
\hline
\textbf{Pop.} & %s & %s & %s & %s & %s & %s & %s & %s & %s
\end{tabular} """ %(populations[0], populations[1], populations[2], populations[3], populations[4], populations[5], populations[6], populations[7], populations[8]) )
    # Begins enumerate for options
    examFile.write(r"\begin{enumerate}[label=\Alph*.]")
    # displayOptionsType: String, Math Mode, or Graph
    if displayOptionsType=="String":
        for i in range(len(choices)):
            examFile.write(r"\item %s" %choices[i])
    elif displayOptionsType=="Math Mode":
        for i in range(len(choices)):
            examFile.write(r"\( \item %s \)" %choices[i])
    elif displayOptionsType=="Graph":
        examFile.write(r"\begin{multicols}{2}")
        for i in range(len(choices)):
            options=["A", "B", "C", "D", "E", "F", "G", "H"]
            examFile.write(r"\item \includegraphics[width = 0.3\textwidth]{../Figures/%s%s%s.png}" %(codeName, options[i], version))
        examFile.write(r"\end{multicols}")
        examFile.write(r"\item None of the above.")
    examFile.write(r"\end{enumerate} }") # The close bracket ends the litem initiated in the first examFile.write
    # Ends enumerate for options
    examFile.close()
def printQuestionToKey(version, codeName, fileNamePrefix, rootDirectory):
    keyFile = open('../Keys/key' + str(fileNamePrefix) + str(version) + '.tex', 'a')
    keyFile.write(r"\litem{")
    # displayStemType: String, Math Mode, or Graph
    if displayStemType=="String":
        keyFile.write(displayStem)
    elif displayStemType=="Math Mode":
        keyFile.write("$%s$" %displayStem)
    elif displayStemType=="Graph":
        keyFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(codeName, version))
    # displayProblemType: String, Math Mode, Graph, or Table
    if displayProblemType=="String":
        keyFile.write(r"""
\begin{center}
    \textit{ %s }
\end{center}
""" %displayProblem)
    elif displayProblemType=="Math Mode":
        keyFile.write(r"\[ %s \]" %displayProblem)
    elif displayProblemType=="Graph":
        keyFile.write(r"""
\begin{center}
    \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
\end{center}
""" %(codeName, version))
    elif displayProblemType=="Table":
        keyFile.write(r"""
\begin{tabular}{c|c|c|c|c|c|c|c|c|c}
\textbf{Year} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \tabularnewline
\hline
\textbf{Pop.} & %s & %s & %s & %s & %s & %s & %s & %s & %s
\end{tabular} """ %(populations[0], populations[1], populations[2], populations[3], populations[4], populations[5], populations[6], populations[7], populations[8]) )
    # Begins enumerate for options
    keyFile.write(r"\begin{enumerate}[label=\Alph*.]")
    # displayOptionsType: String, Math Mode, or Graph
    if displayOptionsType=="String":
        keyFile.write("The solution is %s, which is option %s." %(solution, answerLetter))
        for i in range(len(choices)):
            keyFile.write(r"\item %s" %choices[i])
            keyFile.write(choiceComments[i])
            keyFile.write()
    elif displayOptionsType=="Math Mode":
        keyFile.write("The solution is \( %s \), which is option %s." %(solution, answerLetter))
        for i in range(len(choices)):
            keyFile.write(r"\( \item %s \)" %choices[i])
            keyFile.write(choiceComments[i])
            keyFile.write()
    elif displayOptionsType=="Graph":
        keyFile.write(r"\begin{multicols}{2}")
        keyFile.write(r"""The solution is the graph below, which is option %s.
\\begin{center}
    \\includegraphics[width=0.3\\textwidth]{../Figures/%s%s%s.png}
\\end{center}""" %(answerLetter, codeName, answerLetter, version) )
        for i in range(len(choices)):
            options=["A", "B", "C", "D", "E", "F", "G", "H"]
            keyFile.write(r"\item \includegraphics[width = 0.3\textwidth]{../Figures/%s%s%s.png}" %(codeName, options[i], version))
        keyFile.write(r"\end{multicols}")
        keyFile.write(r"\item None of the above.")
        keyFile.write(r"\begin{enumerate}[label=\Alph*.]")
        for i in range(len(choiceComments)):
            keyFile.write(r"\item %s" %choiceComments[i])
        keyFile.write(r"\end{enumerate}")
        keyFile.write()
    keyFile.write(r"\textbf{General Comment:} %s" %generalComment)
    keyFile.write(r"\end{enumerate} }") # The close bracket ends the litem initiated in the first keyFile.write
    # Ends enumerate for options
    keyFile.write("}")
    keyFile.close()
    # Adds letter to masterAnswerKeyFile
    lettersAnswerKey = open('../Keys/lettersAnswerKey' + str(keyFileName) + str(version) + '.csv', 'a')
    lettersAnswerKey.write("%s," %answerLetter)
    lettersAnswerKey.close()
def printQuestionToFeedback(version, codeName, fileNamePrefix, rootDirectory):
        feedbackFile = open('../Feedback/feedback' + str(fileNamePrefix) + '.tex', 'a')
        feedbackFile.write(r"\litem{")
        # displayStemType: String, Math Mode, or Graph
        if displayStemType=="String":
            feedbackFile.write(displayStem)
        elif displayStemType=="Math Mode":
            feedbackFile.write("$%s$" %displayStem)
        elif displayStemType=="Graph":
            feedbackFile.write(r"""
    \begin{center}
        \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
    \end{center}
    """ %(codeName, version))
        # displayProblemType: String, Math Mode, Graph, or Table
        if displayProblemType=="String":
            feedbackFile.write(r"""
    \begin{center}
        \textit{ %s }
    \end{center}
    """ %displayProblem)
        elif displayProblemType=="Math Mode":
            feedbackFile.write(r"\[ %s \]" %displayProblem)
        elif displayProblemType=="Graph":
            feedbackFile.write(r"""
    \begin{center}
        \includegraphics[width=0.5\textwidth]{../Figures/%s%s.png}
    \end{center}
    """ %(codeName, version))
        elif displayProblemType=="Table":
            feedbackFile.write(r"""
    \begin{tabular}{c|c|c|c|c|c|c|c|c|c}
    \textbf{Year} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \tabularnewline
    \hline
    \textbf{Pop.} & %s & %s & %s & %s & %s & %s & %s & %s & %s
    \end{tabular} """ %(populations[0], populations[1], populations[2], populations[3], populations[4], populations[5], populations[6], populations[7], populations[8]) )
        # displayCorrectSolution
            # displayOptionsType: String, Math Mode, or Graph
            if displayOptionsType=="String":
                feedbackFile.write("The solution is %s, which is option %s." %(solution, answerLetter))
            elif displayOptionsType=="Math Mode":
                feedbackFile.write("The solution is \( %s \), which is option %s." %(solution, answerLetter))
            elif displayOptionsType=="Graph":
                feedbackFile.write(r"\begin{multicols}{2}")
                feedbackFile.write(r"""The solution is the graph below, which is option %s.
        \\begin{center}
            \\includegraphics[width=0.3\\textwidth]{../Figures/%s%s%s.png}
        \\end{center}""" %(answerLetter, codeName, answerLetter, version) )
        # displayStudentSolution
        if studentAnswerLetter == answerLetter:
            superlative=["Excellent", "Magnificent", "Wonderful", "Marvelous", "Brilliant", "Outstanding", "Great job", "Fantastic job", "Awesome", "Exceptional", "Well done"]
            feedbackFile.write("You chose option %s. %s! That is the correct answer." %(studentAnswerLetter, random.choice(superlative))) # Student correct!
        else:
            feedbackFile.write("You chose option %s. Unfortunately, that is not the correct answer." %studentAnswerLetter)
            options=["A", "B", "C", "D", "E", "F", "G", "H"]
            for letter in options:
                index=0
                if studentAnswerLetter == letter and answerLetter != letter:
                     feedbackFile.write(choiceSpecificComments[index])
                     break
                index+=1 # Student incorrect. Prints feedback to improve.
        feedbackFile.close()
