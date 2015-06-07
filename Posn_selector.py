from abc import abstractmethod
from BSLexpr import BSLexpr
from Value import Pair
from BslError import BSLError

class Posn_Selector(BSLexpr):
    """
    To represent a Posn Selector
    """

    def __init__(self, sub_expr):
        self.sub_expr = sub_expr

    def eval_helper(self, defs):
        """
        Returns Value if valid
        :param defs: Scope representing definitions
        :return: Value
        :raise: BSLError if value is not a Pair
        """
        value = self.sub_expr.eval(defs)

        if isinstance(value, Pair):
            return value
        else:
            raise BSLError('Value is not a Pair')

    def eval(self, defs):
        v = self.eval_helper(defs)
        return v

