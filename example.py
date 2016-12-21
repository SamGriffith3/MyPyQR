from mypyqr import qr_gen, qr_read

qr_gen("requirements.txt", "$5.00", "You should really read this file I guess")

qr_read("requirements.txt.png")

