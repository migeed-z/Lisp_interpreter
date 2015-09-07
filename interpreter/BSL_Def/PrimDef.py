import DirPaths
from abc import abstractmethod
from BSLError import BSLError

class PrimDef:
    """
    To represent Primitive Operations
    """

    def __init__(self):
        pass

    @abstractmethod
    def apply(self, name, args):
        """
        applies definition to all elements in args
        :param args: Arguments to evaluate
        :return: Value of the result
        """
        raise NotImplementedError('Method not yet implemented')

    def validate(self, args, type):
        """
        Ensure that list of args are of type type
        :param args: List of values
        :param type: type that args need to be
        :return: True if elements are of type type and false otherwise
        """
        for arg in args:
            if not isinstance(arg, type):
                raise BSLError('Arguments are of incorrect type.')