num = 5
bit_mask = 1 << num.bit_length()
print(bin(num))
print(bin(bit_mask))
bit_mask = bit_mask - 1
print(bin(num))
print(bin(bit_mask))
com = num ^ bit_mask
print(bin(com))


print(com)