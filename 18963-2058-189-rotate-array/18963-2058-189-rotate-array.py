class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
    """
        def swap(start,end,nums):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        swap(0,len(nums)-1,nums)
        k=k%len(nums)
        swap(0,k-1,nums)
        swap(k,len(nums)-1,nums)
       
       