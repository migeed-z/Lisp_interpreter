import DirPaths
from sys import stdin, stdout
from Reader import Reader
from Parser import parse
from ParserError import ParserError
from BSLError import BSLError
from FuncDef import FuncDef
from StructDef import StructDef
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

            if isinstance(ast, FuncDef) or isinstance(ast,StructDef):
                s = ast.eval(s) #S IS A SCOPE
            else:
                try:
                    x = ast.eval(s) #X IS A VALUE
                    print str(x)
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


