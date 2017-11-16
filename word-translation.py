"""
The current working directory contains a file named translation.txt. That file defines word translations; for each line,
the first word translates to the second word. See the example, below.
Write a Python script named word-translation.py which reads a sequence of words from standard input (one per line) and,
for each word, outputs the translated word.

Example translation.txt
one eins
two zwei
three drei
four vier
five funf
six sechs
seven sieben
eight acht
nine neun
ten zehn
"""

import sys

dictionary = {}
toBeTranslated = {}

with open("CHANGE TO FILE LOCATION") as f:
    file = f.readlines()

""" Make dictionary with the English as key, German as value """
for i in range(len(file)):
    currentLine = file[i].rstrip()
    words = currentLine.split()			# split() function by default uses whitespace as it's delimiter
    dictionary[words[0]] = words[1]		# English key in dictionary = German value in dictionary

input = sys.stdin.readlines()

""" See what words need to be translate from input """
for i in range(len(input)):
    if input[i].rstrip() in dictionary:
        toBeTranslated[input[i].rstrip()] = True

""" Find what's True in toBeTranslated list -> then print it's german from dictionary """
for english,translationRequested in toBeTranslated.items():
    if translationRequested:
        print (dictionary[english]) # Print value at English index