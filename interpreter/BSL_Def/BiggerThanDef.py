import DirPaths
from BSLError import BSLError
from PrimDef import PrimDef

class BiggerThanDef(PrimDef):
    """
    To represent > operation
    """
    def apply(self, name, args):
        self.validate(args, (int, complex, float))
        if not len(args) == 2:
            raise BSLError('Must compare two elements')

        return args[0] > args[1]