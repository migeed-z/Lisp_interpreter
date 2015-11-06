import DirPaths
from BSLError import BSLError
from Structure import Structure
from Applicable import Applicable

class SelectorDef(Applicable):

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
        return s.extend('%s-%s' % (ast.name, ast.params[0]), ast)

    def apply(self, defs, vals):

        if not isinstance(vals[0], Structure):
            raise BSLError('Can only select from a Structure')

        if vals[0].name != self.name:
            raise BSLError('Expects a %s, given a %s' % (self.name, vals[0].name))

        tuples = vals[0].tuples
        param = self.params[0]

        # assoc assq
        for tuple in tuples:
            if tuple[0] == param:
                return tuple[1]


