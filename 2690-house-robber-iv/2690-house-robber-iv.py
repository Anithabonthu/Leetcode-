class Solution:
    def func(self,val,a,k):
        c=0
        i=0
        while i<len(a):
            if a[i]<=val:
                c+=1
                i+=1
            i+=1
        return c>=k

    def minCapability(self, nums: List[int], k: int) -> int:
        low=min(nums)
        high=max(nums)
        ans=0
        while low<=high:
            mid=low+((high-low)//2)
            if(self.func(mid,nums,k)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans