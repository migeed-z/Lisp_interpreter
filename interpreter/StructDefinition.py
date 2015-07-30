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
        Extends the scope with 3 definitions. Predicate, Constructor and Selector.
        :param: Current Scope
        :return: New scope
        """
        constructor = ConstructorDef(self.name, self.params)
        selector = SelectorDef(self.name, self.params)
        predicate = PredicateDef(self.name, self.params)

        defs = defs.extend('make_%s' % self.name, constructor).extend('select_%s' % self.name, selector).\
            extend('is_%s' % self.name, predicate)

        return defs