class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni = sorted(list(set(nums)))
        if not uni:
            return 0
        count = 1
        maxi = 1
        for i in range(1,len(uni)):
            if uni[i] == uni[i-1] + 1:
                count += 1
                maxi = max(maxi,count)
            else:
                count = 1
        return maxi
        