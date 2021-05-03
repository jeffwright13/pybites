from sum_n_numbers import sum_numbers

def test_sum_numbers():
    assert sum_numbers() == 5050
    assert sum_numbers([1,2,3]) == 6