from abc import ABCMeta, abstractmethod


class sExpr:

    @abstractmethod
    def eval(self, defs):
        """
        defs: Scope
        Evaluates this sExpression
        :return: The value of evaluating this sExpression
        """
        raise NotImplementedError('Method not yet implemented')


    @abstractmethod
    def equals(self, other):
        """
        Is this sExpr equal to other?
        :param other: Any
        :return: True if this = other and false otherwise
        """
        return NotImplementedError('Method not yet implemented')

    @abstractmethod
    def subst(self, var, val):
        """
        Substitutes all Variable occurrences with val
        :param val: Numerical value
        :return: sExpr
        """
        return NotImplementedError('Method not yet implemented')

    @abstractmethod
    def substAll(self, defs):
        """
        Substitutes all keys in defs with their corresponding values in this sExpr
        :param defs: Dictionary of keys and values
        :return: sExpr
        """
        return NotImplementedError('Method not yet implemented')

