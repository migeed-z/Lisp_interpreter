from interpreter.BSLExpr import BSLExpr
from interpreter.Value import Pair
from interpreter.BSLError import BSLError

class Posn_Selector(BSLExpr):
    """
    To represent a Posn Selector
    """

    def __init__(self, sub_expr):
        self.sub_expr = sub_expr

    def eval(self, defs):
        value = self.sub_expr.eval(defs)

        if isinstance(value, Pair):
            return value
        else:
            raise BSLError('Value is not a Pair')
