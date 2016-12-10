import _datetime

from sqlalchemy.orm import sessionmaker

from python import db_1

Session = sessionmaker(bind=db_1.engine)
session = Session()


rec_1 = db_1.Soaps(name="Castille-Brine", description="A simple soap, with olive oil and sea salt", season="Autumn",
                   date_created=_datetime.date, wholesale=3.50, retail=5.00, batch_size=24, recipe_link="https://cdgx.com")

session.add(rec_1)

print(rec_1.description)





