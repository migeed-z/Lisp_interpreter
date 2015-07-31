from Operation import Operation

class Add(Operation):
    """
    To represent BSLexpr with Addition at the top level
    """

    def __init__(self, args):
        Operation.__init__(self, args)
        self.operation = lambda seq: self.add(seq)
        self.This = Add

    def add(self, seq):
        """
        Adds all elements of this seq
        :param seq: [numbers]
        :return: Value
        """
        total = 0
        for element in seq:
            total = total + element

        return total
