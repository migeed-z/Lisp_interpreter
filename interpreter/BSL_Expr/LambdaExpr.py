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
        return FuncType(self.types, self.body.type_of(acc.helper_extend(self.params, self.types)))

    def __eq__(self, other):
        if not isinstance(other, LambdaExpr):
            return False
        else:
            return (self.params == other.params) \
                   and (self.body == other.body)


