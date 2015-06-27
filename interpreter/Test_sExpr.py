import pytest

from interpreter.Constants import *
from interpreter.Constants import Constants as c
from interpreter.BslError import BSLError
from interpreter import Value as v


def test_eval_num():
    assert Num(1).eval(c.defs1) == 1
    assert Num(9).eval(c.defs1) == 9


def test_eval_expr():
    assert c.list2.helper_eval(c.defs1) == [1, 2, 3]


def test_eval_empty():
    assert BSLlist([]).helper_eval(c.defs1) == []


def test_eval_add():
    assert c.addsexpr1.eval(c.defs1) == 1
    assert c.addsexpr2.eval(c.defs1) == 6


def test_eval_sub():
    assert c.subsexpr1.eval(c.defs1) == -1
    assert c.subsexpr2.eval(c.defs1) == -4

def test_eval_mult():
    assert c.multsexpr1.eval(c.defs1) == 1
    assert c.multsexpr2.eval(c.defs1) == 32

def test_eval_div():
    assert c.divsexpr1.eval(c.defs1) == 1
    assert c.divsexpr2.eval(c.defs1) == 2

def test_eval_comp():
    assert c.compositeSexpr.eval(c.defs1) == 8

def test_eval_var():
    assert c.varsexpr1.eval(c.defs1) == 6


def test_equals():
    assert not c.addsexpr1.equals(c.addsexpr2)
    assert c.addsexpr1.equals(c.addsexpr1)

def test_funcAppEval():

    assert c.funcApp1.eval(c.defs1) == 4
    assert c.funcApp2.eval(c.defs1) == 6
    assert c.funcApp3.eval(c.defs1) == 14


def test_bslError():
    with pytest.raises(BSLError):
        Variable('o').eval(c.defs1)

    with pytest.raises(BSLError):
        c.funcApp3Error.eval(c.defs1)

    with pytest.raises(BSLError):
        c.divsexpr3.eval(c.defs1)

    with pytest.raises(BSLError):
        FuncDef('z', c.var1, [4])

def test_if0():
    assert c.if_1.eval(c.defs1) == 1
    assert c.if_2.eval(c.defs1) == c.funcApp2.eval(c.defs1)
    assert c.funcApp4.eval(c.defs1) == 6


def test_eval_posn():
    assert v.compare(c.posn1.eval(c.defs1), c.pair1)
    assert v.compare(c.funcApp5.eval(c.defs1), c.pair2)

def test_eval_posn_x():
    assert c.posn_x1.eval(c.defs1) == 1
    assert c.posn_x2.eval(c.defs1) == 4
    assert c.posnsexpr.eval(c.defs1) == 6
    assert Posn_x(c.funcApp5).eval(c.defs1) == 42


    with pytest.raises(BSLError):
        c.posn_x1_error.eval(c.defs1)

    with pytest.raises(BSLError):
        c.posnsexpr_error.eval(c.defs1)

    with pytest.raises(BSLError):
        c.posnsexpr_error2.eval(c.defs1)



