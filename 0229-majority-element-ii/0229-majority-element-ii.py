class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        #print(d)
        for ele,count in d.items():
            if count > len(nums)//3:
                ans.append(ele)
        return ans
        