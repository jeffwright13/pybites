from split_and_join import split_in_columns

message1 = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def test_split_in_columns_0():
    assert split_in_columns("") == ""
    
    
def test_split_in_columns_1():
    expected_output_1 = """Hello world!|We hope that you are learning a lot of Python.|Have fun with our Bites of Py.|Keep calm and code in Python!|Become a PyBites ninja!"""
    assert split_in_columns(message1) == expected_output_1


def test_split_in_columns_2():
    assert split_in_columns("\n\n\n\n\n \n") == "||||| |"
    
