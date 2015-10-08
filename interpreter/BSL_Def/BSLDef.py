import DirPaths
from BSLError import BSLError
from abc import abstractmethod

class BSLDef:
    """
    To represent a BSL Defintion
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

    @abstractmethod
    def eval(self, s):
        """
        evaluates this expression by updating the current scope to new_scope
        :param s: current scope
        :return: [None, new_scope]
        """
        raise NotImplementedError('This method is not yet implemented')
