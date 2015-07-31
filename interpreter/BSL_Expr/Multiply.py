from Operation import Operation

class Multiply(Operation):
    """
    To represent BSLexpr with Multiplication at the top level
    """

    def __init__(self, args):
        Operation.__init__(self, args)
        self.operation = lambda seq: self.multiply(seq)
        self.This = Multiply

    def multiply(self, seq):
        """
        Multiplies elements in seq
        :param seq: [number]
        :return: Value
        """
        total = 1
        for element in seq:
            total = total * element

        return total
