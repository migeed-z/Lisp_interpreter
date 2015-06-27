from interpreter import Num, Add, Variable, BSLlist

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

    :param p:
    :return:
    """
    if isinstance(p,(complex,int,float)):
        return Num(p)
    elif isinstance(p,str):
        # do not (NOT) turn 'reserved tokens' into variable references
        # for example '+' is NOT a variable
        # for example 'define' is NOT a variable
        return Variable(p)
    else:
        if not p:
            return False
        elif p[0] == '+':
            operation = p.pop(0)
            result = []
            for element in p:
                element_as_bsl_exp = exp_parser(element)
                if not element_as_bsl_exp:
                    return False
                result.append(element_as_bsl_exp)
            return Add(BSLlist(result))
        elif p[0] == '*':
            pass
        else:
            return False

def def_parser(p):
    """

    :param p: P-expression
    :return: Def(...) or False
    """
    pass





# repl:
#  next = read_p_expression()
#  if next parses as definition, add next-as-definition to scope
#  if next parses as expression, evaluate next-as-expression in scope
#  otherwise say error
#  now loop back to repl