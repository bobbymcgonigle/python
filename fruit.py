# Write a Python script named fruit.py which outputs only those words which are fruits. There are only five fruits: apples, pairs, oranges, bananas and cherries. Your solution must make good use of a dictionary.

import sys
lines = sys.stdin.readlines()

fruit = {
   "apple": True,
   "pair": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}
i = 0
while i < len(lines):
    currentWord = lines[i].strip()          # Strip leading and trailing whitespace.
    if currentWord in fruit:           # Is this a new word?
        print currentWord
    i=i+1