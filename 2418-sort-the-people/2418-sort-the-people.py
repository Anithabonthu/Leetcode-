class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(heights)):
            d[heights[i]]=names[i]
        l=d.keys()
        l=sorted(l,reverse=True)
        ans=[]
        for key in l:
            ans.append(d[key])
        return(ans)
        
        