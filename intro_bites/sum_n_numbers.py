def sum_numbers(numbers=None):
    if numbers == None:
        numbers = list(range(1, 100+1))
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum