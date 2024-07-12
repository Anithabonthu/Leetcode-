class Solution:
    def reverseParentheses(self, s: str) -> str:
        temp=[]
        ans=[]
        for char in s:
            if char=='(':
                temp.append(len(ans))
            elif char==')':
                ind_value=temp.pop()
                ans[ind_value:]=ans[ind_value:][::-1]
            else:
                ans.append(char)
        return("".join(ans))