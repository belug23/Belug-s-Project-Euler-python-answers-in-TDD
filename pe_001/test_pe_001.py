import pytest
from .pe_001 import (
    sum_of_multiple_of_3_and_5_under,
    is_multiple_of_3,
    is_multiple_of_5,
    is_multiple_of_3_or_5,
    get_multiples_of_3_and_5_under,
)


def test_pe001_6_is_multiple_of_3():
    assert is_multiple_of_3(6)


def test_pe001_4_is_not_multiple_of_3():
    assert not is_multiple_of_3(4)


def test_pe001_10_is_multiple_of_5():
    assert is_multiple_of_5(10)


def test_pe001_9_is_not_multiple_of_5():
    assert not is_multiple_of_5(9)


def test_pe001_15_is_multiple_of_3_or_5():
    assert is_multiple_of_3_or_5(15)


def test_pe001_9_is_multiple_of_3_or_5():
    assert is_multiple_of_3_or_5(9)


def test_pe001_10_is_multiple_of_3_or_5():
    assert is_multiple_of_3_or_5(10)


def test_pe001_11_is_not_multiple_of_3_or_5():
    assert not is_multiple_of_3_or_5(11)


def test_pe001_sum_of_multiple_3_and_5_under_10_is_23():
    assert sum_of_multiple_of_3_and_5_under(10) == 23


def test_pe001_sum_raise_valueerror_on_negative_numbers():
    with pytest.raises(ValueError):
        sum_of_multiple_of_3_and_5_under(-1)


def test_pe001_sum_of_multiple_of_3_and_5_under_2_is_0():
    assert sum_of_multiple_of_3_and_5_under(2) == 0


def test_pe001_list_of_multiple_of_3_and_5_under_10():
    assert get_multiples_of_3_and_5_under(10) == [0, 3, 5, 6, 9]


def test_pe001_sum_of_multiple_of_3_and_5_under_100_is_2318():
    assert sum_of_multiple_of_3_and_5_under(100) == 2318
