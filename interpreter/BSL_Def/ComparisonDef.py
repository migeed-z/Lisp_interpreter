import DirPaths
import operator
from BSLError import BSLError
from Num import Num
from Boolean import Boolean
from BSLExpr import BSLExpr
#from PrimDef import PrimDef

class ComparisonDef():
    """
    To represent > operation
    """
    def __init__(self, comp, cls, argcls):
        """
        :param comp: Function that takes two numbers (num, num -> ?) and returns the result of the comparison
        :param cls: class to wrap around the result
        :param argcls: the type that args need to be
        """
        self.comp = comp
        self.cls = cls
        self.argcls = argcls

    def apply(self, name, args):
        self.validate(args, self.argcls)

        return self.cls(apply(self.comp, args))

    def validate(self, args, type):
        """
        Ensure that list of args are of type type
        :param args: List of values
        :param type: type that args need to be
        :return: True if elements are of type type
        :raise: BSLError if an arg is of the wrong type
        """
        for arg in args:
            if not isinstance(arg, type):
                raise BSLError('Arguments are of incorrect type.')

    def update(self, defs):
        """
        :param defs:
        :return:
        """
        add = defs.extend('+', ComparisonDef(lambda *args: reduce(operator.__add__, (arg.num for arg in args)), Num, Num))
        sub = add.extend('-', ComparisonDef(lambda *args: (-1 * args[0].num if len(args) == 1 else
                                                           reduce(operator.__sub__, (arg.num for arg in args))), Num, Num))
        mul = sub.extend('*',ComparisonDef(lambda *args: reduce(operator.__mul__, (arg.num for arg in args)), Num, Num))
        div = mul.extend('/', ComparisonDef(lambda *args: reduce(operator.__div__, (arg.num for arg in args)), Num, Num))
        exp = div.extend('^', ComparisonDef((lambda x, y: pow(x,y)), Num, Num))
        equals = exp.extend('=', ComparisonDef((lambda x, y: x == y), Boolean, BSLExpr))
        bigger_than = equals.extend('>', ComparisonDef((lambda x, y: x > y), Boolean, Num))
        smaller_than = bigger_than.extend('<', ComparisonDef((lambda x, y: x < y), Boolean, Num))
        return smaller_than




