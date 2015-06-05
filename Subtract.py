from Operation import Operation


class Subtract(Operation):
    """
    To represent BSLexpr with Subtraction at the top level
    """

    def __init__(self, args):
        super().__init__(args)
        self.operation = lambda seq: self.subtract(seq)
        self.This = Subtract

    def subtract(self, seq):
        if 1 == len(seq):
            return 0 - seq[0]
        else:
            total = seq.pop(0)
            for element in seq:
                total = total - element
            return total




