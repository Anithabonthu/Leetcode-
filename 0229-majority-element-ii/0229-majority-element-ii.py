class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        ans=[]
        n=len(nums)//3
        temp=list(set(nums))
        for t in temp:
            if nums.count(t)>n:
                ans.append(t)
        return(ans)

        