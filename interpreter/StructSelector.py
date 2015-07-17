from interpreter.BSLExpr import BSLExpr
from interpreter.BSLError import BSLError
from interpreter.Value import Structure
from interpreter.BSLMakeStruct import BSLMakeStruct

class StructSelector(BSLExpr):
    """
    To represent a Struture selector.
    EX:
    (define-struct mystruct (x y z))
    (define s1 (make-mystruct 1 2 3))
    (mystruct-x s1) --> 1
    """

    def __init__(self, subexpr, field_name):
        """
        :param subexpr: BSLExpr
        :param field_name: String to represent the name of the field who's value we want to select
        """
        self.subexpr = subexpr
        self.field_name = field_name

    def eval(self, defs):
        expr = None
        if isinstance(self.subexpr, BSLMakeStruct):
            expr = self.subexpr.eval(defs)

        elif isinstance(self.subexpr, Structure):
            expr = self.subexpr

        if not expr:
            raise BSLError('This is not a Struct.')

        new_defs = expr.add_defs(defs)

        return new_defs.get(self.field_name)








