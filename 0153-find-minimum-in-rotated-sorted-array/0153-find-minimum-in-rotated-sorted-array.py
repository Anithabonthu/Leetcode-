class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=float('inf')
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                ans=min(nums[low],ans)
                low=mid+1
            else:
                ans=min(nums[mid],ans)
                high=mid-1
        return ans
        