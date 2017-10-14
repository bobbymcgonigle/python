from __future__ import division
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="bobby",  # your password
                     db="vasculitis")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM visit")

# print all the first cell of all the rows
january = 0
february = 0
march = 0
april = 0
may = 0
june = 0
july = 0
august = 0
september = 0
october = 0
november = 0
december = 0
for row in cur.fetchall():
    date = row[5]
    if date.month == 01 and row[7] < 50:
        january = january + 1
    if date.month == 02 and row[7] < 50:
        february = february + 1
    if date.month == 03 and row[7] < 50:
        march = march + 1
    if date.month == 04 and row[7] < 50:
        april = april + 1
    if date.month == 05 and row[7] < 50:
        may = may + 1
    if date.month == 06 and row[7] < 50:
        june = june + 1
    if date.month == 07 and row[7] < 50:
        july = july + 1
    if date.month == 8 and row[7] < 50:
        august = august + 1
    if date.month == 9 and row[7] < 50:
        september = september + 1
    if date.month == 10 and row[7] < 50:
        october = october + 1
    if date.month == 11 and row[7] < 50:
        november = november + 1
    if date.month == 12 and row[7] < 50:
        december = december + 1
objects = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
y_pos = np.arange(len(objects))
print january
performance = [january,february,march,april,may,june,july,august,september,october,november,december]
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('No. of people who rated themselves above 50')
plt.title('Per month breakdown of who felt below 50%')
plt.show()
db.close()