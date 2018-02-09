# Super snap is like the game snap except that the matching cards (or words) need not be adjacent; there may be intervening cards.
# Write a Python script named super-snap.py which outputs the message indicated in the first example below when it encounters the first super snap.
# Your script should produce no output if no super snap is encountered.



import sys
aSDdnuwnfikewnfiewnfikfwenwienfwe
lines = sys.stdin.readlines()

cards = {}
snap = False

i = 0
while i < len(lines) and snap != True:
    currentWord = lines[i].strip()
    if currentWord not in cards:
        cards[currentWord] = False
    else:
        print currentWord
        snap = True
    i = i+1
