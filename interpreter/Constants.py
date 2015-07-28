from Num import Num
from Add import Add
from Multiply import Multiply
from Subtract import Subtract
from Divide import Divide
from Variable import Variable
from FuncDefinition import FuncDefinition
from FuncApplication import FuncApplication
from BSLlist import BSLlist
from If0 import If0
from Scope import Scope


class Constants:

    varx = Variable('x')
    vary = Variable('y')
    varz = Variable('z')
    varo = Variable('o')

    emptyList = BSLlist([])
    list123 = BSLlist([Num(1), Num(2), Num(3)])
    listadd123 = BSLlist([Add(list123), Num(-3)])
    listaddsubtract123 = BSLlist([Subtract(list123), Add(list123)])
    listmultiply123 = BSLlist([Multiply(list123)])
    list84 = BSLlist([Num(8), Num(4)])
    listdivide84 = BSLlist([Divide(list84)])
    listx23 = BSLlist([varx, Num(2), Num(3)])
    listy3 = BSLlist([vary, Num(3)])
    list43 = BSLlist([Num(4), Num(3)])
    list403 = BSLlist([Num(4), Num(0), Num(3)])

    expradd1 = Add(BSLlist([Num(1)]))
    expradd123 = Add(list123)
    expradd43 = Add(list43)

    exprsub1 = Subtract(BSLlist([Num(1)]))
    exprsub123 = Subtract(list123)
    exprsub_add123_add123 = Subtract(BSLlist([expradd123, expradd43]))

    exprdiv1 = Divide(BSLlist([Num(1)]))
    exprdiv84 = Divide(list84)
    exprdiv403 = Divide(list403)

    exprmul1 = Multiply(BSLlist([Num(1)]))
    exprmul84 = Multiply(list84)

    expradd_expradd123_exprdiv84 = Add(BSLlist([expradd123, exprdiv84]))

    expraddx23 = Add(listx23)
    expraddy3 = Add(listy3)
    expsub_expraddx23_expradd3 = Subtract(BSLlist([expraddx23, expraddy3]))

    #functions
    func_def_varx = FuncDefinition("f", ["x"], Variable("x"))
    func_app_varx = FuncApplication('f', BSLlist([Num(4)]))

    list_func_app_varx = BSLlist([func_app_varx, Num(2)])
    expradd_func_app_varx = Add(list_func_app_varx)

    funcDef2 = FuncDefinition('g',[], expradd_func_app_varx)
    func_app_emptylist = FuncApplication('g', BSLlist([]))

    expradd_varx_vary = Add(BSLlist([varx, vary]))

    func_def_add_varx_vary = FuncDefinition('z', ['x', 'y'], expradd_varx_vary)
    func_app_varx_vary = FuncApplication('z', BSLlist([Num(7), Num(7)]))
    func_app_error_777 = FuncApplication('z', BSLlist([Num(7), Num(7), Num(7)]))

    if_012 = If0(Num(0), Num(1), Num(2))
    if_varx_varx_emptylist = If0(func_app_varx, func_app_varx, func_app_emptylist)
    if_emptylist_42_varx = If0(func_app_emptylist, Num(42), func_app_varx)

    funcApp4 = FuncApplication('z', BSLlist([if_emptylist_42_varx, Num(2)]))

    func_app_100 = FuncApplication('d', BSLlist([Num(100)]))


    posnsexpr_error2 = Add(BSLlist([Num(1), func_app_100]))

    defs1 = Scope(()).extend('x', 1).extend('y',4).extend('f', func_def_varx).extend('g', funcDef2).\
        extend('z', func_def_add_varx_vary)

    ex1 = '(ex*'
    ex_abc = 'abc'
    ex_1 = '1'

    exx1 = ')'
    exx2 = ex_abc + exx1




