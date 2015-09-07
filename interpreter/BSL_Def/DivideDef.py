import DirPaths
from BSLError import BSLError
from PrimDef import PrimDef

class DivideDef(PrimDef):
    """
    To represent Primitive Operations
    """

    def apply(self, name, args):

        self.validate(args, (int, complex, float))

        if 1 == len(args):
            return 1 / args[0]
        else:
            result = args.pop(0)
            for element in args:
                if element == 0:
                    raise BSLError('Cannot Divide by Zero')
                else:
                    result = result/element

            return result
