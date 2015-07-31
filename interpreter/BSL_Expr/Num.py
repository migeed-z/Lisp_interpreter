from BSLExpr import BSLExpr
from interpreter import BSLError

class Num(BSLExpr):
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

    def __eq__(self, other):
        if not isinstance(other, Num):
            return False
        else:
            return other.num == self.num