from interpreter.BSLExpr import BSLExpr
from interpreter.BslError import BSLError


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
        body = definition.body
        params = definition.params.copy()

        vals = self.sl.helper_eval(defs)
        defs = self.helper_extend(defs, params, vals)

        return body.eval(defs)

    def helper_extend(self, defs, params, vals):
        """
        Extends defs with params and vals
        :param defs: Scope representing the definitions
        :param params: [String]
        :param vals: [number]
        :return: Scope
        :raises: BSLError if len(params) not equal len(vals)
        """

        if len(params) != len(vals):
            raise BSLError("params and vals must be equal")

        while len(params) != 0:
            name = params.pop()
            val = vals.pop()
            defs = defs.extend(name, val)

        return defs

    def equals(self, other):
        """

        :param other:
        :return:
        """
        if not isinstance(other, FuncApplication):
            return False

        else:
            return self.name == other.name and self.sl.helper_equals(other.sl)
