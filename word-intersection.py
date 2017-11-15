'''
The current working directory contains two files, words-1.txt and words-2.txt, each contains a sequence of words, one per line.
Write a Python script named word-intersection.py which outputs only the words which occur in both sequences
(without duplicates, one per line and in alphabetical order).
'''

import sys

with open("file location (change me)") as f:
    firstFile = f.readlines()

with open("file location (change me)") as f:
    secondFile = f.readlines()

inBoth = {}

for i in range(len(firstFile)):
    firstFile[i] = firstFile[i].rstrip()    # Get rid of \n char

for j in range(len(secondFile)):
    secondFile[j] = secondFile[j].rstrip()  # Get rid of \n char
    if secondFile[j] in firstFile:
        inBoth[secondFile[j]] = True

for word,status in sorted(inBoth.items()):
    if status == True:
        print (word)
