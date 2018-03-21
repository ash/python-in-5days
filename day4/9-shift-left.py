# Bitwise shifts can be used for division and multiplication 2^n

x = 1024

print(bin(x))

#x //= 4
x >>= 2
# x = x >> 2

print(bin(x))

print(x)

0b10000000000
0b00100000000
