import DirPaths

from BSLExpr import BSLExpr
from BSLError import BSLError
from Applicable import Applicable


class FuncApplication(BSLExpr):
    """
    To represent function applications
    """

    def __init__(self, fuction_position, sl):
        """
        :param name: Name of the function
        :param sl: [BSLexpr]
        """
        self.function_position = fuction_position
        self.sl = sl

    def eval_internal(self, defs):
        vals = self.sl.helper_eval(defs)
        fun = self.function_position.eval_internal(defs)
        if not isinstance(fun, Applicable):
            raise BSLError('function call: expected a function after the open parenthesis, but received %s' % str(fun))
        return fun.apply(defs, vals)

    def __eq__(self, other):
        if not isinstance(other, FuncApplication):
            return False

        else:
            return self.function_position == other.function_position and self.sl.__eq__(other.sl)
