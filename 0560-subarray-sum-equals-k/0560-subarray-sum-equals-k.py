class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        prefix=0
        count=0
        for i in nums:
            prefix+=i
            rem=prefix-k
            count+=d.get(rem,0)
            d[prefix]=d.get(prefix,0)+1
           
        return count
        