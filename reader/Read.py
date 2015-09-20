import DirPaths
import sys
from sys import stdin, stdout
from Reader import Reader
from Parser import parse
from ParserError import ParserError
from BSLError import BSLError
from BSLExpr import BSLExpr
from FuncDef import FuncDef
from StructDef import StructDef
from Lambda import Lambda
from Scope import Scope


def has_equal_parens(line):
    """
    Returns True if number of right parens is equal to the number of left parens, and returns False otherwise
    :param line: String
    :return:
    """
    left = 0
    right = 0
    for char in line:
        if char == '(':
            left +=1
        elif char == ')':
            right +=1

    if left == right:
        return True

def read_loop():

    s = Scope([]).add_definitions()

    while True:
        userinput = read_lines()

        try:
            r = Reader(userinput)

            p_expr = r.reader()
            print p_expr

            if not p_expr:
                break
        except:
            print ('Reader Error')

        try:
            ast = parse(p_expr)
            if isinstance(ast, BSLExpr):
                try:
                    return ast.eval(s)
                except BSLError:
                    print 'Interpreter Error'

            elif isinstance(ast, FuncDef):
                if not ast.params:
                    s = s.extend(ast.name, ast.body.eval(s))
                else:
                    s = ast.update_func(s)

            elif isinstance(ast, StructDef):
                s = ast.update_scope(s)

            elif isinstance(ast, Lambda):
                s = ast.func_def.update_func(s)
                return ast.func_app.eval(s)

        except ParserError:
            print ('bla bla bla')


def read_lines():
    """
    Reads lines from std input
    :return: List containing input seperated by space
    """
    input_list = []

    while True:
        stdout.write("> ")
        stdout.flush()
        userinput = raw_input()
        input_list.append(userinput)
        all_input = ' '.join(input_list)
        if has_equal_parens(all_input):
            return all_input

def read():
    """
    Reads text from stdin
    :return: s-expression
    """
    while True:
        result = read_loop()
        print result
