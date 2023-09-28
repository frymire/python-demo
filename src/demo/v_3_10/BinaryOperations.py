a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101

print("a & b = ", format(a & b, '08b'))    #  12 = 0000 1100  AND
print("a | b = ", format(a | b, '08b'))    #  61 = 0011 1101  OR
print("a ^ b = ", format(a ^ b, '08b'))    #  49 = 0011 0001  XOR
print("~a = ", format(~a, '08b'))          # -61 = 1100 0011  Ones Complement (flips bits)
print("a << 2 = ", format(a << 2, '08b'))  # 240 = 1111 0000  Shift bits left
print("a >> 2 = ", format(a >> 2, '08b'))  #  15 = 0000 1111  Shift bits right
