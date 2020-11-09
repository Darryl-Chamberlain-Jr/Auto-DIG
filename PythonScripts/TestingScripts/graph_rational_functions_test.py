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


# Idea: We need to graph a rational function with 3 potential holes/asymptotes.
### Already in commonlyUsedFunctions
def generateTerms(coefficients):
    i=0
    if len(coefficients) == 2:
        if coefficients[i] == 1:
            terms = ["x"]
        elif coefficients[i] == -1:
            terms = ["-x"]
        else:
            terms = ["%sx" %coefficients[0]]
    elif len(coefficients) == 1:
        terms = ["%s" %coefficients[0]]
    else:
        if coefficients[i] == 1:
            terms = ["x^{%d}" %(len(coefficients)-1)]
        elif coefficients[i] == -1:
            terms = ["-x^{%d}" %(len(coefficients)-1)]
        else:
            terms = ["%sx^{%d}" %(coefficients[0], len(coefficients)-1)]
    i=i+1
    while i < len(coefficients):
        if coefficients[i] == 0:
            print("Skipping a zero term.")
        elif coefficients[i] < 0:
            if len(coefficients)-i-1 == 1:
                if coefficients[i] == -1:
                    terms.append("-x")
                else:
                    terms.append("-%s x" %(-coefficients[i]))
            elif len(coefficients)-i-1 == 0:
                terms.append("-%s" %(-coefficients[i]))
            else:
                if coefficients[i] == 1:
                    terms.append("-x^{%d}" %(len(coefficients)-i-1))
                else:
                    terms.append("-%s x^{%d}" %(-coefficients[i], len(coefficients)-i-1))
        else:
            if len(coefficients)-i-1 == 1:
                if coefficients[i] == 1:
                    terms.append("+x")
                else:
                    terms.append("+%s x" %(coefficients[i]))
            elif len(coefficients)-i-1 == 0:
                terms.append("+ %s" %(coefficients[i]))
            else:
                if coefficients[i] == 1:
                    terms.append("+ x^{%d}" %(len(coefficients)-i-1))
                else:
                    terms.append("+%s x^{%d}" %(coefficients[i], len(coefficients)-i-1))
        i=i+1
    return terms
def generatePolynomialDisplay(coefficients):
    terms = generateTerms(coefficients)
    if len(terms) == 10:
        polynomial = "%s %s %s %s %s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7], terms[8], terms[9])
    elif len(terms) == 9:
        polynomial = "%s %s %s %s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7], terms[8])
    elif len(terms) == 8:
        polynomial = "%s %s %s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7])
    elif len(terms) == 7:
        polynomial = "%s %s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6])
    elif len(terms) == 6:
        polynomial = "%s %s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4], terms[5])
    elif len(terms) == 5:
        polynomial = "%s %s %s %s %s" %(terms[0], terms[1], terms[2], terms[3], terms[4])
    elif len(terms) == 4:
        polynomial = "%s %s %s %s" %(terms[0], terms[1], terms[2], terms[3])
    elif len(terms) == 3:
        polynomial = "%s %s %s" %(terms[0], terms[1], terms[2])
    elif len(terms) == 2:
        polynomial = "%s %s" %(terms[0], terms[1])
    elif len(terms) == 1:
        polynomial = "%s" %(terms[0])
    else:
        polynomial = "Your polynomial has more than 10 terms."
    return polynomial
#################################################
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
    numerator_function_display=1
    numerator_function_graph=1
    for numerator_zero in numerator_zeros:
        numerator_function_display=numerator_function_display*(numerator_zero[0]*x-numerator_zero[1])
    denominator_function_display=1
    denominator_function_graph=1
    for denominator_zero in denominator_zeros:
        denominator_function_display=denominator_function_display*(denominator_zero[0]*x-denominator_zero[1])
    function_display="f(x)=\\frac{%s}{%s}" %(numerator_function_display, denominator_function_display)
    ### GRAPH ###
    plt.rcParams.update({'font.size': 36})
    y_values=[]
    for x_value in x_values:
        temp_y=( (numerator_zeros[0][0]*x_value - numerator_zeros[0][1])*(numerator_zeros[1][0]*x_value - numerator_zeros[1][1])*(numerator_zeros[2][0]*x_value - numerator_zeros[2][1]) ) / ( (denominator_zeros[0][0]*x_value - denominator_zeros[0][1])*(denominator_zeros[1][0]*x_value - denominator_zeros[1][1])*(denominator_zeros[2][0]*x_value - denominator_zeros[2][1]) )
        y_values.append(temp_y)
    plt.plot(x_values, y_values, linewidth=5, color='blue')
    plt.ylim([float(-10),float(10)])
    print(f"VA at: {vertical_asymptotes}")
    for va in vertical_asymptotes:
        plt.axvline(x= va[1], ls=('dashed'), color='black')
    #for hole in holes:
    #    plt.scatter(hole[1], y_hole, s=80, facecolors='none', edgecolors='r')
    plt.grid(True)
    #plt.savefig('/' + str(DIR) + '/Figures/' + str(thisQuestion) + str(version) + '.png', bbox_inches='tight')
    plt.savefig('testing.png', bbox_inches='tight')
    plt.close()
    return [function_display]

test_num_zeros=[[1,3], [1,-2], [1, 4]]
test_denom_zeros=[[1,4], [1, 1], [1, 5]]
function_display=graph_rational_function_with_undefined_points(test_num_zeros, test_denom_zeros, 0.05)
print(function_display)
