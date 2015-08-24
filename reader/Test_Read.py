from Read import read


def test_foo(capfd):
    read()  # Writes "Hello World!" to stdout
    out, err = capfd.readouterr()
    assert out == "Hello World!"