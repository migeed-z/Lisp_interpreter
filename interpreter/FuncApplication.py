from BSLExpr import BSLExpr

class FuncApplication(BSLExpr):
    """
    To represent function applications
    """

    def __init__(self, name, sl):
        """
        :param name: Name of the function
        :param sl: [BSLexpr]
        """
        self.name = name
        self.sl = sl

    def eval(self, defs):
        definition = defs.get(self.name)
        return definition.apply(defs, self.sl)

    def __eq__(self, other):
        """

        :param other:
        :return:
        """
        if not isinstance(other, FuncApplication):
            return False

        else:
            return self.name == other.name and self.sl.__eq__(other.sl)
