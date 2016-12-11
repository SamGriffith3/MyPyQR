import pyqrcode
from pycode import db_1 as db_1
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db_1.engine)
session = Session()

r = 0
for i in range(len(session.query(db_1.Soaps.name).all())):
    n = session.query(db_1.Soaps.name).all()
    p = session.query(db_1.Soaps.retail).all()
    print(str(n[r]))
    a = str(n[r]).strip()
    b = str(p[r]).strip()
    c = a + b
    name = pyqrcode.create(c)
    name.png(a+'.png', scale=5, quiet_zone=4)
    name.show()
    r = r+1
#TODO create file path for pictures




#For object name in database, create qr code saved as object name.png


