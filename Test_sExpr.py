from Fixtures import *
from Fixtures import Constants as c
from BslError import BSLError
import pytest



def test_eval_num():
    assert Num(1).eval(c.defs1) == 1
    assert Num(9).eval(c.defs1) == 9


def test_eval_expr():
    assert c.list2.helper_eval(c.defs1) == [1, 2, 3]


def test_eval_empty():
    assert SL([]).helper_eval(c.defs1) == []


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

# def test_subst():
#     assert c.varsexpr1.subst('x', 1).equals(c.addsexpr2)
#     assert c.addsexpr1.subst('x', 1).equals(c.addsexpr1)
#
# def test_substAll():
#     assert c.varsexpr3.substAll(c.defs1).equals(c.subsexpr3)

def test_funcAppEval():
    assert c.funcApp1.eval(c.defs1) == 3
    # assert c.funcApp2.eval(c.defs1) == 5
    assert c.funcApp3.eval(c.defs1) == 14


def test_bslError():
    with pytest.raises(BSLError):
        Variable('o').eval(c.defs1)

    with pytest.raises(BSLError):
        c.funcApp3Error.eval(c.defs1)

    with pytest.raises(BSLError):
        c.divsexpr3.eval(c.defs1)





