from Posn_selector import Posn_Selector

class Posn_x(Posn_Selector):

    def __init__(self, sub_expr):
        super().__init__(sub_expr)

    def eval(self, defs):
        return self.eval_helper(defs).right
