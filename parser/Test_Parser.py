from interpreter import Num, Variable, BSLlist, Add, Multiply, Subtract, Divide, FuncDefinition, FuncApplication
from parser import exp_parser, func_def_parser, parse_name, parse_params, validate_duplicates, validate_reserved_words

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
        assert not exp_parser(['+', '+', 1, 3])

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

    def test_function_definition(self):
         assert func_def_parser(['define', ['add', 'x', 'y', 'z'], ['+', 1, 3]]).equals(FuncDefinition('add', ['x', 'y', 'z'],
                                                                                    Add(BSLlist([Num(1), Num(3)]))))
         assert func_def_parser(['define', 'add', ['+', 1, 3]]).equals(FuncDefinition('add', [], Add(BSLlist([Num(1), Num(3)]))))

    def test_not_function_definition(self):

        assert not parse_name('+')
        assert not parse_name(['+', 'x', 'y', 'z'])
        assert not parse_name(['+'])
        assert not parse_params(['Add', 'x', 'x'])
        assert not parse_params(['Add', '+', 'y', 'z'])

        assert not func_def_parser(['define'])
        assert not func_def_parser(['define', 'add'])

        assert not func_def_parser(['a', ['add', 'x', 'y', 'z'], ['+', '+', 3]])
        assert not func_def_parser(['define', ['+', 1, 3]])
        assert not func_def_parser(['define', ['+', 'x', 'y', 'z'], ['+', 1, 3]])
        assert not func_def_parser(['define', ['Add', '+', 'y', 'z'], ['+', 1, 3]])
        assert not func_def_parser(['define', ['Add', 'x', 'y', 'z'], ['+', '+', 3]])

    def test_function_application(self):
        assert exp_parser(['f', 1]).equals(FuncApplication('f', BSLlist([Num(1)])))
        assert exp_parser(['f', 1, 2]).equals(FuncApplication('f', BSLlist([Num(1), Num(2)])))
        assert exp_parser(['x',1]).equals(FuncApplication('x',BSLlist([Num(1)])))
        assert not exp_parser(['define',['x',1],1])





