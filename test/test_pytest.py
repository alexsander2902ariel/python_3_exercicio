from main import sum_numbers_sequence
def test_check_sum_1():
    assert sum_numbers_sequence([0,1,2,3,5,8]) == 19
def test_check_sum_2():
    assert sum_numbers_sequence([.1,.2,.3,.4]) == 1

from main import div_numbers_sequence
def test_check_div_1():
    assert div_numbers_sequence(10,5) == 2
def test_check_div_2():
    assert div_numbers_sequence(.5,.1) == 5

def test_check_sum_3():
        assert sum_numbers_sequence([.1,.2]) == .3 
def test_check_div_3():
    assert div_numbers_sequence(.3,.1) == 3