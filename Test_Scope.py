from Scope import Scope

class Test_scope:

    def test_1(self):

        defs = Scope(()).extend('g',2).extend('f', 1)
        defs2 = defs.extend('x', 3)
        defs3 = defs.extend('f', 3)

        assert defs2.get('x') == 3
        assert defs3.get('f') == 3





