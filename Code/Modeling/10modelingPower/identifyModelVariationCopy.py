import sys
import random

DIR=sys.argv[1]
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
    OS_type=sys.argv[7]
    response_type=sys.argv[8]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

direct1 = ["A used-car company has just offered their best candidate, Nicole, a position in sales. The position offers 16\\% commission on her sales. Her earnings depend on the amount of her sales. For instance, if she sells a vehicle for \\$4,600, she will earn \\$736. She wants to evaluate the offer, but she is not sure how, so she needs to model her total payment based on the average commission of the company in the past year.", "Model: $P = 0.16C$. This is direct variation as \\textit{the amount Nicole makes in the previous month does not affect her amount in the next month}."]
direct2 = ["In 1905, Albert Einstein determined that the speed of a light is constant in a vacuum. With it, he published the famous equation of relativity: $E = mc^2$, where $E$ represents the energy of the object, $m$ represents the mass of the object, and $c$ represents the speed of light in a vacuum.", "Model: $E = mc^2$. This is \\textbf{not} joint variation since $c$ is a constant!"]
direct3 = ["The formal definition of the number $\\pi$ is the ratio of the circumference of any circle, $C$, to its diameter $d$. In other words, $\\pi = \\frac{C}{d}$.", "Model: $\\pi = \\frac{C}{d}$. This may look odd, so we can solve it for circumference: $C = \\pi d$. Here we can see circumference and diameter vary directly - as one increases, the other increases (and not at log or exp speeds)."]
directProblems = [direct1, direct2, direct3]

indirect1 = ["The number of days required to build a parking deck decreases with more workers hired. For the O’Connell Center, it took 20 workers 237 days to finish. How long would it take 10 workers to finish the new parking deck?", "Note that the relation between number of days and works is inverted - as one increases, the other decreases."]
indirect2 = ["``The bends'' is a common risk associated with scuba diving. Nitrogen or any other gas from a diver's air tank increases in pressure as a diver descends. For every 33 feet in ocean water, the pressure due to nitrogen goes up another 11.6 pounds per square inch. By modeling the pressure on a person in terms of the depth in water, we can determine how fast a scuba diver should surface.", "Note the relationship between pressure and depth is inverted. This may seem odd as it appears the distance from the surface to where the diver is is increasing as depth decreases, but that is because we take distance below sea level as a negative value."]
indirect3 = ["A tourist plans to drive 100 miles. Find a formula for the time the trip will take as a function of the speed the tourist drives.", "Model: $D = vt$, so $t = \\frac{D}{v}$. Since the distance is constant, this is an indirect variation."]
indirectProblems = [indirect1, indirect2, indirect3]

joint1 = ["In 1687, Issac Newton published his laws of motion. Newton's Second Law of Motion states that when a constant force acts on a massive body, it causes it to change its velocity at a constant rate. Common real-life physics problems require models of the amount of force on a particular object based on the weight and change in velocity of the object.", "Model: $F = ma$. We are modeling force with two variables: mass of the object and change in velocity (acceleration). Note that acceleration need not be constant - the force that a car would exert in a crash is different whether the change in speed is small (like backing out and hitting a pole) or large (hitting a pole going 60 mph)."]
joint2 = ["There are many equations related to the gravity, or the force that attracts two bodies toward each other. A particularly famous equation describes the force $F$ due to gravity between two objects: $Fr^2 = Gm_1m_2$, where $r$ is the distance between the two objects, $G$ is the gravitational constant, and $m_1, m_2$ are the mass of the objects.", "Model: $Fr^2 = Gm_1m_2$. Note we have more than 3 variables: $F, r, m_1,$ and $m_2$. No matter which we are trying to model, we will need to jointly use the others."]
joint3 = ["In economics, it is common to measure the total value of purchases in an economy (e.g., nominal GDP). The quantity equation states that the amount of money in an economy $M$ multiplied by how fast money circulates (V) is always equal to the price level (P) multiplied by real output (Y). This suggests that in order to measure the total value of purchases in an economy, you can use either the amount of money in the economy and how fast this money circulates OR the price level and the real output of goods in the economy.", "In both equations, we model the total value of purchases as the product of two variables."]
jointProblems = [joint1, joint2, joint3]

