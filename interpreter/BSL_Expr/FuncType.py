from Type import Type


class FuncType(Type):
    """
    Where frm is the first Param, to_again is the second param
    and to is the type of the result
    """

    def __init__(self, frm_list, to_type):
        """
        :param frm_list: [Type]
        :param to_type: Type
        """
        self.frm_list = frm_list
        self.to_type = to_type

    def __eq__(self, other):
        if not isinstance(other, FuncType):
            return False
        else:
            return self.frm_list == other.frm_list \
                   and self.to_type == other.to_type

    def __str__(self):
        return '%s -> %s' % (str(self.frm_list),
                                str(self.to_type))

