class Solution:
    def has_all(self,freq):
        return all(f>0 for f in freq)

    def numberOfSubstrings(self, s: str) -> int:
        left,right,res=0,0,0
        freq=[0]*3
        while right < len(s):
            freq[ord(s[right])-ord('a')]+=1
            while self.has_all(freq):
                res+=len(s)-right
                freq[ord(s[left])-ord('a')]-=1
                left+=1
            right+=1
        return res

        