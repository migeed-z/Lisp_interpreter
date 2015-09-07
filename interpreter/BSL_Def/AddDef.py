from PrimDef import PrimDef

class AddDef(PrimDef):
    """
    To represent Primitive Operations
    """
    def apply(self, name, args):

        self.validate(args, (int, complex, float))
        total = 0
        for element in args:
            total = total + element

        return total


