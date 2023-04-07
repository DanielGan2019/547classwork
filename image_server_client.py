from tkinter import filedialog

# Select image to upload

def select_image():
    filename = filedialog.askopenfilename(initialdir="Images")
    return filename
# Convert style to b64 string
def convert_image_file_to_base64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string
# Upload b64 string to server

# Download watermarked image


def main():
    filename = select_image()
    if filename == "":
        return
    b64_image = convert_image_file_to_base64_string(filename)
    print(b64_image)