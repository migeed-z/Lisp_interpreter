from interpreter.BSLDef import BSLDef

class Definition(BSLDef):
    """
    To represent definitions
    EX: (define x 2) equivalent to x=2 in python
    """

    def __init__(self, name, val):
        """
        :param name: String
        :param val: BSLExp
        """
        self.name = name
        self.val = val

    def equals(self, other):
        if not isinstance(other, Definition):
            return False

        else:
            return self.name == other.name and self.val.equals(other.val)


