import base64

with open("soap1.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    text = base64.b64decode(str)
    print(str)