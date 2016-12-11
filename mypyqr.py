import zbarlight
from PIL import Image


def qr_read(input_file_path):
    with open(input_file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
        codes = zbarlight.scan_codes('qrcode', image)
        code = codes[0].decode('utf8')
        print('QR code:%s' % code)

'''
===================================================================================================
NOTE: zbarlight REQUIRES ZBAR TO BE INSTALLED. PLEASE SEE DOCUMENTATION TO SEE INSTALL INFORMATION
OR CHECK OUT http://zbarlight.readthedocs.io FOR MORE INFORMATION.
===================================================================================================

The qr_read function allows a user to open and read a .png QR code
'''




import pyqrcode
from sqlalchemy.orm import sessionmaker


def qr_gen(filename):
    '''
    The qr_gen function allows a user to define a file path and output the filename as a QR code.
    :return:
    '''
    name = pyqrcode.create(filename)
    name.png(filename + '.png', scale=5, quiet_zone=4)
    name.show()

def qr_gen_db(db_name, tablename, column):

    '''
    ======================================================================
    NOTE: YOU MUST IMPORT YOUR DATABASE FIRST IN ORDER TO CALL qr_gen_db
    ======================================================================

    The qr_gen_db function allows the user to iterate over all instances of a
    column of a particular table and prints a QR code containing that information.

    For example:

    To iterate thru all the user names of a database (db_1):

    qr_gen_db(db_1, Users, name)


    :param db_name: place in the database name you want to use
    :param tablename: input the table you want to search
    :param column: input the column you want to iterate over
    :return:
    '''

    Session = sessionmaker(bind=db_name.engine)
    session = Session()
    r = 0
    for i in range(len(session.query(db_name.tablename.column).all())):
        n = session.query(db_name.tablename.column).all()
        p = session.query(db_name.tablename.column).all()
        print(str(n[r]))
        a = str(n[r]).strip()
        name = pyqrcode.create(a)
        name.png(a+'.png', scale=5, quiet_zone=4)
        name.show()
        r = r+1


def multiple_qr_gen_db(db_name, tablename, column, column2, column3, column4, column5, column6, column7, column8,
                       column9, column10):
    '''

    =============================================================================
    NOTE: YOU MUST IMPORT YOUR DATABASE FIRST IN ORDER TO CALL multiple_qr_gen_db
    =============================================================================

    The multiple_qr_gen_db function allows the user to iterate over all instances of up to 10
    columns of a particular table and prints a QR code containing that information.

    For example:

    To iterate thru all the user names and their hometowns within a database (db_1):

    qr_gen_db(db_1, Users, name, password, hometown)


    :param db_name: place in the database name you want to use
    :param tablename: input the table you want to search
    :param column: input the column(s) you want to iterate over
    :return:
    '''

    Session = sessionmaker(bind=db_name.engine)
    session = Session()
    r = 0
    for i in range(len(session.query(db_name.tablename.column).all())):
        n = session.query(db_name.tablename.column).all()
        n2 = session.query(db_name.tablename.column2).all()
        n3 = session.query(db_name.tablename.column3).all()
        n4 = session.query(db_name.tablename.column4).all()
        n5 = session.query(db_name.tablename.column5).all()
        n6 = session.query(db_name.tablename.column6).all()
        n7 = session.query(db_name.tablename.column7).all()
        n8 = session.query(db_name.tablename.column8).all()
        n9 = session.query(db_name.tablename.column9).all()
        n10 = session.query(db_name.tablename.column10).all()
        print(str(n[r]))
        a = str(n[r]).strip()
        a2 = str(n2[r]).strip()
        a3 = str(n3[r]).strip()
        a4 = str(n4[r]).strip()
        a5 = str(n5[r]).strip()
        a6 = str(n6[r]).strip()
        a7 = str(n7[r]).strip()
        a8 = str(n8[r]).strip()
        a9 = str(n9[r]).strip()
        a10 = str(n10[r]).strip()
        c = a + a2 + a3 + a4 + a5 + a6 + a7 +a8 + a9 +a10
        name = pyqrcode.create(c)
        name.png(a + '.png', scale=5, quiet_zone=4)
        name.show()
        r = r + 1


'''
=================================================================================
MyPyQR is licensed under the MIT License

MIT License

Copyright (c) 2016 SamGriffith3

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
===================================================================================
'''



