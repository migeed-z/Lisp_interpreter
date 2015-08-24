import DirPaths

from BSLExpr import BSLExpr
from BSLError import BSLError


class Variable(BSLExpr):
    """
    To represent a class of Variables
    """

    def __init__(self, name):
        """
        :param name: String representing the name of the variable
        """
        self.name = name

    def eval(self, defs):
        val = defs.get(self.name)
        if not val:
            raise BSLError('Variable not defined')
        else:
            return val

    def equals(self, other):
        if not isinstance(other, Variable):
            return False
        else:
            return self.name == other.name

    def __eq__(self, other):
        if not isinstance(other, Variable):
            return False
        else:
            return other.name == self.name

    def __str__(self):
        return '%s(%s)' % ('Variable', self.name)