notPower1 = ["Social distancing is a common tactic to counter potential epidemics. This is due to the exponential increase in number of people infected as the density of people living in an area increases.", "This is an exponential variation, which grows significantly faster than any power function."]
notPower2 = ["In economics, there are two common equations to model interest earned. The compound interest formula is $A = P (1 + \\frac{r}{n})^{nt}$, where $A$ is the amount of money you end up with, $P$ is your starting money, $r$ is the interest rate, $n$ is the number of times compounded in a year, and $t$ is the total number of years. For example, if you were a parent and wanted to save \\$10,000 in 3 years-time at 3.5\\% interest compounded monthly, you would need to invest about \\$9,000.", "When thinking about power functions, we want the exponent to be constant and the base to be a variable (or variables). In this case, we see variables in the exponent, which tips us off that this is not a power variation."]
notPower3 = ["Big O notation is common in computer science to describe how fast a program can solve a particular problem. Big O notation categorizes functions according to their growth rates, the same way we have categorized modeling real-world problems by certain types of functions. When analyzing a particular program, a student found the computer to need $x^x$ time to complete, where $x$ was the number of inputs into the program.", "We have been modeling real-world problems according to the growth rates of functions. So far, we've seen logarithmics to be the slowest, then power functions, then exponentials as the fastest. But, there are \\textbf{far more types of functions than the ones we've looked at}! One such function is $x^x$, also known as a power tower. This function class grows significantly faster than exponentials. Remember for power variation, we need the exponent to be a constant."]
notPowerProblems = [notPower1, notPower2, notPower3]

#A. Direct variation
#B. Indirect variation
#C. Joint variation
#D. None of the above
######### OLD CODE ##############

typeOfVariation = ["direct", "indirect", "joint", "notPower"]
if typeOfVariation == "direct":
    problemAndGeneralComment = random.choice(directProblems)
    displayProblem = problemAndGeneralComment[0]
    generalComment = problemAndGeneralComment[1]
    option1 = ["\\text{Direct variation}", "", 1]
    option2 = ["\\text{Indirect variation}", "", 0]
    option3 = ["\\text{Joint variation}", "", 0]
    option4 = ["\\text{None of the above}", "", 0]
    displaySolution = option1[0]
elif typeOfVariation == "indirect":
    problemAndGeneralComment = random.choice(indirectProblems)
    displayProblem = problemAndGeneralComment[0]
    generalComment = problemAndGeneralComment[1]
    option1 = ["\\text{Direct variation}", "", 0]
    option2 = ["\\text{Indirect variation}", "", 1]
    option3 = ["\\text{Joint variation}", "", 0]
    option4 = ["\\text{None of the above}", "", 0]
    displaySolution = option2[0]
elif typeOfVariation == "joint":
    problemAndGeneralComment = random.choice(jointProblems)
    displayProblem = problemAndGeneralComment[0]
    generalComment = problemAndGeneralComment[1]
    option1 = ["\\text{Direct variation}", "", 0]
    option2 = ["\\text{Indirect variation}", "", 0]
    option3 = ["\\text{Joint variation}", "", 1]
    option4 = ["\\text{None of the above}", "", 0]
    displaySolution = option3[0]
else:
    problemAndGeneralComment = random.choice(notPowerProblems)
    displayProblem = problemAndGeneralComment[0]
    generalComment = problemAndGeneralComment[1]
    option1 = ["\\text{Direct variation}", "", 0]
    option2 = ["\\text{Indirect variation}", "", 0]
    option3 = ["\\text{Joint variation}", "", 0]
    option4 = ["\\text{None of the above}", "", 1]
    displaySolution = option4[0]

if response_type=="Multiple-Choice":
	displayStem = "Choose the model type that would best describe the scenario below."
else:
	displayStem="What model type would best describe the scenario below?"

answerListTemp = [option1, option2, option3]
random.shuffle(answerListTemp)
answerList = [answerListTemp[0], answerListTemp[1], answerListTemp[2], option4]

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2]]

answerIndex = 0
letters = ["A", "B", "C", "D"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1
# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="String"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
