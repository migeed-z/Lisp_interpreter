from interpreter.BslError import BSLError


class FuncDef:
    """
    To represent function definitions
    """

    def __init__(self, name, body, params):
        """
        :param name: String to represent the name of the function
        :param body: BSLexpr
        :param params: [String]
        """
        self.name = name
        self.body = body

        if all(isinstance(item, str) for item in params):
            self.params = params

        else:
            raise BSLError('Parameters can only be strings')

