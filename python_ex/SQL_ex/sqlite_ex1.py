__author__ = 'Administrator'

import sqlite3


conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values (\'2\',\'Michael\')')

cursor.execute('select * from user where id=?','2')
values = cursor.fetchall()
print values

cursor.close()
conn.close()
