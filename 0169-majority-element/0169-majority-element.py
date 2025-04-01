class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ele=0
        for i in range(0,len(nums)):
            if count==0:
                count=1
                ele=nums[i]
            elif nums[i]==ele:
                count+=1
            else:
                count-=1
        return ele
        