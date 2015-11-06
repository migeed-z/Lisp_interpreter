import copy
import DirPaths

from BSLError import BSLError
from Structure import Structure
from Applicable import Applicable


class ConstructorDef(Applicable):

    def __init__(self, name, params):
        """
        :param name: String
        :param params: [String]
        """
        if len(params) != len(set(params)):
            raise BSLError('Duplicate Params are not allowed in Function definitions')
        self.params = params
        self.name = name

    def apply(self, defs, vals):
        """
        Returns a Structure consisting of the name of the constructor and an
        association list associating structure parameters (fields) w/ values
        :param: make_instance: extend the new scope with the new definitions
        :return: New Scope with parameter defintions
        """

        return Structure(self.name, self.make_tuples(self.params, vals))

    def eval(self, s):
        """
        evaluates this expression by updating the current scope to new_scope
        :param s: current scope
        :return: [None, new_scope]
        """
        return [None, self.update(s)]

    def update(ast,s):
        return s.extend('make-%s' % ast.name, ast)

    def make_tuples(self, params, vals):
        """
        returns a list of tupes of params and vals
        :param params: [String]
        :param vals: [Value]
        :return: [(string, value)]
        :raises: BSLError if len(params) not equal len(vals)
        """
        if len(params) != len(vals):
            raise BSLError("params and vals must be equal")
        new_vals = copy.copy(vals)
        new_params = copy.copy(params)

        result = []
        while len(new_params) != 0:
            name = new_params.pop()
            val = new_vals.pop()
            result.insert(0, (name, val))

        return result