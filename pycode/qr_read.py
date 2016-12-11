import zbarlight
from PIL import Image


def qr_read(file_path):
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
        codes = zbarlight.scan_codes('qrcode', image)
        code = codes[0].decode('utf8')
        print('QR code:%s' % code)
