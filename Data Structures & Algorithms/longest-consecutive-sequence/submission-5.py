class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for i in nums:
            occurence, j = 0, i
            while j in nums:
                occurence += 1
                j+=1
            res = max(res,occurence)
        return res       