from BslError import BSLError
from BSLexpr import BSLexpr

class FuncDef:
    """
    To represent function definitions
    """

    def __init__(self, name, body, params):
        """
        :param name: String to represent the name of the function
        :param body: BSLexpr
        :param params: List of Strings to represent function parameters
        """
        self.validate(name, body, params)
        self.name = name
        self.body = body

        if all(isinstance(item, str) for item in params):
            self.params = params

        else:
            raise BSLError('Parameters can only be strings')

    def validate(self, name, body, params):
        if not isinstance(name, str):
            raise BSLError('name must be a string')
        elif not isinstance(body, BSLexpr):
            raise BSLError('body must be a BSLexpr')
        elif not isinstance(params, list):
            raise BSLError('params must be a list')
        else:
            for item in params:
                if not isinstance(item, str):
                    raise BSLError('parameter must be a string')

