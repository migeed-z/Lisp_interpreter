from Operation import Operation

class Add(Operation):
    """
    To represent sExpr with Addition at the top level
    """

    def __init__(self, args):
        super().__init__(args)
        self.operation = lambda seq: self.add(seq)
        self.This = Add

    def add(self, seq):
        total = 0
        for element in seq:
            total = total + element

        return total
