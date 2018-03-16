# Read a file line by line, iterating over it with 'in':
with open('data.txt') as f:
    lineno = 0
    for line in f:
        lineno += 1
        print(lineno, line.rstrip())
