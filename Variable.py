from sExpr import sExpr
from Num import Num
from BslError import BSLError

class Variable(sExpr):
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

    def subst(self, var, val):
        if var == self.name:
            return Num(val)
        else:
            return self

    def substAll(self, scope_defs):
        expr = self
        defs = scope_defs.defs
        for item in defs:
            expr = expr.subst(item[0], item[1])
        return expr


