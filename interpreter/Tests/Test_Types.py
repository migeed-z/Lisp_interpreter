import pytest
import sys

sys.path.insert(0, '/Users/zeinamigeed/Lisp_interpreter/interpreter/BSL_Expr')
sys.path.insert(0, '/Users/zeinamigeed/Lisp_interpreter/interpreter/Other')

from Scope import Scope
from FuncType import FuncType
from NumType import NumType
from BoolType import BoolType
from Num import Num
from Boolean import Boolean
from Variable import Variable
from BSLlist import BSLlist
from FuncApplication import FuncApplication
from If import If
from LambdaExpr import LambdaExpr
from BSLError import BSLError

#declarations
acc = Scope(()).extend('my_var', NumType())\
    .extend('+', FuncType([NumType(), NumType()], NumType()))\
    .extend('x', NumType())\
    .extend('y', NumType())

#lambdaexpr
typed_lambda_expr1 = LambdaExpr(['x'], Variable('x'), [NumType()])
type_of_lambda_expr1 = FuncType([NumType()], NumType())

typed_lambda_expr2 = LambdaExpr(['x', 'y'], Variable('x'), [NumType(), NumType()])
type_of_lambda_expr2 = FuncType([NumType(), NumType()], NumType())


typed_expr1 = LambdaExpr(['x'],
                         FuncApplication(Variable('x'),
                                         BSLlist([Num(1)])),
                         [FuncType([NumType()], NumType())])

typed_expr2 = LambdaExpr(['y'], Variable('x'), [NumType()])

#function applications
typed_func_app1 = FuncApplication(Variable('+'), BSLlist([Variable('x'), Variable('y')]))
type_of_func_app1 = NumType()

typed_func_app2 = FuncApplication(typed_expr1, BSLlist([typed_expr2]))
type_of_func_app2 = NumType()

typed_func_app_error = FuncApplication(Variable('x'), BSLlist([typed_expr1]))
typed_func_app_error2 = FuncApplication(Variable('+'), BSLlist([Variable('x')]))


def test_consts():
    assert Num(3).type_of(acc) == NumType()
    assert Boolean(True).type_of(acc) == BoolType()

def test_var():
    assert Variable('my_var').type_of(acc) == NumType()


def test_lambda():
    assert typed_lambda_expr1.type_of(acc) == type_of_lambda_expr1
    assert typed_lambda_expr2.type_of(acc) == type_of_lambda_expr2

def test_func_app():
    assert typed_func_app1.type_of(acc) == type_of_func_app1
    assert typed_func_app2.type_of(acc) == type_of_func_app2

def test_func_app_error():
    with pytest.raises(BSLError):
        typed_func_app_error.type_of(acc)

    with pytest.raises(BSLError):
        typed_func_app_error2.type_of(acc)
