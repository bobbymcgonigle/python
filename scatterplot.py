from __future__ import division
import numpy as np
import MySQLdb
from pylab import *
import matplotlib.pyplot as plt

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="bobby",  # your password
                     db="vasculitis")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM patients")

# print all the first cell of all the rows
agesAtFirstVisit = []
for row in cur.fetchall():
    agesAtFirstVisit.insert(row[0],row[7])
healthScore = []
cur.execute("SELECT * FROM visit")
for row in cur.fetchall():
    healthScore.insert(row[20],row[7])
for i in healthScore:
    plt.scatter(agesAtFirstVisit[i], healthScore[i], color='r', s=7, alpha=0.5)
title('Scatterplot showing correlation between age and healthscore: Result: none', bbox={'facecolor':'0.8', 'pad':5})
show()
plt.show()
db.close()