#! /usr/bin/env python3
from sys import stdin, stdout
from Reader import Reader
from parser import exp_parser, func_def_parser
from interpreter import BSLError
from interpreter import Scope


def read():
    """
    Reads text from stdin
    :return: s-expression
    """
    s = Scope([])
    while True:
        stdout.write("\033> ")
        stdout.flush()
        userinput = stdin.readline()
        r = Reader(userinput)

        p_expr = r.reader()
        print('p_expr = ',p_expr)
        if not p_expr:
            break

        is_p_expr_a_bsl_expr = exp_parser(p_expr)

        if not is_p_expr_a_bsl_expr:
            bsl_def = func_def_parser(p_expr)
            if not bsl_def:
                print('wrong!')
            else:
                if isinstance(p_expr[1], str):
                    s = s.extend(bsl_def.name, bsl_def.body.eval(s))
                else:
                    s = s.extend(bsl_def.name, bsl_def)
        else:
            try:
                result = is_p_expr_a_bsl_expr.eval(s)
                print(result)
            except BSLError:
                print('an eval exception happened')

print("Zeina's BSL intepreter, v.0006\n")
read()

