import pyqrcode
import python.db_1 as db1


name = db1.Soaps.name
db_obj_1 = pyqrcode.create()
db_obj_1.png('/pics/'.join(name)+'.png', scale=5)
db_obj_1.show()




#For object name in database, create qr code saved as object name.png


