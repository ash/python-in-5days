# Bitwise operations

x = 10
y = 8
if x > 5 or y < 10:
    print('ok')
else:
    print('not ok')


a = 3 # 0b0011
b = 9 # 0b1001
      # 0b1011

print(bin(a))
print(bin(b))
c = a | b
print(bin(c))
print(c)

print(~c)
print(bin(~c))

