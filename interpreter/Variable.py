from interpreter.BSLexpr import BSLexpr
from interpreter.BslError import BSLError

class Variable(BSLexpr):
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
