# Standard input consists of a sequence of lines. Each line contains an upload result from Einstein. An upload result is the name of a file,
# constructed from the task name with either ".correct" or ".incorrect" appended. See the example, below.
# The lines are in chronological order. A task is considered to have been successfully completed only if the last upload for that task was correct.
# Write a Python script named task-summary-1.py which outputs only the names of tasks which have been successfully completed (one per line, and in alphabetical order).


import sys

lines = sys.stdin.readlines()

files = {}

i = 0                                          
while i < len(lines):                           # Use while loop when we don't know how many times we're gonna iterate
    currentFile = lines[i].strip()              # Strip leading and trailing whitespace.
    
    parse = currentFile.split(".")
    
    addToDictionary = parse[0]+ "." + parse[1]  
    if parse[len(parse)-1] == "correct":        # if file extension is true
        files[addToDictionary] = True           # Index of file = True
    else:
        files[addToDictionary] = False          # Otherwise index of file is False
    i=i+1
    
for word,status in sorted(files.items()):
    if status == True:
        print word
