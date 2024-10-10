class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=""
        for i in s:
            if i.isalnum():
                s1=s1+i
        if s1==s1[::-1]:
            return True
        return False
        