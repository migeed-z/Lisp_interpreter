class SubtractDef:
    """
    To represent Primitive Operations
    """

    def __init__(self, *args):
        pass

    def apply(self, name, args):
        """
        Subtracts all elements in args
        :param name: 
        :param vals: 
        :return:
        """
        if 1 == len(args):
            return 0 - args[0]
        else:
            total = args.pop(0)
            for element in args:
                total = total - element
            return total
