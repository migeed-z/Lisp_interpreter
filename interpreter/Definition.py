from interpreter.BSLExpr import BSLexpr

class Definition:
    """
    To represent definitions
    EX: (define x 2) equivalent to x=2 in python
    """

    def __init__(self, var, val):
        self.var = var
        self.val = val



