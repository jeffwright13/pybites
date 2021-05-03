import sys

VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors(color=None):
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    if color == None:
        while True:
            color = input("Please enter a color:")
    elif color.lower() == "quit":
        print("bye")
    elif color.lower() in VALID_COLORS:
        print(color)
    else:
        print("Not a valid color")

def return_colors(color):
    """Same logic as above but in a fucntion for testing."""
    if color.lower() == "quit":
        return("bye")
    if color.lower() in VALID_COLORS:
        return(color)
    else:
        return("Not a valid color")
