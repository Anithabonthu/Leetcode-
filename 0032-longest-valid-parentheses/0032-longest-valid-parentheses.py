class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0:
            return 0
        res=0
        temp=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                temp.append(i)
            elif s[i]==')':
                temp.pop()
                if temp:
                    res=max(res,(i-temp[-1]))
                else:
                    temp.append(i)
        return res
        