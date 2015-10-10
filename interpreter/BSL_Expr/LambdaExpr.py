from BSLExpr import BSLExpr

class LambdaExpr(BSLExpr):
    """
    To represent a lambda expression.
    """

    def eval_internal(self, defs):
        """
        Evaluates this expression
        :param defs: Scope
        :return: Value of this expresson
        """
        return self


