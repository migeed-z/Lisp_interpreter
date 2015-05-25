from Operation import Operation


class Divide(Operation):
    """
    To represent sExpr with Division at the top level
    """


    def __init__(self, args):
        super().__init__(args)
        self.operation = lambda seq: self.divide(seq)
        self.This = Divide

    def divide (self, seq):
        if 1 == len(seq):
            return 1 / seq[0]
        else:
            result = seq.pop(0)
            for element in seq:
                if element == 0:
                    raise ZeroDivisionError('Cannot Divide by Zero')
                else:
                    result = result/element

            return result


