class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        mini = nums[0]
        res = nums[0]
        for i in range(1,n):
            x = nums[i]
            if x < 0 :
                maxi,mini = mini,maxi
            maxi = max(x,maxi*x)
            mini = min(x,mini*x)
            res = max(res,maxi)
        return res