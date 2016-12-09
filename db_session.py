import db_1
from sqlalchemy.orm import sessionmaker
import _datetime


Session = sessionmaker()
session = Session()


rec_1 = db_1.Soaps(name="Castille-Brine", description="A simple soap, with olive oil and sea salt",  season="Autumn",
                    date_created=_datetime.date, wholesale=3.50, retail=5.00, batch_size=24)

session.add(rec_1)

session.commit()

print(rec_1.description)





