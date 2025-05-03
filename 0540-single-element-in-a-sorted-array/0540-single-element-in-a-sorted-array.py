class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        i=0
        j=1
        while j<len(nums) and i<len(nums):
            if nums[i]!=nums[j]:
                return nums[i]
            i=j+1
            j=i+1
        return nums[i]