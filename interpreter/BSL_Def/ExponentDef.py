from math import pow
import DirPaths
from BSLError import BSLError
from PrimDef import PrimDef

class ExponentDef(PrimDef):
    """
    To represent the exponent definition
    """
    def apply(self, name, vals):
        self.validate(vals, (int, complex, float))

        if not len(vals) == 2:
            raise BSLError('Must only have two arguments')

        base = vals[0]
        power = vals[1]

        return pow(base, power)



