from interpreter.BSLexpr import BSLexpr
from interpreter.BslError import BSLError

class Operation(BSLexpr):
    """
    To represent Algebraic operations on BSLlist
    """

    def __init__(self, args):
        """
        :param args: [BSLexpr]
        """
        self.args = args
        self.operation = lambda seq: 1/0
        self.This = Operation

    def eval(self, defs):
        seq = self.args.helper_eval(defs)
        return self.operation(self.validate(seq))

    def equals(self, other):
        if not isinstance(other, self.This):
            return False
        else:
            return self.args.helper_equals(other.args)

    def validate(self, seq):
        for item in seq:
            if not isinstance(item, (complex, int, float)):
                raise BSLError('Element is not a number')
        return seq