class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp1=[]
        temp2=[]
        for i in nums:
            if i not in temp1:
                temp1.append(i)
            elif i in temp1 and i not in temp2:
                temp2.append(i)
        temp1=temp1+temp2
        temp1.sort()
        for i in range(len(temp1)):
            nums[i]=temp1[i]
        return len(temp1)