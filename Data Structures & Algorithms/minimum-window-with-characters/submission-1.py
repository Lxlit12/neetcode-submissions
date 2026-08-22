from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        overall = len(c)
        l = 0
        r = 0
        res = ""
        while r < len(s):
            if s[r] in c:
                c[s[r]] -= 1
                if c[s[r]] == 0:
                    overall -= 1
            while overall == 0:
                if not res:
                    res = s[l:r+1]
                elif r - l + 1 < len(res):
                    res = s[l:r+1]
                if s[l] in c:
                    c[s[l]] += 1
                    if c[s[l]] > 0:
                        overall += 1
                l += 1
            r += 1
        return res
