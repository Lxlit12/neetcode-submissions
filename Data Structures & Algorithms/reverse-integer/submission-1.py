class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed = str(abs(x))[::-1]
        num = sign * int(reversed)
        if num < -2147483648 or num > 2147483647:
            return 0
        return num