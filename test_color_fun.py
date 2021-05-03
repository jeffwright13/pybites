from color_fun import return_colors, print_colors
import pytest


def test_return_colors():
    assert return_colors("") == "Not a valid color"
    assert return_colors("quit") == "bye"
    assert return_colors("rEd") == "rEd"
    assert return_colors("yellow") == "yellow"

def test_color_fun_None(capfd):
    with pytest.raises(OSError):
        print_colors()

def test_color_fun_blank(capfd):
    print_colors("")
    output = capfd.readouterr()[0].strip()
    assert output == "Not a valid color"

def test_color_fun_quit(capfd):
    print_colors("quit")
    output = capfd.readouterr()[0].strip()
    assert output == "bye"

def test_color_fun_rEd(capfd):
    print_colors("rEd")
    output = capfd.readouterr()[0].strip()
    assert output == "rEd"

def test_color_fun_yellow(capfd):
    print_colors("yellow")
    output = capfd.readouterr()[0].strip()
    assert output == "yellow"
