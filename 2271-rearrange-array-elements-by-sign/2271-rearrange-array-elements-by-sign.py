class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*(len(nums))
        pos=[]
        neg=[]
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        j=0
        for i in pos:
            res[j]=i
            j+=2
        j=1
        for i in neg:
            res[j]=i
            j+=2
        return res
        