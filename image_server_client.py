from tkinter import filedialog
import base64
import requests

server = "http://vcm-21170.vm.duke.edu"

# Select image to upload
def select_image():
    # filename = filedialog.askopenfilename(initialdir="Images")
    filename = "racoon.jpg"
    return filename

# Convert style to b64 string
def convert_image_file_to_base64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string
# Upload b64 string to server
def upload_to_server(b64_image, net_id, id_no):
    new_result = {"image": b64_image, "net_id": net_id, "id_no": id_no}
    r = requests.post(server + "/add_image", json=new_result)
    print(r.text)


# Download watermarked image
def get_watermark_image(net_id, id_no):
    r = requests.get(server + "/get_image/{}/{}".format(net_id,id_no))
    print(r.text)


def main():
    filename = select_image()
    if filename == "":
        return
    b64_image = convert_image_file_to_base64_string(filename)
    print(b64_image)
    upload_to_server(b64_image, "dcg23", 69)
    get_watermark_image('dcg23', 69)

if __name__ == "__main__":
    main()