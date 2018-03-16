# Another paradigm of working with files using the 'with' keyword.
# Here, if something wrong happens while reading a file, it will be closed automatially at the end of the 'with' block.
# If everything was OK, the file will also be preperly closed.

with open('data.txt') as f:
    data = f.read()
    print(data)

print('ok done')
