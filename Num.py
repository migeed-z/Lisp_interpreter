from BSLexpr import BSLexpr


class Num(BSLexpr):
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

