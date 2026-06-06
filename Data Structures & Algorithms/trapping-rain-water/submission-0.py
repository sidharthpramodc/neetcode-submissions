class Solution:
    def trap(self, height: List[int]) -> int:
        Level = 0
        for i in range(len(height)):
            l = r = height[i]
            for j in range(i):
                l = max(l,height[j])
            for m in range(i+1,len(height)):
                r = max(r,height[m])
            Level += min(l,r) - height[i]
        return Level
