class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        length=min(len(first),len(last))
        i=0
        while i<length and first[i]==last[i]:
            i+=1
        if i==0:
            return ""
        return first[:i]