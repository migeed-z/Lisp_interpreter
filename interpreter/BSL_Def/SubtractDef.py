from PrimDef import PrimDef

class SubtractDef(PrimDef):
    """
    To represent Primitive Operations
    """
    def apply(self, name, args):

        self.validate(args, (int, complex, float))
        if 1 == len(args):
            return 0 - args[0]
        else:
            total = args.pop(0)
            for element in args:
                total = total - element
            return total
