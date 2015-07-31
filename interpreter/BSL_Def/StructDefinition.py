from BSLDef import BSLDef
from ConstructorDef import ConstructorDef
from PredicateDef import PredicateDef
from SelectorDef import SelectorDef

class StructDefinition(BSLDef):
    """
    To represent the definition of a Struct
    """
    def __init__(self, name, params):
        BSLDef.__init__(self, name, params)

    def update_scope(self, defs):
        """
        Extends the scope with new definitions: Predicate, Constructor and Selectors.
        :param: Current Scope
        :return: New scope
        """
        constructor = ConstructorDef(self.name, self.params)
        predicate = PredicateDef(self.name, self.params)

        defs = defs.extend('make_%s' % self.name, constructor).extend('is_%s' % self.name, predicate)

        for param in self.params:
            selector = SelectorDef(self.name, [param])
            defs = defs.extend('%s_%s' % (self.name, param), selector)

        return defs