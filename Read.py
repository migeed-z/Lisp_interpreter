from sys import stdin, stdout
from Reader import Reader

def read():
    """
    Reads text from stdin
    :return: s-expression
    """
    stdout.write('Enter an S-expression \n')
    userinput = stdin.readline()
    reader = Reader(userinput)
    return reader.reader()


