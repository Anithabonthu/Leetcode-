class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for ele in s:
            d[ele]=d.get(ele,0)+1
        fre=sorted(d.items() ,key=lambda x: -x[1])
        
        res=""
        for char,count in fre:
            res+=char*count
        return(res)
        