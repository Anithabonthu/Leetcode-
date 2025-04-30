class Solution:
    def findMin(self, nums: List[int]) -> int:
        minValue=nums[0]
        for i in range(1,len(nums)):
            if nums[i] < minValue:
                minValue=nums[i]
        return minValue
        