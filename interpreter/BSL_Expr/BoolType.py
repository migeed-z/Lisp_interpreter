from Type import Type


class BoolType(Type):
    """
    To represent a Boolean type
    """

    def __init__(self):
        """

        :param sl: List of expressions of that type
        :return:
        """
        pass

    def __eq__(self, other):
        return isinstance(other, BoolType)

    def __str__(self):
        return 'Boolean'