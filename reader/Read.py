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


def read():
    """
    Reads a line from the IP and instantiates a Reader using the IP
    and returns the resulting p-expression
    :return: p_expr
    """
    try:
        ip = read_lines()
        r = Reader(ip)
        p_expr = r.reader()
        return p_expr

    except:
        print ('Reader Error')


def read_loop():
    """
    read S-expression, parse and evaluate, print, REPEAT
    :return: None
    """
    s = Scope([]).add_definitions()

    while True:

        try:
            p_expr = read()
            if not p_expr:
                break

            ast = parse(p_expr)

            if isinstance(ast, FuncDef):
                if not ast.params:
                    s = s.extend(ast.name, ast.body.eval(s))
                else:
                    s = ast.update_func(s)

            elif isinstance(ast, StructDef):
                s = ast.update_scope(s)

            else:
                try:
                    print str(ast.eval(s))
                except BSLError:
                    print 'Interpreter Error'

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


print("Zeina's BSL intepreter, v.006\n")
read_loop()


