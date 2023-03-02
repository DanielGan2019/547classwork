import requests


def main():
    out_data = add_message("dcg23", "How are you?")
    r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json = out_data)
    r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_message/dcg23")
    print(r.text)


def add_message(uname, message):
    dict = {"user": uname, "message": message}
    return dict


if __name__ == "__main__":
    main()

