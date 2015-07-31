import copy
from interpreter import BSLError
from BSLDef import BSLDef


class FuncDefinition(BSLDef):

    """
    To represent function definitions
    """

    def __init__(self, name, params, body):
        """
        :param name: String to represent the name of the function
        :param body: BSLexpr
        :param params: [String]
        """
        BSLDef.__init__(self, name, params)
        self.body = body

    def apply(self, defs, vals):
        """
        Applies a function application to this function defintion
        :param defs: Scope
        :param sl: [BSLExpr]
        :return: Value
        """
        body = self.body
        params = copy.copy(self.params)
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
        new_vals = copy.copy(vals)
        new_params = copy.copy(params)
        while len(new_params) != 0:
            name = new_params.pop()
            val = new_vals.pop()
            defs = defs.extend(name, val)

        return defs

    def __eq__(self, other):

        if not isinstance(other, FuncDefinition):
            return False
        else:
            return other.name == self.name and other.params == self.params and (other.body).__eq__(self.body)


