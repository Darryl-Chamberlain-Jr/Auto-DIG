## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file /home/archdoc/git-repos/AAG-College-Algebra/buildExams/Module4A.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_34 = Integer(34); _sage_const_39 = Integer(39); _sage_const_45 = Integer(45); _sage_const_4 = Integer(4); _sage_const_16 = Integer(16); _sage_const_49 = Integer(49); _sage_const_61 = Integer(61); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_5 = Integer(5); _sage_const_6 = Integer(6); _sage_const_63 = Integer(63); _sage_const_17 = Integer(17); _sage_const_67 = Integer(67); _sage_const_82 = Integer(82); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_84 = Integer(84); _sage_const_18 = Integer(18); _sage_const_88 = Integer(88); _sage_const_101 = Integer(101); _sage_const_13 = Integer(13); _sage_const_103 = Integer(103); _sage_const_19 = Integer(19); _sage_const_107 = Integer(107); _sage_const_121 = Integer(121); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_20 = Integer(20); _sage_const_123 = Integer(123); _sage_const_127 = Integer(127); _sage_const_140 = Integer(140); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27)## This file (Module4A.sagetex.sage) was *autogenerated* from Module4A.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('Module4A', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_34 
_st_.blockbegin()
try:
 load("../Code/generalPurposeMethods.sage")
 load("../Code/keyGeneration.sage")
 keyFileName = "Module4"
 version = "A"
except:
 _st_.goboom(_sage_const_39 )
_st_.blockend()
_st_.current_tex_line = _sage_const_45 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_4 
 problemNumber=_sage_const_16 
 load("../Code/quadratic/quadraticFormula.sage")
except:
 _st_.goboom(_sage_const_49 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_0 , latex(displayStem))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_1 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_2 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_3 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_4 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_5 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_6 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_61 )
_st_.current_tex_line = _sage_const_63 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_4 
 problemNumber=_sage_const_17 
 load("../Code/quadratic/quadraticGraphToEquation.sage")
except:
 _st_.goboom(_sage_const_67 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_7 , latex(displayStem))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_8 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_9 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_10 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_11 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_12 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_82 )
_st_.current_tex_line = _sage_const_84 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_4 
 problemNumber=_sage_const_18 
 load("../Code/quadratic/quadraticEquationToGraph.sage")
except:
 _st_.goboom(_sage_const_88 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_13 , latex(functionToGraph))
except:
 _st_.goboom(_sage_const_101 )
_st_.current_tex_line = _sage_const_103 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_4 
 problemNumber=_sage_const_19 
 load("../Code/quadratic/factorLeadingOver1Composite.sage")
except:
 _st_.goboom(_sage_const_107 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_14 , latex(displayStem))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_15 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_16 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_17 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_18 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_19 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_20 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_121 )
_st_.current_tex_line = _sage_const_123 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_4 
 problemNumber=_sage_const_20 
 load("../Code/quadratic/solveQuadraticFactorComposites.sage")
except:
 _st_.goboom(_sage_const_127 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_21 , latex(displayStem))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_22 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_23 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_24 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_25 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_26 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_27 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_140 )
_st_.endofdoc()

