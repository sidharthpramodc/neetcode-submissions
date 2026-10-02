class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = s = 1
        res = []
        for i in range(len(nums)):
            res.append(p)
            p = p*nums[i]
        for i in range(len(nums)):
            res[len(nums)-i-1] *= s
            s *= nums[len(nums)-i-1]
        return res
