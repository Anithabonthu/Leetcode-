class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        res=0
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                left=mid+1
                res=mid+1
            else:
                right=mid-1
                res=mid
        return left