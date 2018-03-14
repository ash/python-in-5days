# List methods

a = []

# Add elements to the end:
a.append(3)
a.append(4)
a.append(5)
print(a)

# Add element at a given position:
a.insert(1, 'my new value')
print(a)

# Different manipulation with merging lists:

b = [10, 11, 12]

#[3, 'my new value', 4, 5, 10, 11, 12]
c = a + b
print(c)

d = a * 3
print(d)

c.append(b)
print(c)

c.extend(b)
print(c)

    