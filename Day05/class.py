import mymath
import sys
import pytest

# res = mymath.add(int(sys.argv[1]), int(sys.argv[2]))
# print(res)

# res2 = mymath.add(int(sys.argv[1]), int(sys.argv[2]))
# print(res2)

# input:
# C:\python_depository\Solutions_Python_BC\Day05> python class.py 500 3

# output:
# 25
# 503

def test_area():
    # result = mymath.area(int(sys.argv[1]), int(sys.argv[2]))
    result = mymath.area(5, 10)
    assert result == 50


@pytest.mark.parametrize("x, y, expected", 
                         [(5, 10, 50), 
                          (10, 10, 100), 
                          (10, 20, 200)])

def test_area(x, y, expected):
    result = mymath.area(x, y)
    assert result == expected