from abc import abstractmethod

class BSLExpr:

    @abstractmethod
    def eval(self, defs):
        """
        Evaluates this expression
        :param defs: Scope
        :return: Value of this expresson
        """
        raise NotImplementedError('Method not yet implemented')

    @abstractmethod
    def equals(self, other):
        """
        Is this BSLexpr equal to other?
        :param other: Any
        :return: True if this = other and false otherwise
        """
        return NotImplementedError('Method not yet implemented')

