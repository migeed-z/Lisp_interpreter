class Scope:
    """
    To represent the definitions as a tuple T, where t[0] is a key, t[1] is a value and t[2] is
    the old scopre
    """

    def __init__(self, defs):
        """
        Initialises the scope from a tuple with three elements
        :param defs: Tuple containing three elements. If no definitions exist, we may use an empty tuple
        :return:
        """
        self.defs = defs

    def extend(self, name, val):
        return Scope((name,val,self))

    def get(self, key):
        if not self.defs:
            return None
        else:
            name = self.defs[0]
            val = self.defs[1]
            old_self = self.defs[2]
            if key == name:
                return val
            else:
                return old_self.get(key) #will return none unless the tuple is formed of three elements




