import pytest
from Reader import Reader

reader1 = Reader("1 2 3 4".split())
reader2 = Reader(" 1 2 3  4".split())
reader3 = Reader(["1", "2", " ", "4"])
reader4 = Reader("1 2 3".split())
reader5 = Reader("1 2 3".split())


class Test_Reader:

    def test_reader(self):

        assert reader1.read_char() == "1"
        assert reader2.read_first_proper_char() == "1"

        assert reader1.read_token_acc(['g','x']) == ['xg234', '']
        assert reader3.read_token_acc(['g', 'x']) == ['xg12', " "]

        assert reader4.read_token(['1']) == [1123, '']

        assert reader5.reader() == 123

