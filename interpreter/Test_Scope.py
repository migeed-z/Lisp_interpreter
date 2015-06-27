import pytest

from interpreter.Scope import Scope
from interpreter.BslError import BSLError


class Test_scope:

    def test_1(self):

        defs = Scope(()).extend('g',2).extend('f', 1)
        defs2 = defs.extend('x', 3)
        defs3 = defs.extend('f', 3)

        assert defs2.get('x') == 3
        assert defs3.get('f') == 3

        # with pytest.raises(BSLError):
        #     defs.extend(4, 4)
        #
        # with pytest.raises(BSLError):
        #     Scope([])
        #
        # with pytest.raises(BSLError):
        #     Scope((1, 2, 3, 4))








