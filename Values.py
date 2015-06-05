from Pair import Pair

def compare(one_value, other_value):
    if (isinstance(one_value, (int, float, complex))) and (isinstance(other_value, (int, float, complex))):
        return other_value == other_value
    else:
        return isinstance(one_value, Pair) and isinstance(other_value, Pair) and \
               compare(one_value.left, one_value.left) and compare(one_value.right, other_value.right)

