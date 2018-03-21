# How to add up two lists element-wise.

l1 = [1,3,5,7]
l2 = [2,4,6,8]

# l3 = l1 + l2
# l3 = l1.add(l2)

# l3 = [3,7,11,15]

l3 = zip(l1, l2)
print(list(l3))

# A list comprehension can be a good solution:
l3 = [l1[i] + l2[i] for i in range(len(l1))]
print(l3)
