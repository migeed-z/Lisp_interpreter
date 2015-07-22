from interpreter.StructSelector import StructSelector

class Posn_x(StructSelector):
    """
    To represent the x-coordinate of a Posn
    """

    def __init__(self, sub_expr):
        super().__init__('posn', sub_expr, 'x')

