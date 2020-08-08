## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file /home/dchamberlain31/git-repos/AAG-College-Algebra/buildExams/Module12MA.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_35 = Integer(35); _sage_const_42 = Integer(42); _sage_const_48 = Integer(48); _sage_const_56 = Integer(56); _sage_const_52 = Integer(52); _sage_const_67 = Integer(67); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_6 = Integer(6); _sage_const_69 = Integer(69); _sage_const_57 = Integer(57); _sage_const_73 = Integer(73); _sage_const_88 = Integer(88); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_90 = Integer(90); _sage_const_58 = Integer(58); _sage_const_94 = Integer(94); _sage_const_109 = Integer(109); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_111 = Integer(111); _sage_const_59 = Integer(59); _sage_const_115 = Integer(115); _sage_const_130 = Integer(130); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_26 = Integer(26); _sage_const_132 = Integer(132); _sage_const_60 = Integer(60); _sage_const_136 = Integer(136); _sage_const_151 = Integer(151); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_30 = Integer(30); _sage_const_31 = Integer(31); _sage_const_32 = Integer(32); _sage_const_33 = Integer(33)## This file (Module12MA.sagetex.sage) was *autogenerated* from Module12MA.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('Module12MA', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_35 
_st_.blockbegin()
try:
 load("../Code/pythonImports.sage")
 load("../Code/intervalMaskingMethod.sage")
 load("../Code/keyGeneration.sage")
 load("../Code/commonlyUsedFunctions.sage")
 keyFileName = "Module12M"
 version = "A"
except:
 _st_.goboom(_sage_const_42 )
_st_.blockend()
_st_.current_tex_line = _sage_const_48 
_st_.blockbegin()
try:
 moduleNumber="12M"
 problemNumber=_sage_const_56 
 load("../Code/12solvingWordProblems/solveModelExp.sage")
except:
 _st_.goboom(_sage_const_52 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_0 , latex(displayStem))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_1 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_2 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_3 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_4 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_5 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_6 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_67 )
_st_.current_tex_line = _sage_const_69 
_st_.blockbegin()
try:
 moduleNumber="12M"
 problemNumber=_sage_const_57 
 load("../Code/12solvingWordProblems/constructModelMixed.sage")
except:
 _st_.goboom(_sage_const_73 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_88 
 _st_.inline(_sage_const_7 , latex(displayStem))
except:
 _st_.goboom(_sage_const_88 )
try:
 _st_.current_tex_line = _sage_const_88 
 _st_.inline(_sage_const_8 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_88 )
try:
 _st_.current_tex_line = _sage_const_88 
 _st_.inline(_sage_const_9 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_88 )
try:
 _st_.current_tex_line = _sage_const_88 
 _st_.inline(_sage_const_10 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_88 )
try:
 _st_.current_tex_line = _sage_const_88 
 _st_.inline(_sage_const_11 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_88 )
try:
 _st_.current_tex_line = _sage_const_88 
 _st_.inline(_sage_const_12 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_88 )
try:
 _st_.current_tex_line = _sage_const_88 
 _st_.inline(_sage_const_13 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_88 )
_st_.current_tex_line = _sage_const_90 
_st_.blockbegin()
try:
   moduleNumber="12M"
   problemNumber=_sage_const_58 
   load("../Code/12solvingWordProblems/identifyModelGraph12.sage")
   
except:
 _st_.goboom(_sage_const_94 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_14 , latex(displayStem))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_15 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_16 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_17 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_18 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_19 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_109 )
_st_.current_tex_line = _sage_const_111 
_st_.blockbegin()
try:
 moduleNumber="12M"
 problemNumber=_sage_const_59 
 load("../Code/12solvingWordProblems/solveModelPower.sage")
except:
 _st_.goboom(_sage_const_115 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_20 , latex(displayStem))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_21 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_22 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_23 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_24 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_25 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_26 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_130 )
_st_.current_tex_line = _sage_const_132 
_st_.blockbegin()
try:
 moduleNumber="12M"
 problemNumber=_sage_const_60 
 load("../Code/12solvingWordProblems/solveModelLinear.sage")
except:
 _st_.goboom(_sage_const_136 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_151 
 _st_.inline(_sage_const_27 , latex(displayStem))
except:
 _st_.goboom(_sage_const_151 )
try:
 _st_.current_tex_line = _sage_const_151 
 _st_.inline(_sage_const_28 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_151 )
try:
 _st_.current_tex_line = _sage_const_151 
 _st_.inline(_sage_const_29 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_151 )
try:
 _st_.current_tex_line = _sage_const_151 
 _st_.inline(_sage_const_30 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_151 )
try:
 _st_.current_tex_line = _sage_const_151 
 _st_.inline(_sage_const_31 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_151 )
try:
 _st_.current_tex_line = _sage_const_151 
 _st_.inline(_sage_const_32 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_151 )
try:
 _st_.current_tex_line = _sage_const_151 
 _st_.inline(_sage_const_33 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_151 )
_st_.endofdoc()

