from BSLexpr import BSLexpr
from BslError import BSLError

class BSLlist:
    """
    To represent List of sExpressions
    """

    def __init__(self, sl):
        """
        :param sl: List of BSLexpr
        """
        self.sl = self.validate(sl)

    def helper_eval(self, defs):
        """
        Returns the values of this list
        :return: List of values of sExpressions evaluations
        """
        result = []
        for sexpr in self.sl:
            result.append(sexpr.eval(defs))

        return result

    def helper_equals(self, element):
        """
        evaluates each sexpression to return a boolean then evaluates booleans and returns the result
        :return: items in this list are equal to items in element
        """
        if len(self.sl) != len(element.sl):
            return False

        else:
            result = True
            for i in range(len(self.sl)):
                result = result and self.sl[i].equals(element.sl[i])

            return result

    def validate(self, sl):
        if not isinstance(sl, list):
            raise BSLError('SL must be a List')

        for item in sl:
            if not isinstance(item, BSLexpr):
                raise BSLError('Not a BSL expression')

        return sl






