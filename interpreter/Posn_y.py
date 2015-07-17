from interpreter.StructSelector import StructSelector

class Posn_y(StructSelector):
    """
    To represent the y coordinate of a Posn
    """

    def __init__(self, sub_expr):
        super().__init__(sub_expr, 'y')

