import pytest

from task6_3_1 import post_request, get_request


@pytest.mark.second
@pytest.mark.parametrize("test_input,expected",
                         [("3+5", 8), ("0+4", 4), ("-3+(-1)", -4), ("1.2+0.5", 1.7)])
def test_adding(test_input, expected, rounding_index):
    print(float(post_request(test_input, rounding_index)))
    assert float(post_request(test_input, rounding_index)) == expected


@pytest.mark.second
@pytest.mark.parametrize("test_input,expected",
                         [("8-7", 1), ("-4.2-3", -7.2), ("0-5", -5), ("-3-(-1)", -2)])
def test_subtracting(test_input, expected, rounding_index):
    print(float(post_request(test_input, rounding_index)))
    assert float(post_request(test_input, rounding_index)) == expected


@pytest.mark.first
@pytest.mark.parametrize("test_input,expected",
                         [("8*7", 56), ("-4*-3", 12), ("0*5", 0), ("-3*1", -3)])
def test_multiplication(test_input, expected, rounding_index):
    print(float(post_request(test_input, rounding_index)))
    assert float(post_request(test_input, rounding_index)) == expected


@pytest.mark.first
@pytest.mark.parametrize("test_input,expected",
                         [("8/2", 4), ("-9/-3", 3), ("-16/4", -4)])
def test_divisione(test_input, expected, rounding_index):
    print(float(post_request(test_input, rounding_index)))
    assert float(post_request(test_input, rounding_index)) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("test_input,expected",
                         [("13/0", "Division by zero except")])
def test_divisione_by_zero(test_input, expected, rounding_index):
    assert post_request(test_input, rounding_index) == expected


@pytest.mark.third
@pytest.mark.parametrize("test_input,expected",
                         [("4", 2), ("9", 3), ("5", 2.24)])
def test_sqrt(test_input, expected, rounding_index):
    print(float(get_request(test_input, rounding_index)))
    assert float(get_request(test_input, rounding_index)) == expected
