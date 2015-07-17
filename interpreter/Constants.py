from interpreter.Num import Num
from interpreter.Add import Add
from interpreter.Multiply import Multiply
from interpreter.Subtract import Subtract
from interpreter.Divide import Divide
from interpreter.Variable import Variable
from interpreter.FuncDefinition import FuncDefinition
from interpreter.FuncApplication import FuncApplication
from interpreter.BSLlist import BSLlist
from interpreter.If0 import If0
from interpreter.Posn import Posn
from interpreter.BSLStruct import BSLStruct
from interpreter.BSLMakeStruct import BSLMakeStruct
from interpreter.Value import Structure
from interpreter.Value import Pair
from interpreter.Posn_x import Posn_x
from interpreter.MakePosn import MakePosn
from interpreter.Scope import Scope
from interpreter.StructSelector import StructSelector


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

    posn11 = MakePosn(Num(1), Num(1))
    pair11 = Pair(1, 1)

    func_app_varx_1 = FuncApplication('f', BSLlist([MakePosn(func_app_varx, Num(1))]))
    pair41 = Pair(4, 1)

    posn_x_11 = Posn_x(posn11)
    posn_y_func_app_varx_1 = Posn_x(func_app_varx_1)

    posn_x1_error = Posn_x(Num(1))

    list_posn_x_11_5 = BSLlist([posn_x_11, Num(5)])
    list_posn11 = BSLlist([posn11])

    expraddposnx_11_5 = Add(list_posn_x_11_5)
    expraddposn11 = Add(list_posn11)

    posn_42_21 = MakePosn(Num(42), Num(21))
    func_def_posn_42_11 = FuncDefinition('d', ['x'], posn_42_21)
    func_app_100 = FuncApplication('d', BSLlist([Num(100)]))
    posn_x_func_app_100 = Posn_x(func_app_100)


    posnsexpr_error2 = Add(BSLlist([Num(1), func_app_100]))

    defs1 = Scope(()).extend('x', 1).extend('y',4).extend('f', func_def_varx).extend('g', funcDef2).extend('z', func_def_add_varx_vary) \
        .extend('d', func_def_posn_42_11)

    ex1 = '(ex*'
    ex_abc = 'abc'
    ex_1 = '1'

    exx1 = ')'
    exx2 = ex_abc + exx1

    #Structs

    struct_def_xy = BSLStruct('struct_posn', ['x', 'y'])
    struct_def_lrm = BSLStruct('lrm', ['left', 'mid', 'right'])

    defs1 = defs1.extend('struct_posn', struct_def_xy).extend('lrm', struct_def_lrm)

    make_struct_12 = BSLMakeStruct('struct_posn', [Num(1), Num(2)])
    val_structure_12 = Structure('struct_posn', [1, 2])

    make_struct_composite_13 = BSLMakeStruct('struct_posn', [make_struct_12, make_struct_12])
    val_structure_composite_13 = Structure('struct_posn', [val_structure_12, val_structure_12])

    make_struct_composite_left_right_mid = BSLMakeStruct('lrm', [make_struct_12, make_struct_composite_13, Variable('x')])
    val_structure_composite_left_right_mid = Structure('lrm',
                                                       [val_structure_12, val_structure_composite_13, 'x'])

    # Struct Selectors
    select_x = StructSelector(val_structure_12, 'x')
    select_mid = StructSelector(val_structure_composite_left_right_mid, 'mid')
    select_mid_make = StructSelector(make_struct_composite_left_right_mid, 'mid')

    #Posn
    defs1 = defs1.extend('posn', Posn())

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
