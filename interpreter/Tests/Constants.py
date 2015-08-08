from interpreter import Divide, Subtract, Add, Multiply, Num
from interpreter import Variable
from interpreter import FuncDefinition
from interpreter import FuncApplication
from interpreter import BSLlist
from interpreter import If0
from interpreter import Scope
from interpreter import Structure
from interpreter import StructDefinition

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

    # funcDef2 = FuncDefinition('g',[], expradd_func_app_varx)
    # func_app_emptylist = FuncApplication('g', BSLlist([]))

    expradd_varx_vary = Add(BSLlist([varx, vary]))

    func_def_add_varx_vary = FuncDefinition('z', ['x', 'y'], expradd_varx_vary)
    func_app_varx_vary = FuncApplication('z', BSLlist([Num(7), Num(7)]))
    func_app_error_777 = FuncApplication('z', BSLlist([Num(7), Num(7), Num(7)]))

    if_012 = If0(Num(0), Num(1), Num(2))
    # if_varx_varx_emptylist = If0(func_app_varx, func_app_varx, func_app_emptylist)
    # if_emptylist_42_varx = If0(func_app_emptylist, Num(42), func_app_varx)

    # funcApp4 = FuncApplication('z', BSLlist([if_emptylist_42_varx, Num(2)]))

    func_app_100 = FuncApplication('d', BSLlist([Num(100)]))


    defs1 = Scope(()).extend('x', 1).extend('y',4)
    defs1 = func_def_varx.update_func(defs1)
    #defs1 = funcDef2.update_func(defs1)
    defs1 = func_def_add_varx_vary.update_func(defs1)

    #structs
    posn_def = StructDefinition('posn', ['x', 'y'])
    defs1 = posn_def.update_scope(defs1)

    zeina_def = StructDefinition('zeina', ['x', 'y'])
    defs1 = zeina_def.update_scope(defs1)

    make_zeina = FuncApplication('make-posn', BSLlist([Num(10), Num(20)]))

    select_zeina_x = FuncApplication('zeina-x', BSLlist([make_zeina]))


    # (define-struct zeina (x y))
    # (zeina-x (make-posn 10 20))

    make_posn = FuncApplication('make-posn', BSLlist([Num(1), Num(2)]))
    make_posn_comp = FuncApplication('make-posn', BSLlist([make_posn, Num(2)]))

    is_posn = FuncApplication('is-posn', BSLlist([make_posn]))
    is_not_posn = FuncApplication('is-posn', BSLlist([Num(3)]))

    select_posn_x = FuncApplication('posn-x', BSLlist([make_posn]))
    select_posn_y = FuncApplication('posn-y', BSLlist([make_posn]))

    select_posn_x_comp = FuncApplication('posn-x', BSLlist([make_posn_comp]))
    select_posn_y_comp = FuncApplication('posn-y', BSLlist([make_posn_comp]))

    value_posn = Structure('posn', [('x', 1), ('y', 2)])
    value_posn_comp = Structure('posn', [('x', value_posn), ('y', 2)])

    #functions using struct
    make_posn_func = FuncApplication('make-posn', BSLlist([func_app_varx, Num(1)]))
    func_app_varx_1 = FuncApplication('f', BSLlist([make_posn_func]))

    value_posn_func = Structure('posn', [('x', 4), ('y', 1)])

    posn_x_func_app_varx_1 = FuncApplication('posn-x', BSLlist([func_app_varx_1]))

    select_posn_x_error = FuncApplication('posn-x', BSLlist([Num(3)]))


    ex1 = '(ex*'
    ex_abc = 'abc'
    ex_1 = '1'

    exx1 = ')'
    exx2 = ex_abc + exx1




