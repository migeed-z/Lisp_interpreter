import copy
import sys
import DirPaths
from LambdaExpr import LambdaExpr
from BSLError import BSLError
from Binding import Binding
from BSLDef import BSLDef


class FuncDef(Binding):

    """
    To represent function definitions
    """

    def __init__(self, name, expr):
        Binding.__init__(self, name, expr)


    def eval(ast,s):
        return [None,s.extend(ast.name, ast.expr.eval_internal(s))]

    def update(self, defs):
        """
        Updates the current scope with this function definition
        :param defs: Current scope
        :return: New scope
        """
        name = self.name
        new_defs = defs.extend(name, self)
        return new_defs


    def __eq__(self, other):

        if not isinstance(other, FuncDef):
            return False
        else:
            return other.name == self.name and other.expr.params == self.expr.params and \
                   (other.expr.body).__eq__(self.expr.body)


