# Generates an answer key file.
# If displaying a picture as the problem, use the name of the picture to define "problem", "solution", or "items"

def convertToNumber(answer):
    answerNumber = 1
    for letter in ["A", "B", "C", "D", "E"]:
        if answer == letter:
            break
        answerNumber = answerNumber+1
    return answerNumber

def writeToKey(keyFileName, version, problemNumber, stem, problemDisplayType, problem, solutionDisplayType, solution, answer, items, itemComments, generalComment):
    keyFile = open('../Keys/key' + str(keyFileName) + str(version) + '.tex', 'a')
    ### Prints the initial question ###
    keyFile.write("%d. %s\n" %(problemNumber, stem))
    if problemDisplayType == "MathMode":
        keyFile.write("\[ %s \] \n" %problem)
    elif problemDisplayType == "NoMathMode":
        keyFile.write("%s \n" %problem)
    elif problemDisplayType == "Graph":
        keyFile.write("\\begin{center} \\includegraphics[width=0.3\\textwidth]{../Figures/%s.png} \\end{center} \n\n" %problem)
    else:
        print("No problem to display")
    ### Decides between types of solutions to print (regular or pictures) ###
    if solutionDisplayType == "MathMode":
        keyFile.write("The solution is $ %s $ \n\n" %solution)
        keyFile.write("\\begin{enumerate}[label=\\Alph*.] \n")
        for i in range(len(items)):
            keyFile.write("\\item $ %s $ \n\n" %items[i])
            keyFile.write(" %s \n" %itemComments[i])
        keyFile.write("\\end{enumerate} \n \n")
    elif solutionDisplayType == "Graphs":
        ### Item comments for pictures have been disabled for now. These may reappear in the future. ###
        keyFile.write("\n \n The solution is  \n \\begin{center} \\includegraphics[width=0.3\\textwidth]{../Figures/%s.png} \\end{center}" %solution)
        keyFile.write("\\begin{tabular}{|c|c|} \n")
        itemLetters=["A", "B", "C", "D", "E"]
        if len(items) % 2 == 1:
            k=0
            while k < (len(items) - 1):
                keyFile.write("\\hline \n & \\tabularnewline \n \\textbf{%s.} \\includegraphics[width=0.3\\textwidth]{../Figures/%s.png} & \\textbf{%s.} \\includegraphics[width=0.3\\textwidth]{../Figures/%s.png} \\tabularnewline \n" %(itemLetters[k], items[k], itemLetters[k+1], items[k+1]) )
                k=k+2
            keyFile.write("\\hline \n & \\tabularnewline \n \\textbf{%s.} \\includegraphics[width=0.3\\textwidth]{../Figures/%s.png} & \\tabularnewline \n" %(itemLetters[k], items[k]))
            keyFile.write("\\hline \n \\end{tabular} \n \n")
        else:
            i=0
            while i < (len(items)):
               keyFile.write("\\hline \n & \\tabularnewline \n \\textbf{%s.} \\includegraphics[width=0.3\\textwidth]{../Figures/%s.png} & \\textbf{%s.} \\includegraphics[width=0.3\\textwidth]{../Figures/%s.png} \\tabularnewline \n" %(itemLetters[i], items[i], itemLetters[i+1], items[i+1]) )
               i=i+2
            keyFile.write("\\hline \n E. None of the figures above. & \\tabularnewline \n")
            keyFile.write("\\hline \n \\end{tabular} \n \n")
        keyFile.write("\\begin{enumerate}[label=\\Alph*.] \n")
        for i in range(len(items)):
            keyFile.write("\\item %s  \n" %itemComments[i])
        keyFile.write("\\end{enumerate} \n \n")
    keyFile.write("%s\n\n" %generalComment)
    keyFile.write("-----------------------------------------------\n\n")
    keyFile.close()
    masterAnswerKeyFileLetters = open('../Keys/lettersAnswerKey' + str(keyFileName) + str(version) + '.csv', 'a')
    masterAnswerKeyFileLetters.write("%s," %answer)
    masterAnswerKeyFileLetters.close()
    masterAnswerKeyFileNumbers = open('../Keys/numbersAnswerKey' + str(keyFileName) + str(version) + '.csv', 'a')
    masterAnswerKeyFileNumbers.write("%d," %convertToNumber(answer))
    masterAnswerKeyFileNumbers.close()
