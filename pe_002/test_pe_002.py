import pytest
from typing import Callable, List

GET_FIB_LIST_TYPE = Callable[[int], List[int]]
GET_SUM_FIB_TYPE = Callable[[int], int]


@pytest.fixture()
def get_fib_list() -> GET_FIB_LIST_TYPE:
    from .pe_002 import get_even_fibonacci_list_under
    return get_even_fibonacci_list_under

@pytest.fixture()
def get_sum_fib() -> GET_SUM_FIB_TYPE:
    from .pe_002 import get_sum_of_even_fibonacci_under
    return get_sum_of_even_fibonacci_under


def test_pe002_list_of_fibonacci_under_10(get_fib_list: GET_FIB_LIST_TYPE):
    assert get_fib_list(10) == [2, 8]


def test_pe002_raise_value_error_under_1(get_fib_list: GET_FIB_LIST_TYPE):
    with pytest.raises(ValueError):
        get_fib_list(1)


def test_pe002_list_of_fibonacci_under_2(get_fib_list: GET_FIB_LIST_TYPE):
    assert get_fib_list(2) == []


def test_pe002_list_of_fibonacci_under_20(get_fib_list: GET_FIB_LIST_TYPE):
    assert get_fib_list(20) == [2, 8]


def test_pe002_sum_of_fibonacci_under_10(get_sum_fib: GET_SUM_FIB_TYPE):
    assert get_sum_fib(10) == 10


def test_pe002_sum_of_fibonacci_under_20(get_sum_fib: GET_SUM_FIB_TYPE):
    assert get_sum_fib(20) == 10
