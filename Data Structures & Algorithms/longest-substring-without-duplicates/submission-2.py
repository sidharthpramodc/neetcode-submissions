class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wordset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in wordset:
                wordset.remove(s[l])
                l+=1
            wordset.add(s[r])
            res = max(res,len(wordset)) 
        return res