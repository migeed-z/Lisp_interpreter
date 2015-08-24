import copy
import sys
sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/BSL_Expr')

from BSLError import BSLError
from AddDef import AddDef
from SubtractDef import SubtractDef
from MultiplyDef import MultiplyDef
from DivideDef import DivideDef
from ExponentDef import ExponentDef




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

    def add_definitions(self):
        add = self.extend('+', AddDef())
        sub = add.extend('-', SubtractDef())
        mul = sub.extend('*', MultiplyDef())
        div = mul.extend('/', DivideDef())
        exp = div.extend('^', ExponentDef())

        return exp

    # def __str__(self):
    #     return '%s(%s)' %('Value', self.defs)


