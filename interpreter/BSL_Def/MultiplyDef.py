class MultiplyDef:
    """
    To represent Primitive Operations
    """

    def __init__(self):
        pass

    def apply(self, name, args):
        """
        Multiplies all elements in args
        :param name: 
        :param vals: 
        :return:
        """
        total = 1
        for element in args:
            total = total * element

        return total