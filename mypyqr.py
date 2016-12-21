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


import zbarlight
from PIL import Image
import pyqrcode
from sqlalchemy.orm import sessionmaker


def qr_read(filename):
    with open(filename, 'rb') as image_file:
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

def qr_gen(*args):

    '''
    The qr_gen function allows a user to call multiple arguments and output a QR code as 'arg1.png'.
    '''
    name = pyqrcode.create(str(args))
    for arg in args:
        name.png(str(arg) + '.png', scale=5, quiet_zone=4)
        name.show()
        return name


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
    for row in session.query(db_name[tablename][column]).all():
        row = row.encode("utf-8").strip()
        qr_code = pyqrcode.create(row)
        qr_code.png("{}.png".format(row), scale=5, quiet_zone=4)
        qr_code.show()
        

#TODO get set of columns argument
def multiple_qr_gen_db(db_name, tablename, columns):
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
    
    for row in session.query(db_name[tablename]).all():
        row_list = []
        row = row.encode("utf-8").strip()
        row_list.append(row)
        
        qr_code = pyqrcode.create(row)
        qr_code.png("{}.png".format(row), scale=5, quiet_zone=4)
        qr_code.show()
