from main import sum_numbers_sequence
def test_check_sum_1():
    assert sum_numbers_sequence([0,1,2,3,5,8]) == 19
def test_check_sum_2():
    assert sum_numbers_sequence([.1,.2,.3,.4]) == 1