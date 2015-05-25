from Operation import Operation


class Multiply(Operation):
    """
    To represent sExpr with Multiplication at the top level
    """

    def __init__(self, args):
        super().__init__(args)
        self.operation = lambda seq: self.multiply(seq)
        self.This = Multiply

    def multiply(self, seq):
        total = 1
        for element in seq:
            total = total * element

        return total
