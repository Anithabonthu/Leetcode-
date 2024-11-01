class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        d={')':'(',']':'[','}':'{'}
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif d.get(s[i])!=stack[-1]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False
                
        