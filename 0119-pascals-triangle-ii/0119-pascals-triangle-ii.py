class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        ans.append(1)
        row=rowIndex+1
        res=1
        for col in range(1,row):
            res=res*(row-col)
            res=res//col
            ans.append(res)
        return ans

