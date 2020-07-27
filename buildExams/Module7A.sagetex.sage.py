## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file /home/archdoc/git-repos/AAG-College-Algebra/buildExams/Module7A.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_34 = Integer(34); _sage_const_39 = Integer(39); _sage_const_45 = Integer(45); _sage_const_7 = Integer(7); _sage_const_31 = Integer(31); _sage_const_49 = Integer(49); _sage_const_62 = Integer(62); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_6 = Integer(6); _sage_const_8 = Integer(8); _sage_const_64 = Integer(64); _sage_const_32 = Integer(32); _sage_const_68 = Integer(68); _sage_const_81 = Integer(81); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_83 = Integer(83); _sage_const_33 = Integer(33); _sage_const_87 = Integer(87); _sage_const_100 = Integer(100); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_102 = Integer(102); _sage_const_106 = Integer(106); _sage_const_129 = Integer(129); _sage_const_23 = Integer(23); _sage_const_24 = Integer(24); _sage_const_131 = Integer(131); _sage_const_35 = Integer(35); _sage_const_135 = Integer(135); _sage_const_154 = Integer(154); _sage_const_25 = Integer(25); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29)## This file (Module7A.sagetex.sage) was *autogenerated* from Module7A.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('Module7A', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_34 
_st_.blockbegin()
try:
 load("../Code/generalPurposeMethods.sage")
 load("../Code/keyGeneration.sage")
 keyFileName = "Module7"
 version = "A"
except:
 _st_.goboom(_sage_const_39 )
_st_.blockend()
_st_.current_tex_line = _sage_const_45 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_7 
 problemNumber=_sage_const_31 
 load("../Code/rational/solveRationalLinear.sage")
except:
 _st_.goboom(_sage_const_49 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_0 , latex(displayStem))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_1 , latex(leftSide))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_2 , latex(factorNumerator3))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_3 , latex(factorDenominator3))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_4 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_5 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_6 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_7 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_8 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_62 )
_st_.current_tex_line = _sage_const_64 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_7 
 problemNumber=_sage_const_32 
 load("../Code/rational/solveRationalQuadratic.sage")
except:
 _st_.goboom(_sage_const_68 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_9 , latex(displayStem))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_10 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_11 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_12 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_13 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_14 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_15 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_81 )
_st_.current_tex_line = _sage_const_83 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_7 
 problemNumber=_sage_const_33 
 load("../Code/rational/domainRational.sage")
except:
 _st_.goboom(_sage_const_87 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_16 , latex(displayStem))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_17 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_18 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_19 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_20 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_21 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_22 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_100 )
_st_.current_tex_line = _sage_const_102 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_7 
 problemNumber=_sage_const_34 
 load("../Code/rational/rationalEquationToGraph.sage")
except:
 _st_.goboom(_sage_const_106 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_23 , latex(displayStem))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_24 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_129 )
_st_.current_tex_line = _sage_const_131 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_7 
 problemNumber=_sage_const_35 
 load("../Code/rational/rationalGraphToEquation.sage")
except:
 _st_.goboom(_sage_const_135 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_25 , latex(displayStem))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_26 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_27 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_28 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_29 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_154 )
_st_.endofdoc()

