class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=sorted(nums)
        return nums.index(l[-1])