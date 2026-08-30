class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
    
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
    
    # If a is a negative number in 32-bit two's complement
        return a & mask if b > 0 else a