import DirPaths

from sys import stdin, stdout
from Reader import Reader
from Parser import exp_parser, func_def_parser, struct_def_parser
from BSLError import BSLError
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

# -> [String]
def read_lines():
    input_list = []
    while True:
        stdout.write("> ")
        stdout.flush()
        userinput = stdin.readline()
        input_list.append(userinput)
        all_input = ' '.join(input_list)
        if has_equal_parens(all_input):
            return all_input

def read():
    """
    Reads text from stdin
    :return: s-expression
    """
    lang = 'BSL'

    s = Scope([]).add_definitions()

    userinput = read_lines()

    # while True:
    #     userinput = read_lines()
    #
    #     try:
    #         print userinput
    #         r = Reader(userinput)
    #
    #         p_expr = r.reader()
    #         print('p_expr = ',p_expr)
    #         if not p_expr:
    #             break
    #     except:
    #         print ('Reader Error')
    #
    #     try:
    #         is_p_expr_a_bsl_expr = exp_parser(p_expr, lang)
    #
    #         if not is_p_expr_a_bsl_expr:
    #
    #             func_def = func_def_parser(p_expr, lang)
    #             if func_def:
    #                 if isinstance(p_expr[1], str):
    #                     s = s.extend(func_def.name, func_def.body.eval(s))
    #                 else:
    #                     s = func_def.update_func(s)
    #
    #             else:
    #                 struct_def = struct_def_parser(p_expr, lang)
    #                 if struct_def:
    #                     s = struct_def.update_scope(s)
    #         else:
    #             try:
    #                 result = is_p_expr_a_bsl_expr.eval(s)
    #                 print(result)
    #             except BSLError:
    #                 print('an eval exception happened')
    #     except:
    #         print ('BSL parse error')

