class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        def sorting(n):
            return (count[n],-n)
        nums.sort(key=sorting)
        return(nums)