from interpreter.BSLExpr import BSLExpr

class StructSelector(BSLExpr):
    """
    To represent a Struture selector.
    EX:
    (define-struct mystruct (x y z))
    (define s1 (make-mystruct 1 2 3))
    (mystruct-x s1) --> 1
    """

    def eval(self, defs):
        pass