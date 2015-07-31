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



