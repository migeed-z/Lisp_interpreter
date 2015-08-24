import DirPaths
from BSLError import BSLError

class DivideDef:
    """
    To represent Primitive Operations
    """

    def __init__(self):
        pass

    def apply(self, name, args):
        """
        Divides all elements in args
        :param name: 
        :param vals: 
        :return:
        """
        if 1 == len(args):
            return 1 / args[0]
        else:
            result = args.pop(0)
            for element in args:
                if element == 0:
                    raise BSLError('Cannot Divide by Zero')
                else:
                    result = result/element

            return result
