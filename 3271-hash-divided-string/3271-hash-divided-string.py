class Solution:
    def stringHash(self, s: str, k: int) -> str:
        alpha="abcdefghijklmnopqrstuvwxyz"
        key=len(s)//k
        list=[s[ind:ind+k] for ind in range(0,len(s),k)]
        res=""
        for st in list:
            temp=0
            for i in st:
                temp = temp + (ord(i)-ord('a'))
            print(temp)
            if temp>=26:
                temp=temp%26
            res = res + alpha[temp]
        return(res)
            
        