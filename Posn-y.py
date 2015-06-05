from sExpr import sExpr
from Pair import Pair
from BslError import BSLError

class Posn_y(sExpr):

    def __init__(self, sub_expr):
        self.sub_expr = sub_expr

    def eval(self, defs):
        value = self.sub_expr.eval(defs)

        if isinstance(value, Pair):
            return value.right
        else:
            raise BSLError('Value is not a pair')