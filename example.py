from mypyqr import qr_gen, qr_read

x = input("Enter Information Here: ")
qr_gen(x)

qr_read(x)

