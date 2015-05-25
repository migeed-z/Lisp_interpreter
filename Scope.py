class Scope:
    # a list of pairs, each pair is a name and a value

    def __init__(self,defs):
        self.defs = defs

    # name: String val: Number -> Scope
    def extend(self, name, val):
        return Scope((name,val,self))

    def get(self, key):
        name = self.defs[0]
        val = self.defs[1]
        old_self = self.defs[2]
        if key == name:
            return val
        else:
            return old_self.get(key)

    #raise Exception('Cannot evaluate variable')



