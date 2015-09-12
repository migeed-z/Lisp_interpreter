import DirPaths

from BSLExpr import BSLExpr
from BSLError import BSLError
from Boolean import Boolean

class And(BSLExpr):
    """
    To represent And
    """
    def __init__(self, sl):
        """
        :param sl: BSLlist
        """
        self.sl = sl

    def eval(self, defs):
        list = self.sl.sl

        for element in list:
            result = element.eval(defs)
            if not isinstance(result, Boolean):
                raise BSLError('Not a boolean')

            if not result:
                return Boolean(False)

        return Boolean(True)

    def __eq__(self, other):
        if not isinstance(other, And):
            return False
        else:
            return self.sl == other.sl


    def is_boolean(self, vals):
        """
        Return True if vals is a list of booleans and false otherwise
        :param vals: [bool]
        :return:
        """

        for element in vals:
            if not isinstance(element, bool):
                return Boolean(False)

        return Boolean(True)

