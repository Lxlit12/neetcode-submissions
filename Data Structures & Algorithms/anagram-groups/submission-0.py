class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram = defaultdict(list)
        for words in strs:
            key = ''.join(sorted(words))
            anagram[key].append(words)
        return list(anagram.values())