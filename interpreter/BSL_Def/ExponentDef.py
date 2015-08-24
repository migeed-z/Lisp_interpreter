from math import pow

class ExponentDef:
    """

    """

    def __init__(self):
        pass

    def apply(self, name, vals):
        """

        :param vals:
        :param name:
        :return:
        """
        #check len == 2

        base = vals[0]
        power = vals[1]

        return pow(base, power)



