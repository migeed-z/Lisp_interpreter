from interpreter.Operation import Operation
from interpreter.BslError import BSLError

class Divide(Operation):
    """
    To represent BSLexpr with Division at the top level
    """

    def __init__(self, args):
        super().__init__(args)
        self.operation = lambda seq: self.divide(seq)
        self.This = Divide

    def divide (self, seq):
        """
        Divide all elements of this seq
        :param seq: [numbers]
        :return: Value
        """
        if 1 == len(seq):
            return 1 / seq[0]
        else:
            result = seq.pop(0)
            for element in seq:
                if element == 0:
                    raise BSLError('Cannot Divide by Zero')
                else:
                    result = result/element

            return result


