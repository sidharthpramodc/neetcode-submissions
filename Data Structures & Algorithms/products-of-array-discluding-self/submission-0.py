class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)):
            result[len(nums)-i-1] *= postfix
            postfix *= nums[len(nums)-i-1]
        return result