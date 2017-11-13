# Write a Python script named german-numbers.py which translates each English-language number into the corresponding German-language number. 
# All of the number words are in the range one to ten, and all are lower case. Your solution must make good use of dictionary.

import sys

lines = sys.stdin.readlines()

numbers = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine":"neun",
    "ten": "zehn",
}
i = 0
while i < len(lines):
    currentWord = lines[i].strip()          # Strip leading and trailing whitespace.
    if currentWord in numbers:        # if currentWord is in Numbers Dictionary
        print numbers[currentWord]    # print the value where currentWord occurs in numbers
    i=i+1