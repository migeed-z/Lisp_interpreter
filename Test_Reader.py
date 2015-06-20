import pytest
from Reader import Reader

reader1 = Reader("1 2 3 4".split()) # (string->list "1 2 3 4")
reader2 = Reader(" 1 2 3  4".split())
reader3 = Reader(["1", "2", " ", "4"])
reader4 = Reader("1 2 3".split())
reader5 = Reader("1 2 3".split())
read_mt = Reader("( )".split())
read_f10 = Reader(['(','f',' ','1','0',')'])
read_f_of_g10 = Reader(['(','f','(','g',' ','1','0',')',')'])
read_blank_old = Reader(['(',' ',' ','f','(','g',')',')'])
read_blank = Reader(["(",
                      " ",
                      " ",
                      " ",
                      " ",
                      "t",
                      "o",
                      "k",
                      "e",
                      "n",
                      "0",
                      "(",
                      "t",
                      "o",
                      "k",
                      "e",
                      "n",
                      "1",
                      ")",
                      ")"])


class Test_Reader:

    def test_reader(self):

        assert reader1.read_char() == "1"
        assert reader2.read_first_proper_char() == "1"

        assert reader1.read_token_acc(['g','x']) == ['xg234', '']
        assert reader3.read_token_acc(['g', 'x']) == ['xg12', " "]

        assert reader4.read_token(['1']) == [1123, '']

        assert reader5.reader() == 123

        assert read_mt.reader() == []
        assert read_f10.reader() == ["f", 10] # (list 'f 10)
        assert read_f_of_g10.reader() == ["f",["g",10]]
        assert read_blank.reader() == ["token0",["token1"]]
