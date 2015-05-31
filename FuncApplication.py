from sExpr import sExpr
from BslError import BSLError

class FuncApplication(sExpr):

    def __init__(self, name, sl):
        """

        :param name: Name of the function
        :param sexpr: Substituted function parameter
        :return:
        """
        #super().__init__('by next week you will see why we called it dumb')
        self.name = name
        self.sl = sl


    def eval(self, defs):
        """
        Evaluates this function application
        :param defs: Scope containing tuples of keys and values
        :return: Numerical value of this function
        """

        vals = self.sl.helper_eval(defs)

        definition = defs.get(self.name) #this is a function defintion
        body = definition.body
        params = definition.params

        defs = self.helper_extend(defs, params, vals)

        return body.eval(defs)


    def helper_extend(self, defs, params, vals):

        if len(params) != len(vals):
            raise BSLError("Params and Vals must be equal")

        while len(params) != 0:
            name = params.pop()
            val = vals.pop()
            defs = defs.extend(name, val)

        return defs

    def subst(self, var, val):
        return self




