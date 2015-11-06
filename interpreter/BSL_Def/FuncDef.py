import copy
import sys
import DirPaths
from LambdaExpr import LambdaExpr
from BSLError import BSLError


class FuncDef:

    """
    To represent function definitions
    """

    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def eval(ast,s):
        return [None, s.extend(ast.name, ast.expr.eval_internal(s))]

    def __eq__(self, other):

        if not isinstance(other, FuncDef):
            return False
        else:
            return other.name == self.name and other.expr == other.expr


