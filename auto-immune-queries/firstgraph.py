from __future__ import division
from pylab import *
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="bobby",  # your password
                     db="Vasculitis")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM patients")

# print all the first cell of all the rows
maleCount = 0
femaleCount = 0
totalAge = 0
totalSize = 0
for row in cur.fetchall():
    if row[6] == "Vasculitis" and row[1] == "Male":
        maleCount = maleCount + 1
        totalSize = totalSize + 1
        totalAge = totalAge + row[2]

    if row[6] == "Vasculitis" and row[1] == "Female":
        femaleCount = femaleCount+1
        totalSize = totalSize + 1
        totalAge = totalAge + row[2]

total = maleCount+femaleCount
femalePercent = femaleCount / (total) * 100
malePercent = maleCount/ (total) * 100

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Male', 'Female'
fracs = [malePercent, femalePercent]
explode=(0, 0.05)

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

title('Percentage of Male and Female Patients', bbox={'facecolor':'0.8', 'pad':5})
show()