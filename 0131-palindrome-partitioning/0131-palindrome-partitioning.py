class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if palindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        def palindrome(s):
            if s==s[::-1]:
                return True
            else:
                return False
    

        dfs(0)
        return res
        