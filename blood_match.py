import requests


def main():
    r = get_ID("http://vcm-7631.vm.duke.edu:5002", "dcg23")
    print(r.text)
    id = r.json()
    donor = get_blood_type("http://vcm-7631.vm.duke.edu:5002", id["Donor"])
    recipient = get_blood_type("http://vcm-7631.vm.duke.edu:5002", id["Recipient"])
    print(donor.text)
    print(recipient.text)
    #mentally checked whether or not donor could give blood to recipient
    answer = post_answer("http://vcm-7631.vm.duke.edu:5002", "Yes")
    print(answer.text)



def get_ID(url, name):
    r = requests.get(url + "/get_patients/" + name)
    return r


def get_blood_type(url, id):
    r = requests.get(url + "/get_blood_type/" + id)
    return r


def post_answer(url, answer):
    out_data = {"Name": "dcg23", "Match":  answer}
    r = requests.post(url + "/match_check", json = out_data)
    return r


if __name__ == "__main__":
    main()