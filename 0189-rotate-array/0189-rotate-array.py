class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return
        k=k if k<=len(nums) else k%len(nums)
        nums[k:],nums[:k]=nums[:len(nums)-k],nums[len(nums)-k:]