from abc import abstractmethod
from BSLexpr import BSLexpr
from Value import Pair
from BslError import BSLError

class Posn_Selector(BSLexpr):
    """
    To represent a Posn Selector
    """

    def __init__(self, sub_expr):
        self.sub_expr = self.validate(sub_expr)

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

    @abstractmethod
    def eval(self, defs):
        raise NotImplementedError('Method not yet implemented')

    def validate(self, sub_expr):
        if not isinstance(sub_expr, BSLexpr):
            raise BSLError('sub-expression must be a posn')
        return sub_expr