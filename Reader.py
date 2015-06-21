from BslError import BSLError

class Reader:
    """

    INPUT:

    An external S-expression has the following textual representation:

    Ex1 is one of:
    
    - '(' followed by Exx
    - Token

    EXX is one of:

    - ')'
    - Ex1 followed by EXX

    Token:

    Any sequence of characters not including '(', ')' or white space chars up to EOF

    EOF:

    Empty string


    OUTPUT

    An S-expression is one of:

    - String
    - Number
    - [S-expression]


    """

    def __init__(self, ip):
        """
        :param ip: [chars]
        :return: None
        """
        self.ip = self.split(ip)

    def reader(self):
        """
        Read S-expression from Standard input
        :return: S-expression
        """
        next = self.read_first_proper_char()
        if next == ')':
            raise BSLError('Unexpected %s' % (')'))
        elif next == "": #???
            raise BSLError('EOF')
        else:
            return self.read_ex1(next)[0]

    def read_ex1(self, char):
        """
        Produce the next Sexpression and the character that follows it
        :param char: String
        :return: [Sexpression, char]
        """
        next = char

        # **** if we start with a space, then we get rid of it ***
        # MF to be explained, why the heck does this work
        if char.isspace():  #why is this condition needed? -- MF: will need whitespace predicate
            next = self.read_first_proper_char()

        if not next:
            raise BSLError('Incomplete s-expression')

        elif next == '(':
            return self.read_exx()

        else:
            return self.read_token([next])

    def read_exx(self):
        """
        Produce a list of S-expressions and the character that follows it
        :return: [[S-expressions] Char]
        """
        return self.read_ex_acc(self.read_first_proper_char())

    def read_ex_acc(self, next):
        """
        Accumulates the char that precedes exx on stdin
        ex:
        r = Reader('4')
        r.read_ex_acc(')')
        [[], '4']
        :param next: String
        :return: [[S-expressions] Char]
        """

        if not next:
            raise BSLError('Incomplete List')
        elif next == ')':
            return [[], self.read_first_proper_char()]
        else:
            s_expr_and_next = self.read_ex1(next)
            first_s_expr = s_expr_and_next[0]
            next_char = s_expr_and_next[1]
            s_expr_list_and_next_char_again = self.read_ex_acc(next_char)
            s_expr_list = s_expr_list_and_next_char_again[0]
            next_char_again = s_expr_list_and_next_char_again[1]
            s_expr_list.insert(0,first_s_expr)
            return [s_expr_list, next_char_again]

    def read_token(self, starts_with):
        """
        Produce the next token and the character that ended it
        :param starts_with: [char]
        :return: [(Symbol or Integer), (Char or "")]
        """
        next_pre_token = self.read_token_acc(starts_with)
        pre_token_first = next_pre_token[0]
        pre_token_second = next_pre_token[1]
        try:
            pre_token_first = int(pre_token_first)
        except ValueError:
            pass

        return [pre_token_first, pre_token_second]

    def read_token_acc(self, prefix):
        """
        Produce rest of current token from ip
        :param prefix: [char]
        :return [(Symbol or Integer), (Char or "")]
        """

        result = ""
        prefix.reverse()
        result = result.join(prefix)
        final_next = ''

        while self.is_not_eof():
            next = self.read_char()
            if  next == ')' or next == '(' or next.isspace():
                final_next = next
                break
            else:
                result = result + next
        return [result, final_next]

    def read_first_proper_char(self):
        """
        Produces the first character that is not a white space
        :return: String
        """
        if not self.ip:
            return False

        for i in range(0, len(self.ip)):
            char = self.read_char()
            if not char.isspace():
                return char

    def read_char(self):
        """
        Reads the next character
        :return: String
        """
        return self.ip.pop(0)

    def is_not_eof(self):
        """
        Is ip not eof?
        :return: True if not eof and False otherwise
        """
        return self.ip

    def is_eof(self):
        """
        Is ip an eof?
        :return: True if eof and False otherwise
        """

        return not self.ip

    def split(self, line):
        """
        Transforms line to list of characters
        :param line: String
        :return: List of characters
        """
        chars = []
        for c in line:
            chars.append(c)
        return chars




#mf_reader = print(Reader(['(','f',' ','1','0',')']).reader())