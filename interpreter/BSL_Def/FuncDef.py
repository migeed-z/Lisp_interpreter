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
        if not ast.expr.params:
            return [None,s.extend(ast.name, ast.expr.body.eval_internal(s))]
        else:
            return [None, ast.update(s)]

    def update(self, defs):
        """
        Updates the current scope with this function definition
        :param defs: Current scope
        :return: New scope
        """
        name = self.name
        new_defs = defs.extend(name, self)
        return new_defs

    def apply(self, defs, vals):
        """
        Applies a function application to this function defintion
        :param defs: Scope
        :param sl: [BSLExpr]
        :return: Value
        """
        body = self.expr.body
        params = copy.copy(self.expr.params)
        defs = self.helper_extend(defs, params, vals)

        return body.eval_internal(defs)

    def helper_extend(self, defs, params, vals):
        """
        Extends defs with params and vals
        :param defs: Scope representing the definitions
        :param params: [String]
        :param vals: [number]
        :return: Scope
        :raises: BSLError if len(params) not equal len(vals)
        """

        if len(params) != len(vals):
            raise BSLError("params and vals must be equal")
        new_vals = copy.copy(vals)
        new_params = copy.copy(params)
        while len(new_params) != 0:
            name = new_params.pop()
            val = new_vals.pop()
            defs = defs.extend(name, val)

        return defs

    def __eq__(self, other):

        if not isinstance(other, FuncDef):
            return False
        else:
            return other.name == self.name and other.expr.params == self.expr.params and \
                   (other.expr.body).__eq__(self.expr.body)


