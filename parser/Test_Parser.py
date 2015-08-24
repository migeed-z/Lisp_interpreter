import DirPaths

from Num import Num
from Variable import Variable
from BSLlist import BSLlist
from FuncDefinition import FuncDefinition
from FuncApplication import FuncApplication
from StructDefinition import StructDefinition

from Parser import exp_parser, func_def_parser, struct_def_parser, ParserError
import pytest

lang = 'BSL'

class Test_parser:
    """
    To represent Parser tests
    """
    def test_nums_and_vars(self):
        assert exp_parser(42, lang) == Num(42)
        assert exp_parser('xyz', lang).__eq__(Variable('xyz'))

    def test_not_bsl_expr(self):

        with pytest.raises(ParserError):
            exp_parser([], lang)

        assert not exp_parser([1], lang) #raise error
        assert not exp_parser([1, '+'], lang)

        with pytest.raises(ParserError):
            exp_parser('+', lang)

        assert not exp_parser([1,'+',1], lang) #raise an error!!!!

        with pytest.raises(ParserError):
            exp_parser(['+',1,[1,'+']], lang)

        with pytest.raises(ParserError):
            exp_parser('define', lang)

        with pytest.raises(ParserError):
            exp_parser(['+', '+', 1, 3], lang)
            exp_parser('+', lang)

        with pytest.raises(ParserError):
            exp_parser(['-'], lang)

        with pytest.raises(ParserError):
            exp_parser(['/'], lang)

    def test_add_bsl_expr(self):
        assert exp_parser(['+'], lang) == FuncApplication('+', BSLlist([]))
        assert exp_parser(['+', 1], lang) == FuncApplication('+', BSLlist([ Num(1)]))
        assert exp_parser(['+', 1, 1], lang) == FuncApplication('+', BSLlist([Num(1), Num(1)]))
        assert exp_parser(['+', 1,['+', 1]], lang) == \
               (FuncApplication('+', BSLlist([Num(1), FuncApplication('+', BSLlist([Num(1)]))])))

    def test_mult_bsl_expr(self):
        assert exp_parser(['*', 1, 1], lang) == (FuncApplication('*', BSLlist([Num(1), Num(1)])))
        assert exp_parser(['*'], lang).__eq__(FuncApplication('*', BSLlist([])))
        assert exp_parser(['*', 1,['*', 1]], lang) == \
               (FuncApplication('*', BSLlist([Num(1), FuncApplication('*',BSLlist([Num(1)]))])))

    def test_subtract_bsl_expr(self):
        assert exp_parser(['-', 1, 1], lang).__eq__(FuncApplication('-', BSLlist([Num(1), Num(1)])))

        assert exp_parser(['-', 1,['-', 1]], lang) ==\
               (FuncApplication('-', BSLlist([Num(1), FuncApplication('-', BSLlist([Num(1)]))])))
        assert exp_parser(['-', 1], lang) == FuncApplication('-', BSLlist([Num(1)]))

    def test_divide_bsl_expr(self):
        assert exp_parser(['/', 1, 1], lang) == (FuncApplication('/', BSLlist([Num(1), Num(1)])))
        assert exp_parser(['/', 1,['-', 1]], lang) ==\
               (FuncApplication('/', BSLlist([Num(1), FuncApplication('-', BSLlist([Num(1)]))])))
        assert exp_parser(['/', 1], lang).__eq__(FuncApplication('/', BSLlist([Num(1)])))

    def test_composite_bsl_expr(self):
        assert exp_parser(['*', 1,['+', 1]], lang) == \
               (FuncApplication('*', BSLlist([Num(1), FuncApplication('+', BSLlist([Num(1)]))])))

        assert exp_parser(['*', 1, ['-', 2, 2], ['/', 1]], lang) == (FuncApplication('*', BSLlist([Num(1), FuncApplication('-', BSLlist([Num(2),
                                                                            Num(2)])), FuncApplication('/', BSLlist([Num(1)]))])))

    def test_function_definition(self):

        assert func_def_parser(['define', ['add', 'x', 'y', 'z'], ['+', 1, 3]], lang)\
            .__eq__(FuncDefinition('add', ['x', 'y', 'z'], FuncApplication('+', BSLlist([Num(1), Num(3)]))))

        assert func_def_parser(['define', 'add', ['+', 1, 3]], lang)\
            .__eq__(FuncDefinition('add', [], FuncApplication('+', BSLlist([Num(1), Num(3)]))))

    def test_struct_definition(self):

        assert struct_def_parser(['define-struct', 'posn', ['x', 'y']], lang) == (StructDefinition('posn', ['x', 'y']))
        assert struct_def_parser(['define-struct', 'add', ['x', 'y', 'z']], lang) == StructDefinition('add', ['x', 'y', 'z'])

        assert not exp_parser(['define-struct', 'add', ['x', 'y', 'z']], lang)

    def test_not_struct_def(self):
        with pytest.raises(ParserError):
            struct_def_parser(['define-struct', 'posn', [1, 2, 3]], lang)

        with pytest.raises(ParserError):
            struct_def_parser(['define-struct', 1, []], lang)

    def test_not_function_definition(self):

        with pytest.raises(ParserError):
            func_def_parser(['define', ['f', 'x', 1, 'y'], 42], lang)

        with pytest.raises(ParserError):
            func_def_parser(['define'], lang)
            func_def_parser(['define', 'add'], lang)
            func_def_parser(['define', ['+', 1, 3]], lang)
            func_def_parser(['define', ['Add', '+', 'y', 'z'], ['+', 1, 3]], lang)

        with pytest.raises(ParserError):
            func_def_parser(['define', ['+', 'x', 'y', 'z'], ['+', 1, 3]], lang)

        with pytest.raises(ParserError):
            func_def_parser(['define', ['Add', 'x', 'y', 'z'], ['+', '+', 3]], lang)

        assert not func_def_parser(['a', ['add', 'x', 'y', 'z'], ['+', '+', 3]], lang)

    def test_function_application(self):

        assert exp_parser(['f', 1], lang) == (FuncApplication('f', BSLlist([Num(1)])))
        assert exp_parser(['f', 1, 2], lang).__eq__(FuncApplication('f', BSLlist([Num(1), Num(2)])))
        assert exp_parser(['x',1], lang).__eq__(FuncApplication('x',BSLlist([Num(1)])))

        assert not exp_parser(['define',['x',1],1], lang)



