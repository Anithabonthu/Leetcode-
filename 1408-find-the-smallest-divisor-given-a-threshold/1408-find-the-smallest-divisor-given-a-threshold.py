import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sumOfD(arr,mid):
            sum1=0
            n=len(arr)
            for i in range(n):
                sum1+=math.ceil(arr[i]/mid)
            return sum1
        low=1
        high=max(nums)
        ans=-1
        while low <= high:
            mid=(low+high)//2
            if sumOfD(nums,mid)<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans