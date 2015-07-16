class Pair:
    """
    Represents a combination of two values
    """
    def __init__(self, left, right):
        """
        :param left: Value
        :param right: Value
        """
        self.left = left
        self.right = right


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


def compare(one_value, other_value):
    if (isinstance(one_value, (int, float, complex))) and (isinstance(other_value, (int, float, complex))):
        return other_value == other_value
    else:
        return isinstance(one_value, Pair) and isinstance(other_value, Pair) and \
               compare(one_value.left, one_value.left) and compare(one_value.right, other_value.right)



        # Value is one of:
        # -- Number
        # -- Pair(Value,Value)
        # -- Struct(String, [Value])

