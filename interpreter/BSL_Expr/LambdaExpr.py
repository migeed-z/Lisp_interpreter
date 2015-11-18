import copy
import DirPaths
from BSLError import BSLError
from BSLExpr import BSLExpr
from Closure import Closure
from FuncType import FuncType


class LambdaExpr(BSLExpr):
    """
    To represent a lambda expression.
    """

    def __init__(self, params, body, types=None):
        """
        :param params: [Strings]
        :param body: [BSLExpr]
        """
        self.params = params
        self.types = types
        self.body = body

    def eval_internal(self, defs):
        """
        Evaluates this expression
        :param defs: Scope
        :return: Value of this expresson
        """
        return Closure(self, defs)

    def type_of(self, acc):
        #Assumes types != None
        return FuncType(self.types, self.body.type_of(self.helper_extend(acc, self.params, self.types)))
       # return FuncType(self.types[0], self.body.type_of([[self.params[0],self.types[0]]]+acc))

    def __eq__(self, other):
        if not isinstance(other, LambdaExpr):
            return False
        else:
            return (self.params == other.params) \
                   and (self.body == other.body)


    def helper_extend(self, defs, params, types):
        """
        Extends defs with params and vals
        :param defs: Scope representing the definitions
        :param params: [String]
        :param vals: [Type]
        :return: Scope
        :raises: BSLError if len(params) not equal len(vals)
        """

        if len(params) != len(types):
            raise BSLError("params and vals must be equal")
        new_vals = copy.copy(types)
        new_params = copy.copy(params)
        while len(new_params) != 0:
            name = new_params.pop()
            val = new_vals.pop()
            defs = defs.extend(name, val)

        return defs