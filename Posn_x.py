from sExpr import sExpr
from Pair import Pair
from BslError import BSLError

class Posn_x(sExpr):

    def __init__(self, sub_expr):
        self.sub_expr = sub_expr

    def eval(self, defs):
        value = self.sub_expr.eval(defs)

        if isinstance(value, Pair):
            return value.left
        else:
            raise BSLError('Value is not a pair')