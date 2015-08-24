class AddDef:
    """
    To represent Primitive Operations
    """

    def __init__(self):
        pass


    def apply(self, name, args):
        """
        Adds all elements in args
        :param name:
        :param vals:
        :return:
        """
        total = 0
        for element in args:
            total = total + element

        return total


