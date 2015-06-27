from interpreter.BSLexpr import BSLexpr
from interpreter.Value import Pair

class Posn(BSLexpr):
    """
    Represents an BSLexpr of the shape (posn e e)
    """
    def __init__(self, posn_x, posn_y):
        """
        :param posn_x: BSLexpr
        :param posn_y: BSLexpr
        """
        self.posn_x = posn_x
        self.posn_y = posn_y

    def eval(self, defs):
        val_x = self.posn_x.eval(defs)
        val_y = self.posn_y.eval(defs)

        return Pair(val_x, val_y)

