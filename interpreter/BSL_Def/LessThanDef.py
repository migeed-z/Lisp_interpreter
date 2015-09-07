import DirPaths
from BSLError import BSLError
from PrimDef import PrimDef

class LessThanDef:
    """
    To represent < operation
    """

    def __init__(self):
        pass

    def apply(self, name, args):

        if not len(args) == 2:
            raise BSLError('Must compare two elements')

        return args[0] < args[1]