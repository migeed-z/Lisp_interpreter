from interpreter.BSLExpr import BSLExpr
from interpreter.Value import Structure
from interpreter.BSLError import BSLError

class BSLMakeStruct(BSLExpr):
    """
    To represent Make Struct, used to create an instance of a structure
    """

    def __init__(self, struct_name, fields):
        """
        :param struct_name: String representing name of the struct
        :param fields: [BSLExpr]
        """
        self.struct_name = struct_name
        self.fields = fields

    def eval(self, defs):
        struct_def = defs.get(self.struct_name)

        if not struct_def:
            raise BSLError('Could not find structure definition')

        elif len(struct_def.fields) != len(self.fields):
            raise BSLError('Incorrect number of fields')

        fields = self.fields
        val_fields = []

        for field in fields:
            val_fields.append(field.eval(defs))

        return Structure(self.struct_name, val_fields)



