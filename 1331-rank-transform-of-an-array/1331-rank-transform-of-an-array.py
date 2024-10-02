class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        arr2=sorted(list(set(arr)))
        for i in range(len(arr2)):
            d[arr2[i]]=i+1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr
        