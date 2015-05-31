class SL:
    """
    To represent List of sExpressions
    """

    def __init__(self, sl):
        self.sl = sl

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
            for i in range(0, len(self.sl)):
                result = result and self.sl[i].equals(element.sl[i])

            return result


    def helper_subst(self, var, val):
        """
        Substitutes all occurences of var in this SL with val
        :param var: String
        :param val: Numerical value
        :return: SL
        """
        result = []
        for sexpr in self.sl:
            result.append(sexpr.subst(var, val))
        return SL(result)

    def helper_substAll(self, defs):
        """
        Substitutes all keys in defs with their corresponding values in this SL
        :param defs: Dictionary of key-value pairs
        :return: SL
        """
        result = []
        for sexpr in self.sl:
            result.append(sexpr.substAll(defs))
        return SL(result)






