class Structure:
    """
    To represent the Value of a Function Application of a ConstuctorDef
    """

    def __init__(self, name, tuples):
        self.name = name
        self.tuples = tuples

    def __eq__(self, other):

        if not isinstance(other, Structure):
            return False

        elif self.name != other.name:
            return False

        else:
            for i in range(len(self.tuples)):
                if self.tuples[i] != other.tuples[i]:
                    return False

        return True

    def __str__(self):
        vals = ()
        for v in self.tuples:
            vals = vals + (v[0],)
        return '%s(%s, %s)' % ('Structure', self.name, str(vals))
