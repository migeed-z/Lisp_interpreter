from interpreter.BSLexpr import BSLexpr
from interpreter.BslError import BSLError


class Num(BSLexpr):
    """
    To represent an atomic, numerical sExpression
    """

    def __init__(self, num):
        """
        :param num: Number
        """
        self.num = self.validate(num)

    def eval(self, defs):
        return self.num

    def equals(self, other):
        if not isinstance(other, Num):
            return False
        else:
            return self.num == other.num

    def validate(self, num):
        if not isinstance(num, (complex, int, float)):
            raise BSLError('field must be a number')
        else:
            return num