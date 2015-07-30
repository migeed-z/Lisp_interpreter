from interpreter import Num, Add, Variable, BSLlist, Multiply, Subtract, Divide, FuncDefinition, FuncApplication
from functools import partial

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
    Parses Parameters given as a String or a List
    :param expr: [string]
    :return: [], False or Expr - Expr[0]
    """
    if isinstance(expr, str):
        return []
    elif isinstance(expr, list):
        expr.pop(0)
        if validate_reserved_words(expr) == False:
            return False

        else:
            return expr


def validate_reserved_words(expr):
    """
    Checkes if any of the reseved words are in the parameter list
    :param expr: [string]
    :return: True if no reserved words are used and False otherwise
    """
    for element in expr:
        if is_reserved(element):
            return False
    return True


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

