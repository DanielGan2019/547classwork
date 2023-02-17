# Feb3 classwork assignment, Daniel Gan


def y_value(p1, p2, x_input):
    m = find_slope(p1, p2)
    b = find_intercept(p1, p2)
    y = (m * x_input) + b
    print("The y value on the line is {}".format(y))
    y = round(y, 5)
    return y


def find_intercept(p1, p2):
    # b = y - mx
    m = find_slope(p1, p2)
    y = (get_y(p1, p2))[0]
    x = (get_x(p1, p2))[0]
    b = y - (m*x)
    return b


def find_slope(p1, p2):
    x1 = (get_x(p1, p2))[0]
    x2 = (get_x(p1, p2))[1]
    y1 = (get_y(p1, p2))[0]
    y2 = (get_y(p1, p2))[1]
    slope = (y2 - y1)/(x2 - x1)
    return slope


def get_x(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    return x1, x2


def get_y(p1, p2):
    y1 = p1[1]
    y2 = p2[1]
    return y1, y2


if __name__ == "__main__":
    y_value((1, 1), (3, 3), 2)
