from abc import abstractmethod

class BSLDef:
    """
    To represent Definitions
    EX: function definitions, structs, definitions
    """

    @abstractmethod
    def equals(self, other):
        raise NotImplementedError('Method not yet implemented')
