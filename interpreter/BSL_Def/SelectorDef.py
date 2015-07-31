from BSLDef import BSLDef
from interpreter import BSLError
from interpreter import Structure

class SelectorDef(BSLDef):

    def __init__(self, name, params):
        """
        :param params:[string] representing only one param to be selected
        """
        BSLDef.__init__(self, name, params)

    def apply(self, defs, vals):

        if not isinstance(vals[0], Structure):
            raise BSLError('Can only select from a Structure')

        tuples = vals[0].tuples
        param = self.params[0]

        for tuple in tuples:
            if tuple[0] == param:
                return tuple[1]


