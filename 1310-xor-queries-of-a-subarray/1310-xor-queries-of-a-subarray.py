class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        ans=[0]*n
        ans[0]=arr[0]
        res=[]
        for i in range(1,n):
            ans[i]=ans[i-1] ^ arr[i]
        for left,right in queries:
            if left==0:
                res.append(ans[right])
            else:
                res.append(ans[right] ^ ans[left-1])

        return(res)
        