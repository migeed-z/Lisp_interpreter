from Operation import Operation

class Add(Operation):
    """
    To represent BSLexpr with Addition at the top level
    """

    def __init__(self, args):
        super().__init__(args)
        self.operation = lambda seq: self.add(seq)
        self.This = Add

    def add(self, seq):
        """
        Adds all elements of this seq
        :param seq: List of numbers
        :return: Value of addition
        """
        total = 0
        for element in seq:
            total = total + element

        return total
