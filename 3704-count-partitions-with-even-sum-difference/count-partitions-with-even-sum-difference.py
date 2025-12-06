class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        count = 0
        for i in range(start,end-1):
            left = nums[0:i+1]
            right = nums[i+1:end]
            if (abs(sum(left) - sum(right)))%2 == 0:
                count +=1
        return(count)


        