from sExpr import sExpr


class Operation(sExpr):
    """
    To represent Algebraic operations on SL
    """

    def __init__(self, args):
        """
        :param args: list of sExpr
        """
        self.args = args
        self.operation = lambda seq : 1/0
        self.This = Operation


    def eval(self, defs):
        seq = self.args.helper_eval(defs)
        return self.operation(seq)

    def equals(self, other):
        if not isinstance(other, self.This):
            return False
        else:
            return self.args.helper_equals(other.args)

    def subst(self, var, val):
        return self.This(self.args.helper_subst(var, val))

    def substAll(self, defs):
        return self.This(self.args.helper_substAll(defs))
