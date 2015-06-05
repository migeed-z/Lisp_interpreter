from Num import Num
from Add import Add
from Multiply import Multiply
from Subtract import Subtract
from Divide import Divide
from Variable import Variable
from FuncDefs import FuncDef
from FuncApplication import FuncApplication
from SL import SL
from Scope import Scope
from If0 import If0
from Posn import Posn
from Pair import Pair
from Posn_x import Posn_x

class Constants:

    var1 = Variable('x')
    var2 = Variable('y')
    var3 = Variable('z')
    var4 = Variable('o')

    emptyList = SL([])
    list2 = SL([Num(1), Num(2), Num(3)])
    list3 = SL([Add(list2), -3])
    list4 = SL([Subtract(list2), Add(list2)])
    list5 = SL([Multiply(list2)])
    list6 = SL([Num(8), Num(4)])
    list7 = SL([Divide(list6)])
    list8 = SL([var1, Num(2), Num(3)])
    list9 = SL([var2, Num(3)])
    list10 = SL([Num(4), Num(3)])
    list11 = SL([Num(4), Num(0), Num(3)])


    addsexpr1 = Add(SL([Num(1)]))
    addsexpr2 = Add(list2)
    addsexpr3 = Add(list10)

    subsexpr1 = Subtract(SL([Num(1)]))
    subsexpr2 = Subtract(list2)
    subsexpr3 = Subtract(SL([addsexpr2, addsexpr3]))

    divsexpr1 = Divide(SL([Num(1)]))
    divsexpr2 = Divide(list6)
    divsexpr3 = Divide(list11)

    multsexpr1 = Multiply(SL([Num(1)]))
    multsexpr2 = Multiply(list6)

    compositeSexpr = Add(SL([addsexpr2, divsexpr2]))

    varsexpr1 = Add(list8)
    varsexpr2 = Add(list9)
    varsexpr3 = Subtract(SL([varsexpr1, varsexpr2]))

    #functions
    funcDef1 = FuncDef("f", Variable("x"), ["x"])
    funcApp1 = FuncApplication('f', SL([Num(4)]))

    list11 = SL([funcApp1, Num(2)])
    funcExpr = Add(list11)

    funcDef2 = FuncDef('g', funcExpr, [])
    funcApp2 = FuncApplication('g', SL([]))

    funcExpr2 = Add(SL([var1, var2]))

    funcDef3 = FuncDef('z', funcExpr2, ['x', 'y'])
    funcApp3 = FuncApplication('z', SL([Num(7), Num(7)]))
    funcApp3Error = FuncApplication('z', SL([Num(7), Num(7), Num(7)]))

    if_1 = If0(Num(0), Num(1), Num(2))
    if_2 = If0(funcApp1, funcApp1, funcApp2)
    if_3 = If0(funcApp2, Num(42), funcApp1)

    funcApp4 = FuncApplication('z', SL([if_3, Num(2)]))

    posn1 = Posn(Num(1), Num(1))
    pair1 = Pair(1, 1)

    funcApp5 = FuncApplication('f', SL([Posn(funcApp1, Num(1))]))
    pair2 = Pair(4, 1)

    posn_x1 = Posn_x(posn1)
    posn_x2 = Posn_x(funcApp5)

    posn_x1_error = Posn_x(Num(1))

    list12 = SL([posn_x1, Num(5)])
    list13 = SL([posn1])

    posnsexpr = Add(list12)
    posnsexpr_error = Add(list13)

    defs1 = Scope(()).extend('x',1).extend('y',4).extend('f', funcDef1).extend('g', funcDef2).extend('z', funcDef3)





