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

    def equals(self, other):

        if isinstance(other, Structure):
            if len(other.fields) != len(self.fields):
                return False

        else:
            if self.name != other.name:
                return False
            for i in range(len(self.fields)):
                if self.fields[i] != other.fields:
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

    #Struct is:
    # -- Structure(*fields)
