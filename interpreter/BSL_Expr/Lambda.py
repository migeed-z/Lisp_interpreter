from BSLExpr import BSLExpr

class Lambda(BSLExpr):
    """
    To represent Lambda expressions
    """

    def __init__(self, func_def, func_app):
        """
        :param func_def: FuncDef
        :param func_app: FunctionApplication
        """
        self.func_def = func_def
        self.func_app = func_app

    def eval(self, defs):
        new_defs = defs.extend('lambda', self.func_def)
        return self.func_app.eval(new_defs)