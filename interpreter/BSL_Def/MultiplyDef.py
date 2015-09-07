from PrimDef import PrimDef

class MultiplyDef(PrimDef):
    """
    To represent Primitive Operations
    """
    def apply(self, name, args):
        self.validate(args, (int, complex, float))
        total = 1
        for element in args:
            total = total * element

        return total