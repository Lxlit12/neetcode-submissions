class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def helper(houses):
            prev2 = 0 #dp[i-2]
            prev1 = 0 #dp[i-1]
            for val in houses:
                curr = max(prev1,prev2+val)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(helper(nums[:-1]),helper(nums[1:]))
