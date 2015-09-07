from PrimDef import PrimDef

class EqualsDef(PrimDef):
    """
    To represent the primitive definition, Equals
    """

    def apply(self, name, args):

        result = True
        first = args[0]
        for element in args:
            if element != first:
                return False
        return result

