class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        low=0
        high=len(nums)-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
               
                ans=min(ans,nums[low])
                low=low+1
                high-=1
                continue
            elif nums[low]<=nums[mid]:
                ans=min(nums[low],ans)
                low=mid+1
            else:
                ans=min(nums[mid],ans)
                high=mid-1
        return ans

        