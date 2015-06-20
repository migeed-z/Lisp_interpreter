from BslError import BSLError


class Reader:

    def __init__(self, ip):
        """
        :param ip: List of characters
        :return: None
        """
        self.ip = ip

    def reader(self):
        """
        Read S-expression from Standard input
        :param ip: String representing ip
        :return: S-expression
        """
        next = self.read_first_proper_char()
        if next == ')':
            raise BSLError('Unexpected %s' % (')'))
        elif next == False:
            raise BSLError('EOF')
        else:
            return self.read_ex1(next)[0]

    def read_ex1(self, char):
        """
        Produce the next sexpression and the character that follows it
        :param char: String
        :return: String representing the result
        """
        next = char
        # MF to be explained, why the heck does this work
        if char.isspace():  #why is this condition needed? -- MF: will need whitespace predicate
            next = char #self.read_first_proper_char()

        if not next:
            raise BSLError('Incomplete s-expression')

        elif next == '(':
            return self.read_exx()

        else:
            return self.read_token([next])

    def read_exx(self):
        """
        Produce a list of sexpressions and the character that follows it
        :return: List-of list-of strings
        """
        return self.read_ex_acc(self.read_first_proper_char())


    def read_ex_acc(self, next):
        """

        :param next: one char
        :return: a list of S-expressions plus the next char
        """

        if next == False:
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


    def read_token(self, stats_with):
        """

        :param stats_with: a list of char
        :return: either a String or a Number followed by the next char
        """
        next_pre_token = self.read_token_acc(stats_with)
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
        :param prefix: List of characters
        [Listof Char] -> (U Symbol Integer) (U Char EOF) ????????
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
        :return: String representing character
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
        :return:
        """
        return self.ip.pop(0)

    def is_not_eof(self):
        return self.ip

    def is_eof(self):
        return not self.ip


#mf_reader = print(Reader(['(','f',' ','1','0',')']).reader())