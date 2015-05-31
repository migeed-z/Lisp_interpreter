from BslError import BSLError

class FuncDef:

    def __init__(self, name, body, params):
        """

        :param name: String to represent the name of the function
        :param body: sExpr
        :param params: List of Strings to represent function parameters
        :return:
        """
        self.name = name
        self.body = body

        if all(isinstance(item, str) for item in params):
            self.params = params

        else:
            raise BSLError('Parameters can only be strings')




