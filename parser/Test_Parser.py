from interpreter.Num import Num
from interpreter.Variable import Variable
from interpreter.BSLlist import BSLlist
from interpreter.Add import Add
from parser.Parser import exp_parser


#  42                 Num(42)
#  'xyz'              Var('xyz')
#  ['+',1,1]          Add([Num(1),Num(1)])
#  ['+',['+',1,1],1]  Add([Add([Num(1),Num(1)]),Num(1)])
#  [1,'+',1]          False
#  ['+',1,['+',1]]    Add([Num(1), Add([Num(1)])
#  ['+',1,[1,'+']]    False
#  []                 False
#  [1]                False


class Test_parser:

    def test_nums(self):
        assert exp_parser(42).equals(Num(42))
        assert exp_parser(['+', 1, 1]).equals(Add(BSLlist([Num(1), Num(1)])))
        assert exp_parser(['+', 1,['+', 1]]).equals(Add(BSLlist([Num(1), Add(BSLlist([Num(1)]))])))
        assert exp_parser('xyz').equals(Variable('xyz'))
        assert not exp_parser([])
        assert not exp_parser([1])
        assert not exp_parser(([1, '+']))
        assert not exp_parser([1,'+',1])
        assert not exp_parser(['+',1,[1,'+']])









