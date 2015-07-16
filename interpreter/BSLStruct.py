from interpreter.BSLDef import BSLDef

class BSLStruct(BSLDef):
    """
    To represent a BSL Structure definition
    """

    def __init__(self, name, fields):
        """
        :param name: String representing the name of the struct
        :param fields: List of fields of the struct
        """
        self.name = name
        self.fields = fields



