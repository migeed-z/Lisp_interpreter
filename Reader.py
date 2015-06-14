from BslError import BSLError

class Reader:

    def __init__(self, ip):
        """
        :param ip: List of characters
        :return: None
        """
        self.ip = ip

    def read_first_proper_char(self):
        """
        Produces the first character that is not a white space
        :return: String representing character
        """
        for i in range(0, len(self.ip)):
            char = self.read_char()
            if not char.isspace():
                return char

    def reader(self):
        """
        Read S-expression from Standard input
        :param ip: String representing ip
        :return: S-expression
        """
        next = self.read_first_proper_char()
        if next == ')':
            raise BSLError('Unexpected %s' % (')'))
        else:
            return self.read_ex1(next)[0]

    def read_ex1(self, char):
        """
        Produce the next sexpression and the character that follows it
        :param char: String
        :return: String representing the result
        """
        next = char
        if char.isspace():  #why is this condition needed?
            next = self.read_first_proper_char()

        if not next:
            raise BSLError('Incomplete s-expression')

        elif next == '(':
            return self.read_exx()

        else:
            return self.read_token([next])

    def read_exx(self):
        pass

    def read_ex_acc(self, next):
        pass

    def read_char(self):
        """
        Reads the next character
        :return:
        """
        return self.ip.pop(0)

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

        while self.ip:

            next = self.read_char()
            if next == ')' or next == '(' or next.isspace():
                final_next = next
                break

            else:
                result = result + next
        return [result, str(final_next)]

    def read_token(self, stats_with):
        """

        :param stats_with:
        :return:
        """
        next_pre_token = self.read_token_acc(stats_with)
        pre_token_first = next_pre_token[0]
        pre_token_second = next_pre_token[1]
        try:
            pre_token_first = int(pre_token_first)
        except ValueError:
            pass

        return [pre_token_first, pre_token_second]



