class BSLlist:
    """
    To represent [sExpressions]
    """

    def __init__(self, sl):
        """
        :param sl: [BSLexpr]
        """
        self.sl = sl

    def helper_eval(self, defs):
        """
        Returns the values of evaluating S-expressions of this list
        :return: [values]
        """
        result = []
        for sexpr in self.sl:
            result.append(sexpr.eval(defs))

        return result

    def __eq__(self, element):
        """
        evaluates each S-expression to return a boolean then evaluates booleans and returns the result
        :return: Items in this list are equal to items in element
        """
        if len(self.sl) != len(element.sl):
            return False

        else:
            result = True
            for i in range(len(self.sl)):
                result = result and self.sl[i].__eq__(element.sl[i])

            return result

    def __len__(self):
        return len(self.sl)



