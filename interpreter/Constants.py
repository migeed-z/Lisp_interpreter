from interpreter.Num import Num
from interpreter.Add import Add
from interpreter.Multiply import Multiply
from interpreter.Subtract import Subtract
from interpreter.Divide import Divide
from interpreter.Variable import Variable
from interpreter.FuncDefs import FuncDef
from interpreter.FuncApplication import FuncApplication
from interpreter.BSLlist import BSLlist
from interpreter.If0 import If0
from interpreter.Posn import Posn
from interpreter.Value import Pair
from interpreter.Posn_x import Posn_x
from interpreter.Scope import Scope


class Constants:

    var1 = Variable('x')
    var2 = Variable('y')
    var3 = Variable('z')
    var4 = Variable('o')

    emptyList = BSLlist([])
    list2 = BSLlist([Num(1), Num(2), Num(3)])
    list3 = BSLlist([Add(list2), Num(-3)])
    list4 = BSLlist([Subtract(list2), Add(list2)])
    list5 = BSLlist([Multiply(list2)])
    list6 = BSLlist([Num(8), Num(4)])
    list7 = BSLlist([Divide(list6)])
    list8 = BSLlist([var1, Num(2), Num(3)])
    list9 = BSLlist([var2, Num(3)])
    list10 = BSLlist([Num(4), Num(3)])
    list11 = BSLlist([Num(4), Num(0), Num(3)])


    addsexpr1 = Add(BSLlist([Num(1)]))
    addsexpr2 = Add(list2)
    addsexpr3 = Add(list10)

    subsexpr1 = Subtract(BSLlist([Num(1)]))
    subsexpr2 = Subtract(list2)
    subsexpr3 = Subtract(BSLlist([addsexpr2, addsexpr3]))

    divsexpr1 = Divide(BSLlist([Num(1)]))
    divsexpr2 = Divide(list6)
    divsexpr3 = Divide(list11)

    multsexpr1 = Multiply(BSLlist([Num(1)]))
    multsexpr2 = Multiply(list6)

    compositeSexpr = Add(BSLlist([addsexpr2, divsexpr2]))

    varsexpr1 = Add(list8)
    varsexpr2 = Add(list9)
    varsexpr3 = Subtract(BSLlist([varsexpr1, varsexpr2]))

    #functions
    funcDef1 = FuncDef("f", Variable("x"), ["x"])
    funcApp1 = FuncApplication('f', BSLlist([Num(4)]))

    list11 = BSLlist([funcApp1, Num(2)])
    funcExpr = Add(list11)

    funcDef2 = FuncDef('g', funcExpr, [])
    funcApp2 = FuncApplication('g', BSLlist([]))

    funcExpr2 = Add(BSLlist([var1, var2]))

    funcDef3 = FuncDef('z', funcExpr2, ['x', 'y'])
    funcApp3 = FuncApplication('z', BSLlist([Num(7), Num(7)]))
    funcApp3Error = FuncApplication('z', BSLlist([Num(7), Num(7), Num(7)]))

    if_1 = If0(Num(0), Num(1), Num(2))
    if_2 = If0(funcApp1, funcApp1, funcApp2)
    if_3 = If0(funcApp2, Num(42), funcApp1)

    funcApp4 = FuncApplication('z', BSLlist([if_3, Num(2)]))

    posn1 = Posn(Num(1), Num(1))
    pair1 = Pair(1, 1)

    funcApp5 = FuncApplication('f', BSLlist([Posn(funcApp1, Num(1))]))
    pair2 = Pair(4, 1)

    posn_x1 = Posn_x(posn1)
    posn_x2 = Posn_x(funcApp5)

    posn_x1_error = Posn_x(Num(1))

    list12 = BSLlist([posn_x1, Num(5)])
    list13 = BSLlist([posn1])

    posnsexpr = Add(list12)
    posnsexpr_error = Add(list13)

    posn2 = Posn(Num(42), Num(21))
    funcdef4 = FuncDef('d', posn2, ['x'])
    funcApp5 = FuncApplication('d', BSLlist([Num(100)]))

    posnsexpr_error2 = Add(BSLlist([Num(1), funcApp5]))

    defs1 = Scope(()).extend('x',1).extend('y',4).extend('f', funcDef1).extend('g', funcDef2).extend('z', funcDef3)\
        .extend('d', funcdef4)

    ex1 = '(ex*'
    ex2 = 'abc' #token
    ex3 = '1'   #token

    exx1 = ')'
    exx2 = ex2 + exx1




# # ;; -----------------------------------------------------------------------------
# # ;; INPUT
# # ;; An external S-expression has the following textual representation:
# # ;; Ex1 is one of:
# # ;; -- '(' followed by Ex*
# # ;; -- Tok
# # ;; Ex* is one of:
# # ;; -- ')'
# # ;; -- Ex1 followed by Ex*
# # ;; Tok is any sequence of characters, not including '(' ')' or whitespace chars,
# # ;;  upto EOF
# #
# # ;; OUTPUT
# # ;; An S-expression is one of:
# # ;; -- Symbol
# # ;; -- Number
# # ;; -- [List-of S-expression] (which includes '() )
