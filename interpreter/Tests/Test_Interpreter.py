import pytest
import sys

sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/BSL_Expr')
sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/Other')

from BSLlist import BSLlist
from Variable import Variable
from BSLError import BSLError
from Lambda import Lambda
from Num import Num
from Boolean import Boolean
from Constants import Constants as c


def test_eval_num():
    assert Num(1).eval(c.defs1) == Num(1)
    assert Num(9).eval(c.defs1) == Num(9)

def test_eval_expr():
    assert c.list123.helper_eval(c.defs1) == [Num(1), Num(2), Num(3)]

def test_eval_empty():
    assert BSLlist([]).helper_eval(c.defs1) == []

def test_eval_add():
    assert c.expradd1.eval(c.defs1) == Num(1)
    assert c.expradd123.eval(c.defs1) == Num(6)

    with pytest.raises(BSLError):
        c.expradderror.eval(c.defs1)

def test_eval_sub():
    assert c.exprsub1.eval(c.defs1) == Num(-1)
    assert c.exprsub123.eval(c.defs1) == Num(-4)

def test_eval_mult():
    assert c.exprmul1.eval(c.defs1) == Num(1)
    assert c.exprmul84.eval(c.defs1) == Num(32)

def test_eval_div():
    assert c.exprdiv1.eval(c.defs1) == Num(1)
    assert c.exprdiv84.eval(c.defs1) == Num(2)

def test_eval_comp():
    assert c.expradd_expradd123_exprdiv84.eval(c.defs1) == Num(8)

def test_eval_var():
    assert c.expraddx23.eval(c.defs1) == Num(6)

def test_equals():
    assert c.expradd1 != c.expradd123
    assert c.expradd1 == c.expradd1
    assert c.func_def_varx != c.funcDef2
    assert c.func_def_varx == c.func_def_varx
    assert c.func_def_varx == c.func_def_varx
    assert c.and3 == c.and3
    assert c.and3 != c.and2

def test_funcAppEval():
    assert c.func_app_varx.eval(c.defs1) == Num(4)
    assert c.func_app_emptylist.eval(c.defs1) == Num(6)
    assert c.func_app_varx_vary.eval(c.defs1) == Num(14)

def test_bslError():
    with pytest.raises(BSLError):
        Variable('o').eval(c.defs1)

    with pytest.raises(BSLError):
        c.func_app_error_777.eval(c.defs1)

    # with pytest.raises(BSLError):
    #     c.exprdiv403.eval(c.defs1)

def test_struct():
    assert c.make_posn.eval(c.defs1) == c.value_posn
    assert c.make_posn_comp.eval(c.defs1) == (c.value_posn_comp)
    assert c.is_posn.eval(c.defs1)
    assert not c.is_not_posn.eval(c.defs1)
    assert c.select_posn_x.eval(c.defs1) == Num(1)
    assert c.select_posn_y.eval(c.defs1) == Num(2)
    assert c.select_posn_y_comp.eval(c.defs1) == Num(2)
    assert c.select_posn_x_comp.eval(c.defs1) == c.value_posn
    assert c.func_app_varx_1.eval(c.defs1) == c.value_posn_func
    assert c.posn_x_func_app_varx_1.eval(c.defs1) == Num(4)


def test_struct_error():
    with pytest.raises(BSLError):
        c.select_posn_x_error.eval(c.defs1)

    with pytest.raises(BSLError):
        c.select_zeina_x.eval(c.defs1)


def test_and():
    assert c.and1.eval(c.defs1) == Boolean(True)
   # assert c.and2.eval(c.defs1) == Boolean(False)
    with pytest.raises(BSLError):
        c.and3.eval(c.defs1)

def test_equal():
    assert c.equals34.eval(c.defs1) == Boolean(False)
    assert c.equals33.eval(c.defs1) == Boolean(True)
    assert c.equals_3_true.eval(c.defs1) == Boolean(False)

def test_str():
    assert str(c.value_posn) == "Structure(posn, ('x', 'y'))"
    assert str(c.varx) == 'Variable(x)'
    assert str(Num(3)) == '3'
    assert str(c.posn_def) == "StructureDefinition(posn, ('y', 'x'))"

def test_if():
    assert c.if_1.eval(c.defs1) == Num(4)
    assert c.if_2.eval(c.defs1) == Num(3)

def test_bigger_and_less_than(): #this test occassionally fails???????????
    assert c.biggerthan34.eval(c.defs1) == Boolean(False)
    assert c.lessthan34.eval(c.defs1) == Boolean(True)

    with pytest.raises(BSLError):
        c.lessthan_error.eval(c.defs1)

def test_lambda():
    assert c.lambdaexpr1.eval(c.defs1) == Num(4)





# >       assert c.lessthan34.eval(c.defs1) == Boolean(True)
# E       assert <Boolean.Boolean instance at 0x10ef732d8> == <Boolean.Boolean instance at 0x10ef73560>
# E        +  where <Boolean.Boolean instance at 0x10ef732d8> = <bound method FuncApplication.eval of <FuncApplication.FuncApplication instance at 0x10ef75638>>(<Scope.Scope instance at 0x10ef67cb0>)
# E        +    where <bound method FuncApplication.eval of <FuncApplication.FuncApplication instance at 0x10ef75638>> = <FuncApplication.FuncApplication instance at 0x10ef75638>.eval
# E        +      where <FuncApplication.FuncApplication instance at 0x10ef75638> = c.lessthan34
# E        +    and   <Scope.Scope instance at 0x10ef67cb0> = c.defs1
# E        +  and   <Boolean.Boolean instance at 0x10ef73560> = Boolean(True)