class Solution:
    def generateRow(self,n):
        res=[]
        ans=1
        res.append(1)
        for i in range(1,n):
            ans=ans*(n-i)
            ans=ans//i
            res.append(ans)
        return res
            
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            ans.append(self.generateRow(i))
        return ans

        
        