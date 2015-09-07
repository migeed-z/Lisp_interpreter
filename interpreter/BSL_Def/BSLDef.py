import DirPaths
from BSLError import BSLError

class BSLDef:
    """
    To represent a BSL Defintion
    """

    def __init__(self, name, params):
        """
        :param params: [String]
        """
        if len(params) != len(set(params)):
            raise BSLError('Duplicate Params are not allowed in Function definitions')
        self.params = params
        self.name = name

