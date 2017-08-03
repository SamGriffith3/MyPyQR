from mypyqr import qr_gen, qr_read
import os

x = input("Enter Information Here: ")
qr_gen(x)

os.open("C:/")
qr_read(x)

