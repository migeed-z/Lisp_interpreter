from interpreter.BSLDef import BSLDef
from interpreter.BSLError import BSLError

class BSLStruct(BSLDef):
    """
    To represent a BSL Structure definition
    """

    def __init__(self, name, fields):
        """
        :param name: String representing the name of the struct
        :param fields: List of Strings
        """
        self.name = name
        if len(fields) != len(set(fields)):
            raise BSLError('Duplicate Params are not allowed in Function definitions')
        self.fields = fields





