#time - O(1)
#space - O(1)

MASK_EVEN = 0xAAAAAAAA # 0xAAAAAAAA is 10101010... in binary
MASK_ODD = 0x55555555 # 0x55555555 is 01010101... in binary

def swap_bits(num):
    return (((num & MASK_EVEN) >> 1)  | ((num & MASK_ODD) << 1))

print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")


0b01010101010101010101010101010101
0b01010101010101010101010101010101