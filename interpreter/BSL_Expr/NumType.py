from Type import Type


class NumType(Type):

    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, NumType)


    def __str__(self):
        return 'Num'