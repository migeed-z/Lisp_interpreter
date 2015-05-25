from SL import SL


class NonEmpty(SL):
    """
    To represent a non-empty list of Sexpr
    """

    def __init__(self, curr, other):
        """

        :param curr: sExpr
        :param other: SL
        :return:
        """
        self.curr = curr
        self.other = other

    def helper_eval(self, defs):
        a = self.curr.eval(defs)
        b = self.other.helper_eval(defs)
        b.insert(0, a)
        return b

    def helper_equals(self, element):
        a = self.curr.equals(element.curr)
        b = self.other.helper_equals(element.other)
        return a and b

    # def helper_subst(self, var, val):
    #     first = self.curr.subst(var, val)
    #     rest = self.other.helper_subst(var, val)
    #     return NonEmpty(first, rest)
    #
    #
    # def helper_substAll(self, defs):
    #     first = self.curr.substAll(defs)
    #     rest = self.other.helper_substAll(defs)
    #     return NonEmpty(first, rest)
    #
    #
    #
