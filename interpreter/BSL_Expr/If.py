import DirPaths

from BSLExpr import BSLExpr
from BSLError import BSLError

class If(BSLExpr):
    """
    To represent an if-statement
    """

    def __init__(self, test, if_branch, else_branch):
        """
        :param test: BSLExpr
        :param if_branch: BSLExpr
        :param else_branch: BSLExpr
        """
        self.test = test
        self.if_branch = if_branch
        self.else_branch = else_branch

    def eval(self, defs):

        self.validate()
        if self.test.eval(defs):
            return self.if_branch.eval(defs)
        else:
            return self.else_branch.eval(defs)

    def validate(self):
        if not isinstance(self.test, BSLExpr):
            raise BSLError('test must be a BSL expression')
        elif not isinstance(self.if_branch, BSLExpr):
            raise BSLError('if_branch must be a BSL expression')
        elif not isinstance(self.else_branch, BSLExpr):
            raise BSLError('else_branch must be a BSL expression')
