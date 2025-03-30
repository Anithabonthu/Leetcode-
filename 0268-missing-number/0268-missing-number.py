class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1=sum(nums)
        n=len(nums)
        s2=(n*(n+1))//2
        return s2-s1
        