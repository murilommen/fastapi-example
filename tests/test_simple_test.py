import pytest


def my_function(x: int) -> int:
    if not isinstance(x, int):
        raise ValueError("variable x must be of int type!")
    return x * 2



def test_my_function_returns_double_the_input():
    actual_result = my_function(x=5)

    assert actual_result == 10


def test_my_function_raises_when_x_is_not_int():
    with pytest.raises(ValueError):
        my_function(x="texto")
    
    with pytest.raises(ValueError):
        my_function(x=1.234234)


