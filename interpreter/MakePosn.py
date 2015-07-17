from interpreter.BSLMakeStruct import BSLMakeStruct

class MakePosn(BSLMakeStruct):
    """
    To represent make-posn
    """

    def __init__(self, x, y):
        """
        :param x: BSLExpr
        :param y: BSLExpr
        """
        super().__init__('posn', [x, y])

