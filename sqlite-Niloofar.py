import sqlite3 as db

conn = db.connect('niloo.db')
c = conn.cursor()

def CreateTable():
    c.execute(
        '''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER, 
                firstname TEXT, 
                lastname TEXT, 
                mobile TEXT
            )
        '''
    )

def Insert(id, firstname, lastname, mobile):
    c.execute(
        '''
            INSERT INTO users(id, firstname, lastname, mobile) values(:id, :firstname, :lastname, :mobile)
        ''', {'id': id, 'firstname': firstname, 'lastname': lastname, 'mobile': mobile}
    )
    conn.commit()


def GetAll():
    c.execute(
        '''
            SELECT * FROM users
        '''
    )
    return c.fetchall()


id = input('id: ')
fname = input('firstname: ')
lname = input('lastname: ')
mobile = input('mobile: ')

CreateTable()
Insert(id, fname, lname, mobile)
print(GetAll())

conn.close()
