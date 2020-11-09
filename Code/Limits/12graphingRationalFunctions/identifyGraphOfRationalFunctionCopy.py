import sys
from sympy import *
import numpy
import random
import math
from decimal import Decimal
import decimal
import traceback
import cmath
import matplotlib.pyplot as plt
from sympy.abc import x, y
from sympy.solvers import solve

DIR=sys.argv[1]
database_name=sys.argv[2]
question_list=sys.argv[3]
version=sys.argv[4]
thisQuestion=sys.argv[5]
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

def coefficientsForPoly(zeros):
    a, b, c = zeros  #(x-a)(x-b)(x-c)
    return [1, -c-a-b, a*b+a*c+b*c, -a*b*c]
def graph_rational_function_with_undefined_points(numerator_zeros, denominator_zeros, step_size):
    vertical_asymptotes=[]
    holes=[]
    for denom_zero in denominator_zeros:
        if denom_zero in numerator_zeros:
            holes.append(denom_zero)
        else:
            vertical_asymptotes.append(denom_zero)
    list_of_zeros=[]
    undefined_values=[]
    for numerator_zero in numerator_zeros:
        list_of_zeros.append(numerator_zero[1]/numerator_zero[0])
    for denominator_zero in denominator_zeros:
        list_of_zeros.append(denominator_zero[1]/denominator_zero[0])
        undefined_values.append(denominator_zero[1]/denominator_zero[0])
    undefined_values=sorted(undefined_values)
    x_values=[]
    index=0
    while index < len(undefined_values)+1:
        if index==0:
            x_values.extend(numpy.arange(undefined_values[index]-2.5, undefined_values[0], step_size))
        elif index == len(undefined_values):
            x_values.extend(numpy.arange(undefined_values[index-1], undefined_values[index-1]+2.5, step_size))
        else:
            x_values.extend(numpy.arange(undefined_values[index-1], undefined_values[index], step_size))
        index+=1
    ### GRAPH ###
    plt.rcParams.update({'font.size': 36})
    y_values=[]
    for x_value in x_values:
        temp_y=( (numerator_zeros[0][0]*x_value - numerator_zeros[0][1])*(numerator_zeros[1][0]*x_value - numerator_zeros[1][1])*(numerator_zeros[2][0]*x_value - numerator_zeros[2][1]) ) / ( (denominator_zeros[0][0]*x_value - denominator_zeros[0][1])*(denominator_zeros[1][0]*x_value - denominator_zeros[1][1])*(denominator_zeros[2][0]*x_value - denominator_zeros[2][1]) )
        y_values.append(temp_y)
    plt.plot(x_values, y_values, linewidth=5, color='blue')
    #plt.ylim([float(-10),float(10)])
    for va in vertical_asymptotes:
        plt.axvline(x= va[1], ls=('dashed'), color='black')
    #for hole in holes:
    #    plt.scatter(hole[1], y_hole, s=80, facecolors='none', edgecolors='r')
    plt.grid(True)
    plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.close()

displayStem = "Which of the following functions \\textit{could} be the graph below?"
displayProblem = f"{thisQuestion}{version}"

# Gives a range of possible values to choose from
possible_values=list(numpy.setdiff1d(numpy.arange(-7, 7, 1), [0]))
denominator_zeros=random.sample(possible_values, 3)
reduced_possibilities=list(numpy.setdiff1d(possible_values, denominator_zeros) )
number_of_vas=random.randint(1, 2)
number_of_holes=3-number_of_vas
if number_of_holes==0:
    holes=[]
    numerator_zeros=random.sample(reduced_possibilities, 3)
else:
    holes=random.sample(denominator_zeros, number_of_holes)
    other_numerator_zeros=random.sample(reduced_possibilities, 3-number_of_holes)
    numerator_zeros=list(numpy.concatenate((holes, other_numerator_zeros), axis=None) )
vertical_asymptotes=list(numpy.setdiff1d(denominator_zeros, holes) )

# Solution
step_size=0.05
graph_rational_function_with_undefined_points( [  [1, numerator_zeros[0]],   [1, numerator_zeros[1]],  [1, numerator_zeros[2]]  ],  [  [1, denominator_zeros[0]], [1, denominator_zeros[1]],  [1, denominator_zeros[2]] ], step_size)
num_poly_solution=generatePolynomialDisplay(coefficientsForPoly(numerator_zeros))
denom_poly_solution=generatePolynomialDisplay(coefficientsForPoly(denominator_zeros))
displaySolution="f(x)=\\frac{%s}{%s}" %(num_poly_solution, denom_poly_solution)

# Distractor 1 - Treat all denominator zeros as VAs
    # Define all numerator zeros as distinct from denominator
distractor_1_numerator_zeros=list(numpy.concatenate(  (other_numerator_zeros, random.sample(reduced_possibilities, number_of_holes) ), axis=None) )
distractor_1_denominator_zeros=denominator_zeros
num_poly_distractor_1=generatePolynomialDisplay(coefficientsForPoly(distractor_1_numerator_zeros))
denom_poly_distractor_1=generatePolynomialDisplay(coefficientsForPoly(distractor_1_denominator_zeros))
display_distractor_1="f(x)=\\frac{%s}{%s}" %(num_poly_distractor_1, denom_poly_distractor_1)

# Disractor 2 - Zeros are negatives of what they should be
distractor_2_numerator_zeros=[i*-1 for i in numerator_zeros]
distractor_2_denominator_zeros=[i*-1 for i in denominator_zeros]
num_poly_distractor_2=generatePolynomialDisplay(coefficientsForPoly(distractor_2_numerator_zeros))
denom_poly_distractor_2=generatePolynomialDisplay(coefficientsForPoly(distractor_2_denominator_zeros))
display_distractor_2="f(x)=\\frac{%s}{%s}" %(num_poly_distractor_2, denom_poly_distractor_2)

# Distractor 3 - Zeros are negatives of what they should be AND all denominator zeros as VAs
negative_reduced_possibilities=list(numpy.setdiff1d(possible_values, [i*-1 for i in denominator_zeros]))
distractor_3_numerator_zeros=list(numpy.concatenate( ([i*-1 for i in other_numerator_zeros], random.sample(negative_reduced_possibilities, number_of_holes)), axis=None ) )
distractor_3_denominator_zeros=[i*-1 for i in denominator_zeros]
num_poly_distractor_3=generatePolynomialDisplay(coefficientsForPoly(distractor_3_numerator_zeros))
denom_poly_distractor_3=generatePolynomialDisplay(coefficientsForPoly(distractor_3_denominator_zeros))
display_distractor_3="f(x)=\\frac{%s}{%s}" %(num_poly_distractor_2, denom_poly_distractor_3)

# Distractor 4 - None of the above

option1=[displaySolution, "This is the correct answer!", 1]
option2=[display_distractor_1, "You treated all of the zeros in the denominator as vertical asymptotes when some of them were holes!", 0]
option3=[display_distractor_2, f"Remember that factors are written as $x-z$. For example, the zero $x={vertical_asymptotes[0]}$ corresponds to the factor $x-({vertical_asymptotes[0]})$.", 0]
option4=[display_distractor_3, "You treated all of the zeros in the denominator as vertical asmptotes when some of them were holes and wrote factors as $x+z$.", 0]
option5=["\\text{None of the above are possible equations for the graph.}", "If you believe none of the functions above could be the graph, please contact the coordinator.", 0]

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "We want to factor the numerator and denominator to determine which zeros in the denominator are vertical asympototes and which are holes."
answerLetter=identifyAnswerLetter(potentialAnswers)

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Graph"
displayOptionsType="Math Mode"
writeToDatabase(DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
