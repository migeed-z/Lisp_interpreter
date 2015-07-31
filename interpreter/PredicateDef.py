from BSLDef import BSLDef
from Value import Structure

class PredicateDef(BSLDef):

    def __init__(self, name, params):
        BSLDef.__init__(self, name, params)

    def apply(self, defs, vals):
        result = True
        if len(vals) > 1:
            result = False
        elif not isinstance(vals[0], Structure):
            result = False

        return result
