class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l1=[]
        for i in arr1:
            if i not in arr2:
                l1.append(i)
        l1.sort()
        res=[]
        for j in arr2:
            cnt=arr1.count(j)
            for k in range(cnt):
                res.append(j)
        return(res+l1)
        
        