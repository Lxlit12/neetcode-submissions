class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)


        maxi = 0
        ans = ""

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]

                if substring == substring[::-1]:
                    if len(substring) > maxi:
                        maxi = len(substring)
                        ans = substring
        return ans
