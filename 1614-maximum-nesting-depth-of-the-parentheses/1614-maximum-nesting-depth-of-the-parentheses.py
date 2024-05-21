class Solution:
    def maxDepth(self, s: str) -> int:
        c,max_num=0,0
        for i in s:
            if i=='(':
                c+=1
                if max_num<c:
                    max_num=c
            if i==')':
                c-=1
        return max_num
                
        