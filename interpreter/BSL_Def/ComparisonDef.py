import DirPaths
from BSLError import BSLError
from Num import Num
from PrimDef import PrimDef

class ComparisonDef(PrimDef):
    """
    To represent > operation
    """
    def __init__(self, comp, cls, argcls):
        """
        :param comp: Function that takes two numbers (num, num -> ?) and returns the result of the comparison
        :param cls: class to wrap around the result
        :param argcls: the type that args need to be
        """
        PrimDef.__init__(self)
        self.comp = comp
        self.cls = cls
        self.argcls = argcls

    def apply(self, name, args):
        self.validate(args, self.argcls)

        return self.cls(apply(self.comp, args))