import DirPaths
from abc import abstractmethod
from BSLError import BSLError

class BSLExpr:

    def eval(ast, s):
        try:
            return [ast.eval_internal(s),s] #X IS A VALUE
        except BSLError, e:
            print str(e)
            return [None, s]

    @abstractmethod
    def eval_internal(self, defs):
        """
        Evaluates this expression
        :param defs: Scope
        :return: Value of this expresson
        """
        raise NotImplementedError('Method not yet implemented')

    @abstractmethod
    def type_of(self, acc):
        """
        Determines the type of this expression
        :return: Type
        """
        raise NotImplementedError('Method not yet implemented')


