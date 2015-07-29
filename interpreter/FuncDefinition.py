import copy
from BSLError import BSLError

class FuncDefinition:

    """
    To represent function definitions
    """

    def __init__(self, name, params, body):
        """
        :param name: String to represent the name of the function
        :param body: BSLexpr
        :param params: [String]
        """
        self.name = name
        self.body = body
        if len(params) != len(set(params)):
            raise BSLError('Duplicate Params are not allowed in Function definitions')
        self.params = params

    def apply(self, defs, sl):
        """
        Applies a function application to this function defintion
        :param defs: Scope
        :param sl: [BSLExpr]
        :return: Value
        """
        body = self.body
        params = copy.copy(self.params)

        vals = sl.helper_eval(defs)
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

    def __eq__(self, other):

        if not isinstance(other, FuncDefinition):
            return False

        else:
            return other.name == self.name and other.params == self.params and (other.body).__eq__(self.body)


