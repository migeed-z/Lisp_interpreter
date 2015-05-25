from sExpr import sExpr

class FuncApplication(sExpr):

    def __init__(self, name, sexpr):
        """

        :param name: Name of the function
        :param sexpr: Substituted function parameter
        :return:
        """
        #super().__init__('by next week you will see why we called it dumb')
        self.name = name
        self.sexpr = sexpr


    def eval(self, defs):
        """
        Evaluates this function application
        :param defs: Scope containing tuples of keys and values
        :return: Numerical value of this function
        """

        val = self.sexpr.eval(defs)

        definition = defs.get(self.name) #this is a function defintion
        body = definition.body
        param = definition.param
        dict = defs.extend(param, val)
        return body.eval(dict)

    def subst(self, var, val):
        return self




