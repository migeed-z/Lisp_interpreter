import pytest
import sys

sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/BSL_Expr')
sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/Other')

from BSLlist import BSLlist
from Variable import Variable
from BSLError import BSLError
from Num import Num


from Constants import Constants as c

# from interpreter import Num, BSLlist, Variable
# from Constants import Constants as c
# from interpreter import BSLError


def test_eval_num():
    assert Num(1).eval(c.defs1) == 1
    assert Num(9).eval(c.defs1) == 9

def test_eval_expr():
    assert c.list123.helper_eval(c.defs1) == [1, 2, 3]

def test_eval_empty():
    assert BSLlist([]).helper_eval(c.defs1) == []

def test_eval_add():
    assert c.expradd1.eval(c.defs1) == 1
    assert c.expradd123.eval(c.defs1) == 6

def test_eval_sub():
    assert c.exprsub1.eval(c.defs1) == -1
    assert c.exprsub123.eval(c.defs1) == -4

def test_eval_mult():
    assert c.exprmul1.eval(c.defs1) == 1
    assert c.exprmul84.eval(c.defs1) == 32

def test_eval_div():
    assert c.exprdiv1.eval(c.defs1) == 1
    assert c.exprdiv84.eval(c.defs1) == 2

def test_eval_comp():
    assert c.expradd_expradd123_exprdiv84.eval(c.defs1) == 8

def test_eval_var():
    assert c.expraddx23.eval(c.defs1) == 6

def test_equals():
    assert not c.expradd1 == c.expradd123
    assert c.expradd1 == c.expradd1
    assert not c.func_def_varx == c.funcDef2
    assert c.func_def_varx == c.func_def_varx
    assert c.func_def_varx == c.func_def_varx

def test_funcAppEval():
    assert c.func_app_varx.eval(c.defs1) == 4
    assert c.func_app_emptylist.eval(c.defs1) == 6
    assert c.func_app_varx_vary.eval(c.defs1) == 14

def test_bslError():
    with pytest.raises(BSLError):
        Variable('o').eval(c.defs1)

    with pytest.raises(BSLError):
        c.func_app_error_777.eval(c.defs1)

    with pytest.raises(BSLError):
        c.exprdiv403.eval(c.defs1)

def test_if0():
    assert c.if_012.eval(c.defs1) == 1
    assert c.if_varx_varx_emptylist.eval(c.defs1) == c.func_app_emptylist.eval(c.defs1)
    assert c.funcApp4.eval(c.defs1) == 6

def test_struct():
    assert c.make_posn.eval(c.defs1) == c.value_posn
    assert c.make_posn_comp.eval(c.defs1) == (c.value_posn_comp)

    assert c.is_posn.eval(c.defs1)
    assert not c.is_not_posn.eval(c.defs1)

    assert c.select_posn_x.eval(c.defs1) == 1
    assert c.select_posn_y.eval(c.defs1) == 2
    assert c.select_posn_y_comp.eval(c.defs1) == 2
    assert c.select_posn_x_comp.eval(c.defs1) == c.value_posn
    assert c.func_app_varx_1.eval(c.defs1) == c.value_posn_func
    assert c.posn_x_func_app_varx_1.eval(c.defs1) == 4


def test_struct_error():
    with pytest.raises(BSLError):
        c.select_posn_x_error.eval(c.defs1)

    with pytest.raises(BSLError):
        c.select_zeina_x.eval(c.defs1)


def test_and():
    assert c.and1.eval(c.defs1) == False
    assert c.and2.eval(c.defs1) == False
    with pytest.raises(BSLError):
        c.and3.eval(c.defs1)

def test_str():
    assert str(c.value_posn) == "Structure(posn, ('x', 'y'))"
    assert str(c.varx) == 'Variable(x)'
    assert str(Num(3)) == 'Num(3)'
    assert str(c.posn_def) == "StructureDefinition(posn, ('y', 'x'))"


    #assert str(c.defs1) == 'x'