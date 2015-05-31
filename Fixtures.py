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
    funcApp1 = FuncApplication('f', SL([Num(3)]))

    list11 = SL([funcApp1, Num(2)])
    funcExpr = Add(list11)

    funcDef2 = FuncDef('g', funcExpr, [])
    funcApp2 = FuncApplication('g', SL([]))

    funcExpr2 = Add(SL([var1, var2]))

    funcDef3 = FuncDef('z', funcExpr2, ['x', 'y'])
    funcApp3 = FuncApplication('z', SL([Num(7), Num(7)]))
    funcApp3Error = FuncApplication('z', SL([Num(7), Num(7), Num(7)]))

#defs1 = Scope([('x', 1), ('y', 4), ('f', funcDef1), ('g', funcDef2)])
    defs1 = Scope([]).extend('x',1).extend('y',4).extend('f', funcDef1).extend('g', funcDef2).extend('z', funcDef3)






