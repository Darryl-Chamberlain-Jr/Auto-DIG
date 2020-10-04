#DIR="home/dchamberlain31/git-repos/Auto-DIG"
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
# NEED TO DEFINE
    # number_of_assessments
    # number_of_questions
    # exam_display_name
    # question_list_name
    # question_list
    # list_of_assessment_titles
    # list_of_file_names

number_of_assessments=1
number_of_questions=24
question_list=( \
# M1
'subgroupReal' 'divideComplex' 'orderOfOperations' \
# M2
'linearTwoPoints' 'linearParOrPer' 'solveRationalLinear' \
# M3
'solveIntegerInequality' 'solveRationalInequality' 'solveCompoundAND' \
# M4
'quadraticEquationToGraph' 'quadraticGraphToEquation' 'quadraticFormula' \
# M5
'domainRadical' 'radicalEquationToGraph' 'solveRadicalLinear' \
# M6
'polyGraphToFunction' 'polyZeroBehavior' 'constructPolyRationals' \
# M7
'solveRationalQuadratic' 'rationalGraphToEquation' 'solveRationalLinear' \
# M8
'domainRangeExp' 'domainRangeLog' 'solveExpDifferentBases' \
)
question_list_name="FinalExamVer"
exam_display_name="MAC 1105 Final Exam"
file_name="FinalExamVer"
list_of_assessment_titles=( "Final Exam" )
list_of_file_names=( $file_name )
