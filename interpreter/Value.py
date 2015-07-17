class Structure:
    """
    Represents a combination of an arbitirary number of values
    """
    def __init__(self, name, fields):
        """
        :param fields: Values to represent an arbitrary number of fields
        """
        self.name = name
        self.fields = fields

    def __eq__(self, other):

        if not isinstance(other, Structure):
            return False

        elif self.name != other.name:
            return False

        elif len(self.fields) != len(other.fields):
            return False

        else:
            for i in range(len(self.fields)):
                if not self.fields[i].__eq__(other.fields[i]):
                    return False

            return True


    def add_defs(self, defs):
        """
        Adds the new defintions of the make-struct to scope
        :param defs: Scope
        :return: a new Scope containing the new defintions
        """
        struct_def = defs.get(self.name)
        def_fields = struct_def.fields
        make_fields = self.fields
        new_defs = defs

        # At this point, we know they are they map to eachother, because we've already
        # evaluated the struct before calling this method in the selector class

        for i in range(len(make_fields)):
            new_defs = new_defs.extend(def_fields[i], make_fields[i])

        return new_defs

class Pair(Structure):
    """
    Represents a combination of two values
    """
    def __init__(self, x, y):
        super().__init__('posn', [x, y])


        # Value is one of:
        # -- Number
        # -- Pair(Value,Value)
        # -- Struct(String, [Value])

