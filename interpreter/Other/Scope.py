import copy
import DirPaths
import operator
from BSLError import BSLError
from PrimitiveFunc import PrimitiveFunc
from Num import Num
from Boolean import Boolean
from BSLExpr import BSLExpr

class Scope:
    """
    To represent the definitions as a tuple T, where t[0] is a key, t[1] is a value and t[2] is
    the old scope
    """

    def __init__(self, defs):
        """
        Initialises the scope from a tuple with three elements
        :param defs: Tuple containing three elements. If no definitions exist, we may use an empty tuple
        """
        self.defs = defs

    def __str__(self):
        return self.defs[0]

    def extend(self, name, val):
        """
        Expends this Scope with name and val
        :param name: String
        :param val: Value corresponding to name
        :return: New scope with extended definitions
        """
        if not isinstance(name, str) :
            raise BSLError('name field must be a string')
        return Scope((name, val, self))

    def get(self, key):
        if not self.defs:
            return None
        else:
            name = self.defs[0]
            val = self.defs[1]
            old_self = self.defs[2]
            if key == name:
                return val
            else:
                return old_self.get(key)

    def helper_extend(self, params, vals):
        """
        Extends this scope with params and vals
        :param params: [String]
        :param vals: [Type]
        :return: Scope
        :raises: BSLError if len(params) not equal len(vals)
        """

        if len(params) != len(vals):
            raise BSLError("params and vals must be equal")
        new_vals = copy.copy(vals)
        new_params = copy.copy(params)
        while len(new_params) != 0:
            name = new_params.pop()
            val = new_vals.pop()
            return self.extend(name, val)

    def add_definitions(self):
        add = self.extend('+', PrimitiveFunc(lambda *args: reduce(operator.__add__, (arg.num for arg in args), 0), Num, Num))
        sub =  add.extend('-', PrimitiveFunc(lambda *args: (-1 * args[0].num if len(args) == 1 else reduce(operator.__sub__, (arg.num for arg in args))), Num, Num))
        mul =  sub.extend('*', PrimitiveFunc(lambda *args: reduce(operator.__mul__, (arg.num for arg in args), 1), Num, Num))
        div =  mul.extend('/', PrimitiveFunc(lambda *args: reduce(operator.__div__, (arg.num for arg in args)), Num, Num))
        exp =  div.extend('^', PrimitiveFunc((lambda x, y: pow(x,y)), Num, Num))
        equals       = exp.extend('=',         PrimitiveFunc((lambda x, y: x == y), Boolean, Num))
        bigger_than  = equals.extend('>',      PrimitiveFunc((lambda x, y: x > y),  Boolean, Num))
        smaller_than = bigger_than.extend('<', PrimitiveFunc((lambda x, y: x < y),  Boolean, Num))
        return smaller_than


