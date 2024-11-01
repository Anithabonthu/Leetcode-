class Solution:
    def makeFancyString(self, s: str) -> str:
        res=s[0]
        count=1
        for i in range(1,len(s)):
            if res[-1]==s[i]:
                count+=1
                if count <3:
                    res=res+s[i]
            else:
                count=1
                res=res+s[i]
        return res