class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerbound(arr,x):
            low=0
            high=len(arr)-1
            ans=0
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>=x:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def upperbound(arr,x):
            low=0
            high=len(arr)-1
            ans=len(arr)
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>x:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans-1
        if target not in nums:
            return [-1,-1]
        if len(nums)==1 and target in nums:
            return [0,0]
        lower=lowerbound(nums,target)
        upper=upperbound(nums,target)
        return [lower,upper]
        