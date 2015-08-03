from interpreter import Num, Add, Variable, BSLlist, Multiply, Subtract, Divide, FuncDefinition, FuncApplication, \
    StructDefinition
from functools import partial
from ParserError import ParserError
import copy



def exp_parser(p):
    """
    To Parse Operation expressions
    :param p:
    :return:
    """
    if isinstance(p,(complex,int,float)):
        return Num(p)
    elif isinstance(p, str):
        if is_reserved(p):
            return False

        else:
            return Variable(p)
    else:
        if not p:
            return False

        #Add expression
        elif p[0] == '+':
            return parse_operation(p, 0, Add)

        #Multiply expression
        elif p[0] == '*':
            return parse_operation(p, 0, Multiply)

        #Subtract expression
        elif p[0] == '-':
            return parse_operation(p, 1, Subtract)

        #Divide expression
        elif p[0] == '/':
            return parse_operation(p, 1, Divide)

        #function application
        elif isinstance(p[0], str) and not is_reserved(p[0]):
            name_of_function = p[0]
            return parse_operation(p, 0, partial(FuncApplication, name_of_function))

        else:
            return False

def struct_def_parser(p):
    """
    Parses Struct Definitions
    :param p: P-expression
    :return: StructDefinition
    """

    if len(p) != 3:
        return False

    elif p[0] != 'define-struct':
        return False

    elif not isinstance(p[1], str):
        raise ParserError('Struct name must be a string')

    elif is_reserved(p[1]):
        raise ParserError('Struct name is a reserved word')

    elif not isinstance(p[2], list):
        raise ParserError('Expects a list of parameters')

    # elif not parse_params(p[2]):
    #     raise ParserError('Expects a list of parameters')

    else:
        check_on_fields = is_list_of_proper_names(p[2])
        if check_on_fields == False:
            raise ParserError('Not a list of field names')

        return StructDefinition(p[1] , p[2])




    #assert struct_def_parser(['define-struct', 'posn', ['x', 'y']]) == StructDefinition('posn', ['x', 'y'])

def func_def_parser(p):
    """
    Parses Function Definitions
    :param p: P-expression
    :return: FuncDefinition
    """
    if len(p) < 3:
        return False

    elif p[0] != 'define':
        return False

    # elif not isinstance(p[1], list):
    #     return False
    #
    # elif len(p[1]) < 2:
    #     return False

    # (define f 42)
    # (define (f x y) 42)

    name = parse_name(p[1])
    params = parse_params(p[1])
    body = exp_parser(p[2])

    if (not name) or (params == False) or (body == False):
        return False

    else:
        return FuncDefinition(name, params, body)


def parse_name_from_string(expr):
    """
    parses name, given as a string
    :param expr: String
    :return: expr or False
    """
    if is_reserved(expr):
        return False
    else:
        return expr


def parse_name(expr):
    """
    Parses Function Definition name
    :param expr: [Parameters, Function name] or 'Function name'
    :return: expr or False
    """

    if isinstance(expr, str):
        return parse_name_from_string(expr)

    elif isinstance(expr, list):
        name = expr[0]
        return parse_name_from_string(name)


def parse_params(expr):
    """
    Given the ENTIRE function header (define (f x y z) x) it is given (f x y z)
    EFFECT: chops off first item
    Givem the ENTIRE struct def (define-struct s (x y z)) it is given (s x y z)
    Parses Parameters given as a String or a List
    :param expr: [string]
    :return:
     [] means we are looking at (define c ...)
     False means we are looking at (define (f define-struct x y z) ...)
     Expr - Expr[0] we are looking at (define (f x y z) ...)
    """

    if isinstance(expr, str):
        return []
    elif isinstance(expr, list):
        expr.pop(0)
        return is_list_of_proper_names(expr)

def is_list_of_proper_names(expr):
    """
    Checks that expr is a list of strings and that no string is a reserved string
    :param expr: [string]
    :return: expr or False
    False means that either a non-string is in expr or one string is reserved word
    expr  means that all elements are strings and not reserved
    """
    if not is_string_list(expr):
        return False
    elif not contains_reserved_words(expr):
        return False
    else:
        return expr
# example: [] is string_list?

# (define (f x y z) ...)
# (define (f) 42)
# (define-struct s (x y z))
# (define-struct s ())
def is_string_list(a_list):
    """
    Checks that every element is a string
    :param a_list: []
    :return: True if list of strings and False otherwise
    """
    for element in a_list:
        if not isinstance(element, str):
            return False

    return True


def contains_reserved_words(expr):
    """
    Checkes if any of the reseved words are in the parameter list
    :param expr: [string]
    :return: True if no reserved words are used and False otherwise
    """
    for element in expr:
        if is_reserved(element):
            return False
    return True


#["+", a, b, c] -> True
#[] -> False

def is_reserved(word):
    """
    Determines if word is reserved
    :param word: String representing the variable
    :return: True if word is reserved and False otherwise
    """
    return word == 'define' or word == '+' or word == '-' or word == '/' or word == '*'

def parse_operation(p, n, C):
    """
    Parses Operation that needs at least n arguments
    :param p: p-expresson
    :param C: Class of operation
    :return: Operation
    """
    p.pop(0)

    if len(p) < n:
        return False
    else:
        result = []
        for element in p:
            element_as_bsl_exp = exp_parser(element)
            if not element_as_bsl_exp:
                return False
            result.append(element_as_bsl_exp)

    return C(BSLlist(result))

