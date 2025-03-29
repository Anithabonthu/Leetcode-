class Solution:
    def check_sorted(self,arr):
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                return False
        return True
    def check(self, nums: List[int]) -> bool:
        if self.check_sorted(nums):
            return True
        else:
            for i in range(1,len(nums)):
                if nums[i-1]>nums[i]:
                    ind=i
                    break
            l1=nums[ind:][::-1]
           # print(l1)
            l2=nums[0:ind][::-1]
            #print(l2)
            l1=l2+l1
            #print(l1)
            l1=l1[::-1]
            #print(l1)
            if self.check_sorted(l1):
                return True
            else:
                return False





        