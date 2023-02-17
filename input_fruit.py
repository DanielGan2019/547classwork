# in_file = open("input_data.txt", "r")
# fruits = in_file.readlines()
# print(fruits)
# in_file.close()


# in_file = open("input_data.txt", "r")
# for line in in_file:
# print(line)
# in_file.close()
def analyze_ID(input_lin):
    patient_data = first_line.strip("\n").("=")
    patient_id = int(patient_data[1])
    return patient_id


def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    id = analyze_ID(first_line)


def test_read_file():
    from input_fruit.py import read_file
    filename = "my_test_data.txt"
    answer = read_file(filename)
    expected = 50
    assert == expected
