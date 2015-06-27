from interpreter import Num, Add, Variable, BSLlist, Multiply, Subtract, Divide
from parser import ParserException

# A P-expression is one of:
# - string, represents a symbol in BSL
# - number
# - [P-expression, ..., P-expression]
#
# STEP 2 a:
# The PARSER consumes P-expressions and produces pre-BSL-expression, it's a BSL-expression but with errors
#
# NAIVE approach
# parser : P-expression -> [Maybe BSLexpr]
#
# A BSLexpr is one of:
# Num(number)
# Var(string)
# Add([Listof BSLexpr])
# Mul([BSLexpr])
# Sub([BSLexpr])
# Div([BSLexpr])
# App(string,[BSLexpr])
#
# A FuncDef is:
# Def(string,string,BSLexpr)


# P-expression -> BSLexpr or False
# checks whether the given P-expression is a BSL expression and, if so, turns it into an instance of BSLexpr
# otherwise produce False
# in                   out
# -------------------------
#  42                 Num(42)
#  'xyz'              Var('xyz')
#  ['+',1,1]          Add([Num(1),Num(1)])
#  ['+',['+',1,1],1]  Add([Add([Num(1),Num(1)]),Num(1)])
#  [1,'+',1]          False
#  ['+',1,['+',1]]    Add([Num(1), Add([Num(1)])
#  ['+',1,[1,'+']]    False
#  []                 False
#  [1]                False


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
            p.pop(0)
            result = []
            for element in p:
                element_as_bsl_exp = exp_parser(element)
                if not element_as_bsl_exp:
                    return False
                result.append(element_as_bsl_exp)
            return Add(BSLlist(result))

        #Multiply expression
        elif p[0] == '*':
            p.pop(0)
            result = []
            for element in p:
                element_as_bsl_exp = exp_parser(element)
                if not element_as_bsl_exp:
                    return False
                result.append(element_as_bsl_exp)
            return Multiply(BSLlist(result))

        #Subtract expression
        elif p[0] == '-':
            p.pop(0)

            if len(p) == 0:
                return False
            else:
                result = []
                for element in p:
                    element_as_bsl_exp = exp_parser(element)
                    if not element_as_bsl_exp:
                        return False
                    result.append(element_as_bsl_exp)

            return Subtract(BSLlist(result))

        #Divide expression
        elif p[0] == '/':
            p.pop(0)

            if len(p) == 0:
                return False
            else:
                result = []
                for element in p:
                    element_as_bsl_exp = exp_parser(element)
                    if not element_as_bsl_exp:
                        return False
                    result.append(element_as_bsl_exp)
            return Divide(BSLlist(result))

        else:
            return False

def def_parser(p):
    """

    :param p: P-expression
    :return: Def(...) or False
    """
    pass



def is_reserved(word):
    """
    Determines if word is reserved
    :param word: String representing the variable
    :return: True if word is reserved and False otherwise
    """
    return word == 'define' or word == '+' or word == '-' or word == '/' or word == '*'

# repl:
#  next = read_p_expression()
#  if next parses as definition, add next-as-definition to scope
#  if next parses as expression, evaluate next-as-expression in scope
#  otherwise say error
#  now loop back to repl