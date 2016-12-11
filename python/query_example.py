from sqlalchemy.orm import sessionmaker
from python import db_1 as db_1

Session = sessionmaker(bind=db_1.engine)
session = Session()

for i in session.query(db_1.Soaps).filter(db_1.Soaps.name == 'Castille-Brine'):
    print(i)

