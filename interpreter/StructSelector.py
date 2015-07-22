from interpreter.BSLExpr import BSLExpr
from interpreter.BSLError import BSLError
from interpreter.Value import Structure

class StructSelector(BSLExpr):
    """
    To represent a Struture selector.
    EX:
    (define-struct mystruct (x y z))
    (define s1 (make-mystruct 1 2 3))
    (mystruct-x s1) --> 1
    """

    def __init__(self, struct_name, subexpr, field_name):
        """
        :param struct_name: String representing the name of the struct
        :param subexpr: BSLExpr
        :param field_name: String to represent the name of the field who's value we want to select
        """
        self.struct_name = struct_name
        self.subexpr = subexpr
        self.field_name = field_name

    def eval(self, defs):
        value_of_subexpr = self.subexpr.eval(defs)
        # looks like Structure("my-struct", [1, 2, 3])

        if not isinstance(value_of_subexpr, Structure):
            raise BSLError('This is not a Struct.')

        if not value_of_subexpr.name == self.struct_name:
            raise BSLError('Expects a different kind of struct')

        new_defs = value_of_subexpr.add_defs(defs)

        return new_defs.get(self.field_name)








