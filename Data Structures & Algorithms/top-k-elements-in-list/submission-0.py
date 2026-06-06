class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencyMap = [[]for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            frequencyMap[c].append(n)               
        final = []
        for i in range(len(frequencyMap)-1,0,-1):
            for n in frequencyMap[i]:
                final.append(n)
                if len(final)==k:
                    return final 