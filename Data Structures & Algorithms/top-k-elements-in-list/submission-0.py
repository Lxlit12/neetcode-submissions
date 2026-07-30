class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        r = Counter(nums)
        result = []
        c = r.most_common(k)
        for i,j in c:
            result.append(i)
        return result