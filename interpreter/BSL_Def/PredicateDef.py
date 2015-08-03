from BSLDef import BSLDef
from interpreter import Structure
from interpreter import BSLError

class PredicateDef(BSLDef):
    """
    Represents a structure predicate definition
    """

    def __init__(self, name, params):
        BSLDef.__init__(self, name, params)

    def apply(self, defs, vals):
        result = True
        if not len(vals) == 1:
            raise BSLError('Wrong number of arguments')
        elif not isinstance(vals[0], Structure):
            result = False

        return result

