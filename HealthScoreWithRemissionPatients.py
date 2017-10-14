from __future__ import division
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

total = 0
size = 0
remissionTotal = 0
remissionSize = 0
for row in cur.fetchall():
    total = total + row[7]
    size = size + 1
    if row[15] == "remission":
        remissionTotal = remissionTotal + row[7]
        remissionSize = remissionSize + 1

average = total/size
remissionAverage = remissionTotal/remissionSize
print "The average healthscore for all vasculitis sufferers: %f" % average
print "The average healthscore for all vasculitis sufferers in remission: %f" % remissionAverage

db.close()