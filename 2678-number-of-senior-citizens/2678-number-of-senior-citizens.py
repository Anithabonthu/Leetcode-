class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=[]
        count=0
        for d in details:
            if d[11:13]>"60":
                count+=1
        return(count)
            