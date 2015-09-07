from Read import read_loop
import mock
import time

def test_read_defs():
    with mock.patch('__builtin__.raw_input', return_value='3'):
        assert read_loop() == 3

    with mock.patch('__builtin__.raw_input', return_value='(+ 1 (+ 4 4 4))'):
        assert read_loop() == 13

def test_read_and():
    with mock.patch('__builtin__.raw_input', return_value='(define x 3)'):
        time.sleep(1)
    with mock.patch('__builtin__.raw_input', return_value='x'):
        assert read_loop() == 3
