import pytest

@pytest.mark.parametrize("p1, p2, x_input, expected",
                         [((1, 1), (3, 3), 2, 2),
                          ((1.0, 1), (3.0, 3), 2, 2),
                          ((-2, 1), (3, 3), 1, 2.2),
                          ((-2, 1), (3, 3), 4, 3.4)])
def test_y_value(p1, p2, x_input, expected):
    from unit_test_classwork import y_value
    answer = y_value(p1, p2, x_input)
    assert answer == expected

@pytest.mark.parametrize("p1, p2, expected",
                         [((1, 1), (3, 3), (1, 3)),
                          ((1.0, 1), (3.0, 3), (1.0, 3.0)),
                          ((-2, 1), (3, 3), (-2, 3))])
def test_get_x(p1, p2, expected):
    from unit_test_classwork import get_x
    answer = get_x(p1, p2)
    assert answer == expected


@pytest.mark.parametrize("p1, p2, expected",
                         [((1, 1), (3, 3), (1, 3)),
                          ((1.0, 1.0), (3.0, 3.0), (1.0, 3.0)),
                          ((-2, -2), (3, 3), (-2, 3))])
def test_get_y(p1, p2, expected):
    from unit_test_classwork import get_y
    answer = get_y(p1, p2)
    assert answer == expected


@pytest.mark.parametrize("p1, p2, expected",
                         [((1, 1), (3, 3), 1),
                          ((1.0, 1), (3.0, 3), 1),
                          ((-2, 1), (3, 3), 0.4)])
def test_find_slope(p1, p2, expected):
    from unit_test_classwork import find_slope
    answer = find_slope(p1, p2)
    assert answer == expected


@pytest.mark.parametrize("p1, p2, expected",
                         [((1, 1), (3, 3), 0),
                          ((1.0, 1), (3.0, 3), 0),
                          ((-2, 1), (3, 3), 1.8)])
def test_find_intercept(p1, p2, expected):
    from unit_test_classwork import find_intercept
    answer = find_intercept(p1, p2)
    assert answer == expected
