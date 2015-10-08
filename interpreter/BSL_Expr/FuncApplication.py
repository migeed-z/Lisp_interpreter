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

    def eval_internal(self, defs):
        vals = self.sl.helper_eval(defs)
        definition = defs.get(self.name)
        return definition.apply(defs, vals)

    def __eq__(self, other):
        if not isinstance(other, FuncApplication):
            return False

        else:
            return self.name == other.name and self.sl.__eq__(other.sl)
