import DirPaths
from BSLExpr import BSLExpr
from FuncType import FuncType
from BSLError import BSLError
from Applicable import Applicable

class FuncApplication(BSLExpr):
    """
    To represent function applications
    """

    def __init__(self, fuction_position, sl):
        """
        :param name: LambdaExpr
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

    def type_of(self, acc):
        func = self.function_position
        t = func.type_of(acc)
        if not isinstance(t, FuncType):
            raise BSLError('%s is not an instance of FuncType' % str(t))
        if t.frm_list == self.sl.type_of_helper(acc):
            return t.to_type
        else:
            raise BSLError('Domain Type does not match the argument type')


