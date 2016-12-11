import pyqrcode
from pycode import db_1 as db_1
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db_1.engine)
session = Session()


n = session.query(db_1.Soaps.name).all()
print(str(n[0]))
'''
name = pyqrcode.create(n[0])
name.png(n+'.png', scale=5, quiet_zone=4)
name.show()
'''




#For object name in database, create qr code saved as object name.png


