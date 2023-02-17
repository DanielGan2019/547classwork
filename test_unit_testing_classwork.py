import pytest


def test_y_value(p1, p2, x_input, expected):
    from unit_testing_classwork import y_value
    answer = y_value(p1, p2, x_input)
    assert answer == expected