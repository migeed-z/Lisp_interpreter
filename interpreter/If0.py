from interpreter.BSLExpr import BSLexpr
from interpreter.BslError import BSLError

class If0(BSLexpr):
    """
    To represent an if-statement
    """

    def __init__(self, test, if_branch, else_branch):
        """
        :param test: BSLExpr
        :param if_branch: BSLExpr
        :param else_branch: BSLExpr
        """
        self.validate(test, if_branch, else_branch)
        self.test = test
        self.if_branch = if_branch
        self.else_branch = else_branch

    def eval(self, defs):
        if self.test.eval(defs) == 0:
            return self.if_branch.eval(defs)

        else:
            return self.else_branch.eval(defs)

    def validate(self, test, if_branch, else_branch):
        if not isinstance(test, BSLexpr):
            raise BSLError('test must be a BSL expression')
        elif not isinstance(if_branch, BSLexpr):
            raise BSLError('if_branch must be a BSL expression')
        elif not isinstance(else_branch, BSLexpr):
            raise BSLError('else_branch must be a BSL expression')

