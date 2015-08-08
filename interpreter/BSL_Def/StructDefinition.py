from BSLDef import BSLDef
from ConstructorDef import ConstructorDef
from PredicateDef import PredicateDef
from SelectorDef import SelectorDef

class StructDefinition(BSLDef):
    """
    To represent (define-struct name (param ...))
    """
    def __init__(self, name, params):
        BSLDef.__init__(self, name, params)

    def update_scope(self, defs):
        """
        Extends the scope with new definitions for make-name, name_param, ..., is_name
        (name-param (make-name ... p ...)) = p
        :param: Current Scope
        :return: New scope with above names
        """
        constructor = ConstructorDef(self.name, self.params)
        predicate = PredicateDef(self.name, self.params)

        defs_plus_constructor = defs.extend('make-%s' % self.name, constructor)
        defs_plus_predicate = defs_plus_constructor.extend('is-%s' % self.name, predicate)
        defs_plus_selectors = defs_plus_predicate
        for param in self.params:
            selector = SelectorDef(self.name, [param])
            defs_plus_selectors = defs_plus_selectors.extend('%s-%s' % (self.name, param), selector)

        return defs_plus_selectors

    def __eq__(self, other):
        if not isinstance(other, StructDefinition):
            return False

        else:
            return self.name == other.name and self.params.__eq__(other.params)

