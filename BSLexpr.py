from abc import ABCMeta, abstractmethod


class BSLexpr:

    @abstractmethod
    def eval(self, defs):
        """
        sexpr Scope -> Value

        Value is one of:
            -- Number
            -- Pair(Value,Value)
        defs: Scope
        Evaluates this sExpression
        :return: The value of evaluating this sExpression
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


