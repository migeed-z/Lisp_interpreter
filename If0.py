from BSLexpr import BSLexpr

class If0(BSLexpr):

    def __init__(self, test, if_branch, else_branch):
        """

        :param test:
        :param if_branch:
        :param else_branch:
        :return:
        """
        self.test = test
        self.if_branch = if_branch
        self.else_branch = else_branch

    def eval(self, defs):
        """

        :param defs:
        :return:
        """
        if self.test.eval(defs) == 0:
            return self.if_branch.eval(defs)

        else:
            return self.else_branch.eval(defs)
