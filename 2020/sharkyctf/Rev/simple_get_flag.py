some = [10, 2, 30, 15, 3, 7, 4, 2, 1, 24, 5, 11, 24, 4, 14,
        13, 5, 6, 19, 20, 23, 9, 10, 2, 30, 15, 3, 7, 4, 2, 1, 24]
second = [0x57, 0x40, 0xa3, 0x78, 0x7d, 0x67, 0x55, 0x40, 0x1e, 0xae, 0x5b, 0x11, 0x5d, 0x40, 0xaa,
          0x17, 0x58, 0x4f, 0x7e, 0x4d, 0x4e, 0x42, 0x5d, 0x51, 0x57, 0x5f, 0x5f, 0x12, 0x1d, 0x5a, 0x4f, 0xbf]
print("some len: %d" % len(some))
print("second len: %d" % len(second))

#! rcx = payload length
#! rdx = end address of payload

# dil: 8bit (ff) -> a char of payload

#! al = payload from back
#! dil = some from back

#! al += dil

#! rax ^= 42
#! r10 = second from back
# a == r10

flag = ""

for i in range(len(some)):
    flag += chr((second[i] ^ 42) - some[i])

print(flag)
