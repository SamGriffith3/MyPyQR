import _datetime
from sqlalchemy.orm import sessionmaker
from python import db_1 as db_1


Session = sessionmaker(bind=db_1.engine)
session = Session()

print(db_1.User)
print(db_1.Soaps)
def add_user():
    u = input("Username: ")
    if u == db_1.User.name:
        print("That name is taken, please try a new one:")
    else:
        print("Sweet Name!")
    p = input("Password: ")
    user = db_1.User(name=u, password=p)
    session.add(user)


def add_soap():
    n = input("Soap Name: ")
    d = input("Description: ")
    s = input("Selling Season: ")
    dt = _datetime.datetime.now()
    ws = input("Wholesale Price: $")
    if ws != float:
        print("This has to be a floating number. Ex: 3.14, or 252.57")
        ws = input("Wholesale Price: $")
    rt = input("Retail Price: $")
    if rt != float:
        print("This has to be a floating number. Ex: 6.21, or 232324.59")
        rt = input("Retail Price: $")
    bs = input("Batch Size: ")
    if bs != int:
        print("As an integer, if you don't mind")
        bs = input("Batch Size: ")
    lnk = input("Recipe Link")
    r = db_1.Soaps(name=n, description=d, season=s, date_created=dt, wholesale=ws, retail=rt, batch_size=bs,
                   recipe_link=lnk)
    db_1.add(r)



add_user()
add_soap()

'''
#Run the Session
x = input("What would you like to do?")
if x.lower == "add user":
    add_user()
elif x.lower == "add soap":
    add_soap()
elif x.lower == "bye" or "stop":
    print("Have a nice poop!")
else:
    print("Make up your mind!")
'''

session.commit()


print("ALL DONE")





