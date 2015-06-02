from sExpr import sExpr
from Pair import Pair

class Posn(sExpr):
    """
    Represents an sExpr of the shape (posn e e)
    """
    def __init__(self, posn_x, posn_y):
        """

        :param posn_x: sExpr
        :param posn_y: sExpr
        :return:
        """
        self.posn_x = posn_x
        self.posn_y = posn_y

    def eval(self, defs):
        val_x = self.posn_x.eval(defs)
        val_y = self.posn_y.eval(defs)

        return Pair(val_x, val_y)

