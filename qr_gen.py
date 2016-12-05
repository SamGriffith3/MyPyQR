import qrtools
import pyqrcode

qr = pyqrcode.create("Horn")
qr.png("horn.png", scale=6)

qr = qrtools.QR()
qr.decode("horn.png")
print qr.data
