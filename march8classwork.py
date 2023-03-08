from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type,
                   "tests": []}
    db[id] = new_patient


def add_test_to_db(id, test_name, test_result):
    add_test = {"id": id,
                "test_name": test_name,
                "test_result": test_result}
    db[id] = add_test


@app.route("/new_patient", methods = ["POST"])
def post_new_patient():
    # get input data
    in_data = request.get_json()
    # call other functions to do work
    answer, status_code = new_patient_driver(in_data)  
    # return a response
    return jsonify(answer)


@app.route("/add_test", methods = ["POST"])
def post_add_test():
    # get input data
    in_data = request.get_json()
    # call other functions to do work
    answer, status_code = add_test_driver(in_data)  
    # return a response
    return jsonify(answer)


def add_test_driver(in_data):
    validation = validate_add_test(in_data)
    if validation is not True:
        return validation, 400
    add_test_to_db(in_data["id"], in_data["test_name"], in_data["test_result"])
    return "Test succesfully added", 200


def new_patient_driver(in_data):
    # validate input
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    # do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # return answer
    return "Patient succesfully added", 200


def validate_add_test(in_data):
    if type(in_data) is not dict:
        return "input is not a dictionary"
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "key {} has the incorrect value type".format(key)
    return True


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "key {} has the incorrect value type".format(key)
    return True


if __name__ == '__main__':
    app.run()



