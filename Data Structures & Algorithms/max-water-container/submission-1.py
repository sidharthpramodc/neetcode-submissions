class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        maxarea = min(heights[l],heights[r])*(r-l)
        while l<r:
            maxarea = max(maxarea,min(heights[l],heights[r])*(r-l))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return maxarea