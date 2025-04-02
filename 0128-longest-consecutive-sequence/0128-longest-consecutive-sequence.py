class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt=0
        maxi=0
        lastsmall=float('-inf')
        for i in range(len(nums)):
            if nums[i]-1 == lastsmall:
                cnt+=1
                lastsmall=nums[i]
            elif nums[i]!=lastsmall:
                cnt=1
                lastsmall=nums[i]
            maxi=max(maxi,cnt)
            #print(maxi)
        return maxi

