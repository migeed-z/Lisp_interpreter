from BSLexpr import BSLexpr
from BslError import BSLError

class Operation(BSLexpr):
    """
    To represent Algebraic operations on BSLlist
    """

    def __init__(self, args):
        """
        :param args: list of BSLexpr
        """
        self.args = args
        self.operation = lambda seq: 1/0
        self.This = Operation

    def eval(self, defs):
        seq = self.args.helper_eval(defs)
        for item in seq:
            if not isinstance(item, (complex, int, float)):
                raise BSLError('Element is not a number')

        else:
            return self.operation(seq)

    def equals(self, other):
        if not isinstance(other, self.This):
            return False
        else:
            return self.args.helper_equals(other.args)

