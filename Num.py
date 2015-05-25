from sExpr import sExpr


class Num(sExpr):
    """
    To represent an atomic, numerical sExpression
    """

    def __init__(self, num):
        """
        :param num: Number
        """
        self.num = num

    def eval(self, defs):
        return self.num

    def equals(self, other):
        if not isinstance(other, Num):
            return False
        else:
            return self.num == other.num

    def subst(self, var, val):
        return self

    def substAll(self, defs):
        return self
