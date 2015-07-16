from interpreter.BSLDef import BSLDef
from interpreter.BSLError import BSLError

class FuncDefinition(BSLDef):
    """
    To represent function definitions
    """

    def __init__(self, name, params, body):
        """
        :param name: String to represent the name of the function
        :param body: BSLexpr
        :param params: [String]
        """
        self.name = name
        self.body = body
        if len(params) != len(set(params)):
            raise BSLError('Duplicate Params are not allowed in Function definitions')
        self.params = params

    def equals(self, other):
        """
        is this equal to other?
        :param other:
        :return:
        """

        if not isinstance(other, FuncDefinition):
            return False

        else:
            return other.name == self.name and other.params == self.params and (other.body).equals(self.body)


