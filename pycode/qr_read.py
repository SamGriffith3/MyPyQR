import zbarlight
from PIL import Image

file_path = '/home/sam/PycharmProjects/MyPyQR/This is the start of something beautiful.png'
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()
    codes = zbarlight.scan_codes('qrcode', image)
    code = codes[0].decode('utf8')
    print('QR code:%s' % code)
