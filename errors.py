#Class Exercise
#Making exception error for list index out of range


def main():
    b = gen_exception(4)
    print(b)


def gen_exception(list_size):
    try:
        list = [None] * list_size
        a = list[list_size+3]
        return a
    except IndexError:
        print("Index is out of range, Try again")



if __name__ == "__main__":
    main()