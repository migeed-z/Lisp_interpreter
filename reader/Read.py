import DirPaths
from sys import stdin, stdout
from Reader import Reader
from Parser import parse
from ParserError import ParserError
from BSLError import BSLError
from FuncDef import FuncDef
from StructDef import StructDef
from Scope import Scope
from Global_Scope import foo


def read_eval_print_loop():
    """
    read S-expression, parse and evaluate, print, REPEAT
    :return: None
    """
    global_s = foo

    while True:

        try:
            p_expr = read()
            if p_expr == False:
                break
            elif not p_expr:
                continue
            ast = parse(p_expr)
            [the_value,s] = ast.eval(global_s.getter())
            global_s.setter(s)
            if the_value:
                print str(the_value)
        except ParserError:
            print ('bla bla bla')


def read():
    """
    Reads a line from the IP and instantiates a Reader using the IP
    and returns the resulting p-expression
    :return: p_expr
    """
    try:
        ip = read_lines()
        if not ip:
            return False
        r = Reader(ip)
        p_expr = r.reader()
        return p_expr

    except:
        return None


def read_lines():
    """
    Reads lines from std input
    :return: List containing input seperated by space
    """
    input_list = []
    stdout.write("> ")
    stdout.flush()

    while True:
        try:
            userinput = raw_input()
            input_list.append(userinput)
            all_input = ' '.join(input_list)
            if has_equal_parens(all_input):
                return all_input

        except (EOFError):
            return None



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


print("Zeina's BSL intepreter, v.06\n")
read_eval_print_loop()


