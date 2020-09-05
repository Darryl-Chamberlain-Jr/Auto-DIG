# IDEA - Create lists for each type.

# LINEAR
linear1 = "\\text{A town has an initial population of 100. It's population for the next five years is: 190, 280, 370, 460, 550.}"
linear2 = "\\text{The number of people afflicted with the common cold in the winter months steadily decreased by 205 each year from 2005 until 2010. In 2005, 12,025 people were inflicted.}"
linear3 = "\\text{Jenna and her friend, Khalil, are having a contest to see who can save the most money. Jenna has already saved \$110 and every week she saves an additional \$20. Khalil has already saved \$80 and every week he saves an additional \$25. In how many weeks will Jenna and Khalil have the same amount of money?}"

listOfLinear = [linear1, linear2, linear3]


# DIRECT VARIATION
direct1 = "\\text{A town has an initial population of 100. It's population for the next five years is: 400, 900, 1600, 2500, 3600.}"
direct1 = "\\text{The number of people afflicted with the common cold in the summer months increased by the square of the temperature above 50 degrees Fahrenheit each year from 2005 until 2010. In 2005, 12,025 people were inflicted.}"
direct2 = "\\text{The number of people afflicted with the common cold in the winter months decreased by the square of the temperature below 50 degrees Fahrenheit each year from 2005 until 2010. In 2005, 12,025 people were inflicted.}"
direct3 = "\\text{}"
listOfDirect = [direct0, direct1, direct2, direct3]


# INDIRECT VARIATION
indirect1 = "\\text{A town has an initial population of 100. It's population for the next five years is: 50, 33, 25, 20, 17.}"
indirect0 = "\\text{The number of days required to build a parking deck decreases with more workers hired. For the O’Connell Center, it took 20 workers 237 days to finish. How long would it take 10 workers to finish the new parking deck?}"
indirect1 = "\\text{Ellen can wash her car in 60 minutes. Her older sister Sara can do the same job in 45 minutes. How long will it take if they wash the car together?}"
indirect2 = "\\text{The number of people afflicted with the common cold in the winter months decreased by the square of the number of people vaccinated each year from 2005 until 2010. In 2005, 12,025 people were inflicted.}"

# EXPONENTIAL
exponential1 = "\\text{A town has an initial population of 10. It's population for the next five years is: 20, 40, 80, 160, 320.}"
exponential0 = "\\text{An extremely rich uncle has offered you a choice between \$1,000,000 or a penny doubled every day for the next 30 days. Which should you choose if you want to maximize your newfound riches?}"
exponential1 = "\\text{In 2007, a university study was published investigating the crash risk of alcohol impaired driving. Data from 2,871 crashes were used to measure the association of a person’s blood alcohol level (BAC) with the risk of being in an accident. The table below shows results from the study. The relative risk is a measure of how many times more likely a person is to crash. So, for example, a person with a BAC of 0.09 is 3.54 times as likely to crash as a person who has not been drinking alcohol.} \\\
 \\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\\hline
\\textbf{BAC} & 0 & 0.01 & 0.03 & 0.05 & 0.07 & 0.09 & 0.11 & 0.13 & 0.15 & 0.17 & 0.19 & 0.21 \\\
\\hline
\\textbf{Risk} & 1 & 1.03 & 1.06 & 1.38 & 2.09 & 3.54 & 6.41 & 12.6 & 22.1 & 39.05 & 65.32 & 99.78 \\\
\\hline
\\end{tabular}
"
exponential2 = "\\text{Your bank offers a savings account that will increase your total balance by 0.2\% annually. You want to decide how much to initially deposit to earn \$1000 in 10 years.}"
exponential3 = "\\text{A population of bacteria quadruples every hour. The population was initially observed to be 200.}"

exponential5 = "\\text{A ball bounced 4 times, reaching three-fourths of its previous height with each bounce. After the fourth bounce, the ball reached a height of 25 cm. How high was the ball when it was dropped?}"
exponential6 = "\\text{Carlos has taken an initial dose of a prescription medication orally. The medicine is absorbed rapidly by the large intestine and absorbed slowly as it is digested otherwise.}"


# LOGARITHMIC
logarithmic1 = "\\text{}"
logarithmic0 = "\\text{Carlos has taken an initial dose of a prescription medication orally. The medicine is absorbed slowly by the large intestine and absorbed rapidly as it is digested otherwise.}"


# TYPE OF PROBLEM TO BE DETERMINED BY MODULE
typesToChooseFrom=['linear', 'direct', 'indirect', 'joint', 'exponential', 'logarithmic']
problemType = random.choice(typesToChooseFrom)
displayStem = "True or False: it would be appropriate to model the situation below with a %s function." %moduleType

if problemType == 'linear'
    displayProblem = random.choice(listOfLinear)
    if problemType == moduleType:
        displaySolution = "\\text{True}"
    else:
        displaySolution = "\\text{False}"
    choice = ["True", "False"]
    comments =
elif problemType == 'direct'
    displayProblem = listOfLinear[ZZ.random_element(0, 4)]
    displaySolution = "\\text{True}"
else:
    displayProblem = listOfNotLinear[ZZ.random_element(0, 4)]
    answer = "\\text{False}"

comments = "General Comments: For linear functions, we are looking for a \\textbf{constant} change between the quantities. That means we are adding/subtracting the same number each time."
######
### moduleNumber, version, problemNumber are defined in the tex file ###
writeQuestionToFile(moduleNumber, version, problemNumber, displayStem, displayProblem)
writeSolutionAndOptionsToFile(moduleNumber, version, displaySolution, choices, choiceComments)
writeCommentsToFile(moduleNumber, version, comments)
