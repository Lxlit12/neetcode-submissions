class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = set()
        m = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        s.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        if len(s) == 0:
            return m
        else:
            for i in sorted(s):
                m.append(i)
        return m