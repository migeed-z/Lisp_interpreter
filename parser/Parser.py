import sys
sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/BSL_Expr')
sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/BSL_Def')


from Num import Num
from Variable import Variable
from BSLlist import BSLlist
from FuncDefinition import FuncDefinition
from FuncApplication import FuncApplication
from StructDefinition import StructDefinition
from ParserError import ParserError


def exp_parser(p, lang):
    """
    To Parse Operation expressions
    :param p: p-expression
    :param lang: String representing Language used. EX: BSL
    :return:
    """
    if isinstance(p,(complex,int,float)):
        return Num(p)

    elif isinstance(p, str):
        if is_reserved(p):
            my_lang(lang)
        else:
            return Variable(p)
    elif not p:
        raise ParserError('Expected a function after the open parenthesis, but nothing is there')

    # now we know it is a parenthesize P-expression
    if p[0] == '+':
        return parse_operation(p, 0, '+', lang)

    #Multiply expression
    elif p[0] == '*':
        return parse_operation(p, 0, '*', lang)

    #Subtract expression
    elif p[0] == '-':
        return parse_operation(p, 1, '-', lang)

    #Divide expression
    elif p[0] == '/':
        return parse_operation(p, 1, '/', lang)

    #function application
    elif isinstance(p[0], str) and not is_reserved(p[0]):
        name_of_function = p[0]
        return parse_operation(p, 0, name_of_function, lang)

    else:
        return False
        # raise ParserError('Expected a function after the open parenthesis but recieved %s' %str(p[0]))

def struct_def_parser(p, lang):
    """
    Parses Struct Definitions
    :param p: P-expression
    :param lang: String representing Language used. EX: BSL
    :return: StructDefinition
    """

    if p[0] != 'define-struct':
        return False

    elif len(p) != 3:
        raise ParserError('length of p-expression must have length >= 3')

    elif not isinstance(p[1], str):
        raise ParserError('Struct name must be a string')

    elif is_reserved(p[1]):
        raise ParserError('Struct name is a reserved word')

    elif not isinstance(p[2], list):
        raise ParserError('Expects a list of parameters')

    else:
        check_on_fields = is_list_of_proper_names(p[2])
        if check_on_fields == False:
            raise ParserError('Not a list of field names')

        return StructDefinition(p[1], p[2])

def func_def_parser(p, lang):
    """
    Parses Function Definitions
    :param p: P-expression
    :param lang: String representing Language used. EX: BSL
    :return: FuncDefinition
    """
    if p[0] != 'define':
        return False

    elif len(p) < 3:
        raise ParserError('p-expression must have length >= 3')

    name_or_params = p[1]

    if isinstance(name_or_params, str):
        name = parse_name_from_string(name_or_params)
        if not name:
            raise ParserError('Wrong function name')
        else:
            body = exp_parser(p[2], lang)
            return FuncDefinition(name, [], body)

    elif isinstance(name_or_params, list):

        list_of_names_and_params = p[1]
        name = list_of_names_and_params[0]
        params = list_of_names_and_params[1:]

        parsed_name = parse_name_from_string(name)
        parsed_params = is_list_of_proper_names(params)
        body = exp_parser(p[2], lang)

        if parsed_name == False or parsed_params == False:
            raise ParserError('Wrong name or params')
        else:
            return FuncDefinition(parsed_name, parsed_params, body)


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

def is_reserved(word):
    """
    Determines if word is reserved
    :param word: String representing the variable
    :return: True if word is reserved and False otherwise
    """
    return word == 'define' or word == '+' or word == '-' or word == '/' or word == '*' or word == 'define-struct'

def parse_operation(p, n, name, lang):
    """
    Parses Operation that needs at least n arguments
    :param p: p-expresson
    :param name: name of operation
    :return: Operation
    """
    p.pop(0)

    if len(p) < n:
        raise ParserError('expects at least %s argument, but found none' % str(n))

    else:
        result = []
        for element in p:
            element_as_bsl_exp = exp_parser(element, lang)
            if not element_as_bsl_exp:
                raise ParserError('expects s-expressions in the list of arguments')
            result.append(element_as_bsl_exp)

    return FuncApplication(name, BSLlist(result))

def my_lang(lang):
    if lang == 'BSL':
        raise ParserError('This word is reserved')
    return False
