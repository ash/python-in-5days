# Now, writing to the file. Notice the 'w' (=write) or 'a' (append) mode:

with open('data2.txt', 'w') as f:
    f.write('abc\n')
    f.write('def\n')

with open('data3.txt', 'a') as f:
    # Take care of newlines
    f.writelines(['a\n', 'b\n', 'c\n'])

# r = read (default)
# w = write
# a = append
# x = exclusive write

# b, t = binary or text modes (test is default)
