class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ""
        for char in s:
            if char.isalnum():
                f += char.lower()
        left = 0
        right = len(f)-1
        flag = True
        while left < right:
            if f[left] == f[right]:
                flag = True
            else:
                return False
            left += 1
            right -= 1
        return True

           