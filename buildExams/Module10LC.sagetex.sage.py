## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file /home/dchamberlain31/git-repos/AAG-College-Algebra/buildExams/Module10LC.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_35 = Integer(35); _sage_const_42 = Integer(42); _sage_const_47 = Integer(47); _sage_const_66 = Integer(66); _sage_const_51 = Integer(51); _sage_const_64 = Integer(64); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_6 = Integer(6); _sage_const_65 = Integer(65); _sage_const_67 = Integer(67); _sage_const_69 = Integer(69); _sage_const_82 = Integer(82); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_83 = Integer(83); _sage_const_68 = Integer(68); _sage_const_87 = Integer(87); _sage_const_100 = Integer(100); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_101 = Integer(101); _sage_const_105 = Integer(105); _sage_const_118 = Integer(118); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_119 = Integer(119); _sage_const_70 = Integer(70); _sage_const_123 = Integer(123); _sage_const_136 = Integer(136); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_30 = Integer(30); _sage_const_31 = Integer(31); _sage_const_32 = Integer(32); _sage_const_33 = Integer(33); _sage_const_34 = Integer(34)## This file (Module10LC.sagetex.sage) was *autogenerated* from Module10LC.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('Module10LC', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_35 
_st_.blockbegin()
try:
 load("../Code/pythonImports.sage")
 load("../Code/intervalMaskingMethod.sage")
 load("../Code/keyGeneration.sage")
 load("../Code/commonlyUsedFunctions.sage")
 keyFileName = "Module10L"
 version = "C"
except:
 _st_.goboom(_sage_const_42 )
_st_.blockend()
_st_.current_tex_line = _sage_const_47 
_st_.blockbegin()
try:
 moduleNumber="10L"
 problemNumber=_sage_const_66 
 load("../Code/14syntheticDivision/syntheticDivision.sage")
except:
 _st_.goboom(_sage_const_51 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_0 , latex(displayStem))
except:
 _st_.goboom(_sage_const_64 )
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_1 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_64 )
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_2 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_64 )
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_3 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_64 )
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_4 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_64 )
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_5 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_64 )
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_6 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_64 )
_st_.current_tex_line = _sage_const_65 
_st_.blockbegin()
try:
 moduleNumber="10L"
 problemNumber=_sage_const_67 
 load("../Code/14syntheticDivision/factorUsingSynthetic2Integers.sage")
except:
 _st_.goboom(_sage_const_69 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_7 , latex(displayStem))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_8 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_9 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_10 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_11 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_12 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_13 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_82 )
_st_.current_tex_line = _sage_const_83 
_st_.blockbegin()
try:
 moduleNumber="10L"
 problemNumber=_sage_const_68 
 load("../Code/14syntheticDivision/possibleRoots.sage")
except:
 _st_.goboom(_sage_const_87 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_14 , latex(displayStem))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_15 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_16 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_17 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_18 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_19 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_20 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_100 )
_st_.current_tex_line = _sage_const_101 
_st_.blockbegin()
try:
 moduleNumber="10L"
 problemNumber=_sage_const_69 
 load("../Code/14syntheticDivision/factorUsingSynthetic2Rationals.sage")
except:
 _st_.goboom(_sage_const_105 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_21 , latex(displayStem))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_22 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_23 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_24 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_25 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_26 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_27 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_118 )
_st_.current_tex_line = _sage_const_119 
_st_.blockbegin()
try:
 moduleNumber="10L"
 problemNumber=_sage_const_70 
 load("../Code/14syntheticDivision/syntheticDivisionMissingTerms.sage")
except:
 _st_.goboom(_sage_const_123 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_28 , latex(displayStem))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_29 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_30 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_31 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_32 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_33 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_34 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_136 )
_st_.endofdoc()

