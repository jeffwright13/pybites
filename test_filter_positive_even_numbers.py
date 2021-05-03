from filter_positive_even_numbers import filter_positive_even_numbers


def test_empty():
       data = []
       assert filter_positive_even_numbers(data) == []

def test_none():
       data = None
       assert filter_positive_even_numbers(data) == []

def test_even_odd():
       data = [-2,-1,0,1,2,3,4]
       assert filter_positive_even_numbers(data) == [2,4]

def test_zeros():
       data = [0,0,0,0,0]
       assert filter_positive_even_numbers(data) == []

def test_even():
       data = [-2,0,-2,0,2,0,4]
       assert filter_positive_even_numbers(data) == [2,4]
