import DirPaths
from Structure import Structure
from Applicable import Applicable
from BSLError import BSLError
from Boolean import Boolean

class PredicateDef(Applicable):
    """
    Represents a structure predicate definition
    """

    def __init__(self, name, params):
        """
        :param name: String
        :param params: [String]
        """
        if len(params) != len(set(params)):
            raise BSLError('Duplicate Params are not allowed in Function definitions')
        self.params = params
        self.name = name

    def eval(self, s):
        """
        evaluates this expression by updating the current scope to new_scope
        :param s: current scope
        :return: [None, new_scope]
        """
        return [None, self.update(s)]

    def update(ast,s):
        return s.extend('%s?' % ast.name, ast)

    def apply(self, defs, vals):
        result = Boolean(True)
        if not len(vals) == 1:
            raise BSLError('Wrong number of arguments')
        elif not isinstance(vals[0], Structure):
            result = Boolean(False)

        return result

