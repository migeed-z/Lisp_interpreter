from interpreter.BSLStruct import BSLStruct

class Posn(BSLStruct):
    """
    To represent a BSL Posn
    """

    def __init__(self):
        super().__init__('Posn', ['x', 'y'])


