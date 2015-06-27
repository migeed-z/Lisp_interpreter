from interpreter import Num, Variable, BSLlist, Add, Multiply, Subtract, Divide
from parser import exp_parser

class Test_parser:
    """
    To represent Parser tests
    """

    def test_nums_and_vars(self):
        assert exp_parser(42).equals(Num(42))
        assert exp_parser('xyz').equals(Variable('xyz'))

    def test_not_bsl_expr(self):
        assert not exp_parser([])
        assert not exp_parser([1])
        assert not exp_parser(([1, '+']))
        assert not exp_parser([1,'+',1])
        assert not exp_parser(['+',1,[1,'+']])
        assert not exp_parser(['-'])
        assert not exp_parser(['/'])
        assert not exp_parser('+')
        assert not exp_parser('define')

    def test_add_bsl_expr(self):
        assert exp_parser(['+']).equals(Add(BSLlist([])))
        assert exp_parser(['+', 1]).equals(Add(BSLlist([ Num(1)])))
        assert exp_parser(['+', 1, 1]).equals(Add(BSLlist([Num(1), Num(1)])))
        assert exp_parser(['+', 1,['+', 1]]).equals(Add(BSLlist([Num(1), Add(BSLlist([Num(1)]))])))

    def test_mult_bsl_expr(self):
        assert exp_parser(['*', 1, 1]).equals(Multiply(BSLlist([Num(1), Num(1)])))
        assert exp_parser(['*']).equals(Multiply(BSLlist([])))
        assert exp_parser(['*', 1,['*', 1]]).equals(Multiply(BSLlist([Num(1), Multiply(BSLlist([Num(1)]))])))

    def test_subtract_bsl_expr(self):
        assert exp_parser(['-', 1, 1]).equals(Subtract(BSLlist([Num(1), Num(1)])))
        assert exp_parser(['-', 1,['-', 1]]).equals(Subtract(BSLlist([Num(1), Subtract(BSLlist([Num(1)]))])))
        assert exp_parser(['-', 1]).equals(Subtract(BSLlist([Num(1)])))

    def test_divide_bsl_expr(self):
        assert exp_parser(['/', 1, 1]).equals(Divide(BSLlist([Num(1), Num(1)])))
        assert exp_parser(['/', 1,['-', 1]]).equals(Divide(BSLlist([Num(1), Subtract(BSLlist([Num(1)]))])))
        assert exp_parser(['/', 1]).equals(Divide(BSLlist([Num(1)])))

    def test_composite_bsl_expr(self):
        assert exp_parser(['*', 1,['+', 1]]).equals(Multiply(BSLlist([Num(1), Add(BSLlist([Num(1)]))])))
        assert exp_parser(['*', 1, ['-', 2, 2], ['/', 1]]).equals(Multiply(BSLlist([Num(1), Subtract(BSLlist([Num(2),
                                                                                Num(2)])), Divide(BSLlist([Num(1)]))])))










