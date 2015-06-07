from BSLexpr import BSLexpr
from BslError import BSLError

class Variable(BSLexpr):
    """
    To represent a class of Variables
    """

    def __init__(self, name):
        """
        :param name: String representing the name of the variable
        """
        self.name = self.validate(name)

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

    def validate(self, name):
        if not isinstance(name, str):
            raise BSLError('field must be a string')
        return name
