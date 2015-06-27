#! /usr/bin/env python3
from sys import stdin, stdout

from reader.Reader import Reader
from parser.Parser import exp_parser
from interpreter import Scope
from interpreter.BslError import BSLError


def read():
    """
    Reads text from stdin
    :return: s-expression
    """
    stdout.write('> ')
    stdout.flush()
    userinput = stdin.readline()
    r = Reader(userinput)

    while True:
        p_expr = r.reader()
        print('p_expr = ',p_expr)
        if not p_expr:
            break

        bsl_expr = exp_parser(p_expr)

        if not bsl_expr:
            print('dumbo!!')
        else:
            try:
                result = bsl_expr.eval(Scope([]))
                print(result)
            except BSLError:
                print('an eval exception happened')

print("Zeina's BSL intepreter, v.0006\n")
read()
