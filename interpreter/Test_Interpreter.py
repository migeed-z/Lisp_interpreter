import pytest
from interpreter import Constants as c, BSLError, Value as v, Num, BSLlist, Variable, Posn_x


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
    assert not c.expradd1.equals(c.expradd123)
    assert c.expradd1.equals(c.expradd1)
    assert not c.func_def_varx.equals(c.funcDef2)
    assert c.func_def_varx.equals(c.func_def_varx)
    assert not c.func_app_varx_1.equals(c.func_def_posn_42_11)
    assert c.func_def_varx.equals(c.func_def_varx)

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


def test_eval_posn():
    assert v.compare(c.posn11.eval(c.defs1), c.pair11)
    assert v.compare(c.func_app_varx_1.eval(c.defs1), c.pair41)

def test_eval_posn_x():
    assert c.posn_x_11.eval(c.defs1) == 1
    assert c.posn_y_func_app_varx_1.eval(c.defs1) == 4
    assert c.expraddposnx_11_5.eval(c.defs1) == 6
    assert Posn_x(c.func_app_100).eval(c.defs1) == 42


    with pytest.raises(BSLError):
        c.posn_x1_error.eval(c.defs1)

    with pytest.raises(BSLError):
        c.expraddposn11.eval(c.defs1)

    with pytest.raises(BSLError):
        c.posnsexpr_error2.eval(c.defs1)



