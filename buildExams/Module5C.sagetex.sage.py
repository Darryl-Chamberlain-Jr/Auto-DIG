## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file /home/archdoc/git-repos/AAG-College-Algebra/buildExams/Module5C.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_34 = Integer(34); _sage_const_39 = Integer(39); _sage_const_45 = Integer(45); _sage_const_5 = Integer(5); _sage_const_21 = Integer(21); _sage_const_49 = Integer(49); _sage_const_73 = Integer(73); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_75 = Integer(75); _sage_const_22 = Integer(22); _sage_const_79 = Integer(79); _sage_const_92 = Integer(92); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_6 = Integer(6); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_94 = Integer(94); _sage_const_23 = Integer(23); _sage_const_98 = Integer(98); _sage_const_110 = Integer(110); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_112 = Integer(112); _sage_const_24 = Integer(24); _sage_const_116 = Integer(116); _sage_const_129 = Integer(129); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_131 = Integer(131); _sage_const_25 = Integer(25); _sage_const_135 = Integer(135); _sage_const_153 = Integer(153); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27)## This file (Module5C.sagetex.sage) was *autogenerated* from Module5C.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('Module5C', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_34 
_st_.blockbegin()
try:
 load("../Code/generalPurposeMethods.sage")
 load("../Code/keyGeneration.sage")
 keyFileName = "Module5"
 version = "C"
except:
 _st_.goboom(_sage_const_39 )
_st_.blockend()
_st_.current_tex_line = _sage_const_45 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_5 
 problemNumber=_sage_const_21 
 load("../Code/radical/radicalEquationToGraph.sage")
except:
 _st_.goboom(_sage_const_49 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_73 
 _st_.inline(_sage_const_0 , latex(displayStem))
except:
 _st_.goboom(_sage_const_73 )
try:
 _st_.current_tex_line = _sage_const_73 
 _st_.inline(_sage_const_1 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_73 )
_st_.current_tex_line = _sage_const_75 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_5 
 problemNumber=_sage_const_22 
 load("../Code/radical/solveRadicalLinear.sage")
except:
 _st_.goboom(_sage_const_79 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_2 , latex(displayStem))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_3 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_4 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_5 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_6 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_7 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_8 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_92 )
_st_.current_tex_line = _sage_const_94 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_5 
 problemNumber=_sage_const_23 
 load("../Code/radical/domainRadical.sage")
except:
 _st_.goboom(_sage_const_98 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_9 , latex(displayStem))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_10 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_11 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_12 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_13 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_14 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_15 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_110 )
_st_.current_tex_line = _sage_const_112 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_5 
 problemNumber=_sage_const_24 
 load("../Code/radical/solveRadicalQuadratic.sage")
except:
 _st_.goboom(_sage_const_116 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_16 , latex(displayStem))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_17 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_18 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_19 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_20 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_21 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_22 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_129 )
_st_.current_tex_line = _sage_const_131 
_st_.blockbegin()
try:
 moduleNumber=_sage_const_5 
 problemNumber=_sage_const_25 
 load("../Code/radical/radicalGraphToEquation.sage")
except:
 _st_.goboom(_sage_const_135 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_153 
 _st_.inline(_sage_const_23 , latex(displayStem))
except:
 _st_.goboom(_sage_const_153 )
try:
 _st_.current_tex_line = _sage_const_153 
 _st_.inline(_sage_const_24 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_153 )
try:
 _st_.current_tex_line = _sage_const_153 
 _st_.inline(_sage_const_25 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_153 )
try:
 _st_.current_tex_line = _sage_const_153 
 _st_.inline(_sage_const_26 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_153 )
try:
 _st_.current_tex_line = _sage_const_153 
 _st_.inline(_sage_const_27 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_153 )
_st_.endofdoc()

