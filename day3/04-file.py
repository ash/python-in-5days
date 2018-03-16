# A straightforward way of reading text from files

f = open('data.txt')

# Read all its content
data = f.read()
print(data)

# Close the file when we are done with it
f.close()
