from mypyqr import qr_gen, qr_read

qr_gen("Item #1", "$5.00", "You should really read this file")

qr_read("Item #1.png")

