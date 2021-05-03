"""
Bite 1. Sum n numbers

   Write a function that can sum up numbers:

       It should receive a sequence of n numbers.
       If no argument is provided, return sum of numbers 1..100.
       Look closely to the type of the function's default argument ...

   Have fun!
"""


def sum_numbers(numbers=None):
    pass
    if numbers == None:
        numbers = list(range(1, 100 + 1))
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum
