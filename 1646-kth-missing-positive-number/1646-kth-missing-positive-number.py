class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        while k:
            if i not in arr:
                k-=1
            i+=1
        return i-1
        