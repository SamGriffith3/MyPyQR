
import pyqrcode


#For object name in database, create qr code saved as object name.png
db_obj_1 = pyqrcode.create("this is some test text, yeah")
db_obj_1.png('soap1.png', scale=5)
db_obj_1.show()

