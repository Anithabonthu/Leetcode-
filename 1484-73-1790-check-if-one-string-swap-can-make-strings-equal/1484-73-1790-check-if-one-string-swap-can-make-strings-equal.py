class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if sorted(list(s1))!=sorted(list(s2)):
            return False
        stack=[0]*len(s1)
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                stack[i]=1
        count=stack.count(0)
        if count==2:
            return True
        return False
        
        