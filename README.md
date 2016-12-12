# MyPyQR

Version 0.1.0          © 2016 Sam Griffith

##MyPyQR exists to allow pythoners to access to the world of QR codes

##Installation

###PLEASE NOTE:
###Due to the unfortunate nature of QR codes, this code was not written purely within python and thus requires the installation of Zbar barcode reader. Please check out their installation documentation here: http://zbar.sourceforge.net/download.html


##About the Code:

calling qr_read(filepath) allows a user to open and read a .png QR code


calling qr_gen(filepath) allows a user to define a file path and output the filename as a QR code.


calling qr_gen_db(db_name, tablename, column) allows the user to iterate over all instances of a
    column of a particular table and prints a QR code containing that information.

    For example:

    To iterate thru all the user names of a database (db_1):

    qr_gen_db(db_1, Users, name)
    
    
calling multiple_qr_gen_db(db_name, tablename, column(1-10)) allows the user to iterate over all instances of up to 10 columns of a particular table and prints a QR code containing that information.

    For example:

    To iterate thru all the user names and their hometowns within a database (db_1):

    qr_gen_db(db_1, Users, name, password, hometown)
                       
